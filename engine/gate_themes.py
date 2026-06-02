"""
Gate Conditioning Themes — the foundation of the belief generation engine.

Each gate has:
- high_expression: authentic energy when in a DEFINED center
- distortion: what gets absorbed/distorted when in an OPEN center (hanging gate)
- distortion is the raw material from which limiting beliefs are derived
"""

GATE_CONDITIONING = {
    # ═══════════════════════════════════════════
    # HEAD CENTER GATES (61, 63, 64)
    # ═══════════════════════════════════════════
    61: {
        "center": "Head",
        "name": "Mystery",
        "high_expression": "Pressure to know the unknowable. Inner truth that doesn't need external validation.",
        "distortion": "Absorbing others' existential questions. Feeling pressured to have answers to unanswerable questions. Believing your uncertainty is inadequacy.",
    },
    63: {
        "center": "Head",
        "name": "Doubt",
        "high_expression": "Healthy skepticism. Pressure to question assumptions. Logical inquiry.",
        "distortion": "Absorbing others' doubt and confusion. Chronic second-guessing. Believing you're uncertain because you're not smart enough — when it's actually others' doubt you're amplifying.",
    },
    64: {
        "center": "Head",
        "name": "Confusion",
        "high_expression": "Pressure to make sense of the past. Pattern recognition through memory.",
        "distortion": "Absorbing collective confusion. Feeling lost in possibilities. Believing clarity will never come — when you're processing everyone's confusion simultaneously.",
    },

    # ═══════════════════════════════════════════
    # AJNA CENTER GATES (4, 11, 17, 24, 43, 47)
    # ═══════════════════════════════════════════
    47: {
        "center": "Ajna",
        "name": "Realizing",
        "high_expression": "Mental clarity through abstraction. Making sense of experience. Epiphany.",
        "distortion": "Absorbing others' mental fog. Feeling pressured to 'figure it out' right now. Believing confusion is personal failure rather than amplified collective uncertainty. Grasping at certainty that isn't yours to hold.",
    },
    4: {
        "center": "Ajna",
        "name": "Formulization",
        "high_expression": "Logical answers. Mental formulas. Solving through structure.",
        "distortion": "Absorbing pressure to have the 'right' answer. Believing there's one correct mental framework. Over-intellectualizing to feel safe in an undefined mind.",
    },
    11: {
        "center": "Ajna",
        "name": "Ideas",
        "high_expression": "Endless ideation. Curiosity. Creative mental generation.",
        "distortion": "Absorbing others' ideas and mistaking them for your own. Mental overwhelm from too many possibilities. Believing you must act on every idea.",
    },
    17: {
        "center": "Ajna",
        "name": "Opinions",
        "high_expression": "Forming and sharing opinions. Mental perspective.",
        "distortion": "Absorbing others' opinions and feeling pressured to defend them as your own. Believing you need fixed opinions to be taken seriously.",
    },
    24: {
        "center": "Ajna",
        "name": "Rationalizing",
        "high_expression": "Rational insight. Making sense through reason. Mental return to truth.",
        "distortion": "Absorbing others' need for rational explanations. Over-rationalizing feelings. Believing everything must make logical sense.",
    },
    43: {
        "center": "Ajna",
        "name": "Insight",
        "high_expression": "Breakthrough knowing. Structural insight. Inner epiphany.",
        "distortion": "Absorbing pressure to have breakthrough insights on demand. Believing your knowing isn't valid unless it arrives dramatically.",
    },

    # ═══════════════════════════════════════════
    # THROAT GATES (8, 12, 16, 20, 23, 31, 33, 35, 45, 56, 62)
    # ═══════════════════════════════════════════
    8: {
        "center": "Throat",
        "name": "Contribution",
        "high_expression": "Creative contribution. Self-expression through individuality.",
        "distortion": "Absorbing pressure to constantly contribute something unique. Believing silence means you have nothing valuable to offer.",
    },
    12: {
        "center": "Throat",
        "name": "Caution",
        "high_expression": "Knowing when to speak. Social articulation with emotional depth.",
        "distortion": "Absorbing others' emotional restraint or impulsiveness. Believing you must always calibrate your expression to others' moods.",
    },
    45: {
        "center": "Throat",
        "name": "The Gatherer",
        "high_expression": "Gathering resources and people. Leadership through providing.",
        "distortion": "Absorbing pressure to always be the provider. Believing your worth is in what you gather for others.",
    },

    # ═══════════════════════════════════════════
    # ROOT CENTER GATES (19, 38, 39, 41, 52, 53, 54, 58, 60)
    # ═══════════════════════════════════════════
    38: {
        "center": "Root",
        "name": "The Fighter",
        "high_expression": "Fighting for what matters. Purpose-driven struggle. Knowing what's worth the fight.",
        "distortion": "Absorbing pressure to fight battles that aren't yours. Adrenaline addiction from amplified urgency. Believing peace is laziness. Chronic tension from carrying fights you absorbed from others.",
    },
    52: {
        "center": "Root",
        "name": "Inaction",
        "high_expression": "Stillness as power. Knowing when NOT to move. Concentration.",
        "distortion": "Absorbing pressure to act when stillness is correct. Believing inaction is failure. The paradox: you're wired for focused stillness but amplify others' urgency to move.",
    },
    58: {
        "center": "Root",
        "name": "Aliveness",
        "high_expression": "Joy in correction. Vitality through improvement. Pressure to make things better.",
        "distortion": "Absorbing pressure to fix everything. Believing nothing can rest until it's improved. Chronic dissatisfaction from amplifying others' discontent.",
    },
    60: {
        "center": "Root",
        "name": "Acceptance",
        "high_expression": "Accepting limitation as fuel. Pressure that finds peace in boundaries.",
        "distortion": "Absorbing others' restlessness with limitation. Believing acceptance means giving up. Oscillating between forced acceptance and rebellion against limits that aren't yours.",
    },
    53: {
        "center": "Root",
        "name": "Beginnings",
        "high_expression": "Pressure to start. Initiating new cycles. Development energy.",
        "distortion": "Absorbing pressure to keep starting. Believing you must always be initiating. Chronic beginning without completion — then blaming yourself.",
    },
    54: {
        "center": "Root",
        "name": "Ambition",
        "high_expression": "Drive to rise. Material ambition. Pressure to transcend circumstances.",
        "distortion": "Absorbing others' ambition and mistaking it for your own drive. Believing you're not ambitious enough — when you're amplifying everyone's hunger.",
    },

    # ═══════════════════════════════════════════
    # SACRAL GATES (3, 5, 9, 14, 27, 29, 34, 42, 59)
    # ═══════════════════════════════════════════
    14: {
        "center": "Sacral",
        "name": "Power Skills",
        "high_expression": "Sacral power in skilled action. Resources through mastery.",
        "distortion": "Absorbing others' drive to acquire skills and resources. Believing you must constantly develop new competencies to be valuable. Mistaking amplified ambition for genuine sacral response.",
    },
    29: {
        "center": "Sacral",
        "name": "The Abyssal",
        "high_expression": "Saying yes to experience. Deep commitment. Throwing yourself in fully.",
        "distortion": "Absorbing others' enthusiastic commitment and saying yes when your body says no. Believing you must be 'all in' to be worthy. Over-committing from amplified sacral energy.",
    },
    34: {
        "center": "Sacral",
        "name": "Power",
        "high_expression": "Raw sacral power. Pure life force. Self-empowered action.",
        "distortion": "Absorbing raw Generator power and feeling like you should have it too. Believing your power is measured in sustained output. Mistaking borrowed sacral surges for your own capacity.",
    },
    42: {
        "center": "Sacral",
        "name": "Growth",
        "high_expression": "Completion energy. Bringing things to fruition. Cyclical growth.",
        "distortion": "Absorbing pressure to finish everything. Believing incompletion is personal failure. Amplifying others' growth cycles and feeling left behind.",
    },

    # ═══════════════════════════════════════════
    # SOLAR PLEXUS GATES (6, 22, 30, 36, 37, 49, 55)
    # ═══════════════════════════════════════════
    22: {
        "center": "Solar Plexus",
        "name": "Grace",
        "high_expression": "Emotional grace. Beauty in feeling. Openness through vulnerability.",
        "distortion": "Absorbing others' emotional states and believing they're yours. Feeling responsible for the emotional atmosphere. Believing you caused the tension in the room.",
    },
    30: {
        "center": "Solar Plexus",
        "name": "Recognition of Feelings",
        "high_expression": "Emotional clarity. Recognizing and naming feelings. Emotional wisdom.",
        "distortion": "Absorbing emotional chaos and believing you must make sense of it. Feeling responsible for processing everyone's unspoken feelings. Emotional exhaustion from amplification.",
    },
    37: {
        "center": "Solar Plexus",
        "name": "Friendship",
        "high_expression": "Emotional bonds. Community. Friendship through emotional connection.",
        "distortion": "Absorbing obligation to maintain emotional harmony for the tribe. Believing conflict is your fault. Carrying the emotional weight of every relationship.",
    },
    36: {
        "center": "Solar Plexus",
        "name": "Crisis",
        "high_expression": "Emotional depth through crisis. Transformation through feeling.",
        "distortion": "Absorbing crisis energy and feeling perpetually in emergency. Believing peace means something's wrong. Emotional drama addiction from amplification.",
    },
}

# Categories and their expansion patterns
CATEGORIES = [
    "general",
    "environmental",
    "generational",
    "physical",
    "mental",
    "spiritual",
    "subconscious",
    "conscious",
    "absorbed",
]

CATEGORY_DESCRIPTIONS = {
    "general": "Core beliefs summarizing the center's conditioning pattern",
    "environmental": "Beliefs absorbed from workplaces, schools, social settings, physical environments",
    "generational": "Beliefs inherited through family lineage, ancestors, cultural DNA",
    "physical": "Beliefs stored in the body, posture, nervous system, physical sensations",
    "mental": "Beliefs held as thought patterns, cognitive loops, mental frameworks",
    "spiritual": "Beliefs about purpose, worthiness, cosmic place, existential meaning",
    "subconscious": "Beliefs operating below conscious awareness — the hidden drivers",
    "conscious": "Beliefs you're aware of but feel powerless to change",
    "absorbed": "Beliefs picked up from specific relationships, partners, mentors, or cultures",
}
