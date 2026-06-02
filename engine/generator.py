"""
Belief Deprogrammer — Main Generation Engine (v2.0 — 4-Layer Tree Model)

Takes a Human Design chart JSON and generates a personalized belief workbook
organized by depth, following the integrated tree model:

  Layer 1 (SOIL):  Faulty Core Identity — "I am broken."     (center-level, who you ARE)
  Layer 2 (ROOTS): Faulty Core Beliefs  — "My worth = output" (gate general, structural)
  Layer 3 (TRUNK): Limiting Beliefs     — "I should work 8hrs"(gate × categories, rules)
  Layer 4 (LEAVES):Negative Programs    — "I'm so lazy..."    (auto-thoughts, daily chatter)

Users progress from deepest identity → through structural beliefs → to daily thoughts.
This creates an ARC: you've finished when your inner monologue changes.

Integrated methodologies:
  - Bradley Nelson's Belief Code tree model (soil→roots→trunk→branches)
  - Allie Duzett's 30 Days of Belief Work (5 beliefs/day, present-tense positive)
  - Human Design center mechanics (open centers × hanging gates × conditioning)
"""

from typing import Dict, List, Tuple, Optional
from engine.gate_themes import GATE_CONDITIONING, CATEGORIES, CATEGORY_DESCRIPTIONS
from engine.context_injector import DesignContext

# ── Layer Definitions ──────────────────────────────────────────

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
       "These are the 'rules' your system runs on.",
    3: "The specific 'shoulds,' 'musts,' and 'can'ts' that govern your daily choices. "
       "These feel personal and real — but they are distortions of energy that was "
       "never yours. Each one traces back to a gate you absorbed.",
    4: "The automatic thoughts — the constant inner chatter. 'I'm so lazy.' 'Why can't "
       "I just...' 'Something is wrong with me.' These are symptoms, not causes. "
       "When the layers above clear, these dissolve on their own.",
}

# Center-to-gate mapping
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
    """A single limiting → empowering belief pair with depth layer."""

    def __init__(self, limiting: str, empowering: str, center: str, gate: Optional[int],
                 category: str, layer: int, day: int):
        self.limiting = limiting
        self.empowering = empowering
        self.center = center
        self.gate = gate
        self.category = category
        self.layer = layer
        self.day = day

    @property
    def layer_name(self) -> str:
        return LAYER_NAMES.get(self.layer, f"Layer {self.layer}")


