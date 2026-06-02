"""
Belief Deprogrammer — Main Generation Engine (v3.0 — Duzett-Aligned)

Generates personalized belief workbooks from Human Design charts.

FORMAT RULES (Duzett methodology):
  1. Limiting beliefs: ONE atomic statement. No compounds.
  2. Empowering beliefs: PURELY positive. No negatives ("not", "don't", "never").
  3. Empowering beliefs: ONE cohesive thought. No concatenated phrases.
  4. Empowering beliefs: Directly counter the SPECIFIC limiting belief.
  5. Design context INFORMS the belief but is NOT pasted into it verbatim.
"""

from typing import Dict, List, Tuple, Optional
from engine.gate_themes import GATE_CONDITIONING, CATEGORIES, CATEGORY_DESCRIPTIONS
from engine.context_injector import DesignContext

LAYER_NAMES = {
    1: "The Soil — Faulty Core Identity",
    2: "The Roots — Faulty Core Beliefs",
    3: "The Trunk — Limiting Beliefs",
    4: "The Leaves — Negative Programs",
}

LAYER_DESCRIPTIONS = {
    1: "Who you believe you ARE at the deepest level. These beliefs formed in childhood, "
       "absorbed before you could question them. They feel like identity — but they are "
       "conditioning. Clearing these unlocks everything below.",
    2: "The structural beliefs that spread from your core identity. How you believe the "
       "world works, what your worth depends on, what you must do to be safe or loved. "
       "These are the rules your system runs on.",
    3: "The specific 'shoulds,' 'musts,' and 'can'ts' that govern your daily choices. "
       "These feel personal and real — but they are distortions of energy that was "
       "never yours.",
    4: "The automatic thoughts — the constant inner chatter. These are symptoms, not "
       "causes. When the layers above clear, these dissolve on their own.",
}

CENTER_GATES = {
    "Head": [61, 63, 64],
    "Ajna": [4, 11, 17, 24, 43, 47],
    "Throat": [8, 12, 16, 20, 23, 31, 33, 35, 45, 56, 62],
    "G": [1, 2, 7, 10, 13, 15, 25, 46],
    "Heart/Ego": [21, 26, 40, 51],
    "Sacral": [3, 5, 9, 14, 27, 29, 34, 42, 59],
    "Spleen": [18, 28, 32, 44, 48, 50, 57],
    "Solar Plexus": [6, 22, 30, 36, 37, 49, 55],
    "Root": [19, 38, 39, 41, 52, 53, 54, 58, 60],
}


class BeliefPair:
    def __init__(self, limiting: str, empowering: str, center: str,
                 gate: Optional[int], category: str, layer: int, day: int):
        self.limiting = limiting
        self.empowering = empowering
        self.center = center
        self.gate = gate
        self.category = category
        self.layer = layer
        self.day = day


