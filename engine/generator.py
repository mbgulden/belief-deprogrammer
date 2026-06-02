"""
Belief Deprogrammer v4 — Gemini-Quality Belief Generation

Generates deeply personal, specific, human beliefs from open HD centers.
No gate names. No HD jargon. No boilerplate concatenation.

Structure per open center:
  EMOTIONS → what you actually FEEL in this center
  LIMITING BELIEFS → what you personally believe (3 core × 3 subordinates each)
  PROGRAMMED BELIEFS → what society/culture taught you (3 core × 3 sub each)
  INHERITED BELIEFS → what your ancestors passed down (3 core × 3 sub each)

Every belief is a real sentence a human would actually think.
Every empowering belief specifically counters its limiting belief.
No negatives in empowering beliefs. No "I am a Projector" repetition.
"""

from typing import Dict, List, Tuple, Optional
from engine.context_injector import DesignContext


class BeliefPair:
    def __init__(self, limiting: str, empowering: str, center: str,
                 category: str, depth: str = "core"):
        self.limiting = limiting
        self.empowering = empowering
        self.center = center
        self.category = category
        self.depth = depth  # "core" or "subordinate"


class Section:
    """A grouped section of beliefs (emotions, limiting, programmed, inherited)."""
    def __init__(self, title: str, description: str, items: List = None):
        self.title = title
        self.description = description
        self.items = items or []


class CenterWorkbook:
    """Complete belief work for one open center."""
    def __init__(self, center: str):
        self.center = center
        self.emotions: List[Tuple[str, List[str]]] = []  # (emotion_name, [examples])
        self.limiting: List[Tuple[str, str, List[Tuple[str, str]]]] = []  # (lim, emp, [(sub_lim, sub_emp)])
        self.programmed: List[Tuple[str, str, List[Tuple[str, str]]]] = []
        self.inherited: List[Tuple[str, str, List[Tuple[str, str]]]] = []


# ═══════════════════════════════════════════════════════════════
# HAND-CRAFTED BELIEF CONTENT — per open center
# Modeled after Gemini doc quality. No gates. No jargon. Real human thoughts.
# ═══════════════════════════════════════════════════════════════

