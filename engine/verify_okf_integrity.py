#!/usr/bin/env python3
import os
import re
import sys

okf_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../okf'))

def parse_frontmatter(content):
    frontmatter = {}
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        yaml_text = match.group(1)
        for line in yaml_text.split('\n'):
            if ':' in line:
                key, val = line.split(':', 1)
                key = key.strip()
                val = val.strip()
                if val.startswith('[') and val.endswith(']'):
                    val = [t.strip().strip('"').strip("'") for t in val[1:-1].split(',')]
                else:
                    val = val.strip('"').strip("'")
                frontmatter[key] = val
    return frontmatter

def parse_links(content, file_dir_rel):
    links_found = []
    # Find markdown links [Text](Href)
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    for text, href in links:
        # Skip external links
        if href.startswith('http://') or href.startswith('https://') or href.startswith('#') or href.startswith('mailto:'):
            continue
        # Resolve path
        resolved = os.path.normpath(os.path.join(file_dir_rel, href.split('#')[0]))
        resolved = resolved.replace('\\', '/')
        if resolved not in links_found:
            links_found.append(resolved)
    return links_found

def main():
    print("═══ OKF Integrity and Ontological Validation ═══")
    print(f"OKF Root: {okf_root}\n")

    all_docs = {}
    
    # 1. Gather all documents
    for root, dirs, files in os.walk(okf_root):
        if 'output' in root:
            continue
        for file in files:
            if file.endswith('.md'):
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, okf_root).replace('\\', '/')
                all_docs[rel_path] = {
                    'abs_path': abs_path,
                    'content': '',
                    'frontmatter': {},
                    'links': []
                }

    # 2. Parse frontmatter and links
    for rel_path, doc_info in all_docs.items():
        with open(doc_info['abs_path'], 'r', encoding='utf-8') as f:
            content = f.read()
            doc_info['content'] = content
            doc_info['frontmatter'] = parse_frontmatter(content)
            doc_info['links'] = parse_links(content, os.path.dirname(rel_path))

    failures = 0
    warnings = 0

    print(f"Scanned {len(all_docs)} markdown files.\n")

    # 3. Check Metadata / Frontmatter schemas
    print("--- Checking Ontological Frontmatter Schemas ---")
    required_keys = ['type', 'title', 'description', 'tags', 'timestamp', 'status']
    for rel_path, doc_info in all_docs.items():
        fm = doc_info['frontmatter']
        missing = [k for k in required_keys if k not in fm]
        if missing:
            print(f"⚠️  {rel_path}: Missing frontmatter key(s): {', '.join(missing)}")
            warnings += 1
        
        # Check validity of status
        if fm.get('status') not in ['current', 'active', 'stable', 'deprecated', None]:
            print(f"⚠️  {rel_path}: Unknown status '{fm.get('status')}'")
            warnings += 1

    # 4. Validate Link Existence
    print("\n--- Validating Link Existence ---")
    link_graph = {} # node -> set of linked nodes
    for rel_path in all_docs:
        link_graph[rel_path] = set()

    for rel_path, doc_info in all_docs.items():
        for link in doc_info['links']:
            # If it's a directory link, append '/index.md'
            link_target = link
            if link_target in [d for d in all_docs if os.path.isdir(os.path.join(okf_root, d))]:
                link_target = (link_target + '/index.md').replace('//', '/')
            elif os.path.isdir(os.path.join(okf_root, link_target)):
                link_target = (link_target + '/index.md').replace('//', '/')
            
            # Check if resolved file exists
            if link_target not in all_docs:
                # Try adding .md if not present
                if not link_target.endswith('.md') and (link_target + '.md') in all_docs:
                    link_target += '.md'
                elif link_target == '' and 'index.md' in all_docs:
                    link_target = 'index.md'
                else:
                    print(f"❌ {rel_path} contains broken link to: {link} (resolved: {link_target})")
                    failures += 1
                    continue
            
            link_graph[rel_path].add(link_target)

    # 5. Check Bidirectionality and Identify Orphans/Dead-Ends
    print("\n--- Analyzing Graph Density (Orphans, Dead-Ends, Bidirectionality) ---")
    for node in all_docs:
        incoming_links = [src for src, targets in link_graph.items() if node in targets]
        outgoing_links = list(link_graph[node])
        
        # Check if Orphan (no incoming links, unless it's index.md)
        if not incoming_links and node != 'index.md':
            print(f"❌ Orphan Node detected: {node} (No other pages link to this file)")
            failures += 1
        
        # Check if Dead-End (no outgoing links)
        if not outgoing_links:
            print(f"❌ Dead-End Node detected: {node} (This page contains no outgoing local links)")
            failures += 1
            
        # Check Bidirectionality of outgoing links
        for target in outgoing_links:
            if target != node and node not in link_graph[target]:
                # If target is index.md or self-links, maybe excuse it, but let's report it
                print(f"⚠️  Unidirectional Link: {node} ──> {target} (Missing return link {target} ──> {node})")
                warnings += 1

    # Summary
    print("\n═══ Validation Summary ═══")
    print(f"Total Failures (Blockers): {failures}")
    print(f"Total Warnings: {warnings}")
    
    if failures > 0:
        print("\n❌ Ontological validation FAILED due to critical structural errors.")
        sys.exit(1)
    else:
        print("\n✅ Ontological validation PASSED successfully.")
        sys.exit(0)

if __name__ == '__main__':
    main()