class WorkbookGenerator:

    def __init__(self, chart: dict):
        self.chart = chart
        self.context = DesignContext(chart)
        self.beliefs: List[BeliefPair] = []

    # ═══════════════════════════════════════════════════════════
    # MAIN GENERATION
    # ═══════════════════════════════════════════════════════════

    def generate(self, tier: str = "comprehensive") -> List[BeliefPair]:
        hanging = self.context.get_hanging_gates(CENTER_GATES)

        # Layer 1: Core Identity
        for center in self.context.undefined_centers:
            self._generate_layer1(center)

        # Layer 2: Core Beliefs
        for center in self.context.undefined_centers:
            if center in hanging:
                for gate in hanging[center]:
                    if gate in GATE_CONDITIONING:
                        self._generate_layer2(center, gate)

        # Layer 3: Limiting Beliefs
        for center in self.context.undefined_centers:
            if center in hanging:
                for gate in hanging[center]:
                    if gate in GATE_CONDITIONING:
                        self._generate_layer3(center, gate, tier)

        # Layer 4: Negative Programs
        for center in self.context.undefined_centers:
            if center in hanging:
                for gate in hanging[center]:
                    if gate in GATE_CONDITIONING:
                        self._generate_layer4(center, gate, tier)

        self._generate_cross_center()
        self._generate_design()

        if tier == "short":
            self.beliefs = self._distill(self.beliefs, 50)

        return self.beliefs

    # ═══════════════════════════════════════════════════════════
    # LAYER 1 — Core Identity
    # ═══════════════════════════════════════════════════════════

    def _generate_layer1(self, center: str):
        """One atomic limiting belief → one positive empowering belief."""
        for limiting, empowering in self._identity_pairs(center):
            self.beliefs.append(BeliefPair(
                limiting=limiting, empowering=empowering,
                center=center, gate=None, category="general",
                layer=1, day=self._next_day()
            ))

    def _identity_pairs(self, center: str) -> List[Tuple[str, str]]:
        """Single-thought limiting beliefs with positive, self-contained empowering counters."""
        t = self.context.type
        a = self.context.authority

        IDENTITY = {
            "Head": [
                ("I am fundamentally confused and uncertain.",
                 "I am receptive and panoramic. My mind holds many questions at once, and the right answers arrive when I am still."),
                ("Everyone else knows what matters and I never do.",
                 "I perceive what others overlook. My clarity emerges through synthesis, through stillness, through trusting the spaciousness of my mind."),
                ("My scattered mind means something is missing in me.",
                 "My open mind is spacious by design. I absorb the world's curiosity and distill it into insight that serves my purpose."),
            ],
            "Ajna": [
                ("I am indecisive at my core.",
                 "I am spacious and discerning. I process many perspectives and arrive at the right decision in the right moment."),
                ("I cannot commit to anything because I do not know what I believe.",
                 "I commit when clarity arrives through my body. My knowing is somatic and trustworthy, and I honor its timing."),
                ("My thoughts lack structure and conviction.",
                 "My mind is fluid and adaptive. I hold complexity with ease and synthesize insights that linear minds overlook."),
                ("I am mentally inferior to people with sharper, more certain minds.",
                 "I possess an adaptive intelligence that moves freely across perspectives. I think in panoramas and find wisdom in spaciousness."),
            ],
            "Sacral": [
                ("I am fundamentally incapable of sustaining anything.",
                 f"I am a {t} — built for precise, deep impact. My rhythm of work and rest is correct for my design, and I trust it completely."),
                ("I am lazy at my core.",
                 "I am designed to rest. My body enforces boundaries that protect my gifts. What looks like idleness is actually the restoration that fuels my clarity."),
                ("My inability to keep going means I am broken.",
                 "My design is a precision instrument. A scalpel completes its work and rests. I complete my work and I rest. Both are correct."),
                ("I am less valuable than people who produce consistently.",
                 "My value is in what I perceive, guide, and recognize. One insight born from stillness surpasses a thousand hours of forced output."),
            ],
            "Solar Plexus": [
                ("I am emotionally unstable and unpredictable.",
                 "I am exquisitely sensitive. I feel the emotional field with precision, and I distinguish with ease between what is mine and what passes through me."),
                ("I cause the conflict wherever I go.",
                 "I detect tension that already exists. My sensitivity reveals what needs attention, and I navigate the emotional terrain with grace."),
                ("My emotions will control me forever.",
                 "I feel the wave and I remain anchored. My body knows the difference between amplification and truth, and I trust that knowing completely."),
            ],
            "Root": [
                ("I am a restless person incapable of peace.",
                 "I am sensitized to pressure, and I am anchored in stillness. Calm is my birthright, and I return to it with each exhale."),
                ("I am permanently behind everyone else.",
                 f"I move on {t} time, governed by recognition and invitation. My pace is precise and correct, and I arrive exactly when I am meant to."),
                ("I cannot handle the pressure of life.",
                 "I handle genuine pressure with clarity. Borrowed urgency from the field passes through me, and I remain centered in my own rhythm."),
            ],
            "Heart/Ego": [
                ("I am fundamentally unworthy.",
                 "I arrived valuable. My worth is inherent and radiates from my being. I release the need to earn what I have always been."),
                ("I have nothing of real value to offer anyone.",
                 "I offer what no amount of effort can produce: clear seeing, precise guidance, and recognition of what others miss in themselves."),
            ],
            "Spleen": [
                ("I am unsafe and my instincts betray me.",
                 f"I am vigilant and discerning. My {a.lower()} authority knows instantly what is safe and what aligns. I trust my body completely."),
                ("I lack the intuition that other people naturally have.",
                 "I pick up intuitive signals from the entire field. What feels like absence is actually abundance — I am learning to distinguish my signal from the noise."),
            ],
            "G": [
                ("I have no fixed identity and that terrifies me.",
                 "I am identity-fluid by design. I discover myself through the right spaces, people, and invitations, and each discovery reveals more of my wholeness."),
                ("I have no direction and never will.",
                 "My direction reveals itself through alignment. I follow the invitations that resonate, and the path becomes clear with each step I take."),
            ],
        }
        return IDENTITY.get(center, [
            (f"My undefined {center} makes me incomplete.",
             f"My open {center} is a receiver, a channel for wisdom. What I take in becomes insight. What I release was never mine. I am whole as I am.")
        ])

    # ═══════════════════════════════════════════════════════════
    # LAYER 2 — Faulty Core Beliefs
    # ═══════════════════════════════════════════════════════════

    def _generate_layer2(self, center: str, gate: int):
        gd = GATE_CONDITIONING.get(gate)
        if not gd: return
        gn = gd["name"]
        ds = gd["distortion"].split('.')[0]

        pairs = [
            (f"My worth is tied to how I handle {gn} energy.",
             f"My worth is independent of any energy I absorb. I carry the {gn} frequency with grace, and I release the pressure to perform it."),
            (f"I have organized my understanding of life around the {gn} pattern.",
             f"I am rewriting my relationship with {gn} energy. I receive it with awareness, I witness it with compassion, and I let it pass without attaching meaning."),
            (f"The {gn} distortion is a fundamental law of my existence.",
             f"The {gn} energy is a signal I received, a frequency I encountered. I witness it, I release it, and I remain centered in my own authentic design."),
        ]
        for lim, emp in pairs:
            self.beliefs.append(BeliefPair(
                limiting=lim, empowering=emp,
                center=center, gate=gate, category="general",
                layer=2, day=self._next_day()
            ))

    # ═══════════════════════════════════════════════════════════
    # LAYER 3 — Limiting Beliefs
    # ═══════════════════════════════════════════════════════════

    def _generate_layer3(self, center: str, gate: int, tier: str):
        gd = GATE_CONDITIONING.get(gate)
        if not gd: return
        gn = gd["name"]
        ds = gd["distortion"].split('.')[0]
        count = 2 if tier == "comprehensive" else 1

        for cat in CATEGORIES:
            limits = self._limiting_for_category(ds, cat, center, gate, gn, count)
            emps = self._empowering_for_category(ds, cat, center, gate, gn, count)
            for lim, emp in zip(limits, emps):
                self.beliefs.append(BeliefPair(
                    limiting=lim, empowering=emp,
                    center=center, gate=gate, category=cat,
                    layer=3, day=self._next_day()
                ))

    def _limiting_for_category(self, ds: str, cat: str, center: str,
                                gate: int, gn: str, count: int) -> List[str]:
        """Single atomic limiting beliefs per category."""
        bases = {
            "general": [
                f"I have absorbed the {gn} energy of others and believed it was my own.",
                f"My open {center} amplifies {gn} energy from everyone around me.",
            ],
            "environmental": [
                f"Growing up, the environments I was in rewarded the {gn} pattern.",
                f"Every workplace and school I attended reinforced the {gn} distortion.",
            ],
            "generational": [
                f"My family line carries the {gn} pattern across generations.",
                f"I inherited the {gn} energy from those who came before me.",
            ],
            "physical": [
                f"My body stores the {gn} pattern as physical tension.",
                f"My nervous system learned to brace for the {gn} energy.",
            ],
            "mental": [
                f"My mind loops on the {gn} pattern.",
                f"I catch myself thinking I must manage the {gn} energy perfectly.",
            ],
            "spiritual": [
                f"I have believed the {gn} distortion is part of my spiritual purpose.",
                f"I have carried the {gn} pattern as if it were a soul obligation.",
            ],
            "subconscious": [
                f"Below my awareness, the {gn} distortion drives my choices.",
                f"My subconscious runs a program that treats {gn} energy as dangerous.",
            ],
            "conscious": [
                f"I see the {gn} pattern and still feel powerless to release it.",
                f"I recognize the {gn} distortion and have believed I cannot change it.",
            ],
            "absorbed": [
                f"Someone I trusted imprinted the {gn} energy onto me.",
                f"A formative relationship transferred the {gn} pattern into my system.",
            ],
        }
        return bases.get(cat, [f"I believe the {gn} energy defines me."])[:count]

    def _empowering_for_category(self, ds: str, cat: str, center: str,
                                   gate: int, gn: str, count: int) -> List[str]:
        """Positive, self-contained empowering beliefs — no negatives, no boilerplate."""
        t = self.context.type
        a = self.context.authority

        bases = {
            "general": [
                f"I hold the {gn} frequency with clarity and release it with ease. The energy flows through my open {center} without becoming my identity.",
                f"My open {center} is a receiver of {gn} energy. I observe it, I honor it, and I let it pass through me freely.",
            ],
            "environmental": [
                f"I am free from the environmental conditioning that attached me to the {gn} pattern. I choose spaces that honor my natural rhythm.",
                f"The {gn} distortion that my environments taught me is released. I create new environments that reflect my authentic design.",
            ],
            "generational": [
                f"The {gn} pattern that ran through my lineage stops with me. I am the one who breaks this chain and heals this inheritance.",
                f"My ancestors carried what they could. I carry it differently. The {gn} energy transforms through me into wisdom for the generations that follow.",
            ],
            "physical": [
                f"My body releases the {gn} tension with each breath. My tissues soften, my nervous system settles, and I return to ease.",
                f"My physical self knows safety now. The {gn} pattern that my body braced against is dissolving, and I inhabit my body with trust.",
            ],
            "mental": [
                f"My thoughts around {gn} energy are quiet and clear. I observe the pattern without engaging it, and my mind remains spacious.",
                f"I release the mental loop of {gn} management. My mind is free to wander, create, and rest without the burden of borrowed energy.",
            ],
            "spiritual": [
                f"The {gn} frequency was a passing signal that served its purpose in my journey. My soul's contract is with my authentic design, and I honor that fully now.",
                f"My purpose exists beyond the {gn} pattern. I am here to guide, to see, and to recognize — and the {gn} energy serves that purpose freely, without defining it.",
            ],
            "subconscious": [
                f"My deeper self is releasing the {gn} program. What ran below awareness is rising into light, and I welcome its departure with compassion.",
                f"The hidden {gn} pattern that drove my choices is dissolving. My subconscious aligns with my design, and my actions flow from truth rather than from conditioning.",
            ],
            "conscious": [
                f"I see the {gn} pattern with clarity now, and I release it with the same clarity. Awareness is the doorway, and I walk through it freely.",
                f"The {gn} distortion I recognized is the one I release. I have always had the power to let it go, and I exercise that power now.",
            ],
            "absorbed": [
                f"The {gn} energy I absorbed from others returns to its source. I carry only what is mine, and I am lighter for what I release.",
                f"I release the {gn} imprint that was transferred to me. That relationship shaped me, and I honor what it taught me while stepping fully into my own self.",
            ],
        }
        return bases.get(cat, [f"I hold the {gn} energy with peace and release it with ease."])[:count]

    # ═══════════════════════════════════════════════════════════
    # LAYER 4 — Negative Programs
    # ═══════════════════════════════════════════════════════════

    def _generate_layer4(self, center: str, gate: int, tier: str):
        gd = GATE_CONDITIONING.get(gate)
        if not gd: return
        gn = gd["name"]

        pairs = [
            (f"I am terrible at handling {gn} energy.",
             f"I handle {gn} energy with ease. I notice it, I release it, and I return to center without struggle."),
            (f"Everyone else manages {gn} energy better than I do.",
             f"My experience with {gn} energy is unique to my design. I compare only to my own growth, and I am proud of how far I have come."),
            (f"I keep repeating the same {gn} pattern and I will never change.",
             f"Every time I notice the {gn} pattern, I loosen its hold. Progress is cumulative, and I am undoing layers that took decades to form."),
            (f"The {gn} energy makes me feel fundamentally wrong.",
             f"The {gn} energy is a frequency I encounter, separate from who I am. I am whole and correct regardless of what energy passes through me."),
        ]
        count = len(pairs) if tier == "comprehensive" else 2
        for lim, emp in pairs[:count]:
            self.beliefs.append(BeliefPair(
                limiting=lim, empowering=emp,
                center=center, gate=gate, category="general",
                layer=4, day=self._next_day()
            ))

    # ═══════════════════════════════════════════════════════════
    # CROSS-CENTER + DESIGN BELIEFS
    # ═══════════════════════════════════════════════════════════

    def _generate_cross_center(self):
        undef = set(self.context.undefined_centers)
        t = self.context.type

        if "Sacral" in undef and "Root" in undef:
            self.beliefs.append(BeliefPair(
                limiting="My worth depends on how much I produce, and I feel constant panic about falling short.",
                empowering=f"I am a {t}. My worth is in my seeing, my guiding, and my recognition. The urgency and life force I feel are amplified from the field. I release them and remain centered in my value.",
                center="Sacral+Root", gate=None, category="general",
                layer=2, day=self._next_day()
            ))

        if "Solar Plexus" in undef and "Ajna" in undef:
            self.beliefs.append(BeliefPair(
                limiting="I must think through every feeling until it makes logical sense.",
                empowering="My feelings complete themselves without mental approval. I feel, I release, and I trust my body to know what the feeling wanted me to understand.",
                center="Solar Plexus+Ajna", gate=None, category="general",
                layer=3, day=self._next_day()
            ))

        if "Head" in undef and "Root" in undef:
            self.beliefs.append(BeliefPair(
                limiting="Questions demand answers and answers demand action, and I am trapped between both.",
                empowering="I breathe into the space between question and answer. The mental pressure and physical urgency are borrowed signals. I release both and trust the timing of my own clarity.",
                center="Head+Root", gate=None, category="general",
                layer=2, day=self._next_day()
            ))

    def _generate_design(self):
        t = self.context.type
        m = self.context.motivation
        a = self.context.authority

        if t == "Projector":
            self.beliefs.append(BeliefPair(
                limiting="Success requires grinding harder and longer than everyone else.",
                empowering="I succeed through recognition and invitation. I guide with precision when I am seen, and I rest when I am between invitations. Grinding was Generator conditioning that I release with gratitude for what it taught me.",
                center="Design", gate=None, category="general",
                layer=1, day=self._next_day()
            ))
            self.beliefs.append(BeliefPair(
                limiting="If I stop pushing, everything I have built will collapse.",
                empowering="What I build from rest and invitation endures. What I built from borrowed energy served its purpose and can be released. I trust the foundation I create when I am aligned with my design.",
                center="Design", gate=None, category="general",
                layer=2, day=self._next_day()
            ))

        if m == "Fear":
            self.beliefs.append(BeliefPair(
                limiting="My fear is a malfunction I must suppress or overcome.",
                empowering="My fear is a compass. It points toward what needs my attention with clarity and precision. I follow it to understanding and then I move forward.",
                center="Design", gate=None, category="general",
                layer=2, day=self._next_day()
            ))

        if a == "Splenic":
            self.beliefs.append(BeliefPair(
                limiting="A gut feeling is not a valid reason for a decision.",
                empowering="My body knows instantly and speaks once. My instantaneous knowing is a complete answer. I trust what arrives in the moment without requiring justification.",
                center="Design", gate=None, category="general",
                layer=3, day=self._next_day()
            ))

    # ═══════════════════════════════════════════════════════════
    # HELPERS
    # ═══════════════════════════════════════════════════════════

    def _next_day(self) -> int:
        return (len(self.beliefs) // 5) + 1

    def _distill(self, beliefs: List[BeliefPair], max_beliefs: int = 50) -> List[BeliefPair]:
        distilled = []
        seen = set()
        quotas = {1: int(max_beliefs * 0.30), 2: int(max_beliefs * 0.25),
                   3: int(max_beliefs * 0.25), 4: int(max_beliefs * 0.20)}
        for layer in [1, 2, 3, 4]:
            layer_b = [b for b in beliefs if b.layer == layer]
            design = [b for b in layer_b if b.center == "Design"]
            centers = [b for b in layer_b if b.center not in ("Design",) and b.gate is None]
            gates = [b for b in layer_b if b.gate is not None]
            count = 0
            for b in design + centers + gates:
                if count >= quotas.get(layer, 10): break
                key = (b.layer, b.center, b.category, b.gate)
                if key not in seen:
                    distilled.append(b); seen.add(key); count += 1
        return distilled[:max_beliefs]

    # ═══════════════════════════════════════════════════════════
    # FORMATTER
    # ═══════════════════════════════════════════════════════════

    def format_markdown(self, tier: str = "comprehensive") -> str:
        lines = [
            f"# Belief Deprogrammer — Personalized Workbook",
            f"",
            f"**Generated for:** {self.chart.get('name', 'You')}",
            f"**Type:** {self.context.type} | **Authority:** {self.context.authority}",
            f"**Profile:** {self.context.profile} | **Cross:** {self.context.cross}",
            f"**Motivation:** {self.context.motivation} | **Cognition:** {self.context.cognition}",
            f"**Defined:** {', '.join(self.context.defined_centers)}",
            f"**Open:** {', '.join(self.context.undefined_centers)}",
            f"**Tier:** {tier} | **Beliefs:** {len(self.beliefs)}",
            f"",
            f"---",
            f"",
            f"## Your Belief Tree",
            f"",
            self._render_tree(),
            f"",
            f"---",
            f"",
            f"## How This Workbook Works",
            f"",
            f"Each pairing contains a limiting belief and its empowering replacement.",
            f"Work through **5 per day** following this protocol:",
            f"",
            f"1. **Read** the limiting belief aloud.",
            f"2. **Feel** where it lives in your body.",
            f"3. **Clear** it — scribble, tap, breathe, or your preferred modality.",
            f"4. **Read** the empowering belief aloud, slowly, **three times**.",
            f"5. **Pause.** Let your body register the shift.",
            f"",
            f"The workbook progresses through **4 layers** from deepest identity to daily thoughts:",
            f"",
        ]
        for layer in [1, 2, 3, 4]:
            lcount = len([b for b in self.beliefs if b.layer == layer])
            lines.append(f"**Layer {layer} — {LAYER_NAMES[layer]}** ({lcount} beliefs)")
            lines.append(f"> {LAYER_DESCRIPTIONS[layer]}")
            lines.append("")

        lines.extend(["---", ""])

        belief_num = 1
        by_layer = {1: [], 2: [], 3: [], 4: []}
        for b in self.beliefs:
            by_layer[b.layer].append(b)

        for layer in [1, 2, 3, 4]:
            if not by_layer[layer]: continue
            lines.append(f"## LAYER {layer}: {LAYER_NAMES[layer]}")
            lines.append("")
            by_day = {}
            for b in by_layer[layer]:
                if b.day not in by_day: by_day[b.day] = []
                by_day[b.day].append(b)
            for day in sorted(by_day.keys()):
                lines.append(f"### Day {day}")
                lines.append("")
                for b in by_day[day]:
                    gate_str = f" — Gate {b.gate} ({GATE_CONDITIONING[b.gate]['name']})" if b.gate and b.gate in GATE_CONDITIONING else ""
                    center_str = b.center if b.center != "Design" else "Your Design"
                    lines.append(f"#### Belief {belief_num}")
                    lines.append(f"*Layer {b.layer} | {center_str}{gate_str} | {b.category}*")
                    lines.append("")
                    lines.append(f"**Limiting:** \"{b.limiting}\"")
                    lines.append("")
                    lines.append(f"**Empowering:** \"{b.empowering}\"")
                    lines.append("")
                    lines.append("---")
                    lines.append("")
                    belief_num += 1
        lines.append("")
        lines.append(f"*Generated by Belief Deprogrammer — {len(self.beliefs)} belief pairs across 4 layers*")
        return "\n".join(lines)

    def _render_tree(self) -> str:
        by_layer = {1: 0, 2: 0, 3: 0, 4: 0}
        for b in self.beliefs:
            by_layer[b.layer] = by_layer.get(b.layer, 0) + 1
        return "\n".join([
            "```",
            f"                    ┌──────────────────────────┐",
            f"                    │  LAYER 4: NEGATIVE       │",
            f"                    │  PROGRAMS                │",
            f"                    │  {by_layer[4]:>4} daily thoughts      │",
            f"                    └────────────┬─────────────┘",
            f"                                 │",
            f"                    ┌────────────▼─────────────┐",
            f"                    │  LAYER 3: LIMITING        │",
            f"                    │  BELIEFS                  │",
            f"                    │  {by_layer[3]:>4} specific 'shoulds'   │",
            f"                    └────────────┬─────────────┘",
            f"                                 │",
            f"                    ┌────────────▼─────────────┐",
            f"                    │  LAYER 2: FAULTY CORE     │",
            f"                    │  BELIEFS                  │",
            f"                    │  {by_layer[2]:>4} structural beliefs    │",
            f"                    └────────────┬─────────────┘",
            f"                                 │",
            f"                    ┌────────────▼─────────────┐",
            f"                    │  LAYER 1: FAULTY CORE     │",
            f"                    │  IDENTITY                 │",
            f"                    │  {by_layer[1]:>4} 'I am...' beliefs     │",
            f"                    └──────────────────────────┘",
            f"  Progression: Layer 1 → 4 (identity → daily chatter)",
            f"```",
        ])
