"""
Context Injector — crafts the personal design language used in empowering beliefs.

Every empowering belief references the person's actual design:
- "As a [Type], I am not here to..."
- "My [Authority] gives me..."
- "My defined [Center] means I don't need..."

This module extracts the relevant design context from any chart JSON
and provides injectable phrases for belief generation.
"""

from typing import Dict, List, Optional


class DesignContext:
    """Personal design context extracted from a chart for belief generation."""

    def __init__(self, chart: dict):
        self.type = chart.get("hd_type", "Projector")
        self.authority = chart.get("authority", "Splenic")
        self.profile = chart.get("profile", "3/5")
        self.definition = chart.get("definition", "Split")
        self.cross = chart.get("incarnation_cross", {}).get("name", "Unknown")
        self.defined_centers = chart.get("defined_centers", [])
        self.undefined_centers = chart.get("undefined_centers", [])
        self.motivation = chart.get("motivation", "Unknown")
        self.cognition = chart.get("cognition", "Unknown")
        self.personality_gates = set(chart.get("personality_gates", []))
        self.design_gates = set(chart.get("design_gates", []))
        self.all_active_gates = set(chart.get("all_active_gates", []))

    @property
    def type_phrase(self) -> str:
        phrases = {
            "Projector": "I am a Projector — I am here to guide, not to grind. I succeed through recognition and invitation, not through sustained output.",
            "Generator": "I am a Generator — I am here to respond and build. My sacral response guides me to the right work.",
            "Manifesting Generator": "I am a Manifesting Generator — I am here to respond and then move fast. My multi-passionate nature is not scattered — it is designed.",
            "Manifestor": "I am a Manifestor — I am here to initiate and impact. I move without waiting, and I inform to create peace.",
            "Reflector": "I am a Reflector — I am here to mirror the health of the community. My changing nature is not inconsistency — it is wisdom.",
        }
        return phrases.get(self.type, f"I am a {self.type}.")

    @property
    def authority_phrase(self) -> str:
        phrases = {
            "Splenic": "My Splenic authority gives me instant, quiet knowing in the moment. I don't need to wait for emotional clarity.",
            "Emotional": "My Emotional authority requires time. Nothing is true in the now. I wait for clarity across my wave.",
            "Sacral": "My Sacral authority responds through my gut. My body says yes or no — my mind doesn't get a vote.",
            "Ego": "My Ego authority speaks through my willpower. What I truly want, I have the power to pursue.",
            "Self-Projected": "My Self-Projected authority needs to hear myself speak. I find clarity through my own voice.",
            "Lunar (Reflector)": "My Lunar authority needs a full 28-day cycle. I don't decide in the moment — I wait for the full reflection.",
        }
        return phrases.get(self.authority, f"My {self.authority} authority guides my decisions.")

    @property
    def defined_centers_phrase(self) -> str:
        if not self.defined_centers:
            return ""
        centers = ", ".join(self.defined_centers)
        return f"My defined centers ({centers}) give me consistent access to their energy. I don't need to borrow what I already have."

    @property
    def motivation_phrase(self) -> str:
        phrases = {
            "Fear": "I am Fear-motivated — I move when I see the threat clearly. Vigilance is my fuel, not my enemy.",
            "Hope": "I am Hope-motivated — I move toward what is possible. My fuel is vision, not fear.",
            "Desire": "I am Desire-motivated — I move toward what I truly want. My wanting is not greed — it is direction.",
            "Need": "I am Need-motivated — I move when the need is genuine. Meeting real needs is my compass.",
            "Guilt": "I am Guilt-motivated — I move to make things right. My guilt, when healthy, is an alignment signal.",
            "Innocence": "I am Innocence-motivated — I move from presence, not from pressure. My way is trust, not force.",
            "Leader": "I am Leader-motivated — I move when I see someone who needs my guidance. My engine runs on serving others.",
        }
        return phrases.get(self.motivation, "")

    def empowering_for_center(self, center: str, gate: Optional[int] = None) -> Dict[str, str]:
        """Generate the empowering context specific to an open center."""
        context = {
            "center": center,
            "type_phrase": self.type_phrase,
            "authority_phrase": self.authority_phrase,
            "motivation_phrase": self.motivation_phrase,
        }

        # Center-specific empowering truths
        center_truths = {
            "Head": "I don't need to answer every question. My open Head absorbs inquiry — I release what's not mine.",
            "Ajna": "I don't need fixed certainty. My open Ajna processes many perspectives — that's wisdom, not confusion.",
            "Throat": "I don't need to speak to be heard. My open Throat amplifies expression — I speak when moved, not when pressured.",
            "G": "I don't need a fixed identity. My open G reflects direction — I find myself through the right people and places.",
            "Heart/Ego": "I don't need to prove my worth. My open Heart amplifies willpower — my value is inherent, not earned.",
            "Sacral": "I don't need to sustain output. My open Sacral absorbs life force — I work in bursts, guided by invitation.",
            "Spleen": "I don't need to hold onto what's not safe. My open Spleen amplifies intuition — I release fear that isn't mine.",
            "Solar Plexus": "I don't need to manage everyone's emotions. My open Solar Plexus amplifies feelings — I feel deeply but I am not responsible for the emotional field.",
            "Root": "I don't need to rush. My open Root amplifies pressure — I move at my own pace, free from borrowed urgency.",
        }
        context["center_truth"] = center_truths.get(center, "")

        return context

    def get_hanging_gates(self, center_to_gates: Dict[str, List[int]]) -> Dict[str, List[int]]:
        """Identify which active gates are hanging in undefined centers."""
        hanging = {}
        for center, gates in center_to_gates.items():
            if center in self.undefined_centers:
                active_in_center = [g for g in gates if g in self.all_active_gates]
                if active_in_center:
                    hanging[center] = active_in_center
        return hanging

    def hanging_gates_by_center(self) -> Dict[str, List[int]]:
        """Compute hanging gates for all undefined centers using the gate_themes index.

        Returns: {center_name: [gate_numbers]} for centers that have active hanging gates.
                 Centers that are undefined but have zero active gates are NOT in this dict
                 (they are 'fully open').
        """
        from engine.gate_themes import CENTER_TO_GATES
        return self.get_hanging_gates(CENTER_TO_GATES)

    def fully_open_centers(self) -> List[str]:
        """Return undefined centers that have ZERO active hanging gates (pure amplification)."""
        hanging = self.hanging_gates_by_center()
        return [c for c in self.undefined_centers if c not in hanging]