def get_center_content(center: str, context: DesignContext) -> CenterWorkbook:
    """Return Gemini-quality belief content for a given open center."""
    wb = CenterWorkbook(center)
    t = context.type
    a = context.authority
    m = context.motivation

    # ── HEAD (Open Crown) ──
    if center == "Head":
        wb.emotions = [
            ("Overwhelm — Mental Flooding", [
                "Feeling completely paralyzed by having too many ideas or too much inspiration at once and not knowing where to start.",
                "A heavy, buzzing sensation in the head when walking into a busy room because you are absorbing everyone else's mental chatter.",
                "The exhausting feeling of your brain spinning out of control trying to process a problem that isn't even yours to solve.",
            ]),
            ("Anxiety — Mental Urgency", [
                "A tight, panicky feeling that you must find the answer to a question right now, or else something bad will happen.",
                "Lying awake at night with a racing heart because your mind won't stop trying to predict and solve future scenarios.",
                "The stressful compulsion to constantly consume information (scrolling, researching, reading) to ease the discomfort of not knowing.",
            ]),
            ("Confusion — Mental Fog", [
                "Losing your own train of thought or completely forgetting your original purpose because you became derailed by someone else's idea.",
                "Feeling mentally scattered and unable to focus, resulting in a sense of being lost in the clouds.",
                f"Second-guessing your own inner knowing ({a.lower()} authority) because the mental pressure of 'what if?' clouds your immediate intuition.",
            ]),
        ]

        wb.limiting = [
            ("I must have the answer to every question.",
             "I am comfortable with the unknown, and I trust that the right answers will come to me when I truly need them.",
             [
                 ("If I don't know the answer, people will think I'm incompetent.",
                  "My value lies in my presence and perspective, in my presence and my perspective."),
                 ("Uncertainty means I lack control and am unsafe.",
                  f"Uncertainty is a space of infinite possibility where my {a.lower()} intuition can guide me safely."),
                 ("I have to figure it out immediately to make this mental pressure stop.",
                  "I can observe mental pressure without letting it dictate my actions; I am allowed to just let it pass through me."),
             ]),
            ("If I can't logically figure this out, I can't move forward.",
             f"I trust my {a.lower()} instincts to guide my steps, even when my mind doesn't have the logical blueprint yet.",
             [
                 ("Logic is the only valid way to make a successful decision.",
                  f"My bodily intuition ({a}) is far faster and more accurate for me than mental logic."),
                 ("If I just follow a feeling, I will make a foolish mistake.",
                  f"My {a.lower()} instinct is an ancient, highly evolved survival mechanism designed to keep me safe and successful."),
                 ("I need to justify my actions with reasons that make sense to others.",
                  "I am free to keep private my intuitive knowing to anyone."),
             ]),
            ("My mind's worries are a true reflection of reality.",
             "My mind often amplifies the fears of others; I choose to anchor into the grounded reality of my own body.",
             [
                 ("If I feel anxious, something must be terribly wrong.",
                  "Anxiety in my head is often just foreign energy passing through; it is an inaccurate reflection of my actual life."),
                 ("I have to solve these worries to feel safe.",
                  f"Safety comes from my {a.lower()} authority in the present moment, from being present in hypothetical worries in my head."),
                 ("I can't relax until my mind is completely quiet.",
                  "I can find deep relaxation in my body even while my open mind observes passing mental traffic."),
             ]),
        ]

        wb.programmed = [
            ("My worth is tied to how much I know and how smart I appear.",
             f"My true worth comes from my unique energy, my ability to guide others, and my innate {t} wisdom.",
             [
                 ("I have to constantly prove my intelligence to earn my place.",
                  "I am naturally recognized for my wisdom without needing to force or prove it."),
                 ("Being smart means retaining facts and data like everyone else.",
                  "My brilliance is fluid; I take in inspiration, synthesize it, and let it go rather than hoarding it."),
                 ("If someone knows more than me, I am less valuable in this situation.",
                  "I release the need to know everything; my gift is knowing how to direct and guide the information others hold."),
             ]),
            ("Having doubts or changing my mind is a sign of weakness or instability.",
             "My open mind is designed to be flexible; changing my perspective as new inspiration arrives is a sign of immense wisdom.",
             [
                 ("I must pick one viewpoint and defend it forever to be respected.",
                  "True respect comes from my willingness to evolve and remain open to new truths."),
                 ("Doubt means I am failing or doing something wrong.",
                  "Doubt is simply my open Crown sampling different possibilities before my Spleen gives me the final signal."),
                 ("Consistency in thought is the highest virtue.",
                  "Adaptability and openness are my highest virtues when it comes to mental inspiration."),
             ]),
            ("I should always be thinking about something productive.",
             "Mental emptiness is my natural, healthy state; I allow my mind to rest so it can be a clear vessel for true inspiration.",
             [
                 ("Daydreaming or zoning out is lazy and wasteful.",
                  "Zoning out is a necessary energetic hygiene practice that clears my open Crown."),
                 ("If I'm not actively solving a problem, I'm falling behind.",
                  "My greatest insights arrive when I stop forcing my mind to work and allow stillness."),
                 ("Constant mental output equals my value to my family.",
                  "My peaceful, grounded presence is far more valuable to my family than my constant mental output."),
             ]),
        ]

        wb.inherited = [
            ("Life is a dangerous puzzle, and it is my duty to foresee and solve every problem to keep the family safe.",
             "Life is an experience to be lived, not a puzzle to be solved; I trust my present-moment instincts to keep my family safe.",
             [
                 ("If I don't anticipate every worst-case scenario, disaster will strike.",
                  "I release the burden of the future and trust my Spleen to alert me to real danger in the exact moment it's needed."),
                 ("Relaxing my vigilance leaves my loved ones unprotected.",
                  "My most powerful protection is my grounded, calm energy, which only comes when I release mental hyper-vigilance."),
                 ("My ancestors survived by overthinking, so I must do the same.",
                  "I honor my ancestors' survival, but I am safe now to release their mental armor and live freely."),
             ]),
            ("I am responsible for carrying the mental and emotional burdens of my tribe.",
             "I can be deeply compassionate and supportive without taking the mental weight of others into my own energy field.",
             [
                 ("If I don't worry about their problems, it means I don't care.",
                  "Worrying is not love; maintaining my own clear energy is the best way to care for my tribe."),
                 ("It is selfish to have a clear, peaceful mind when others are struggling.",
                  "My peaceful mind is a lighthouse for others; I serve them best by staying out of the storm."),
                 ("I am the designated sponge for my family's stress.",
                  "I choose to be a mirror that reflects their stress back to them for their own growth, rather than a sponge that absorbs it."),
             ]),
            ("Peace of mind is an illusion; there is always another shoe about to drop.",
             "Deep mental peace is my birthright and my baseline; I welcome periods of mental silence with joy and trust.",
             [
                 ("If things are calm, it's just the quiet before the storm.",
                  "Calm is simply calm; I allow myself to fully enjoy and anchor into peaceful moments without anticipating disaster."),
                 ("I must mentally rehearse trauma so I won't be caught off guard.",
                  "I find peace by releasing future worries; I choose to live in the safety of the present."),
                 ("True relaxation makes me vulnerable to attack.",
                  "True relaxation connects me deeply to my Splenic instincts, making me infinitely more resilient, protected, and aware."),
             ]),
        ]

    # ── SACRAL ──
    elif center == "Sacral":
        wb.emotions = [
            ("Exhaustion — Deep Bone Tiredness", [
                "A leaden heaviness in the body that sleep doesn't fix, as if you're running on a battery that never fully charges.",
                "The feeling of being drained after even small social interactions because you've been absorbing and amplifying other people's life force.",
                "Waking up already tired, carrying a fatigue that feels existential rather than physical — like your very being is underpowered.",
            ]),
            ("Guilt — The 'I Should Be Doing More' Feeling", [
                "A constant background hum of guilt whenever you sit still, as if inactivity is a moral failing rather than a biological need.",
                "Watching others work steadily through the day and feeling a sinking shame that you will never be able to do that.",
                "The specific guilt of canceling plans or leaving early because your body simply cannot continue, and believing this makes you unreliable.",
            ]),
            ("Inadequacy — The Broken Motor", [
                "A deep, wordless conviction that something essential is missing from your design — that other people got an engine you were denied.",
                "Feeling like a fraud in every professional setting because you know you can't sustain the output that seems effortless for everyone else.",
                "The humiliation of being seen as lazy when you are actually operating at absolute capacity every single day.",
            ]),
        ]

        wb.limiting = [
            ("Something is fundamentally wrong with me because I can't keep going like other people.",
             f"I am a {t} — I was given a different operating system, a correct one for who I am. My need for rest is a design feature, not a defect.",
             [
                 ("I am simply not trying hard enough — if I pushed more, I could match everyone else.",
                  "I am already operating at maximum capacity. Pushing harder only damages me. My ceiling is correct for my design."),
                 ("My exhaustion means I am weak and undisciplined.",
                  "My exhaustion means I have been absorbing and amplifying other people's energy. It is accurate feedback, not character failure."),
                 ("I will never be able to hold down a normal job or relationship because of this.",
                  "I was not designed for normal. I was designed for precise, strategic impact. The right work and the right people will honor my rhythm."),
             ]),
            ("Rest must be earned — I only deserve to stop when I have produced enough visible output.",
             "Rest is my birthright and my maintenance requirement, a requirement for my wellbeing. I stop because my design requires it, and that is enough.",
             [
                 ("If I rest before I'm completely crashed, I am being lazy.",
                  "Resting before the crash is intelligence, wise self-preservation. I am preserving myself rather than recovering from damage."),
                 ("People will judge me for resting so much.",
                  "The people who matter understand that my rest is productive. Others' judgments are projections of their own conditioning."),
                 ("I can't rest — there's always more to do and I'll fall behind.",
                  "There will always be more to do. I am a human being with natural, healthy limits. I do what I can with the energy I have, and I release the rest."),
             ]),
            ("My value as a person is directly proportional to how much I can produce.",
             "My value is inherent, fixed, and independent of output. I am valuable because I exist, not because I produce. What I see and guide is my gift — not my grind.",
             [
                 ("If I'm not producing, I'm taking up space I don't deserve.",
                  "I take up exactly the space I need. My presence alone has value. I contribute through presence and insight."),
                 ("The only way to prove my worth is through visible, measurable output.",
                  "I prove my worth through clarity, guidance, recognition, and presence — things that cannot be measured in hours or units."),
                 ("People only value me for what I can do for them.",
                  "The right people value me for who I am and what I see. What I do for them flows naturally from recognition, not from proving."),
             ]),
        ]

        wb.programmed = [
            ("A 40-hour work week is normal, and if I can't maintain it, I am failing at adulthood.",
             "The 40-hour week was designed by and for Generators with defined Sacrals. It was never designed for me. My rhythm is different and equally valid.",
             [
                 ("Everyone else manages a full schedule — I should be able to as well.",
                  "Everyone else has a different energetic design. I compare only to my own capacity, and I honor what my body tells me."),
                 ("Part-time or flexible work means I'm not serious or committed.",
                  "Flexible work means I am serious about sustainability. I deliver more in focused bursts than most people deliver in full days."),
                 ("The economy requires full-time grind, and I'll be left behind.",
                  "I create value through insight and guidance, not through hours logged. My economic model is different by design, not by deficiency."),
             ]),
            ("Hustle culture is aspirational — if I'm not grinding, I'm not growing.",
             "Hustle culture is Generator propaganda. I grow through recognition, stillness, and strategic action — not through relentless grinding.",
             [
                 ("Successful people work 24/7 — I should model that.",
                  "Successful people with my design work in bursts of brilliance followed by deep rest. The 24/7 model is for a different type."),
                 ("Sleep is for the weak — I should be able to push through.",
                  "Sleep is my most productive activity. My body repairs, my mind clears, and my guidance sharpens during rest."),
                 ("Side hustles and constant productivity are how you get ahead.",
                  "I get ahead by being recognized for what I already see, by being recognized for what I already see. My one insight is worth a hundred side hustles."),
             ]),
            ("If I want to be respected professionally, I must match the pace of my colleagues.",
             "I earn professional respect through the quality of my guidance and the accuracy of my seeing — not through matching anyone's pace.",
             [
                 ("Colleagues will think I'm slacking if I work fewer hours.",
                  "Colleagues will notice my results, not my hours. What I deliver in two focused hours exceeds their eight scattered ones."),
                 ("I should hide how much I rest so I appear normal.",
                  "I am honest about my design. Hiding costs more energy than being seen. The right environments honor transparency."),
                 ("Career advancement requires consistent, grinding presence.",
                  f"My career advances when I am recognized and invited, not when I am present for the most hours. I am a {t} — my path is different."),
             ]),
        ]

        wb.inherited = [
            ("In my family, you worked until the job was done — rest was for the weak and the privileged.",
             "I break the family pattern. In my design, rest is strength. I work until my body says stop, and that is the completion of my duty.",
             [
                 ("My grandparents worked themselves to death and I owe them the same sacrifice.",
                  "I honor my grandparents' sacrifice by choosing a different path. They worked so I could break the cycle, not repeat it."),
                 ("Stopping before exhaustion is disrespectful to those who couldn't stop.",
                  "Stopping before exhaustion honors those who couldn't stop. I use the freedom they fought for to live differently."),
                 ("Hard work is the only path to dignity in my family.",
                  "Dignity in my lineage now comes through wisdom, presence, and breaking generational patterns — not through self-destruction."),
             ]),
            ("Money only comes through suffering — if it's not hard, it's not honest.",
             "Money comes through alignment, recognition, and the value I provide through my unique gifts. It does not require suffering.",
             [
                 ("If earning is easy, I must be cheating or someone is being exploited.",
                  "Ease in earning means I am aligned with my design. I provide genuine value and I am compensated for it. No suffering required."),
                 ("My family never had financial ease, so I shouldn't either.",
                  "I am the one who changes the financial story. My ease breaks the chain, and my abundance blesses everyone who came before me."),
                 ("I have to struggle to prove I deserve what I earn.",
                  "I deserve what I earn because I provide value. The struggle was inherited conditioning, not cosmic law. I release it."),
             ]),
            ("You don't get to rest while there's work to be done — there's always work to be done.",
             "There is always more work, and there is always a need for rest. I choose rest because a depleted guide cannot guide anyone.",
             [
                 ("Rest is a luxury I haven't earned yet, and maybe never will.",
                  "Rest is a necessity I claim now. Waiting to 'earn' rest is waiting to break. I choose restoration before the crash."),
                 ("My ancestors would be ashamed of how much I rest.",
                  "My ancestors would be proud that I live in a world where I can rest. Their sacrifice was for my freedom, not for my exhaustion."),
                 ("Guilt during rest means I should be working.",
                  "Guilt during rest is inherited programming, not truth. I feel it, I release it, and I continue resting because my body needs it."),
             ]),
        ]

    # ── SOLAR PLEXUS ──
    elif center == "Solar Plexus":
        wb.emotions = [
            ("Emotional Whiplash — Riding Waves That Aren't Yours", [
                "Sudden mood shifts that seem to come from nowhere, leaving you confused about what you actually feel versus what someone nearby is feeling.",
                "The disorienting experience of being fine, then walking into a room and suddenly feeling heavy, anxious, or angry — absorbing the emotional field.",
                "Losing track of your own emotional baseline because you've been amplifying so many other people's feelings that you no longer know which are yours.",
            ]),
            ("Conflict Terror — The Peacekeeper's Exhaustion", [
                "A visceral, physical fear when tension enters a room, as if conflict is a personal failure you must immediately resolve.",
                "The draining, compulsive need to manage everyone's emotional state so you can finally relax — a job that never ends.",
                "Preemptively suppressing your own needs and feelings to avoid creating any ripple that might upset someone else.",
            ]),
            ("Numbness — The Emotional Shutdown", [
                "Going emotionally blank after too much amplification, like a circuit breaker tripping to protect the system.",
                "Feeling guilty for not caring enough about something, when the truth is you've been caring about everything too much for too long.",
                "The hollow, flat sensation of being disconnected from your own emotional life because you've been living in everyone else's.",
            ]),
        ]

        wb.limiting = [
            ("I am responsible for the emotional atmosphere everywhere I go.",
             "I am sensitive to the emotional field, but I am not responsible for managing it. I feel what is present, and I release what is not mine.",
             [
                 ("If there is tension, I caused it or I must fix it.",
                  "Tension in the room existed before I arrived and will exist after I leave. I am a sensor, a receiver of information, separate from its origin."),
                 ("Everyone's feelings are my job to manage.",
                  "Everyone's feelings are their own to manage. I can be compassionate without being responsible. My peace is my priority."),
                 ("I can't relax until everyone around me is okay.",
                  "I can relax regardless of the emotional state of others. My peace is independent of the field. I am allowed to be okay while others process."),
             ]),
            ("If I feel something strongly, it must be true — the emotion IS the fact.",
             "I feel everything deeply, and I distinguish between emotional information and factual truth. My feelings are data, not destiny.",
             [
                 ("This wave of sadness means my life is actually sad and will always be.",
                  f"This wave of sadness is moving through me, amplified by my open center. Waves pass. My {a.lower()} self remains steady beneath them."),
                 ("I made a terrible decision because I feel terrible about it right now.",
                  "Feelings about a decision are not the same as the decision's correctness. I wait for clarity across the wave before evaluating."),
                 ("My emotional intensity is proof that I'm broken or unstable.",
                  "My emotional intensity is proof that I am exquisitely sensitive. I feel more because I sense more. This is a gift, properly understood."),
             ]),
            ("Conflict is dangerous and must be avoided at all costs.",
             "Conflict is information. It reveals what needs attention. I can be present in conflict without absorbing it, and I can speak my truth without destroying peace.",
             [
                 ("If someone is upset with me, I have done something terribly wrong.",
                  "Someone being upset with me may reflect their state, their expectations, or their projection. It is not automatically my fault or my problem to solve."),
                 ("Keeping the peace means swallowing my own needs and feelings.",
                  "Keeping authentic peace means including my needs in the equation. False peace built on my silence is not peace — it is suppression."),
                 ("I will lose people if I express anger or disappointment.",
                  "I will lose only the people who required my silence. Those who stay through my honest expression are the ones who were always meant to stay."),
             ]),
        ]

        wb.programmed = [
            ("Being emotional means being irrational — I should be logical and controlled at all times.",
             "My emotional depth is a form of intelligence, not a form of weakness. I feel deeply and I think clearly. Both are true simultaneously.",
             [
                 ("Professional settings require emotional suppression.",
                  "I bring my full self to every setting. My emotional awareness makes me more perceptive, not less professional."),
                 ("Crying or showing vulnerability means I've lost control.",
                  "Crying is a release valve, a healthy release of pressure. My vulnerability connects me to others and demonstrates strength, demonstrates strength."),
                 ("The ideal state is calm and rational — anything else is a problem to fix.",
                  "The full emotional spectrum is the ideal state. Joy, sorrow, anger, and peace all belong. I don't need to fix feelings — I need to feel them."),
             ]),
            ("Good people don't get angry or hold resentment.",
             "Anger is a healthy signal that a boundary has been crossed. Resentment is information about where I have over-given. Both are valid teachers.",
             [
                 ("If I'm angry, I'm the problem.",
                  "If I'm angry, something needs my attention. The anger is the messenger, not the problem. I listen to what it's telling me."),
                 ("Forgiveness means pretending nothing happened.",
                  "Forgiveness means releasing the emotional charge, not erasing the boundary. I can forgive and still protect myself."),
                 ("I should process anger privately so it doesn't affect anyone.",
                  "I process anger in ways that honor my design. Sometimes that is private. Sometimes it needs witness. Both are correct."),
             ]),
            ("Emotional stability means feeling the same way consistently.",
             "Emotional health means feeling what is true in each moment and allowing it to move through me. Stability is in my ability to feel, not in fixed states.",
             [
                 ("My mood swings mean I'm unstable or unpredictable.",
                  "My mood shifts reflect my sensitivity to the field. I am consistent in my values and my love, even when my emotions fluctuate."),
                 ("I should aim for constant happiness and equanimity.",
                  "I aim for authenticity, not constant happiness. Every emotion has information and value. The full range is the full life."),
                 ("People can't rely on someone whose emotional state changes.",
                  f"People can rely on me because I am honest about where I am. My integrity is consistent even when my mood is fluid. I am a {t} — reliability comes through clarity, not through emotional flatness."),
             ]),
        ]

        wb.inherited = [
            ("In my family, we didn't talk about feelings — we just pushed through.",
             "I am the one who breaks the silence. I talk about feelings, I name them, and I let them move through me. This heals backward through my lineage.",
             [
                 ("Emotional expression is weakness and will get me rejected by my family.",
                  "Emotional expression is courage. My family's discomfort with feelings is their conditioning, not a rule I must follow."),
                 ("If I start feeling, I'll never stop — the dam will break and drown me.",
                  "I can feel in increments. I open the valve slowly, with support. The dam was the problem — the flow is the healing."),
                 ("My parents couldn't handle their feelings, so I learned to handle everyone's.",
                  "I release the role of family emotional processor. I was a child who adapted to survive. I am an adult who gets to choose differently now."),
             ]),
            ("Strong women in my family carried everyone's emotional weight without complaint — that's just what we do.",
             "I honor the strong ones who came before me by choosing a different strength: the strength to put down what was never mine to carry.",
             [
                 ("If I stop carrying the emotional load, the family will fall apart.",
                  "The family held together long before I started carrying this load. My release gives others permission to carry their own share."),
                 ("Self-sacrifice is love — the more I give up, the more I prove I care.",
                  "Self-honoring is love. The more I care for myself, the more genuine care I have available for others. Sacrifice is not required."),
                 ("I owe it to my mother and grandmothers to continue their pattern.",
                  "I owe them the freedom they could not claim. My liberation honors them more than my repetition of their pain ever could."),
             ]),
            ("If something bad happens, it's because of something I felt or did — I attracted it.",
             "Events happen because life happens, not because my feelings manifested them. I release the superstition that my emotions control reality.",
             [
                 ("My anxiety caused the bad thing to happen — I made it real by worrying.",
                  "My anxiety is a response to uncertainty, a response to uncertainty, separate from causation. I did not manifest misfortune. Correlation is not causation."),
                 ("I have to control my thoughts perfectly or I'll bring disaster.",
                  "I release the burden of perfect thoughts. My mind can wander, worry, and wonder without summoning catastrophe. I am safe to think freely."),
                 ("The world is emotionally dangerous and I must stay vigilant.",
                  "The world contains danger and safety, and I am equipped to discern between them. Vigilance is exhausting. Trust is sustainable."),
             ]),
        ]

    # ── ROOT ──
    elif center == "Root":
        wb.emotions = [
            ("Pressure — The Invisible Weight", [
                "A constant physical sensation of being pushed from behind, as if something urgently needs doing and you're already late.",
                "The feeling of a countdown timer running in your chest that never reaches zero — perpetual adrenaline with no clear target.",
                "An ambient stress that attaches itself to whatever task is in front of you, making even small things feel existentially urgent.",
            ]),
            ("Restlessness — The Inability to Settle", [
                "A buzzing physical energy that makes sitting still feel like fighting gravity — your body wants to move even when you have nowhere to go.",
                "The maddening experience of being exhausted but unable to stop, because stopping feels like the pressure will crush you.",
                "Fidgeting, pacing, leg bouncing — your body expressing a pressure your mind can't name or release.",
            ]),
            ("Panic — The Deadline That Doesn't Exist", [
                "Sudden surges of fight-or-flight with no apparent trigger — your body reacting to amplified urgency that has no source in your actual life.",
                "The specific terror of believing you've forgotten something critically important, even after checking everything.",
                "Waking from sleep with a jolt of adrenaline, heart pounding, convinced you're already behind on a day that hasn't started.",
            ]),
        ]

        wb.limiting = [
            ("I should be doing something right now — stillness is failure.",
             "Stillness is a valid and necessary state. I accomplish more by being still when I need to be still than by moving when my body needs rest.",
             [
                 ("Every moment of stillness is a missed opportunity.",
                  "Every moment of stillness is an investment in clarity. Opportunities look different from a rested nervous system."),
                 ("People who are successful never stop moving.",
                  "People who are successful with my design stop frequently. Their power is in strategic stillness, not constant motion."),
                 ("If I'm not busy, I don't matter.",
                  "My significance is independent of my busyness. I matter because I exist, and what I contribute when I do move is precise and powerful."),
             ]),
            ("The urgency I feel is real and demands immediate action.",
             "The urgency I feel is often amplified from the environment. I pause, I breathe, and I discern what is genuinely urgent from what is borrowed pressure.",
             [
                 ("If it feels urgent, I must act now.",
                  "Feeling urgent and being urgent are different. I wait for my body to confirm before I move. Urgency amplifies — clarity discriminates."),
                 ("Waiting means I'll miss the window and fail.",
                  "Waiting is part of my strategy. The right window stays open. What closes before I'm ready was not my door."),
                 ("My nervous system is an accurate barometer of what needs doing.",
                  "My nervous system is an amplifier, a signal receiver. It tells me there is pressure, not what the pressure means. My conscious discernment decodes the signal."),
             ]),
            ("I am inherently behind — everyone else is ahead of me.",
             "I am exactly on time for my own life. The race I'm comparing myself to does not exist. My trajectory is correct for my design.",
             [
                 ("I need to catch up to where I should be by now.",
                  "There is no 'should be.' There is only where I am. From here, I take the next aligned step. That is enough."),
                 ("My peers have accomplished more than me.",
                  "My peers have different designs, different timelines, and different definitions of accomplishment. My path is incomparable."),
                 ("I wasted too much time and I can never get it back.",
                  "Time I spent surviving, resting, healing, or simply being was well-spent and essential. It was preparation. I arrive at each moment exactly when I'm ready."),
             ]),
        ]

        wb.programmed = [
            ("Busy people are important people — a full calendar equals a full life.",
             "A spacious calendar equals a spacious mind. My importance is not measured by how booked I am. I create space for what matters.",
             [
                 ("If my calendar isn't packed, I'm not in demand.",
                  "I am in demand for my vision, not my availability. Scarcity of my time increases the value of my presence."),
                 ("Downtime on the calendar is wasted space I should fill.",
                  "Downtime on the calendar is protected space for restoration. It is the foundation on which everything else is built."),
                 ("Productivity culture says maximize every minute.",
                  "I reject productivity culture. I practice presence culture. Some minutes are for doing. Some are for being. Both are productive."),
             ]),
            ("Speed is a virtue — faster is always better.",
             "Speed is neutral. My correct speed is the one my body sets. I move at the pace of wisdom, not the pace of panic.",
             [
                 ("Quick decisions mean good decisions.",
                  "Quick decisions mean reactive decisions. I take the time my design requires. My best choices brew, not bolt."),
                 ("If I'm not moving fast, I'll be overtaken.",
                  "I am walking my own path. Those who pass me are on their own path. I stay on mine, at my pace, and I arrive precisely when I should."),
                 ("Rapid response is professional — delays are disrespectful.",
                  "Thoughtful response is professional. I respond when I have clarity, not when pressure demands. My timing is correct."),
             ]),
            ("The early bird gets the worm — starting early is morally superior.",
             "Starting when I am ready is superior. My body's readiness, not the clock, determines when I begin. I start when I am fueled, not when I am forced.",
             [
                 ("Morning people are more disciplined and successful.",
                  "People who honor their body's rhythm are more successful. My rhythm may include mornings, afternoons, or nights. All are valid."),
                 ("Sleeping in means I'm lazy and unfocused.",
                  "Sleeping in means my body needed sleep. Rest is productivity. I don't apologize for meeting my body's needs."),
                 ("I should train myself to be a morning person.",
                  "I train myself to listen to my body, not to override it. My natural rhythm is correct. I work with it rather than against it."),
             ]),
        ]

        wb.inherited = [
            ("In my family, you didn't sit down until everyone else was served — your needs came last.",
             "My needs come first so I can genuinely serve others from overflow, from wholeness and surplus. I sit down when my body needs to sit.",
             [
                 ("Putting myself first is selfish and my family would judge me.",
                  "Putting myself first is sustainable. My family's judgment is inherited conditioning. I break the pattern by resting visibly and unapologetically."),
                 ("I owe it to my parents to maintain their standard of sacrifice.",
                  "I owe my parents gratitude, evolution. Their sacrifice bought my freedom. I honor them by using it, not by mimicking their exhaustion."),
                 ("If I'm comfortable while others are working, I've done something wrong.",
                  "My comfort while others work is a valid choice — it is a different design. I am free to define my own anyone's pace to be worthy of ease."),
             ]),
            ("My ancestors survived by staying vigilant — they never rested because rest meant death.",
             "My ancestors survived so that I could rest. Their vigilance kept them alive. My rest keeps me alive in a world where the threats have changed.",
             [
                 ("I carry their hyper-vigilance in my blood — I can't just turn it off.",
                  "I acknowledge the vigilance I inherited. I thank it for keeping my lineage alive. And I gently set it down because the war is over."),
                 ("The adrenaline that saved them is the anxiety that's killing me.",
                  "The same chemical that saved my ancestors is burning through me. I release the ancient alarm. I am safe. The danger is memory, not present reality."),
                 ("Letting go of urgency feels like betraying their struggle.",
                  "Letting go of urgency is the completion of their struggle. They fought for a world where their descendant could be calm. I am that descendant."),
             ]),
            ("Hard times are always coming — you stay ready by never getting comfortable.",
             "Hard times may come, and I will face them from a rested nervous system. Comfort is not complacency — it is the foundation from which I respond effectively.",
             [
                 ("If I relax, I'll be caught off guard when the next crisis hits.",
                  "If I relax, I'll have reserves when the next crisis hits. The rested version of me handles crisis better than the depleted version ever could."),
                 ("Pessimism is realism — hoping for the best is naive.",
                  "Pessimism is a trauma response. Clear-eyed awareness of what is, paired with openness to what could be, is realism. I hold both."),
                 ("Life is fundamentally hard and always will be.",
                  "Life contains hard moments and easy moments. I am learning to receive the easy ones without suspicion. Joy is allowed to stay."),
             ]),
        ]

    # ── AJNA ──
    elif center == "Ajna":
        wb.emotions = [
            ("Doubt — The Endless Second-Guessing", [
                "The exhausting internal loop of questioning every decision after it's made, unable to land on certainty.",
                "Feeling like you need to research one more thing, read one more article, get one more opinion before you can finally decide — and that 'one more' never ends.",
                "The specific frustration of watching other people make confident, quick decisions and wondering what's wrong with your mind that you can't do the same.",
            ]),
            ("Fog — The Mental Static", [
                "A thick, heavy sensation in the head when trying to form a clear thought — like thinking through syrup.",
                "Knowing you're intelligent but being unable to access your intelligence on demand because your mind is processing everyone else's mental noise.",
                "The disorienting experience of having clarity alone, then losing it entirely the moment someone asks you to explain it.",
            ]),
            ("Inadequacy — The Certainty Deficit", [
                "A deep shame about not having fixed opinions, as if conviction is a prerequisite for being taken seriously.",
                "Feeling intellectually outclassed in every conversation because everyone else seems to arrive with fully-formed positions while you're still processing.",
                "The quiet terror of being asked 'what do you think?' and having nothing definitive to offer because you see too many sides.",
            ]),
        ]

        wb.limiting = [
            ("I should have a clear, fixed opinion about things — not having one means I'm intellectually weak.",
             "My mind processes many perspectives simultaneously. I arrive at clarity through synthesis, through spacious, open awareness. My spacious thinking is a strength.",
             [
                 ("People won't respect me if I can't take a firm stand.",
                  "People respect my depth of consideration. Taking time to form an opinion demonstrates wisdom, demonstrates strength. I am thorough, thorough and deliberate."),
                 ("Changing my mind means I was wrong before.",
                  "Changing my mind means I learned something new. Evolution of thought is the hallmark of intelligence. I grow openly and visibly."),
                 ("I need to have an answer ready for every question.",
                  "I am allowed to say 'I'm still forming my thoughts on that.' Curiosity and openness are more impressive than premature certainty."),
             ]),
            ("I can't trust my own thinking — it's unreliable and inconsistent.",
             f"I can trust my thinking process, which is fluid and adaptive. My {a.lower()} authority provides the final word, and my mind provides the exploration.",
             [
                 ("My thoughts change too much — something must be broken.",
                  "My thoughts change because I take in new information. Fluidity is intelligence. A mind that never changes has stopped learning."),
                 ("I need external validation to know if my thinking is correct.",
                  "I validate my own thinking through results, alignment, and inner knowing. External feedback is information, not permission."),
                 ("My scattered thoughts mean I'll never accomplish anything focused.",
                  "My scattered thoughts are my brainstorming phase. When the time comes to execute, I synthesize and focus. The scatter is collection, not chaos."),
             ]),
            ("I'm not as smart as people who can articulate their position instantly.",
             "My intelligence is deep, not fast. I process thoroughly and deliver insight that is worth the wait. Speed of articulation is not depth of understanding.",
             [
                 ("Quick thinkers are smarter than me.",
                  "Quick thinkers think quickly. Deep thinkers think thoroughly. Both are forms of intelligence. Mine is depth, and depth takes time."),
                 ("I should be able to debate and defend my position on the spot.",
                  "I think best in reflection, not in combat. I am not required to perform my intelligence on anyone else's timeline or format."),
                 ("My mind goes blank under pressure — that proves I don't know anything.",
                  "My mind going blank under pressure is my system protecting itself from overload. It's a circuit breaker, not a reflection of my knowledge."),
             ]),
        ]

        wb.programmed = [
            ("A degree or certification proves you know what you're talking about — without credentials, your knowledge doesn't count.",
             "My knowledge counts because I have lived it, synthesized it, and can apply it. Credentials confirm; they do not confer. My wisdom stands on its own.",
             [
                 ("I need more education before I can call myself an expert.",
                  "I am an expert through experience, study, and application. Formal education adds to my expertise; it does not create it."),
                 ("People will question my authority without credentials.",
                  "People question authority regardless of credentials. I lead with results and insight. Those who need paper proof are not my audience."),
                 ("I should go back to school to legitimize what I already know.",
                  "I legitimize what I know by using it. Practical application is the highest credential. I invest in education when it serves growth, not validation."),
             ]),
            ("You need to pick a lane — being interested in everything means you're a master of nothing.",
             "My breadth of interest is my superpower. I connect dots across disciplines that specialists miss. I am a synthesist, and synthesis is mastery.",
             [
                 ("Jack of all trades, master of none — that's a failure.",
                  "Jack of all trades, connector of all domains. I see patterns across fields that narrow specialists cannot. Integration is my expertise."),
                 ("I should pick one thing and go deep like everyone else.",
                  "Going wide IS how I go deep. My depth is in the connections, in the connections between fields. I trust how my mind naturally works."),
                 ("My varied interests make me look unfocused and scattered.",
                  "My varied interests make me innovative and adaptable. The world needs generalists who can translate between specialties."),
             ]),
            ("Intelligence is measurable — tests, grades, and metrics define how smart you are.",
             "Intelligence is multidimensional and mostly unmeasurable. My ability to synthesize, perceive, and guide cannot be captured by any test. I am smart in ways that matter.",
             [
                 ("My test scores or grades define my intellectual ceiling.",
                  "My intellectual capacity is not bounded by any score. Tests measure a narrow band of performance, not the full spectrum of my intelligence."),
                 ("I'm not a 'numbers person' so I'm limited in certain fields.",
                  "I can learn anything I need to learn. Labels like 'numbers person' or 'creative type' are false binaries. I contain multitudes."),
                 ("If I was really smart, I'd have accomplished more by now.",
                  "Accomplishment is a function of timing, opportunity, and design — not just intelligence. My timeline is correct. My mind is more than enough."),
             ]),
        ]

        wb.inherited = [
            ("In my family, you had to be right — being wrong was dangerous and humiliating.",
             "I release the need to be right. I prioritize learning, growing, and being honest over being correct. My safety does not depend on my perfection.",
             [
                 ("Admitting I'm wrong means losing face and losing love.",
                  "Admitting I'm wrong builds trust. People connect with honesty, not with perfection. I am loved for my humanity, not my infallibility."),
                 ("I must defend my position to the death or I'm weak.",
                  "I can hold a position and release it gracefully when new information arrives. Flexibility is strength. Rigidity is fear."),
                 ("My family argued to win — that's how you prove your worth.",
                  "I discuss to understand. Winning arguments is inherited programming. Genuine understanding is my chosen value."),
             ]),
            ("Education was the only way out for my family — if you're not credentialed, you're nothing.",
             "Education opened doors for my family, and I honor that. I also expand the definition — my lived education, my synthesis, and my guidance are equally valid credentials.",
             [
                 ("Without a diploma on the wall, I'm a fraud.",
                  "My results are my diploma. My clients' success is my accreditation. The wall is optional. The value is real."),
                 ("My ancestors sacrificed for my education — I owe them a degree.",
                  "My ancestors sacrificed for my opportunity, not specifically for a degree. I honor them by using my mind fully, however that looks."),
                 ("People from my background have to work twice as hard to be taken seriously.",
                  "I work smart, not twice as hard. My background gave me perspective, resilience, and hunger. These are advantages, not deficits I must overcome."),
             ]),
            ("Thinking too much is dangerous — it leads away from faith and family.",
             "Thinking deeply leads me toward truth, which includes faith and family in expanded forms. My mind is not a threat to my belonging. It is the vehicle of my contribution.",
             [
                 ("Questioning inherited beliefs means betraying my roots.",
                  "Questioning inherited beliefs means I am awake. I can honor my roots while growing my own branches. The tree is stronger for the questioning."),
                 ("Intellectual curiosity made people in my family leave the fold.",
                  "Intellectual curiosity expands the fold. Those who left found wider belonging. Those who stayed found deeper faith. Both are valid."),
                 ("There is a danger in knowing too much — stay humble, stay small.",
                  "Knowledge is power, not danger. I can be humble and expansive. I can stay grounded and reach high. Smallness is not humility — it is hiding."),
             ]),
        ]

    # ── HEART/EGO ──
    elif center == "Heart/Ego":
        wb.emotions = [
            ("Unworthiness — The Invisible Ledger", [
                "A gnawing sense that you owe the world something you haven't paid yet, and until you pay it, you don't deserve good things.",
                "The specific shame of receiving a compliment or gift and immediately feeling like you need to give something back to balance the scales.",
                "A chronic, low-grade belief that you're getting away with something — that any moment, someone will discover you don't belong.",
            ]),
            ("Emptiness — The Hollow Chest", [
                "A physical sensation of hollowness in the chest when you try to assert yourself or claim what you want.",
                "The feeling that your willpower is borrowed, not generated — like the gas tank is always on empty and you're coasting on fumes.",
                "Watching others go after what they want with conviction while you feel frozen, unsure if you even have the right to want anything.",
            ]),
            ("Resignation — The Surrendered Will", [
                "A quiet, settled belief that wanting things is pointless because you won't follow through anyway.",
                "The preemptive defeat of not starting because you've learned that your motivation will evaporate before you finish.",
                "Feeling fundamentally unreliable to yourself — like you can't trust your own promises because your willpower has failed too many times.",
            ]),
        ]

        wb.limiting = [
            ("I am fundamentally unworthy of success, love, and good things.",
             "I arrived worthy. My worth was never in question — only my awareness of it was. I am inherently deserving of all the good that comes to me.",
             [
                 ("I have to earn my worth through sacrifice and proving.",
                  "My worth is my birthright. I do good things because I am worthy, not to become worthy. The direction is reversed."),
                 ("People will eventually discover I'm a fraud and don't belong here.",
                  f"I belong wherever I am invited. My {t} design means I am seen and recognized for exactly who I am. I am not hiding — I am unfolding."),
                 ("Other people deserve success — I have to work harder for less.",
                  "I deserve success on the same terms as anyone else. I release the inherited ledger that says my account starts in the negative."),
             ]),
            ("I can't commit to anything because I don't have the willpower to follow through.",
             f"I commit through my {a.lower()} authority, which is instantaneous and certain. When my body says yes, my will aligns. I don't need constant willpower — I need aligned invitation.",
             [
                 ("My track record of unfinished projects proves I'm incapable.",
                  "My track record proves I was starting from borrowed energy rather than from genuine invitation. Aligned starts lead to sustainable completion."),
                 ("I get excited and then lose interest — that's a character flaw.",
                  "I explore possibilities, and my body tells me which ones are mine to continue. Discontinuing what isn't mine is discernment, part of the exploration."),
                 ("People can't count on me because my commitment is unreliable.",
                  "People can count on me when I commit from my authority rather than from pressure. My yes, when genuine, is absolute. My no, when spoken, is final."),
             ]),
            ("I have nothing of real value to offer — my contribution is replaceable.",
             "I offer what no amount of effort can produce: clear seeing, precise recognition, and guidance that transforms. My contribution is irreplaceable.",
             [
                 ("Anyone could do what I do — probably better.",
                  "No one sees what I see from where I stand. My unique combination of design, experience, and perspective produces insight that cannot be replicated."),
                 ("I should charge less because my work isn't worth premium rates.",
                  "I charge what my guidance is worth. The right clients recognize the value and pay it gladly. Undercharging is self-sabotage, not humility."),
                 ("I need more skills, more credentials, more proof before I can offer real value.",
                  "I am already valuable. What I know now is more than enough to help the people who need exactly what I offer. I start now, not after more preparation."),
             ]),
        ]

        wb.programmed = [
            ("Your value to society is measured by your income, title, and output.",
             "My value to society is measured by the lives I touch, the clarity I bring, and the guidance I offer. Income and titles are byproducts, not measures.",
             [
                 ("If I'm not earning well, I must not be providing value.",
                  "Earnings reflect monetization, not value. Many of the most valuable people in history earned nothing. I separate worth from revenue."),
                 ("I need an impressive title to be taken seriously.",
                  "I am taken seriously because of what I bring to the room, not because of what's printed on a card. My presence is my title."),
                 ("My LinkedIn or resume should tell a coherent, linear success story.",
                  "My story is a constellation, not a line. The diverse path brought me here, and every point on the map contributed to my current capacity."),
             ]),
            ("Real adults have stable careers, retirement plans, and consistent trajectories.",
             "Real adults live authentically. My trajectory is correct for my design, even when it doesn't match the template. Stability looks different for different people.",
             [
                 ("I should have figured out my career by now.",
                  "I figure out my next step, not my entire career. Life reveals itself incrementally. I am on track for a life that is mine, not a template."),
                 ("Not having a clear 5-year plan means I'm directionless.",
                  "My direction is guided by recognition and invitation, not by a rigid plan. I respond to life as it presents itself, and that is more adaptive than any plan."),
                 ("I'm falling behind my peers on the standard life milestones.",
                  "Standard milestones were designed for standard designs. My milestones are custom. I measure my progress against my own path, not against a generic timeline."),
             ]),
            ("Willpower is a muscle — if yours is weak, you just need to train it harder.",
             f"Willpower for a {t} comes through alignment, not through training. When I am correctly invited and recognized, my will engages effortlessly.",
             [
                 ("I should be able to discipline myself into consistency.",
                  "Consistency through discipline is Generator programming. My consistency comes through following my authority. Alignment creates its own momentum."),
                 ("Motivational speakers and productivity systems work for everyone — I just haven't found the right one.",
                  "Productivity systems are built for defined Sacrals. My system is: wait for invitation, trust my authority, rest deeply between bursts. That is my productivity."),
                 ("If I just wanted it badly enough, I'd make it happen.",
                  "Wanting is alignment with invitation is my fuel. Invitation is. When the right door opens and my body says yes, I walk through with power. Until then, I wait in peace."),
             ]),
        ]

        wb.inherited = [
            ("In my family, your worth was measured by your paycheck — if you weren't earning, you weren't contributing.",
             "I measure contribution by impact, presence, and the quality of what I bring — not by the number on a check. My worth precedes and exceeds my income.",
             [
                 ("My father or grandfather worked himself to death and that was honorable.",
                  "I honor their sacrifice. I also choose a different honor: sustainability, presence, and breaking the cycle of self-destruction as proof of worth."),
                 ("Money worries are genetic — I inherited financial anxiety and can't escape it.",
                  "I inherited financial patterns, not financial destiny. I can learn new relationships with money. Anxiety is a passed-down habit, not a biological sentence."),
                 ("The men in my family provide — if I can't provide, I'm failing at manhood.",
                  "My definition of providing includes presence, guidance, emotional availability, and wisdom. I provide in ways my ancestors could not, and that expands manhood rather than failing it."),
             ]),
            ("We come from humble people — reaching above your station brings shame and failure.",
             "I come from humble people who gave me the foundation to rise. Reaching is not arrogance. Rising is not betrayal. My success honors where I came from.",
             [
                 ("Wanting more than my parents had is ungrateful.",
                  "Wanting more is wanting to expand the legacy, not reject it. My parents wanted more for me than they had. Achieving it fulfills their hopes, not insults them."),
                 ("People from my background don't make it in certain industries.",
                  "People from my background bring perspective that those industries desperately need. I am not an imposter — I am a pioneer."),
                 ("If I become too successful, my family won't relate to me anymore.",
                  "If I become successful, I expand the definition of what's possible for my family. They may take time to adjust. I hold space for their journey alongside my own."),
             ]),
            ("You don't get to rest until you've made it — and most of us never make it.",
             "I rest because rest is how I sustain the journey. 'Making it' is not a finish line — it's a rhythm. I rest at every stage of the climb, and that is how I summit.",
             [
                 ("Rest is a reward for the successful — I haven't earned it yet.",
                  "Rest is the fuel for success, not the reward for it. I rest now, at this stage, because the next stage requires a full tank."),
                 ("My ancestors never rested — what right do I have?",
                  "My ancestors rested when they could. I have the right to rest because I live in a world they helped build. I honor them by using the peace they sacrificed for."),
                 ("If I stop pushing, I'll slide back into poverty or obscurity.",
                  "I am not on a cliff edge. I am on a path. Resting does not erase forward progress. It consolidates it. I can pause without losing ground."),
             ]),
        ]

    # ── SPLEEN ──
    elif center == "Spleen":
        wb.emotions = [
            ("Fear — The Constant Low Hum", [
                "A baseline sense that something is wrong, something is about to happen, some invisible threat is approaching — with no specific evidence.",
                "The physical sensation of being startled easily, as if your nervous system is tuned to a frequency of danger that others can't hear.",
                "A exhausting hyper-awareness of your body's signals — every ache, every unusual sensation triggers a cascade of worst-case scenarios.",
            ]),
            ("Hyper-vigilance — The Scanner That Never Sleeps", [
                "Involuntarily scanning every room for exits, every face for threat, every situation for what could go wrong.",
                "The inability to fully relax in public or around others because part of you is always on sentry duty.",
                "Exhaustion that comes from being the early warning system for everyone around you, catching dangers they don't even perceive.",
            ]),
            ("Disconnection — The Muted Instinct", [
                "The frustration of knowing you have strong intuition but being unable to access it reliably — it's there one day and gone the next.",
                "Making a decision that felt right, only to have it blow up, and wondering if you can ever trust your gut again.",
                "The paradox of feeling deeply unsafe while simultaneously being unable to tell what is actually dangerous versus what is just amplified fear.",
            ]),
        ]

        wb.limiting = [
            ("I am fundamentally unsafe — the world is dangerous and I am unprotected.",
             "I am fundamentally safe, and my body is equipped with an exquisite early warning system that alerts me to genuine threats. The baseline fear is amplification, not reality.",
             [
                 ("This constant sense of dread means actual danger is present.",
                  "The constant sense of dread means my open Spleen is amplifying fear from the environment. I distinguish between amplified signal and genuine threat."),
                 ("I can never truly relax because something bad is always about to happen.",
                  "I can relax because most of what I feel is borrowed fear passing through me. When genuine danger arises, my Spleen will alert me. Until then, I rest."),
                 ("People who feel safe are naive — I see what they don't see.",
                  "People who feel safe are not naive — they have defined Spleens or different conditioning. My hyper-vigilance is a pattern, not superior perception."),
             ]),
            ("I can't trust my instincts — they've been wrong too many times.",
             f"My {a.lower()} authority is instantaneous and accurate when it's actually my signal. What I've been hearing is everyone else's fear mixed with my own intuition. I am learning to distinguish them.",
             [
                 ("Every time I followed my gut, I got burned.",
                  "What I thought was my gut was often amplified fear from my open Spleen. My genuine instinct has a different quality — quieter, simpler, more certain."),
                 ("My intuition is unreliable — it shows up randomly and I can't depend on it.",
                  f"My intuition is consistent in its nature: it speaks once, softly, in the moment. I am learning to recognize its voice and trust its timing."),
                 ("I need external confirmation before I act on a feeling.",
                  "My feeling IS the confirmation. My body's yes and no are complete answers. I don't need external validation for what I already know internally."),
             ]),
            ("I absorb everyone's fear and anxiety — I'm an emotional sponge with no protection.",
             "I am sensitive to fear in the environment, and I have the power to release it. I am a sensor, not a sponge. I detect, I acknowledge, I let go.",
             [
                 ("Other people's anxiety becomes my anxiety and there's nothing I can do.",
                  "Other people's anxiety passes through me when I let it. I observe it, I name it as not mine, and I release it. The more I practice, the faster it moves."),
                 ("I have to avoid anxious people or I'll be contaminated.",
                  "I don't need to avoid anxious people — I need to maintain my internal boundary. I can be present with someone in distress without absorbing their distress."),
                 ("Taking on others' fear is how I show I care.",
                  "Staying clear and grounded is how I show I care. I can support someone better from a place of calm than from a place of shared panic."),
             ]),
        ]

        wb.programmed = [
            ("Real security comes from money, insurance, backup plans, and controlling every variable.",
             "Real security comes from trusting my body's knowing in the present moment. Preparedness is wise. Obsessive control is fear. I practice the first and release the second.",
             [
                 ("If I don't have a backup plan for my backup plan, I'm being irresponsible.",
                  "One backup plan is preparation. Three backup plans is anxiety. I prepare reasonably and trust my ability to respond to what actually happens."),
                 ("Financial security is the only real security.",
                  "Financial security is one form of security. Somatic security — knowing I can trust my body — is deeper and more reliable. I build both."),
                 ("The world is getting more dangerous and I need to protect against everything.",
                  "The world contains risk and safety, as it always has. I can reasonably prepare without living in a fortress of fear. My awareness is protection enough."),
             ]),
            ("If you're not worried, you're not paying attention.",
             "If I'm not worried, I am present. Worry is not attention — it is borrowed fear masquerading as vigilance. True attention is calm and clear.",
             [
                 ("Worrying is my way of being prepared — it's productive.",
                  "Worrying is rehearsing a future that hasn't arrived. It taxes my nervous system without improving outcomes. Planning is productive. Worrying is draining."),
                 ("The responsible people are the ones who worry.",
                  "The responsible people are the ones who act, not the ones who worry. I can be responsible without being afraid. I separate concern from anxiety."),
                 ("If I stop worrying, I'll miss something important.",
                  "Stopping worry creates space for genuine intuition to surface. What is important will reach me without me hunting for it anxiously."),
             ]),
            ("Trust must be earned slowly — people are dangerous until proven safe.",
             "Trust can be given in increments and adjusted as information arrives. I don't need to start from suspicion. I start from openness and calibrate from experience.",
             [
                 ("Everyone has an agenda — I need to figure out what people really want.",
                  "Most people are doing their best. I can be discerning without being paranoid. I read people's energy, not their hidden motives."),
                 ("I've been betrayed before — I won't let it happen again.",
                  "I was betrayed because someone made a choice, not because I was too trusting. I keep my heart open and my boundaries clear. Both can coexist."),
                 ("Safety means keeping people at a distance.",
                  "Safety means knowing I can handle whatever happens, including disappointment. Distance is not protection — resilience is."),
             ]),
        ]

        wb.inherited = [
            ("My family survived by being suspicious of outsiders — trust the family, question everyone else.",
             "I honor my family's survival strategy and I expand it. I can trust selectively, love widely, and maintain discernment without inherited suspicion.",
             [
                 ("Strangers are threats until proven otherwise.",
                  "Strangers are neutral until their actions provide information. I approach people with openness and adjust based on what I experience, not what I inherited."),
                 ("The world outside the family is hostile and unforgiving.",
                  "The world contains hostility and warmth. I have navigated both. My family's experience of the world was real, and mine is different in important ways."),
                 ("Blood is the only bond you can truly trust.",
                  "Trust is built through consistency, presence, and integrity — not through genetics. I have blood bonds and chosen bonds. Both can be trustworthy."),
             ]),
            ("There is always a hidden danger — my grandmother survived by never letting her guard down.",
             "My grandmother survived by never letting her guard down, and that vigilance served her. I live in a different world with different tools. I can lower my guard and still be safe.",
             [
                 ("I carry my grandmother's fear in my cells — I can't escape it.",
                  "I carry my grandmother's resilience in my cells, and her fear was part of that. I honor the fear by transforming it, not by repeating it."),
                 ("Lowering my guard means forgetting what they went through.",
                  "Lowering my guard means I am free in ways they could not be. That freedom is the fruition of their sacrifice, not the erasure of it."),
                 ("Vigilance is love — staying on alert is how I protect my family.",
                  "Presence is love. Calm is protection. A grounded parent protects better than an anxious one. My family needs my peace, not my panic."),
             ]),
            ("Pain is inevitable — don't get comfortable because life will take it away.",
             "Joy and pain both arrive, and neither is permanent. I can fully enjoy the good without bracing for its end. The bracing steals the joy without preventing the loss.",
             [
                 ("Happiness is always followed by disaster — I've seen the pattern.",
                  "Happiness and difficulty alternate in every life. The pattern does not mean happiness causes disaster. They coexist in a rhythm, and I can enjoy the peaks."),
                 ("If I let myself be happy, I'll be blindsided when it ends.",
                  "If I let myself be happy, I will have BEEN happy. That is not wasted — it is accumulated. Joy banked is joy earned, regardless of what follows."),
                 ("The family curse is that good things never last for us.",
                  "The family story is rewriting through me. Good things last as long as they last, and I savor them fully while they're here. That is the new inheritance."),
             ]),
        ]

    # ── G CENTER ──
    elif center == "G":
        wb.emotions = [
            ("Lostness — The Missing Compass", [
                "A hollow, directionless feeling as if you're wandering without a map while everyone else seems to have a GPS.",
                "The confusion of genuinely not knowing what you want — not because you haven't thought about it, but because your sense of direction fluctuates with your environment.",
                "A quiet panic when asked 'where do you see yourself in five years?' because your honest answer is 'it depends on who I'm with and what finds me.'",
            ]),
            ("Identity Drift — The Shape-Shifter's Exhaustion", [
                "The subtle terror of noticing you're a different person with different people — and not knowing which version is real.",
                "Exhaustion from constantly mirroring the identity of whoever you're with, losing yourself in the process.",
                "The grief of feeling like you've never had a solid self — just a collection of reflections of other people.",
            ]),
            ("Unbelonging — The Eternal Outsider", [
                "A pervasive sense that you don't truly belong anywhere, even in spaces where you are welcomed and loved.",
                "Watching groups form, bonds deepen, and communities coalesce while feeling like you're behind glass — present but not part of it.",
                "The ache of knowing you're loved but still feeling fundamentally alone, as if love can reach you but can't quite land.",
            ]),
        ]

        wb.limiting = [
            ("I don't know who I am — I have no fixed identity.",
             "I am identity-fluid by design. I discover myself through the right spaces, the right people, and the right invitations. My self is revealed relationally, not defined in isolation.",
             [
                 ("Everyone else has a solid sense of self — I'm hollow.",
                  "Everyone else has a different design. My sense of self is discovered through experience and relationship, not through internal fixedness. I am not hollow — I am open."),
                 ("I change who I am depending on who I'm with — that's fake.",
                  "I reflect different facets depending on who I'm with. This is sensitivity, not fakery. The full me contains all these facets — none is more real than the others."),
                 ("I'll never figure out who I really am.",
                  "I am not a puzzle to be solved. I am an unfolding to be experienced. Each year, each person, each place reveals another layer. This is the journey."),
             ]),
            ("I have no direction — I don't know where I'm going in life.",
             f"My direction reveals itself through alignment and invitation, not through forcing a path. As a {t}, I am guided to where I'm needed. The path becomes clear as I walk it.",
             [
                 ("I should have a clear life plan like everyone else.",
                  "Life plans are for defined Gs. My path emerges through following what lights me up and saying yes to the right invitations. This is not lack — it's a different navigation system."),
                 ("Not knowing my purpose means I'm failing at life.",
                  "Not knowing my purpose means I'm open to being found by it. Purpose that announces itself is more powerful than purpose that is manufactured."),
                 ("I'm drifting while everyone else is advancing.",
                  "I am not drifting — I am magnetizing. The right directions, people, and opportunities are drawn to my openness. My trajectory looks different but arrives precisely where it should."),
             ]),
            ("I don't belong anywhere — I'm fundamentally out of place.",
             "I belong wherever I am recognized and invited. My belonging is not static — it is dynamic and relational. I am home in the right spaces with the right people.",
             [
                 ("There's something wrong with me that keeps me from fitting in.",
                  "There is nothing wrong with me. I fit where I'm meant to fit. Not fitting everywhere is a filter, not a flaw."),
                 ("Everyone else has found their people — I'm still searching.",
                  "Finding my people is a process of being in the right places at the right times. The search is part of the exploration — it is the journey toward alignment."),
                 ("I'll always feel like an outsider.",
                  "Feeling like an outsider is a sensation I experience, not a permanent state. In the right spaces, I feel at home. I trust that more of those spaces are coming."),
             ]),
        ]

        wb.programmed = [
            ("You need to find your passion and pursue it relentlessly — that's how you build a meaningful life.",
             "I don't need one passion — I need alignment. My meaningful life is built through following what resonates in each season, not through forcing a single obsession.",
             [
                 ("I should have found my 'one thing' by now.",
                  "I am not a 'one thing' person. I am a constellation. Different stars light up at different times. The whole sky is my calling."),
                 ("People who change direction are flaky and unreliable.",
                  "People who change direction are responsive to life. I change because I grow, because I learn, because new invitations arrive. This is adaptability, not flakiness."),
                 ("A life without a singular mission is a wasted life.",
                  "A life with many missions is a rich life. I don't need singularity to have significance. My impact is cumulative and multidimensional."),
             ]),
            ("You are the architect of your own life — if you're lost, you just haven't planned well enough.",
             "I am the co-creator of my life, along with the invitations life presents me. Being responsive is not being passive. I build with what arrives, and what arrives is often better than what I could have planned.",
             [
                 ("If I just planned more, I'd feel less lost.",
                  "Planning more would not resolve my open G — it would just create more rigid expectations to feel disappointed by. My peace comes from trusting the unfolding."),
                 ("Taking life as it comes means I have no ambition.",
                  "Taking life as it comes while following my authority is the most ambitious thing I can do. I pursue what is correct for me, not what looks ambitious from the outside."),
                 ("Successful people impose their will on the world.",
                  "Successful people with my design respond to the world. They are invited, they recognize, they guide. Success through imposition belongs to Manifestors. Mine comes through alignment."),
             ]),
            ("You should know who you are by now — identity is something you build in your twenties.",
             "Identity is something I experience across my entire life. I am not late. I am not behind. My self is revealed in layers, and each decade I know myself more deeply.",
             [
                 ("I'm too old to still be figuring myself out.",
                  "I will be figuring myself out until my last breath, because I am alive and changing. Self-knowledge is not a destination — it is a relationship."),
                 ("Mature adults have stable identities.",
                  "Mature adults have honest relationships with their changing selves. Stability is in the honesty, not in the fixity."),
                 ("I missed the window to become someone.",
                  "There is no window. There is only today. Whoever I become, I am becoming now. The past is not a locked door — it is the road I took to get here."),
             ]),
        ]

        wb.inherited = [
            ("In my family, you stuck to the path — deviation was dangerous and selfish.",
             "I honor my family's path and I walk my own. Deviation is not betrayal — it is evolution. My path expands what is possible for everyone who comes after me.",
             [
                 ("Leaving the expected path means I'm rejecting my family.",
                  "Leaving the expected path means I am living my design. I love my family AND I live differently. These are not contradictions."),
                 ("My parents sacrificed for me to have a stable life — I owe them conformity.",
                  "My parents sacrificed for me to have choices. Making different choices honors their sacrifice more than copying their choices would."),
                 ("The safe path is the right path — risk is irresponsibility.",
                  "The safe path is one option. The aligned path — regardless of risk — is my option. I can be responsible and unconventional."),
             ]),
            ("We are simple people — don't get ideas above your station.",
             "We are people with depth, dreams, and capacity. My station is wherever I can reach, and I reach without apology. My rising lifts the whole lineage.",
             [
                 ("Aspiring beyond my background is arrogant.",
                  "Aspiring beyond my background is courageous. My background is my foundation, not my ceiling. I build upward with pride."),
                 ("People like us don't do things like that.",
                  "I am the first 'people like us' to do things like this. That makes me a pioneer, not a pretender."),
                 ("My family will feel left behind if I rise too far.",
                  "My rising creates a new reference point for my family. What they do with that is their journey. My journey is to rise as high as I am called."),
             ]),
            ("Home is a specific place and leaving it means losing yourself.",
             "Home is where I am aligned. I carry home within me. Places change, and my sense of self adapts and deepens through every move and every new belonging.",
             [
                 ("I'll never feel at home anywhere else.",
                  "I can feel at home in many places. Home is a feeling I cultivate, not just a location I inherit. I am building home wherever I go."),
                 ("Leaving my hometown means abandoning my roots.",
                  "Roots can stretch. I am connected to where I came from AND to where I am going. The roots grow with me."),
                 ("My children should know the same home I knew.",
                  "My children will know the home I create for them. It may look different from mine, and it will be just as valid. Different is not less."),
             ]),
        ]

    return wb