class WorkbookGenerator:
    """Main belief workbook generator with 4-layer tree model."""

    def __init__(self, chart: dict):
        self.chart = chart
        self.context = DesignContext(chart)
        self.beliefs: List[BeliefPair] = []
        self._belief_count = 0

    # ═══════════════════════════════════════════════════════════
    # MAIN GENERATION
    # ═══════════════════════════════════════════════════════════

    def generate(self, tier: str = "comprehensive") -> List[BeliefPair]:
        """Generate the full 4-layer belief workbook."""
        hanging = self.context.get_hanging_gates(CENTER_GATES)

        # ═══ LAYER 1: SOIL — Faulty Core Identity ═══
        for center in self.context.undefined_centers:
            self._generate_layer1_identity(center)

        # ═══ LAYER 2: ROOTS — Faulty Core Beliefs ═══
        for center in self.context.undefined_centers:
            if center in hanging:
                for gate in hanging[center]:
                    if gate in GATE_CONDITIONING:
                        self._generate_layer2_core_beliefs(center, gate)

        # ═══ LAYER 3: TRUNK — Limiting Beliefs ═══
        for center in self.context.undefined_centers:
            if center in hanging:
                for gate in hanging[center]:
                    if gate in GATE_CONDITIONING:
                        self._generate_layer3_limiting_beliefs(center, gate, tier)

        # ═══ LAYER 4: LEAVES — Negative Programs ═══
        for center in self.context.undefined_centers:
            if center in hanging:
                for gate in hanging[center]:
                    if gate in GATE_CONDITIONING:
                        self._generate_layer4_negative_programs(center, gate, tier)

        # Cross-center interactions (mixed layers)
        self._generate_cross_center_beliefs()

        # Design-specific beliefs (identity layer)
        self._generate_design_beliefs()

        # Short tier: distill across all layers
        if tier == "short":
            self.beliefs = self._distill(self.beliefs, max_beliefs=50)

        return self.beliefs

    # ═══════════════════════════════════════════════════════════
    # LAYER 1: SOIL — Core Identity ("I am...")
    # ═══════════════════════════════════════════════════════════

    def _generate_layer1_identity(self, center: str):
        """Generate the deepest identity-level beliefs for an open center.

        These are the "I AM" statements — beliefs about who you are at your core,
        absorbed in childhood before conscious questioning was possible.
        """
        ctx = self.context.empowering_for_center(center)
        identities = self._center_identity_themes(center)

        for limiting, empowering in identities:
            self.beliefs.append(BeliefPair(
                limiting=limiting.format(**ctx),
                empowering=empowering.format(**ctx),
                center=center, gate=None, category="general",
                layer=1, day=self._next_day()
            ))

    def _center_identity_themes(self, center: str) -> List[Tuple[str, str]]:
        """Deep identity-level limiting/empowering pairs per open center."""
        themes = {
            "Head": [
                ("At my core, I am confused. Other people seem to know what matters — I never do.",
                 "{type_phrase} My open Head receives the world's questions. I am not confused at my core — I am receptive. The questions that matter most will find me when my mind is still."),
                ("I am not a deep thinker. My mind is scattered and unreliable.",
                 "{type_phrase} My open Head amplifies mental energy from everywhere. I am not scattered — I am panoramic. I see connections others miss because I hold multiple questions at once."),
                ("I am fundamentally uncertain. Everyone else has convictions I can't access.",
                 "{type_phrase} Uncertainty is not a flaw in my design — it is my design. My open Head keeps me curious when others calcify. I release the need to have answers."),
            ],
            "Ajna": [
                ("I am indecisive at my core. I can't commit to anything because I don't really know what I believe.",
                 "{type_phrase} My open Ajna processes multiple truths. I am not indecisive — I am spacious. My mind holds complexity that fixed minds cannot."),
                ("I am not an intellectual. My thoughts aren't structured or impressive.",
                 "{type_phrase} My open Ajna reflects mental diversity. I don't need rigid structure to be intelligent. My knowing arrives through synthesis, not through narrowing."),
                ("I am mentally inferior. Other people's thinking is sharper and more certain.",
                 "{type_phrase} My open Ajna is not inferior — it is adaptive. I think fluidly because I'm not trapped in one framework. Flexibility is my intellectual gift."),
            ],
            "Sacral": [
                ("I am fundamentally incapable. I can't sustain anything — work, relationships, projects. I'm broken.",
                 "{type_phrase} {center_truth} I am not broken — I am designed differently. A scalpel is not a broken bulldozer. It is precise because it stops."),
                ("I am lazy. That's the truth about me that I've been hiding from.",
                 "{type_phrase} I am not lazy — I am a being without a Sacral motor. What looks like laziness is actually my body enforcing a boundary my Generator conditioning keeps overriding."),
                ("I am less valuable than people who can produce consistently.",
                 "{type_phrase} My value is not in output. I am a Projector — I am here to see, to guide, to recognize. What I produce in five aligned minutes exceeds their five forced hours."),
            ],
            "Solar Plexus": [
                ("I am emotionally unstable. I feel everything too deeply and it ruins things.",
                 "{type_phrase} My open Solar Plexus amplifies the emotional field. I am not unstable — I am exquisitely sensitive. What I feel is real, but not everything I feel is mine."),
                ("I am the cause of conflict. Wherever I go, tension follows — it must be me.",
                 "{type_phrase} I do not create conflict — I detect it before others do. My open Solar Plexus feels tension that already exists. I release the responsibility I was never given."),
                ("I am doomed to ride emotional waves that aren't even mine forever.",
                 "{type_phrase} I feel the collective wave, but I am not the wave. My {authority_phrase} guides me through emotional terrain that I was never meant to claim as my own."),
            ],
            "Root": [
                ("I am a restless person who can never settle. Peace is not in my nature.",
                 "{type_phrase} My open Root amplifies urgency from the entire field. I am not restless by nature — I am sensitized to borrowed pressure. Stillness is my birthright."),
                ("I am always behind. Everyone else moves forward while I spin in place.",
                 "{type_phrase} I am not behind. I am a Projector on Projector time. My pace is correct when I move from invitation, not from pressure. The race was never mine."),
                ("I am fundamentally unable to handle pressure.",
                 "{type_phrase} I handle pressure brilliantly — when it's mine. What I can't handle is EVERYONE'S pressure at once. I release urgency that was never addressed to me."),
            ],
            "Heart/Ego": [
                ("I am not worthy. I have nothing of value to offer and I never will.",
                 "{type_phrase} My open Heart amplifies worthiness questions from the collective. I am not unworthy — I am an amplifier. My value is inherent, not proven. I release the need to earn my existence."),
                ("I am weak-willed. I can't commit to anything or follow through.",
                 "{type_phrase} My open Heart absorbs willpower from others. I am not weak — I am non-resistant. I commit when my {authority_phrase} says yes, not when pressure says should."),
            ],
            "Spleen": [
                ("I am unsafe. I can't trust my instincts because they're always wrong.",
                 "{type_phrase} My open Spleen amplifies fear from the environment. I am not unsafe — I am vigilant. I distinguish between real danger and absorbed anxiety. My body knows the difference."),
                ("I am not intuitive. Other people just know things — I never do.",
                 "{type_phrase} My open Spleen picks up everyone's intuitive hits. What feels like 'not knowing' is actually 'knowing too much at once.' I learn to discern my signal from the noise."),
            ],
            "G": [
                ("I don't know who I am. I have no fixed identity and that terrifies me.",
                 "{type_phrase} My open G reflects identity from my environment. I am not identity-less — I am identity-fluid. I find myself through the right people and places, not through forcing a fixed self."),
                ("I have no direction. Everyone else seems to know where they're going.",
                 "{type_phrase} My open G receives direction from life itself. I don't need a fixed compass — I need the right invitations. My path reveals itself when I stop forcing it."),
            ],
        }
        return themes.get(center, [
            (f"I am incomplete because my {center} is undefined.",
             f"{{type_phrase}} My open {center} is not a hole — it is a receiver. What I take in becomes wisdom. What I release was never mine. I am complete as I am."),
        ])

    # ═══════════════════════════════════════════════════════════
    # LAYER 2: ROOTS — Core Beliefs (structural, "My worth depends on...")
    # ═══════════════════════════════════════════════════════════

    def _generate_layer2_core_beliefs(self, center: str, gate: int):
        """Generate structural core beliefs from a hanging gate's distortion theme.

        These are the 'rules' — beliefs about how the world works that spread
        from the core identity layer. 'My worth depends on output.' 'I must earn rest.'
        """
        gate_data = GATE_CONDITIONING.get(gate)
        if not gate_data:
            return

        ctx = self.context.empowering_for_center(center, gate)
        gate_name = gate_data["name"]
        dist_short = gate_data["distortion"].split('.')[0]

        # Layer 2: 3 core beliefs blending identity truth with gate distortion
        core_beliefs = [
            (
                f"Because of who I am, I believe my worth depends on how I handle the {gate_name} energy I carry.",
                f"My worth is independent of any energy I absorb. {ctx.get('center_truth', '')} The {gate_name} pattern was never mine to perform. I release the belief that my value is performance-based."
            ),
            (
                f"The {gate_name} distortion has convinced me that {dist_short.lower()}. This feels like a fundamental law of my existence.",
                f"{ctx.get('type_phrase', '')} What feels like a law is actually conditioning. The {gate_name} energy I absorbed created a false rule. I don't live by rules that were written by other people's energy."
            ),
            (
                f"I have built my understanding of how life works around the {gate_name} pattern. My operating system runs on the belief that {dist_short.lower()}.",
                f"I am rewriting my operating system. {ctx.get('authority_phrase', '')} The {gate_name} energy is a signal I received, not a truth I must embody. I uninstall programs I didn't write."
            ),
        ]

        for limiting, empowering in core_beliefs:
            self.beliefs.append(BeliefPair(
                limiting=limiting.format(**ctx),
                empowering=empowering.format(**ctx),
                center=center, gate=gate, category="general",
                layer=2, day=self._next_day()
            ))

    # ═══════════════════════════════════════════════════════════
    # LAYER 3: TRUNK — Limiting Beliefs (specific "shoulds")
    # ═══════════════════════════════════════════════════════════

    def _generate_layer3_limiting_beliefs(self, center: str, gate: int, tier: str):
        """Generate specific limiting beliefs across categories.

        These are the 'I should...' 'I must...' 'I can't...' rules that govern
        daily choices. Each traces back to a specific gate distortion.
        """
        gate_data = GATE_CONDITIONING.get(gate)
        if not gate_data:
            return

        distortion = gate_data["distortion"]
        ctx = self.context.empowering_for_center(center, gate)
        gate_name = gate_data["name"]
        count = 2 if tier == "comprehensive" else 1

        for category in CATEGORIES:
            limiting_beliefs = self._expand_to_category(
                distortion, category, center, gate, gate_name, count
            )
            for lb in limiting_beliefs:
                empowering = self._craft_empowering(lb, ctx, center, gate)
                self.beliefs.append(BeliefPair(
                    limiting=lb.format(**ctx),
                    empowering=empowering.format(**ctx),
                    center=center, gate=gate, category=category,
                    layer=3, day=self._next_day()
                ))

    # ═══════════════════════════════════════════════════════════
    # LAYER 4: LEAVES — Negative Programs (daily self-talk)
    # ═══════════════════════════════════════════════════════════

    def _generate_layer4_negative_programs(self, center: str, gate: int, tier: str):
        """Generate negative program beliefs — daily automatic self-talk.

        These are the surface-level thoughts that run on loop: 'I'm so lazy.'
        'Why can't I just push through?' 'Something is wrong with me.'
        They are symptoms of the deeper layers, not causes.
        """
        gate_data = GATE_CONDITIONING.get(gate)
        if not gate_data:
            return

        ctx = self.context.empowering_for_center(center, gate)
        gate_name = gate_data["name"]
        dist_short = gate_data["distortion"].split('.')[0]

        # Layer 4: 3-5 daily self-talk variants
        negative_talks = [
            (f"I'm so bad at managing {gate_name} energy. Why can't I just be normal?",
             f"I am not supposed to manage {gate_name} energy — I am supposed to recognize it as NOT MINE. It's not a skill deficit. It's a design feature. {ctx.get('center_truth', '')}"),
            (f"Everyone else handles {gate_name} energy fine. What's wrong with me?",
             f"Everyone else has a different design. I compare my open {center} to their defined ones — which is like comparing a radio receiver to a radio station. Both work. Differently."),
            (f"I keep repeating the same {gate_name} pattern. I'll never change.",
             f"Repeating a pattern doesn't mean I'm broken — it means the pattern is DEEP. {ctx.get('type_phrase', '')} I am undoing layers that took decades to form. Progress is not linear. Every time I catch it, I loosen it."),
            (f"The {gate_name} energy makes me feel like {dist_short[:60].lower().strip()} and I hate this about myself.",
             f"What I hate is not me — it's the distortion. The {gate_name} energy, when expressed authentically, is a gift. The distortion came from absorption, not from essence. I separate the two."),
        ]

        count = len(negative_talks) if tier == "comprehensive" else 2
        for limiting, empowering in negative_talks[:count]:
            self.beliefs.append(BeliefPair(
                limiting=limiting.format(**ctx),
                empowering=empowering.format(**ctx),
                center=center, gate=gate, category="general",
                layer=4, day=self._next_day()
            ))

    # ═══════════════════════════════════════════════════════════
    # CROSS-CENTER + DESIGN BELIEFS
    # ═══════════════════════════════════════════════════════════

    def _generate_cross_center_beliefs(self):
        """Cross-center interactions — layer 2-3."""
        undefined = set(self.context.undefined_centers)

        if "Sacral" in undefined and "Root" in undefined:
            self.beliefs.append(BeliefPair(
                limiting="My worth depends on how much I produce, and I feel constant panic that I'm not producing enough.",
                empowering=f"{self.context.type_phrase} I absorb urgency (open Root) + life force (open Sacral) that aren't mine. My worth was never in my output. I release the pressure that was never mine.",
                center="Sacral+Root", gate=None, category="general",
                layer=2, day=self._next_day()
            ))

        if "Solar Plexus" in undefined and "Ajna" in undefined:
            self.beliefs.append(BeliefPair(
                limiting="I have to process my emotions intellectually until they make sense, or I'll make a terrible decision.",
                empowering=f"{self.context.authority_phrase} Feelings don't need mental approval. My open Solar Plexus amplifies emotion; my open Ajna amplifies thought. Neither needs to dominate.",
                center="Solar Plexus+Ajna", gate=None, category="general",
                layer=3, day=self._next_day()
            ))

        if "Head" in undefined and "Root" in undefined:
            self.beliefs.append(BeliefPair(
                limiting="Questions demand immediate answers, and I must act on the answers immediately. I'm trapped between mental and physical pressure.",
                empowering=f"{self.context.type_phrase} Mental pressure (open Head) + physical pressure (open Root) create urgency that isn't real. I breathe. I release the question AND the urgency.",
                center="Head+Root", gate=None, category="general",
                layer=2, day=self._next_day()
            ))

    def _generate_design_beliefs(self):
        """Design-specific beliefs — layer 1-2."""
        if self.context.type == "Projector":
            self.beliefs.append(BeliefPair(
                limiting="I am destined to be overlooked unless I force my way in. Success requires grinding harder than everyone else.",
                empowering="I am a Projector. I don't grind — I see. My success arrives through recognition and invitation, not through force. Waiting is strategy. Grinding is Generator conditioning that I release now.",
                center="Design", gate=None, category="general",
                layer=1, day=self._next_day()
            ))
            self.beliefs.append(BeliefPair(
                limiting="If I stop pushing, everything will fall apart and I'll lose everything I've built.",
                empowering="What is built on borrowed energy crumbles. What is built on invitation endures. I stop pushing not because I give up, but because I finally trust my design. My rest is productive.",
                center="Design", gate=None, category="general",
                layer=2, day=self._next_day()
            ))

        if self.context.motivation == "Fear":
            self.beliefs.append(BeliefPair(
                limiting="My fear is a malfunction. I need to suppress it or overcome it to be successful.",
                empowering=f"{self.context.motivation_phrase} Fear is not my enemy — it is my compass. It shows me what needs my attention. I don't suppress it. I follow it to clarity, and then I move.",
                center="Design", gate=None, category="general",
                layer=2, day=self._next_day()
            ))

        if self.context.authority == "Splenic":
            self.beliefs.append(BeliefPair(
                limiting="A gut feeling isn't a real decision. I need logic and evidence to justify everything.",
                empowering="My Splenic authority is instantaneous truth. It speaks once, quietly, and it never repeats itself. 'I know because I know' is complete. I don't owe anyone a thesis on my intuition.",
                center="Design", gate=None, category="general",
                layer=3, day=self._next_day()
            ))

    # ═══════════════════════════════════════════════════════════
    # CATEGORY EXPANSION (Layer 3 helper)
    # ═══════════════════════════════════════════════════════════

    def _expand_to_category(self, distortion: str, category: str, center: str,
                            gate: int, gate_name: str, count: int) -> List[str]:
        """Expand gate distortion into category-specific limiting beliefs."""
        dist_short = distortion.split('.')[0] if '.' in distortion else distortion

        if category == "general":
            return [
                f"I have absorbed the {gate_name} energy of others and believed it was my own — {dist_short.lower()}",
                f"My open {center} picks up {gate_name} energy from everyone around me, and I have mistaken this amplification for my personal truth.",
            ][:count]

        patterns = {
            "environmental": [
                f"Growing up, the environments I was in rewarded the {gate_name} pattern — I learned that {dist_short.lower()}",
                f"Every workplace and school I attended reinforced the belief that {dist_short.lower()}",
            ],
            "generational": [
                f"This runs in my family line. My ancestors carried the {gate_name} energy, and I inherited the belief that {dist_short.lower()}",
                f"Generations before me survived through this pattern. I absorbed, without consent, the belief that {dist_short.lower()}",
            ],
            "physical": [
                f"My body stores the {gate_name} pattern physically. I feel it as tension, fatigue, or restlessness — my body learned to believe {dist_short.lower()}",
                f"My nervous system was trained by this {gate_name} amplification. Physically, I react as if {dist_short.lower()}",
            ],
            "mental": [
                f"My mind loops on the {gate_name} pattern. I catch myself thinking: '{dist_short}'",
                f"The mental framework I operate from was built on absorbed {gate_name} energy. My thoughts tell me {dist_short.lower()}",
            ],
            "spiritual": [
                f"On a spiritual level, I have believed the {gate_name} distortion is my purpose — as if I was meant to carry {dist_short.lower()}",
                f"My sense of existential meaning got tangled with {gate_name} energy. Spiritually, I have felt that {dist_short.lower()}",
            ],
            "subconscious": [
                f"Below my conscious awareness, the {gate_name} distortion runs automatically. My subconscious operates as if {dist_short.lower()}",
                f"Without my permission, the {gate_name} pattern drives my choices. A hidden program says {dist_short.lower()}",
            ],
            "conscious": [
                f"I see this {gate_name} pattern clearly and still feel stuck in it. I consciously know I believe {dist_short.lower()}, and I have not known how to release it.",
                f"I am aware of the {gate_name} distortion — I can feel it operating — and I have felt powerless to change it.",
            ],
            "absorbed": [
                f"Specific people in my life imprinted the {gate_name} energy on me. I absorbed from them the belief that {dist_short.lower()}",
                f"A formative relationship transferred the {gate_name} distortion into me. From that person, I absorbed the belief that {dist_short.lower()}",
            ],
        }

        return patterns.get(category, [f"I believe {dist_short.lower()}"])[:count]

    def _craft_empowering(self, limiting: str, ctx: dict, center: str,
                          gate: Optional[int] = None) -> str:
        """Craft an empowering counter-belief using personal design context."""
        parts = [
            ctx.get("type_phrase", ""),
            ctx.get("center_truth", ""),
            ctx.get("authority_phrase", ""),
        ]
        if ctx.get("motivation_phrase"):
            parts.append(ctx["motivation_phrase"])

        empowering = ". ".join(p for p in parts if p)

        if gate and gate in GATE_CONDITIONING:
            gate_name = GATE_CONDITIONING[gate]["name"]
            empowering += f" The {gate_name} energy I carry is a gift, not a distortion — when I honor my design, it expresses authentically."

        empowering += " I release what was never mine. I am correct as I am."
        return empowering

    # ═══════════════════════════════════════════════════════════
    # TIER DISTILLATION (preserves layer balance)
    # ═══════════════════════════════════════════════════════════

    def _next_day(self) -> int:
        return (len(self.beliefs) // 5) + 1

    def _distill(self, beliefs: List[BeliefPair], max_beliefs: int = 50) -> List[BeliefPair]:
        """Distill to short tier while preserving layer proportions."""
        distilled = []
        seen = set()

        # Layer proportions for short tier: 30% L1, 25% L2, 25% L3, 20% L4
        quotas = {
            1: int(max_beliefs * 0.30),
            2: int(max_beliefs * 0.25),
            3: int(max_beliefs * 0.25),
            4: int(max_beliefs * 0.20),
        }

        for layer in [1, 2, 3, 4]:
            layer_beliefs = [b for b in beliefs if b.layer == layer]
            # Take design-first, then center-level, then gate-specific
            design = [b for b in layer_beliefs if b.center == "Design"]
            centers = [b for b in layer_beliefs if b.center not in ("Design",) and b.gate is None]
            gates = [b for b in layer_beliefs if b.gate is not None]

            count = 0
            for b in design + centers + gates:
                if count >= quotas.get(layer, 10):
                    break
                key = (b.layer, b.center, b.category, b.gate)
                if key not in seen:
                    distilled.append(b)
                    seen.add(key)
                    count += 1

        return distilled[:max_beliefs]

    # ═══════════════════════════════════════════════════════════
    # WORKBOOK FORMATTER (layered progression)
    # ═══════════════════════════════════════════════════════════

    def format_markdown(self, tier: str = "comprehensive") -> str:
        """Format the workbook with 4-layer progression."""
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
            f"This workbook is organized in **4 layers**, working from the deepest "
            f"conditioning to the surface-level chatter:",
            f"",
        ]

        for layer in [1, 2, 3, 4]:
            lines.append(f"**Layer {layer}:** {LAYER_NAMES[layer]}")
            lines.append(f"> {LAYER_DESCRIPTIONS[layer]}")
            lines.append("")

        lines.extend([
            f"Each day, you'll work through **5 belief pairs**:",
            f"",
            f"1. **Read** the limiting belief aloud.",
            f"2. **Feel** where it lives in your body.",
            f"3. **Clear** it — scribble, tap, breathe, or your preferred modality.",
            f"4. **Read** the empowering belief aloud, slowly, **three times**.",
            f"5. **Pause.** Let your body register the shift.",
            f"",
            f"You'll start at **Layer 1 — Core Identity** and work DOWN through "
            f"the tree. By the time you reach Layer 4, the daily negative programs "
            f"will be dissolving from the root, not just being managed at the surface.",
            f"",
            "---",
            "",
        ])

        # Group beliefs by layer, then by day within each layer
        belief_num = 1
        by_layer = {1: [], 2: [], 3: [], 4: []}
        for b in self.beliefs:
            by_layer[b.layer].append(b)

        for layer in [1, 2, 3, 4]:
            layer_beliefs = by_layer[layer]
            if not layer_beliefs:
                continue

            lines.append(f"## LAYER {layer}: {LAYER_NAMES[layer]}")
            lines.append("")
            lines.append(f"*{LAYER_DESCRIPTIONS[layer]}*")
            lines.append("")

            # Group by day
            by_day = {}
            for b in layer_beliefs:
                if b.day not in by_day:
                    by_day[b.day] = []
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
        """Render the belief tree visualization as ASCII art."""
        total = len(self.beliefs)
        by_layer = {1: 0, 2: 0, 3: 0, 4: 0}
        for b in self.beliefs:
            by_layer[b.layer] = by_layer.get(b.layer, 0) + 1

        tree = [
            f"```",
            f"                    ┌──────────────────────────┐",
            f"                    │  LAYER 4: NEGATIVE       │",
            f"                    │  PROGRAMS                │",
            f"                    │  {by_layer[4]:>4} daily thoughts      │",
            f"                    │  'I'm so lazy...'        │",
            f"                    └────────────┬─────────────┘",
            f"                                 │",
            f"                    ┌────────────▼─────────────┐",
            f"                    │  LAYER 3: LIMITING        │",
            f"                    │  BELIEFS                  │",
            f"                    │  {by_layer[3]:>4} 'shoulds' & rules     │",
            f"                    │  'I must work harder...'  │",
            f"                    └────────────┬─────────────┘",
            f"                                 │",
            f"                    ┌────────────▼─────────────┐",
            f"                    │  LAYER 2: FAULTY CORE     │",
            f"                    │  BELIEFS                  │",
            f"                    │  {by_layer[2]:>4} structural beliefs    │",
            f"                    │  'My worth = output...'   │",
            f"                    └────────────┬─────────────┘",
            f"                                 │",
            f"                    ┌────────────▼─────────────┐",
            f"                    │  LAYER 1: FAULTY CORE     │",
            f"                    │  IDENTITY                 │",
            f"                    │  {by_layer[1]:>4} 'I am...' beliefs     │",
            f"                    │  'I am broken...'         │",
            f"                    └──────────────────────────┘",
            f"",
            f"  Source: {len(self.context.undefined_centers)} open centers × {len([b for b in self.beliefs if b.gate])//len(self.context.undefined_centers) if self.context.undefined_centers else 0} hanging gates",
            f"  Progression: Layer 1 → Layer 4 (identity → daily thoughts)",
            f"```",
        ]
        return "\n".join(tree)
