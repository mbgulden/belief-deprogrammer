"""
Belief Deprogrammer — Main Generation Engine

Takes a Human Design chart JSON and generates a personalized belief workbook.

Architecture:
  chart → extract(open_centers, hanging_gates, design_context)
        → for each open center × hanging gate × category:
            → generate limiting belief (from gate distortion theme)
            → generate empowering belief (from personal design context)
        → add cross-center interactions
        → add design-specific beliefs
        → format as workbook (markdown → PDF/JSON)

Output tiers:
  - short: 30-50 core beliefs for rapid reset
  - comprehensive: 600-1000+ beliefs for complete deconditioning
"""

from typing import Dict, List, Tuple, Optional
from engine.gate_themes import GATE_CONDITIONING, CATEGORIES, CATEGORY_DESCRIPTIONS
from engine.context_injector import DesignContext

# Center-to-gate mapping (which gates belong to which center)
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

# Category-specific expansion patterns — how a gate distortion manifests in each domain
CATEGORY_EXPANSIONS = {
    "environmental": "I absorbed this from {source}. My environment taught me that {distortion}",
    "generational": "This runs in my lineage. {ancestor_pattern}. I inherited the belief that {distortion}",
    "physical": "My body holds this. I feel {sensation} when {trigger}. My body learned that {distortion}",
    "mental": "My mind loops on this. I catch myself thinking '{thought}'. This mental pattern says {distortion}",
    "spiritual": "This touches my purpose. I've believed that spiritually, {spiritual_belief}. This says {distortion}",
    "subconscious": "This operates below my awareness. Without realizing it, I {behavior}. Underneath, I believe {distortion}",
    "conscious": "I know this one. I'm aware I {aware_behavior}, but I feel stuck. I consciously believe {distortion}",
    "absorbed": "I picked this up from {person}. Their {trait} became my belief that {distortion}",
}


class BeliefPair:
    """A single limiting → empowering belief pair."""

    def __init__(self, limiting: str, empowering: str, center: str, gate: Optional[int],
                 category: str, day: int):
        self.limiting = limiting
        self.empowering = empowering
        self.center = center
        self.gate = gate
        self.category = category
        self.day = day

    def to_markdown(self, index: int) -> str:
        gate_str = f"Gate {self.gate} — " if self.gate else ""
        return (
            f"### Belief {index}\n"
            f"**Limiting:** \"{self.limiting}\"\n"
            f"**Empowering:** \"{self.empowering}\"\n"
        )