# ═══════════════════════════════════════════════════════════════
# GENERATOR
# ═══════════════════════════════════════════════════════════════

class WorkbookGenerator:

    def __init__(self, chart: dict):
        self.chart = chart
        self.context = DesignContext(chart)
        self.beliefs: List[BeliefPair] = []
        self.all_pairs: List[Tuple[str, CenterWorkbook]] = []

    def generate(self, tier: str = "comprehensive") -> List[BeliefPair]:
        for center in self.context.undefined_centers:
            wb = get_center_content(center, self.context)
            self.all_pairs.append((center, wb))

            # Collect all limiting beliefs + their subordinates
            for lim, emp, subs in wb.limiting:
                self.beliefs.append(BeliefPair(lim, emp, center, "limiting", "core"))
                for s_lim, s_emp in subs:
                    self.beliefs.append(BeliefPair(s_lim, s_emp, center, "limiting", "subordinate"))

            for lim, emp, subs in wb.programmed:
                self.beliefs.append(BeliefPair(lim, emp, center, "programmed", "core"))
                for s_lim, s_emp in subs:
                    self.beliefs.append(BeliefPair(s_lim, s_emp, center, "programmed", "subordinate"))

            for lim, emp, subs in wb.inherited:
                self.beliefs.append(BeliefPair(lim, emp, center, "inherited", "core"))
                for s_lim, s_emp in subs:
                    self.beliefs.append(BeliefPair(s_lim, s_emp, center, "inherited", "subordinate"))

        # Add design-specific
        self._add_design_beliefs()

        if tier == "short":
            self.beliefs = self._distill(self.beliefs, 50)

        return self.beliefs

    def _add_design_beliefs(self):
        t = self.context.type
        a = self.context.authority
        m = self.context.motivation

        if t == "Projector":
            self.beliefs.append(BeliefPair(
                "Success requires grinding harder and longer than everyone else.",
                "I succeed through recognition and invitation. I guide with precision when I am seen, and I rest when I am between invitations. Grinding was Generator conditioning that I release.",
                "Design", "design", "core"))
            self.beliefs.append(BeliefPair(
                "If I stop pushing, everything I have built will collapse.",
                "What I build from alignment and invitation endures. What I built from borrowed energy served its purpose and can be released. I trust the foundation I create when I am aligned with my design.",
                "Design", "design", "core"))

        if m == "Fear":
            self.beliefs.append(BeliefPair(
                "My fear is a malfunction I must suppress or overcome.",
                "My fear is a compass. It points toward what needs my attention with clarity and precision. I follow it to understanding and then I move forward with confidence.",
                "Design", "design", "core"))

        if a == "Splenic":
            self.beliefs.append(BeliefPair(
                "A gut feeling is not a valid reason for a decision.",
                "My body knows instantly and speaks once. My instantaneous knowing is a complete answer. I trust what arrives in the moment without requiring justification.",
                "Design", "design", "core"))

    def _distill(self, beliefs: List[BeliefPair], max_beliefs: int = 50) -> List[BeliefPair]:
        # Take core beliefs from each category per center (most impactful)
        distilled = []
        seen = set()
        # Priority: limiting core > programmed core > inherited core > design
        priorities = ["limiting", "programmed", "inherited", "design"]
        for priority in priorities:
            for b in beliefs:
                if b.category == priority and b.depth == "core":
                    key = (b.center, b.category)
                    if key not in seen:
                        distilled.append(b)
                        seen.add(key)
                        if len(distilled) >= max_beliefs:
                            return distilled[:max_beliefs]
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
            f"**Tier:** {tier} | **Belief Pairs:** {len(self.beliefs)}",
            f"",
            f"---",
            f"",
            f"## How This Workbook Works",
            f"",
            f"Each open center in your design absorbs and amplifies energy from the world.",
            f"This workbook names exactly what you absorb — the emotions that live there,",
            f"the beliefs that formed, and the empowering replacements that set you free.",
            f"",
            f"**For each limiting belief, read it aloud, feel where it lives in your body,",
            f"clear it (scribble, tap, breathe), and read the empowering belief three times.**",
            f"",
            f"Work through 5 belief pairs per day.",
            f"",
            f"---",
            f"",
        ]

        belief_num = 1
        day = 1
        per_day = 0

        for center, wb in self.all_pairs:
            lines.append(f"## Open {center} Center")
            lines.append("")

            # Emotions section
            if wb.emotions:
                lines.append(f"### What You Feel Here — Emotions")
                for emotion, examples in wb.emotions:
                    lines.append(f"**{emotion}**")
                    for ex in examples:
                        lines.append(f"- {ex}")
                    lines.append("")
                lines.append("")

            # Belief sections
            for section_name, section_beliefs in [("Limiting Beliefs", wb.limiting),
                                                    ("Programmed Beliefs", wb.programmed),
                                                    ("Inherited Beliefs", wb.inherited)]:
                lines.append(f"### {section_name}")
                lines.append("")
                for lim, emp, subs in section_beliefs:
                    lines.append(f"#### Belief {belief_num} — Core")
                    lines.append(f"**Limiting:** \"{lim}\"")
                    lines.append("")
                    lines.append(f"**Empowering:** \"{emp}\"")
                    lines.append("")
                    belief_num += 1
                    per_day += 1
                    if per_day % 5 == 0:
                        day += 1

                    for i, (s_lim, s_emp) in enumerate(subs, 1):
                        lines.append(f"**Subordinate {i}:**")
                        lines.append(f"**Limiting:** \"{s_lim}\"")
                        lines.append(f"**Empowering:** \"{s_emp}\"")
                        lines.append("")
                        belief_num += 1
                        per_day += 1
                        if per_day % 5 == 0:
                            day += 1

                    lines.append("---")
                    lines.append("")

        # Design beliefs
        design_beliefs = [b for b in self.beliefs if b.center == "Design"]
        if design_beliefs:
            lines.append(f"## Your Design — Core Truths")
            lines.append("")
            for b in design_beliefs:
                lines.append(f"#### Belief {belief_num}")
                lines.append(f"**Limiting:** \"{b.limiting}\"")
                lines.append("")
                lines.append(f"**Empowering:** \"{b.empowering}\"")
                lines.append("")
                lines.append("---")
                lines.append("")
                belief_num += 1

        lines.append(f"*Generated by Belief Deprogrammer — {len(self.beliefs)} belief pairs*")
        return "\n".join(lines)
