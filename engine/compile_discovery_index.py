#!/usr/bin/env python3
import os
import re
import json

okf_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../okf'))

def parse_frontmatter(content):
    frontmatter = {}
    # Find the text between first and second '---'
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        yaml_text = match.group(1)
        for line in yaml_text.split('\n'):
            if ':' in line:
                key, val = line.split(':', 1)
                key = key.strip()
                val = val.strip()
                # Parse list like [tag1, tag2]
                if val.startswith('[') and val.endswith(']'):
                    val = [t.strip().strip('"').strip("'") for t in val[1:-1].split(',')]
                else:
                    val = val.strip('"').strip("'")
                frontmatter[key] = val
    return frontmatter

def parse_relations(content, file_dir_rel):
    relations = []
    # Find all Markdown links
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    for text, href in links:
        # Ignore external links (http/https/etc.)
        if href.startswith('http://') or href.startswith('https://') or href.startswith('#'):
            continue
        # Only process relative .md files
        if href.endswith('.md'):
            # Resolve the relative path
            # file_dir_rel is like 'cognitive_biases'
            # href is like '../methodologies/socratic_questioning.md'
            resolved = os.path.normpath(os.path.join(file_dir_rel, href))
            # Make sure it uses forward slashes
            resolved = resolved.replace('\\', '/')
            if resolved not in relations:
                relations.append(resolved)
    return relations

def main():
    docs = []
    for root, dirs, files in os.walk(okf_root):
        # Skip output directory
        if 'output' in root:
            continue
        for file in files:
            if file.endswith('.md'):
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, okf_root).replace('\\', '/')
                
                with open(abs_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                fm = parse_frontmatter(content)
                # Determine title
                title = fm.get('title')
                if not title:
                    # Find first heading
                    h_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                    title = h_match.group(1).strip() if h_match else file
                
                file_dir_rel = os.path.dirname(rel_path)
                relations = parse_relations(content, file_dir_rel)
                
                doc_type = fm.get('type')
                if not doc_type:
                    # Infer type from directory
                    if 'cognitive_biases' in rel_path:
                        doc_type = 'cognitive_bias'
                    elif 'methodologies' in rel_path:
                        doc_type = 'deprogramming_vector'
                    elif 'cases' in rel_path:
                        doc_type = 'case_study'
                    elif 'audits' in rel_path:
                        doc_type = 'audit'
                    elif 'research' in rel_path:
                        doc_type = 'research'
                    else:
                        doc_type = 'index'
                
                docs.append({
                    "path": abs_path,
                    "relative": rel_path,
                    "title": title,
                    "type": doc_type,
                    "description": fm.get('description', ''),
                    "tags": fm.get('tags', []),
                    "relations": relations,
                    "timestamp": fm.get('timestamp', ''),
                    "status": fm.get('status', 'active')
                })
                
    # Sort docs by relative path
    docs.sort(key=lambda d: d['relative'])
    
    # Calculate counts
    primary_sections = {}
    for doc in docs:
        parent = doc['relative'].split('/')[0]
        if '/' not in doc['relative']:
            parent = 'okf'
        primary_sections[parent] = primary_sections.get(parent, 0) + 1
        
    sections_list = []
    for name, count in primary_sections.items():
        # Inferred type
        t = 'index'
        if name == 'cognitive_biases':
            t = 'cognitive_bias'
        elif name == 'methodologies':
            t = 'deprogramming_vector'
        elif name == 'cases':
            t = 'case_study'
        elif name == 'audits':
            t = 'audit'
        elif name == 'research':
            t = 'research'
        sections_list.append({
            "name": name,
            "type": t,
            "doc_count": count
        })
    sections_list.sort(key=lambda s: s['name'])
    
    profile = {
        "project": {
            "name": "Belief Deprogrammer",
            "tagline": "Personalized Human Design Deconditioning",
            "description": "Epistemologically grounded deprogramming knowledge base.",
            "mission": "Empower individuals to safely identify, deconstruct, and dissolve limiting conditioning through integrated psychological and somatic modalities.",
            "type": "knowledge-base",
            "status": "active"
        },
        "content": {
            "primary_sections": sections_list,
            "assets": [
                "assets/belief_systems_map.svg",
                "assets/belief_deconditioning_concept.png"
            ],
            "testimonials_or_quotes": []
        },
        "design": {
            "color_palette": ["#00ffff", "#ff0055", "#00ff55", "#ffaa00"],
            "typography": "Georgia, system-ui, sans-serif",
            "mood": "scientific, premium, deep, mystical-yet-rational",
            "reference_sites": []
        },
        "technical": {
            "stack": ["HTML5", "CSS3", "JavaScript", "Python API Server"],
            "deployment": "Cloudflare Pages (landing), Python Service (engine)",
            "github_repo": "mbgulden/belief-deprogrammer",
            "live_url": "https://belief-deprogrammer.pages.dev"
        },
        "automation": {
            "workflows": []
        },
        "okf_docs": docs,
        "metadata": {
            "okf_root": okf_root,
            "ingest_date": "2026-06-24T00:00:00Z",
            "doc_count": len(docs)
        },
        "primary_sections": sections_list
    }
    
    output_path = os.path.join(okf_root, 'output/belief-deprogrammer-profile.json')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(profile, f, indent=2)
        
    print(f"Compiled index containing {len(docs)} documents to {output_path}")

if __name__ == '__main__':
    main()
