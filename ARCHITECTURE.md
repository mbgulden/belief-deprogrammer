# Belief Deprogrammer — Architecture

## Vision

A personalized belief-reprogramming engine that takes any Human Design chart as input and generates a comprehensive, life-changing deconditioning workbook. Not a template with blanks filled in — a genuinely personalized output where every belief is derived from the individual's unique design elements.

## The Belief Tree Model

```
ROOT (Open Center)
 └─ TRUNK (Core Conditioning Theme)
     └─ BRANCH (Category × Gate)
         └─ TWIG (Specific Limiting Belief)
             └─ LEAF (Empowering Counter-Belief)
```

### Combinatorial Scope

| Element | Count |
|---|---|
| Open centers per person | 2–5 typical, 9 max |
| Hanging gates per open center | 2–6 average |
| Belief categories | 9 |
| Beliefs per gate per category | 3–5 |
| **Typical total (comprehensive)** | **600–1,000+** |
| **Short punchy** | **30–50** |

Plus: cross-center interactions, type/profile/cross-specific, and variable-specific beliefs.

## Generation Algorithm

```
chart → extract(open_centers, hanging_gates, type, authority, profile, cross, variable)
     → for_each open_center:
         → generate_center_level_beliefs(center, categories, chart_context)
         → for_each hanging_gate in center:
             → gate_theme = GATE_CONDITIONING_THEMES[gate]
             → for_each category:
                 → limiting = apply_category(gate_theme, category, chart_context)
                 → empowering = generate_counter(limiting, chart_context)
                 → add(limiting, empowering)
     → generate_cross_center_interactions(chart)
     → generate_design_specific(chart)
     → if tier == 'short': distill_to_core(50)
     → format_workbook
```

## Gate Conditioning Themes

Every gate has a "high expression" (when in a defined center) and a "distorted expression" (when in an open center, absorbing). The belief engine maps the distorted expression through each of the 9 categories.

Example — Gate 53 (Beginnings, Root):

| Category | Distortion |
|---|---|
| General | "I must keep starting things to feel alive" |
| Environmental | "My workplace rewards perpetual initiation over completion" |
| Generational | "My ancestors survived by never stopping — I inherited their urgency" |
| Physical | "My body stores pressure to begin like a spring that never releases" |
| Mental | "My mind races with beginnings I can't finish — I believe I'm failing" |
| Spiritual | "Stopping feels like spiritual death — my purpose is to keep going" |
| Subconscious | "Below awareness, I equate stillness with danger — I keep initiating" |
| Conscious | "I know I start too many things, but I believe I have no choice" |
| Absorbed | "I absorbed my father's restless ambition — his unfinished starts live in me" |

## Personal Context Injection

Every empowering belief is crafted from the person's ACTUAL design:

- **Type**: "I am a Projector — I am not here to initiate."
- **Authority**: "My Splenic authority gives an instant knowing."
- **Profile**: "As a 3/5, I learn through trial — my 'failures' are data."
- **Cross**: "My Cross of Rulership guides me to lead through recognition."
- **Defined centers**: "My defined Heart gives me willpower — I don't need borrowed sacral energy."
- **Motivation**: "I am Fear-motivated — I move when I see the threat clearly, not when I'm pushed."

## Two-Tier Output

### Short Punchy (30–50 Beliefs)
- One trunk belief per open center
- One leaf per category per center (the most impactful)
- Design-specific core beliefs
- Readable in one sitting
- Designed for rapid shift — the "emergency reset"

### Comprehensive (600–1,000+ Beliefs)
- Full belief tree: every gate × every category × multiple beliefs
- Cross-center interactions
- 30-day program structure (Duzett: 5 beliefs/day)
- Includes scribbling/tapping prompts
- Designed for complete deconditioning over weeks

## Technology

- **Core engine**: Python package in `belief-deprogrammer/engine/`
- **API**: FastAPI endpoint (same server as HD Engine, port 8000)
- **Integration**: HD website at `humandesignengine.com/belief-deprogrammer`
- **CLI**: `belief-deprogrammer generate --chart=chart.json --tier=comprehensive`
- **Input**: OHDMCP chart JSON
- **Output**: Markdown workbook, PDF (via pandoc), JSON (for web rendering)

## Project Structure

```
belief-deprogrammer/
├── engine/
│   ├── __init__.py
│   ├── generator.py       # Main generation algorithm
│   ├── gate_themes.py     # Per-gate conditioning themes
│   ├── category_expander.py  # Theme → category variations
│   ├── context_injector.py   # Personal design context
│   ├── cross_center.py    # Cross-center interaction beliefs
│   ├── distiller.py       # Short punchy extraction
│   └── formatter.py       # Workbook output (MD, JSON)
├── data/
│   ├── gate_conditioning.json  # All 64 gates × distortion themes
│   ├── category_patterns.json  # 9 categories × expansion patterns
│   └── empowering_templates.json  # Counter-belief templates
├── workbook/              # Static workbook (reference/seed content)
├── api/
│   └── belief_endpoint.py
├── cli.py
└── tests/
```
