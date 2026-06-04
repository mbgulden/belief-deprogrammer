"""
Gate Conditioning Themes — the foundation of the belief generation engine.

Each gate has:
- high_expression: authentic energy when in a DEFINED center
- distortion: what gets absorbed/distorted when in an OPEN center (hanging gate)
- distortion is the raw material from which limiting beliefs are derived
"""

GATE_CONDITIONING = {
    1: {
        "center": "G",
        "name": "Self-Expression",
        "high_expression": "Creative direction through authentic self-expression. Knowing who you are and expressing it naturally without needing approval.",
        "distortion": "Absorbing others\' creative identities and mistaking them for your own direction. Feeling lost about who you are because you\'re amplifying everyone else\'s self-expression. Believing you need to find \'your thing\' — when you\'re drowning in borrowed identities.",
    },
    2: {
        "center": "G",
        "name": "The Receptive",
        "high_expression": "Natural receptivity to direction. Knowing where to go by being open to being guided. Magnetic stillness that attracts the right path.",
        "distortion": "Absorbing others\' direction and feeling pulled in every direction at once. Believing you don\'t know where you\'re going because you lack inner compass — when you\'re actually receiving everyone\'s directional signals simultaneously. Chronic passivity from confusing receptivity with having no will of your own.",
    },
    3: {
        "center": "Sacral",
        "name": "Ordering",
        "high_expression": "Initiating new order out of chaos. Sacral energy for beginning mutation. Making things new.",
        "distortion": "Absorbing pressure to keep innovating and starting fresh cycles. Believing you must constantly reinvent to be valuable. Chronic beginning without sustaining — you\'re amplifying others\' restless beginnings through an undefined sacral.",
    },
    4: {
        "center": "Ajna",
        "name": "Formulization",
        "high_expression": "Logical answers. Mental formulas. Solving through structure.",
        "distortion": "Absorbing pressure to have the \'right\' answer. Believing there\'s one correct mental framework. Over-intellectualizing to feel safe in an undefined mind.",
    },
    5: {
        "center": "Sacral",
        "name": "Fixed Rhythms",
        "high_expression": "Sustained sacral rhythm. Maintaining consistent patterns. Power through repetition.",
        "distortion": "Absorbing others\' need for routine and mistaking it for your own natural rhythm. Believing you\'re undisciplined when you can\'t maintain borrowed patterns. Forcing fixed habits that exhaust you — because the rhythm belongs to someone else\'s sacral.",
    },
    6: {
        "center": "Solar Plexus",
        "name": "Conflict",
        "high_expression": "Emotional boundary wisdom. Knowing when to open and when to close. Intimacy through emotional regulation and healthy friction.",
        "distortion": "Absorbing others\' emotional boundaries and feeling either invaded or walled off. Believing emotional friction means something is fundamentally wrong with you. Oscillating between over-exposure and total withdrawal from amplified relational tension that you didn\'t create.",
    },
    7: {
        "center": "G",
        "name": "The Role of the Self",
        "high_expression": "Natural leadership through authentic role. Guiding others by being exactly who you are. Direction for the collective through self-trust.",
        "distortion": "Absorbing pressure to lead and direct others when it\'s not your time. Feeling responsible for everyone\'s direction. Believing you must have all the answers for the group — when you\'re amplifying leadership energy that isn\'t yours to carry alone.",
    },
    8: {
        "center": "Throat",
        "name": "Contribution",
        "high_expression": "Creative contribution. Self-expression through individuality.",
        "distortion": "Absorbing pressure to constantly contribute something unique. Believing silence means you have nothing valuable to offer.",
    },
    9: {
        "center": "Sacral",
        "name": "Focus",
        "high_expression": "Sustained focus on the details that matter. Sacral energy for precision. Power through concentration.",
        "distortion": "Absorbing pressure to maintain laser focus and believing scattered attention is a character flaw. Mistaking amplified hyperfocus for your own capacity — then crashing. Feeling deficient when you can\'t sustain borrowed concentration.",
    },
    10: {
        "center": "G",
        "name": "The Behavior of the Self",
        "high_expression": "Self-love as foundation for authentic behavior. Empowerment through being true to yourself. Natural alignment with your own ways.",
        "distortion": "Absorbing others\' judgments about how you should behave. Believing self-love must be earned through correct behavior. Chronic self-criticism from amplifying external standards — mistaking others\' discomfort with your authenticity as proof you\'re wrong.",
    },
    11: {
        "center": "Ajna",
        "name": "Ideas",
        "high_expression": "Endless ideation. Curiosity. Creative mental generation.",
        "distortion": "Absorbing others\' ideas and mistaking them for your own. Mental overwhelm from too many possibilities. Believing you must act on every idea.",
    },
    12: {
        "center": "Throat",
        "name": "Caution",
        "high_expression": "Knowing when to speak. Social articulation with emotional depth.",
        "distortion": "Absorbing others\' emotional restraint or impulsiveness. Believing you must always calibrate your expression to others\' moods.",
    },
    13: {
        "center": "G",
        "name": "The Listener",
        "high_expression": "Holding space for others\' stories. Deep listening that heals through presence. Memory and wisdom through witnessing.",
        "distortion": "Absorbing everyone\'s life stories and feeling burdened by them. Believing you must carry and remember every story shared with you. Emotional exhaustion from being the designated listener — mistaking your gift for an obligation to absorb everyone\'s past.",
    },
    14: {
        "center": "Sacral",
        "name": "Power Skills",
        "high_expression": "Sacral power in skilled action. Resources through mastery.",
        "distortion": "Absorbing others\' drive to acquire skills and resources. Believing you must constantly develop new competencies to be valuable. Mistaking amplified ambition for genuine sacral response.",
    },
    15: {
        "center": "G",
        "name": "The Extremes",
        "high_expression": "Embracing the full spectrum of human behavior. Natural rhythm that accepts all expressions of self. Love of humanity in all its diversity.",
        "distortion": "Absorbing others\' extremes and oscillating between personas that aren\'t yours. Believing you must accommodate everyone\'s rhythm at the expense of your own. Extreme behavioral shifts from amplifying whoever you\'re with — losing your own natural timing.",
    },
    16: {
        "center": "Throat",
        "name": "Skills",
        "high_expression": "Expressing skills with enthusiasm. Recognition of talent through rhythm. Sharing mastery with joy.",
        "distortion": "Absorbing pressure to constantly demonstrate enthusiasm for your abilities. Believing your value is in your visible skillset — that you must perform talent to be heard. Mistaking amplified expectation for genuine desire to share.",
    },
    17: {
        "center": "Ajna",
        "name": "Opinions",
        "high_expression": "Forming and sharing opinions. Mental perspective.",
        "distortion": "Absorbing others\' opinions and feeling pressured to defend them as your own. Believing you need fixed opinions to be taken seriously.",
    },
    18: {
        "center": "Spleen",
        "name": "Correction",
        "high_expression": "Instinct for what needs fixing. Spotting flaws in service of health. Satisfaction through improvement.",
        "distortion": "Absorbing others\' dissatisfaction and feeling compelled to correct what isn\'t yours to fix. Believing everything imperfect is your responsibility. Chronic fault-finding that exhausts relationships — you\'re amplifying everyone\'s discontent through an open spleen.",
    },
    19: {
        "center": "Root",
        "name": "Wanting",
        "high_expression": "Pressure to approach the tribe. Healthy need. Emotional sensitivity that connects.",
        "distortion": "Absorbing others\' unmet needs and feeling perpetually wanting. Believing your needs are too much — when you\'re amplifying everyone\'s unspoken longing. Rejecting yourself before anyone else can, because the pressure to belong feels unbearable.",
    },
    20: {
        "center": "Throat",
        "name": "The Now",
        "high_expression": "Speaking from pure presence. Expressing only what\'s alive in the moment. Contemplative awareness through voice.",
        "distortion": "Absorbing others\' urgency to speak before presence arrives. Believing silence in conversation is failure or awkwardness. Forcing words when there\'s nothing authentic to say — then feeling misaligned with what came out.",
    },
    21: {
        "center": "Heart/Ego",
        "name": "The Hunter",
        "high_expression": "Natural authority over resources. Knowing when to control and when to release. Leadership through earned respect.",
        "distortion": "Absorbing pressure to control situations that aren\'t yours to manage. Believing loss of control means personal failure. Chronic micromanaging from amplifying others\' need for authority — grasping at control to feel worthy in an undefined ego.",
    },
    22: {
        "center": "Solar Plexus",
        "name": "Grace",
        "high_expression": "Emotional grace. Beauty in feeling. Openness through vulnerability.",
        "distortion": "Absorbing others\' emotional states and believing they\'re yours. Feeling responsible for the emotional atmosphere. Believing you caused the tension in the room.",
    },
    23: {
        "center": "Throat",
        "name": "Assimilation",
        "high_expression": "Expressing individual knowing clearly. Breakthrough articulation of new understanding. The gift of making the complex simple.",
        "distortion": "Absorbing pressure to explain insights before they\'re ripe. Believing you\'re being misunderstood because you are the problem — not because the timing isn\'t right yet. Fearing that speaking novel truths will make you sound crazy, so you stay silent or over-explain.",
    },
    24: {
        "center": "Ajna",
        "name": "Rationalizing",
        "high_expression": "Rational insight. Making sense through reason. Mental return to truth.",
        "distortion": "Absorbing others\' need for rational explanations. Over-rationalizing feelings. Believing everything must make logical sense.",
    },
    25: {
        "center": "G",
        "name": "Innocence",
        "high_expression": "Unconditional universal love. Pure connection to spirit through innocence. Loving without agenda or expectation.",
        "distortion": "Absorbing others\' need for love and feeling responsible for filling that void. Believing you must love everyone unconditionally — even when boundaries are needed. Spiritual bypassing from amplifying collective longing for divine love, mistaking absorbed pain for your own calling to heal.",
    },
    26: {
        "center": "Heart/Ego",
        "name": "The Egoist",
        "high_expression": "Persuasion through integrity. Selling what matters with heart. Ego power used in service of truth.",
        "distortion": "Absorbing pressure to sell, perform, and prove yourself constantly. Believing your worth is measured by what you can convince others of. Chronic self-promotion from amplifying collective ego hunger — mistaking borrowed ambition for your own authentic will.",
    },
    27: {
        "center": "Sacral",
        "name": "Caring",
        "high_expression": "Nourishing energy. Caring for others through sustained sacral warmth. Protection through provision.",
        "distortion": "Absorbing pressure to care for everyone and believing your worth is measured by how much you give. Over-nourishing others until you\'re depleted — mistaking amplified caretaking drive for your own sacral fuel. Resentment masked as love.",
    },
    28: {
        "center": "Spleen",
        "name": "The Game Player",
        "high_expression": "Struggle for meaning. Instinct for what\'s worth fighting for. Finding purpose through risk.",
        "distortion": "Absorbing others\' existential struggle and feeling life must be a battle to matter. Believing ease means you\'re not trying hard enough. Taking on fights you don\'t actually care about because you\'ve amplified someone else\'s life-or-death intensity.",
    },
    29: {
        "center": "Sacral",
        "name": "The Abyssal",
        "high_expression": "Saying yes to experience. Deep commitment. Throwing yourself in fully.",
        "distortion": "Absorbing others\' enthusiastic commitment and saying yes when your body says no. Believing you must be \'all in\' to be worthy. Over-committing from amplified sacral energy.",
    },
    30: {
        "center": "Solar Plexus",
        "name": "Recognition of Feelings",
        "high_expression": "Emotional clarity. Recognizing and naming feelings. Emotional wisdom.",
        "distortion": "Absorbing emotional chaos and believing you must make sense of it. Feeling responsible for processing everyone\'s unspoken feelings. Emotional exhaustion from amplification.",
    },
    31: {
        "center": "Throat",
        "name": "Leading",
        "high_expression": "Speaking for the collective. Leadership through democratic voice. Influence that unifies rather than dominates.",
        "distortion": "Absorbing pressure to lead when you aren\'t designated. Believing you must influence or direct others to have value. Taking on leadership burdens that fragment your own direction — then resenting those who didn\'t ask you to carry them.",
    },
    32: {
        "center": "Spleen",
        "name": "Continuity",
        "high_expression": "Instinct for what endures. Knowing what will last. Tribal memory and preservation.",
        "distortion": "Absorbing collective fear of collapse. Believing everything you care about will fail unless you hold it together. Carrying the instinctual weight of tribal survival — when you\'re actually amplifying ancestral dread through an open spleen.",
    },
    33: {
        "center": "Throat",
        "name": "Privacy",
        "high_expression": "Sharing wisdom from reflection. Knowing when to retreat. Storytelling that catalyses collective learning after the cycle completes.",
        "distortion": "Absorbing pressure to share your story before the cycle finishes. Believing withdrawal means avoidance. Forcing reflective wisdom into premature articulation — then feeling exposed and regretting oversharing.",
    },
    34: {
        "center": "Sacral",
        "name": "Power",
        "high_expression": "Raw sacral power. Pure life force. Self-empowered action.",
        "distortion": "Absorbing raw Generator power and feeling like you should have it too. Believing your power is measured in sustained output. Mistaking borrowed sacral surges for your own capacity.",
    },
    35: {
        "center": "Throat",
        "name": "Change",
        "high_expression": "Expressing the hunger for experience. Initiating change with emotional clarity. Progress through exploration.",
        "distortion": "Absorbing others\' restlessness and mistaking it for your own hunger. Believing contentment equals stagnation. Chronic pursuit of novelty from amplified collective dissatisfaction — never arriving because the hunger isn\'t yours.",
    },
    36: {
        "center": "Solar Plexus",
        "name": "Crisis",
        "high_expression": "Emotional depth through crisis. Transformation through feeling.",
        "distortion": "Absorbing crisis energy and feeling perpetually in emergency. Believing peace means something\'s wrong. Emotional drama addiction from amplification.",
    },
    37: {
        "center": "Solar Plexus",
        "name": "Friendship",
        "high_expression": "Emotional bonds. Community. Friendship through emotional connection.",
        "distortion": "Absorbing obligation to maintain emotional harmony for the tribe. Believing conflict is your fault. Carrying the emotional weight of every relationship.",
    },
    38: {
        "center": "Root",
        "name": "The Fighter",
        "high_expression": "Fighting for what matters. Purpose-driven struggle. Knowing what\'s worth the fight.",
        "distortion": "Absorbing pressure to fight battles that aren\'t yours. Adrenaline addiction from amplified urgency. Believing peace is laziness. Chronic tension from carrying fights you absorbed from others.",
    },
    39: {
        "center": "Root",
        "name": "The Provocateur",
        "high_expression": "Pressure to provoke emotional clarity. Piercing through pretense. Finding spirit through challenge.",
        "distortion": "Absorbing pressure to provoke when no provocation is needed. Believing you must disrupt peace to be authentic. Pushing people away through amplified challenge energy — then feeling isolated and misunderstood.",
    },
    40: {
        "center": "Heart/Ego",
        "name": "Deliverance",
        "high_expression": "Earning rest through genuine contribution. Knowing when to provide and when to withdraw. Healthy boundaries around willpower.",
        "distortion": "Absorbing others\' inability to rest and feeling guilty when you do. Believing you must earn every moment of peace through exhausting effort. Chronic burnout from amplifying collective willpower — never feeling you\'ve done enough to deserve rest.",
    },
    41: {
        "center": "Root",
        "name": "Contraction",
        "high_expression": "Pressure to feel deeply. Imagination fueled by longing. Fantasy as initiation.",
        "distortion": "Absorbing others\' unexpressed desire and living in perpetual anticipation. Believing the fantasy is better than reality because you\'re amplifying collective projection. Contracting inward to avoid the vulnerability of actual experience.",
    },
    42: {
        "center": "Sacral",
        "name": "Growth",
        "high_expression": "Completion energy. Bringing things to fruition. Cyclical growth.",
        "distortion": "Absorbing pressure to finish everything. Believing incompletion is personal failure. Amplifying others\' growth cycles and feeling left behind.",
    },
    43: {
        "center": "Ajna",
        "name": "Insight",
        "high_expression": "Breakthrough knowing. Structural insight. Inner epiphany.",
        "distortion": "Absorbing pressure to have breakthrough insights on demand. Believing your knowing isn\'t valid unless it arrives dramatically.",
    },
    44: {
        "center": "Spleen",
        "name": "Alertness",
        "high_expression": "Pattern recognition. Instinct for survival patterns. Knowing who and what to trust.",
        "distortion": "Absorbing others\' hypervigilance and living in constant threat-detection mode. Believing danger is always imminent — because you\'re amplifying every alert signal around you. Mistaking borrowed fear for your own instinct.",
    },
    45: {
        "center": "Throat",
        "name": "The Gatherer",
        "high_expression": "Gathering resources and people. Leadership through providing.",
        "distortion": "Absorbing pressure to always be the provider. Believing your worth is in what you gather for others.",
    },
    46: {
        "center": "G",
        "name": "Determination",
        "high_expression": "Serendipity through embodied presence. Being in the right place at the right time. Love of the physical body and its wisdom.",
        "distortion": "Absorbing others\' urgency to be somewhere else. Believing you\'re always in the wrong place at the wrong time. Chronic FOMO from amplifying collective restlessness — missing the serendipity that\'s already present. Mistaking embodied timing for being \'stuck.\'",
    },
    47: {
        "center": "Ajna",
        "name": "Realizing",
        "high_expression": "Mental clarity through abstraction. Making sense of experience. Epiphany.",
        "distortion": "Absorbing others\' mental fog. Feeling pressured to \'figure it out\' right now. Believing confusion is personal failure rather than amplified collective uncertainty. Grasping at certainty that isn\'t yours to hold.",
    },
    48: {
        "center": "Spleen",
        "name": "Depth",
        "high_expression": "Deep instinctive knowing. Solutions that come from the well of body wisdom. Resourcefulness through depth.",
        "distortion": "Absorbing pressure to have deep solutions on demand. Believing you must always go deeper — when the body wisdom you\'re chasing isn\'t yours to access. Feeling shallow or inadequate because you can\'t reach the depth others project onto you.",
    },
    49: {
        "center": "Solar Plexus",
        "name": "Principles",
        "high_expression": "Emotional clarity about tribal needs. Principled revolution. Knowing who truly belongs and acting from that clarity.",
        "distortion": "Absorbing rejection sensitivity from the tribe. Believing exclusion is personal evidence of unworthiness. Feeling emotionally responsible for upholding principles that aren\'t yours — then rebelling against them in confusion, not realizing you amplified a collective wound.",
    },
    50: {
        "center": "Spleen",
        "name": "Values",
        "high_expression": "Preservation of values. Tribal caretaking through instinct. Knowing what must be protected.",
        "distortion": "Absorbing others\' moral panic. Believing you\'re the guardian of values that aren\'t authentically yours. Carrying the weight of protecting the tribe — then resenting everyone for it. Moral exhaustion from amplifying collective fear of corruption.",
    },
    51: {
        "center": "Heart/Ego",
        "name": "Shock",
        "high_expression": "Initiating through healthy competition. Awakening others through shock. Willpower to face the unknown.",
        "distortion": "Absorbing competitive energy and feeling you must constantly prove yourself through comparison. Believing your awakening must come through dramatic shock. Chronic restlessness from amplifying others\' initiation energy — mistaking borrowed urgency for your own path to transformation.",
    },
    52: {
        "center": "Root",
        "name": "Inaction",
        "high_expression": "Stillness as power. Knowing when NOT to move. Concentration.",
        "distortion": "Absorbing pressure to act when stillness is correct. Believing inaction is failure. The paradox: you\'re wired for focused stillness but amplify others\' urgency to move.",
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
        "distortion": "Absorbing others\' ambition and mistaking it for your own drive. Believing you\'re not ambitious enough — when you\'re amplifying everyone\'s hunger.",
    },
    55: {
        "center": "Solar Plexus",
        "name": "Spirit",
        "high_expression": "Riding the full spectrum of emotional spirit. Profound feeling as creative fuel. Abundance through emotional depth — from melancholy to ecstasy.",
        "distortion": "Absorbing the collective emotional wave and believing every low means something is deeply and personally wrong. Fearing your emotional depth is too much for others. Mistaking amplified melancholy for personal hopelessness — when you\'re surfing a wave that isn\'t yours.",
    },
    56: {
        "center": "Throat",
        "name": "Stimulation",
        "high_expression": "Storytelling that illuminates. Sharing ideas through narrative. Stimulation through curiosity expressed.",
        "distortion": "Absorbing pressure to make every experience a story worth telling. Believing your life must be narratable to be meaningful. Performing experience for others\' stimulation instead of living it directly — reducing lived reality to future material.",
    },
    57: {
        "center": "Spleen",
        "name": "Intuition",
        "high_expression": "Clarity in the now. Acute intuitive awareness. Knowing what\'s true in the present moment.",
        "distortion": "Absorbing others\' anxiety about the future and losing your natural clarity. Believing intuition must always be loud and dramatic — when you\'re amplifying everyone\'s noise and can\'t hear your own quiet knowing. Second-guessing what you actually do sense.",
    },
    58: {
        "center": "Root",
        "name": "Aliveness",
        "high_expression": "Joy in correction. Vitality through improvement. Pressure to make things better.",
        "distortion": "Absorbing pressure to fix everything. Believing nothing can rest until it\'s improved. Chronic dissatisfaction from amplifying others\' discontent.",
    },
    59: {
        "center": "Sacral",
        "name": "Sexuality",
        "high_expression": "Creation through intimacy. Breaking bonds to form deeper connection. Sacral power in union.",
        "distortion": "Absorbing others\' sexual energy and confusing it with genuine desire. Believing you must always be available or desirable. Mistaking amplified attraction for connection — and then wondering why intimacy feels hollow when the borrowed sacral charge fades.",
    },
    60: {
        "center": "Root",
        "name": "Acceptance",
        "high_expression": "Accepting limitation as fuel. Pressure that finds peace in boundaries.",
        "distortion": "Absorbing others\' restlessness with limitation. Believing acceptance means giving up. Oscillating between forced acceptance and rebellion against limits that aren\'t yours.",
    },
    61: {
        "center": "Head",
        "name": "Mystery",
        "high_expression": "Pressure to know the unknowable. Inner truth that doesn\'t need external validation.",
        "distortion": "Absorbing others\' existential questions. Feeling pressured to have answers to unanswerable questions. Believing your uncertainty is inadequacy.",
    },
    62: {
        "center": "Throat",
        "name": "Detail",
        "high_expression": "Precise articulation. Naming things clearly and carefully. The power of detail and logical expression.",
        "distortion": "Absorbing pressure to have every fact correct before speaking. Believing imprecision is incompetence. Over-detailing from amplified need for logical certainty — losing the forest for the trees and exhausting listeners with unnecessary precision.",
    },
    63: {
        "center": "Head",
        "name": "Doubt",
        "high_expression": "Healthy skepticism. Pressure to question assumptions. Logical inquiry.",
        "distortion": "Absorbing others\' doubt and confusion. Chronic second-guessing. Believing you\'re uncertain because you\'re not smart enough — when it\'s actually others\' doubt you\'re amplifying.",
    },
    64: {
        "center": "Head",
        "name": "Confusion",
        "high_expression": "Pressure to make sense of the past. Pattern recognition through memory.",
        "distortion": "Absorbing collective confusion. Feeling lost in possibilities. Believing clarity will never come — when you\'re processing everyone\'s confusion simultaneously.",
    },
}

# ── Reverse index: center → list of gate numbers ──
def build_center_to_gates() -> dict:
    """Build reverse lookup: center name → list of gate numbers in that center."""
    mapping = {}
    for gate_num, data in GATE_CONDITIONING.items():
        center = data["center"]
        if center not in mapping:
            mapping[center] = []
        mapping[center].append(gate_num)
    return mapping

CENTER_TO_GATES = build_center_to_gates()

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