class WorkbookGenerator:
    """Main belief workbook generator."""

    def __init__(self, chart: dict):
        self.chart = chart
        self.context = DesignContext(chart)
        self.beliefs: List[BeliefPair] = []
        self.day_counter = 1

    def generate(self, tier: str = "comprehensive") -> List[BeliefPair]:
        """Generate the full belief workbook."""
        # Step 1: Identify hanging gates in open centers
        hanging = self.context.get_hanging_gates(CENTER_GATES)

        # Step 2: Generate center-level beliefs (for completely open centers too)
        for center in self.context.undefined_centers:
            self._generate_center_beliefs(center)
            # Gate-specific beliefs
            if center in hanging:
                for gate in hanging[center]:
                    if gate in GATE_CONDITIONING:
                        self._generate_gate_beliefs(center, gate, tier)

        # Step 3: Cross-center interactions
        self._generate_cross_center_beliefs()

        # Step 4: Design-specific beliefs
        self._generate_design_beliefs()

        # Step 5: If short tier, distill
        if tier == "short":
            self.beliefs = self._distill(self.beliefs, max_beliefs=50)

        return self.beliefs

    def _generate_center_beliefs(self, center: str):
        """Generate core beliefs for an open center (trunk level)."""
        ctx = self.context.empowering_for_center(center)
        center_themes = self._center_core_themes(center)

        for i, (limiting, empowering) in enumerate(center_themes):
            # Only general category for center-level beliefs
            self.beliefs.append(BeliefPair(
                limiting=limiting.format(**ctx),
                empowering=empowering.format(**ctx),
                center=center, gate=None, category="general",
                day=self._next_day()
            ))

    def _generate_gate_beliefs(self, center: str, gate: int, tier: str):
        """Generate beliefs for a specific hanging gate across all categories."""
        gate_data = GATE_CONDITIONING.get(gate)
        if not gate_data:
            return

        distortion = gate_data["distortion"]
        ctx = self.context.empowering_for_center(center, gate)
        gate_name = gate_data["name"]

        # How many categories to cover
        categories_to_cover = CATEGORIES
        beliefs_per_category = 3 if tier == "comprehensive" else 1

        for category in categories_to_cover:
            limiting_beliefs = self._expand_to_category(
                distortion, category, center, gate, gate_name, beliefs_per_category
            )
            for lb in limiting_beliefs:
                empowering = self._craft_empowering(lb, ctx, center, gate)
                self.beliefs.append(BeliefPair(
                    limiting=lb.format(**ctx),
                    empowering=empowering.format(**ctx),
                    center=center, gate=gate, category=category,
                    day=self._next_day()
                ))

    def _expand_to_category(self, distortion: str, category: str, center: str,
                            gate: int, gate_name: str, count: int) -> List[str]:
        """Expand a gate distortion into category-specific limiting beliefs.
        
        Each limiting belief is a complete, natural-sounding sentence — not a
        template fragment with raw distortion text injected.
        """
        # Distill the distortion into shorter key themes for sentence construction
        distortion_short = distortion.split('.')[0] if '.' in distortion else distortion

        if category == "general":
            return [
                f"I have absorbed the {gate_name} energy of others and believed it was my own — {distortion_short.lower()}",
                f"My open {center} picks up {gate_name} energy from everyone around me, and I have mistaken this amplification for my personal truth.",
                f"For years, I identified with the {gate_name} pattern — but it was never mine. I absorbed it and called it me.",
            ][:count]

        patterns = {
            "environmental": [
                f"Growing up, the environments I was in rewarded the {gate_name} pattern — I learned that {distortion_short.lower()}",
                f"Every workplace and school I attended reinforced the belief that {distortion_short.lower()}",
                f"The physical spaces I've occupied taught me, silently and persistently, that {distortion_short.lower()}",
            ],
            "generational": [
                f"This runs in my family line. My ancestors carried the {gate_name} energy, and I inherited the belief that {distortion_short.lower()}",
                f"Generations before me survived through this pattern. I absorbed, without consent, the belief that {distortion_short.lower()}",
                f"My lineage imprinted me with the {gate_name} distortion. I carry the inherited belief that {distortion_short.lower()}",
            ],
            "physical": [
                f"My body stores the {gate_name} pattern physically. I feel it as tension, fatigue, or restlessness — my body learned to believe {distortion_short.lower()}",
                f"When I check in with my physical self, I find the {gate_name} distortion lodged in my tissues. My body holds the belief that {distortion_short.lower()}",
                f"My nervous system was trained by this {gate_name} amplification. Physically, I react as if {distortion_short.lower()}",
            ],
            "mental": [
                f"My mind loops on the {gate_name} pattern. I catch myself thinking: '{distortion_short}'",
                f"Intellectually, I have organized my understanding of myself around the {gate_name} distortion — I think I am someone who {distortion_short.lower()}",
                f"The mental framework I operate from was built on absorbed {gate_name} energy. My thoughts tell me {distortion_short.lower()}",
            ],
            "spiritual": [
                f"On a spiritual level, I have believed the {gate_name} distortion is my purpose — as if I was meant to carry {distortion_short.lower()}",
                f"My sense of existential meaning got tangled with {gate_name} energy. Spiritually, I have felt that {distortion_short.lower()}",
                f"I have carried the {gate_name} pattern as if it were a soul contract. Deep down, I believed {distortion_short.lower()}",
            ],
            "subconscious": [
                f"Below my conscious awareness, the {gate_name} distortion runs automatically. My subconscious operates as if {distortion_short.lower()}",
                f"Without my permission or awareness, the {gate_name} pattern drives my choices. I have been running a hidden program that says {distortion_short.lower()}",
                f"My shadow self absorbed the {gate_name} energy long ago. Subconsciously, I live as if {distortion_short.lower()}",
            ],
            "conscious": [
                f"I see this {gate_name} pattern clearly and still feel stuck in it. I consciously know I believe {distortion_short.lower()}, and I have not known how to release it.",
                f"I am aware of the {gate_name} distortion — I can feel it operating — and I have felt powerless to change the belief that {distortion_short.lower()}",
                f"This is not hidden from me. I recognize the {gate_name} pattern and I consciously hold the belief that {distortion_short.lower()}",
            ],
            "absorbed": [
                f"Specific people in my life imprinted the {gate_name} energy on me. I absorbed from them the belief that {distortion_short.lower()}",
                f"Someone I loved, respected, or feared modeled the {gate_name} pattern, and I internalized it — I absorbed the belief that {distortion_short.lower()}",
                f"A formative relationship transferred the {gate_name} distortion into me. From that person, I absorbed the belief that {distortion_short.lower()}",
            ],
        }

        return patterns.get(category, [f"I believe {distortion_short.lower()}"])[:count]

    def _craft_empowering(self, limiting: str, ctx: dict, center: str,
                          gate: Optional[int] = None) -> str:
        """Craft an empowering counter-belief using personal design context."""
        # Core structure: acknowledge the conditioning, then state the design truth
        parts = [
            ctx.get("type_phrase", ""),
            ctx.get("center_truth", ""),
            ctx.get("authority_phrase", ""),
        ]
        if ctx.get("motivation_phrase"):
            parts.append(ctx["motivation_phrase"])

        # Combine into empowering statement
        empowering = ". ".join(p for p in parts if p)

        # For specific gates, add gate-specific empowerment
        if gate and gate in GATE_CONDITIONING:
            gate_name = GATE_CONDITIONING[gate]["name"]
            empowering += f" The {gate_name} energy I carry is a gift, not a distortion — when I honor my design, it expresses authentically."

        empowering += " I release what was never mine. I am correct as I am."

        return empowering

    def _center_core_themes(self, center: str) -> List[Tuple[str, str]]:
        """Core trunk-level limiting/empowering pairs per open center."""
        themes = {
            "Head": [
                ("I must answer every question that enters my mind",
                 "{type_phrase} I don't need to resolve every question. My open {center} receives inquiry — I release what's not mine."),
                ("My confusion means I'm not smart enough",
                 "{type_phrase} My open {center} amplifies collective confusion. My intelligence is not measured by having all the answers."),
                ("I should be figuring something important out right now",
                 "{type_phrase} Mental pressure to 'figure it out' is amplified from others. I rest in not-knowing."),
            ],
            "Ajna": [
                ("I need to have fixed opinions and beliefs to be taken seriously",
                 "{type_phrase} My open {center} processes many perspectives. Flexibility is wisdom, not weakness."),
                ("My indecision means I'm broken",
                 "{type_phrase} My open {center} sees multiple truths simultaneously. I don't need false certainty to be whole."),
                ("I should know exactly what I believe",
                 "{type_phrase} Certainty is not required. My open {center} reflects mental diversity — that's my gift."),
            ],
            "Sacral": [
                ("I should be able to sustain output like other people",
                 "{type_phrase} {center_truth} My exhaustion is accurate feedback, not failure."),
                ("Rest must be earned through visible productivity",
                 "{type_phrase} Rest is my birthright. I was never given sacral fuel — I was given vision."),
                ("Something is wrong with me because I can't keep going",
                 "{type_phrase} My design is a scalpel, not a bulldozer. I am precisely built for short, deep impact."),
            ],
            "Solar Plexus": [
                ("I caused the tension in the room — it's my fault",
                 "{type_phrase} {center_truth} The discomfort I feel is amplified from others, not created by me."),
                ("I must manage everyone's emotional state to keep peace",
                 "{type_phrase} I feel deeply, but I am not responsible for the emotional field. I release the burden."),
                ("If I feel it, it's mine",
                 "{type_phrase} My open {center} amplifies emotions. I feel everything — but not everything I feel is mine."),
            ],
            "Root": [
                ("I should be doing something right now — stillness is laziness",
                 "{type_phrase} {center_truth} I move at my own pace."),
                ("The urgency I feel is real and requires immediate action",
                 "{type_phrase} Urgency is amplified from others. My {authority_phrase}"),
                ("I'm falling behind — everyone else is moving faster",
                 "{type_phrase} I am exactly on time for my design. The race I thought I was in does not apply to me."),
            ],
        }
        return themes.get(center, [
            (f"I believe my undefined {center} makes me incomplete",
             f"{{type_phrase}} My open {{center}} is not a deficiency — it is a receptor for wisdom."),
        ])

    def _generate_cross_center_beliefs(self):
        """Generate beliefs from interactions between multiple open centers."""
        undefined = set(self.context.undefined_centers)

        # Sacral + Root interaction (workaholic pattern)
        if "Sacral" in undefined and "Root" in undefined:
            self.beliefs.append(BeliefPair(
                limiting="I feel constant pressure to work, and when I try to match it, I crash. This cycle defines me.",
                empowering=f"{self.context.type_phrase} I feel urgency (open Root) + life force (open Sacral) that aren't mine. My work rhythm is bursts of guidance, not sustained output. The pressure is borrowed. I release it.",
                center="Sacral+Root", gate=None, category="general",
                day=self._next_day()
            ))

        # Solar Plexus + Ajna interaction (emotional thinking pattern)
        if "Solar Plexus" in undefined and "Ajna" in undefined:
            self.beliefs.append(BeliefPair(
                limiting="I need to think through my feelings until they make logical sense.",
                empowering=f"{self.context.authority_phrase} My feelings (open Solar Plexus) don't need my mind's (open Ajna) approval. I feel, I release, I don't need to understand everything.",
                center="Solar Plexus+Ajna", gate=None, category="general",
                day=self._next_day()
            ))

        # Head + Root interaction (pressure cooker)
        if "Head" in undefined and "Root" in undefined:
            self.beliefs.append(BeliefPair(
                limiting="Questions demand answers, and I must act on them immediately. The pressure from both ends is crushing.",
                empowering=f"{self.context.type_phrase} Mental pressure (open Head) + physical pressure (open Root) create a vice grip that isn't mine. I breathe. I release the question AND the urgency. Neither is mine.",
                center="Head+Root", gate=None, category="general",
                day=self._next_day()
            ))

    def _generate_design_beliefs(self):
        """Generate beliefs specific to the person's Type, Profile, Cross, and Motivation."""
        # Projector-specific
        if self.context.type == "Projector":
            self.beliefs.append(BeliefPair(
                limiting="Success requires grinding, consistency, and doing more than everyone else.",
                empowering=f"I am a Projector. My success comes through being recognized, invited, and then guiding with precision. I don't grind — I see. What I see is what I'm paid for. My consistency is in clarity, not in output.",
                center="Design", gate=None, category="general",
                day=self._next_day()
            ))
            self.beliefs.append(BeliefPair(
                limiting="If I'm not invited, I should invite myself — otherwise I'll be overlooked forever.",
                empowering="Waiting for invitation is not passivity — it is strategy. When I force my way in, I'm received as intrusive. When I'm invited, I'm received as the guide I am. I trust the timing.",
                center="Design", gate=None, category="general",
                day=self._next_day()
            ))

        # Fear motivation specific
        if self.context.motivation == "Fear":
            self.beliefs.append(BeliefPair(
                limiting="My fear means something is wrong. I should suppress it or fix it.",
                empowering=f"{self.context.motivation_phrase} I see threats clearly — that is my gift, not my malfunction. My fear points to what needs my attention. I don't suppress it — I follow it to clarity.",
                center="Design", gate=None, category="general",
                day=self._next_day()
            ))

        # Splenic authority specific
        if self.context.authority == "Splenic":
            self.beliefs.append(BeliefPair(
                limiting="I need to explain or justify my decisions — a 'gut feeling' isn't enough.",
                empowering="My Splenic authority speaks once, quietly, and never repeats itself. I don't owe anyone an explanation for what my body knows instantly. 'I know because I know' is a complete answer.",
                center="Design", gate=None, category="general",
                day=self._next_day()
            ))

    def _next_day(self) -> int:
        """Increment day counter every 5 beliefs (Duzett format)."""
        belief_count = len(self.beliefs)
        day = (belief_count // 5) + 1
        return day

    def _distill(self, beliefs: List[BeliefPair], max_beliefs: int = 50) -> List[BeliefPair]:
        """Distill comprehensive beliefs down to a short punchy set."""
        # Priority: center-level > cross-center > design-specific > gate-specific
        # Take one per center per category first, then fill with most impactful
        distilled = []
        seen = set()

        # First: center-level general beliefs (3 per open center)
        for b in beliefs:
            if b.gate is None and b.category == "general" and b.center in self.context.undefined_centers:
                key = (b.center, b.category)
                if key not in seen:
                    distilled.append(b)
                    seen.add(key)

        # Then: cross-center + design-specific
        for b in beliefs:
            if b.center in ("Sacral+Root", "Solar Plexus+Ajna", "Head+Root", "Design"):
                distilled.append(b)

        # Fill remaining with one per center per category
        for b in beliefs:
            if len(distilled) >= max_beliefs:
                break
            key = (b.center, b.category, b.gate)
            if key not in seen:
                distilled.append(b)
                seen.add(key)

        return distilled[:max_beliefs]

    def format_markdown(self, tier: str = "comprehensive") -> str:
        """Format the workbook as markdown."""
        lines = [
            f"# Belief Deprogrammer — Personalized Workbook",
            f"",
            f"**Generated for:** {self.chart.get('name', 'You')}",
            f"**Type:** {self.context.type} | **Authority:** {self.context.authority}",
            f"**Profile:** {self.context.profile} | **Definition:** {self.context.definition}",
            f"**Motivation:** {self.context.motivation} | **Cognition:** {self.context.cognition}",
            f"**Tier:** {tier}",
            f"",
            f"## How to Use This Workbook",
            f"",
            f"Based on Allie Duzett's '30 Days of Belief Work' methodology:",
            f"",
            f"1. **Read** the limiting belief aloud.",
            f"2. **Feel** where it lives in your body.",
            f"3. **Clear** it — scribble, tap, breathe, or your preferred modality.",
            f"4. **Read** the empowering belief aloud, slowly, three times.",
            f"5. **Pause.** Let your body register the shift.",
            f"",
            f"Do **5 belief pairs per day**. Each day is marked below.",
            f"",
            "---",
            "",
        ]

        # Group by day
        by_day = {}
        for b in self.beliefs:
            day = b.day
            if day not in by_day:
                by_day[day] = []
            by_day[day].append(b)

        belief_num = 1
        for day in sorted(by_day.keys()):
            lines.append(f"## Day {day}")
            lines.append("")
            for b in by_day[day]:
                gate_str = f" — Gate {b.gate} ({GATE_CONDITIONING[b.gate]['name']})" if b.gate and b.gate in GATE_CONDITIONING else ""
                lines.append(f"### Belief {belief_num}")
                lines.append(f"*{b.center}{gate_str} | {b.category}*")
                lines.append("")
                lines.append(f"**Limiting:** \"{b.limiting}\"")
                lines.append("")
                lines.append(f"**Empowering:** \"{b.empowering}\"")
                lines.append("")
                lines.append("---")
                lines.append("")
                belief_num += 1

        lines.append("")
        lines.append(f"*Generated by Belief Deprogrammer — {len(self.beliefs)} belief pairs*")

        return "\n".join(lines)
