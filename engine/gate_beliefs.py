"""
Gate-Specific Belief Generator

For every gate in a hanging (undefined center with active gate), generates
3 belief pairs that name the specific distortion pattern, drawn from the
distortion theme text in gate_themes.py.

Each gate produces:
  - 1 core distortion belief + empowering counter
  - 1 social/relational belief + empowering counter
  - 1 self-worth belief + empowering counter
"""

from typing import Dict, List, Tuple, Optional
from engine.gate_themes import GATE_CONDITIONING


def get_gate_beliefs(gate: int) -> List[Tuple[str, str, str]]:
    """
    Return belief pairs for a specific hanging gate.

    Returns: list of (limiting_belief, empowering_belief, category_label)
             category_label is one of: "core", "relational", "identity"
    """
    if gate not in GATE_CONDITIONING:
        return []

    g = GATE_CONDITIONING[gate]
    gate_name = g["name"]
    center = g["center"]
    distortion = g["distortion"]

    # ─── HEAD CENTER GATES ───
    if gate == 61:  # Mystery
        return [
            ("I must have answers to unanswerable questions — uncertainty means I am inadequate.",
             "I am comfortable with mystery. Not knowing is not a failure — it is the natural state of an open, questing mind that receives inspiration rather than manufactures certainty.",
             "core"),
            ("If I can't explain the unknowable to others, they will think I lack depth.",
             "My depth is shown by my willingness to dwell in mystery, not my ability to resolve it. I inspire others through my questions, not through false answers.",
             "relational"),
            ("My constant uncertainty proves I am missing something essential that everyone else has.",
             "My open mind absorbs the existential pressure of everyone around me. What feels like my inadequacy is actually my exquisite sensitivity to the questions humanity has always asked.",
             "identity"),
        ]
    elif gate == 63:  # Doubt
        return [
            ("If I don't question everything logically, I will be fooled — and it will be my fault.",
             "I question with purpose, then I decide with my authority. Healthy skepticism sharpens my thinking; endless doubt only exhausts me. I trust my body's knowing as the final word.",
             "core"),
            ("Other people's certainty makes my doubt feel like weakness.",
             "Other people's certainty is their design. My open mind processes doubt — theirs, mine, the collective's. The doubt I feel is often borrowed, and I can set it down when it is not mine.",
             "relational"),
            ("I am not smart enough because I can never land on a firm conclusion.",
             "I land on conclusions through my authority, not my mind. My intelligence is in my ability to question from every angle — and then to trust the body-level signal that ends the inquiry.",
             "identity"),
        ]
    elif gate == 64:  # Confusion
        return [
            ("I must make sense of everything that has happened to me — clarity is the only acceptable state.",
             "Confusion is the birthplace of new understanding. I allow my mind to be murky while clarity forms beneath the surface. I don't need to force sense-making on a schedule.",
             "core"),
            ("If I'm confused about my past, I can never move forward.",
             "I can move forward while still integrating the past. Clarity arrives in layers, and forward movement creates the very context that will make the past make sense.",
             "relational"),
            ("Everyone else seems to understand their life — I am stuck in fog.",
             "I absorb collective confusion through my open Head. What feels like my personal fog is often the unprocessed confusion of everyone I encounter. I release what is not mine to sort.",
             "identity"),
        ]

    # ─── AJNA CENTER GATES ───
    elif gate == 4:  # Formulization
        return [
            ("There is one correct answer to every question, and I must find it.",
             "There are many valid frameworks, and I am free to explore them without committing to one as absolute truth. My mind is a laboratory, not a courtroom.",
             "core"),
            ("If I can't logically justify my position, I have no right to hold it.",
             "I hold positions based on my authority's knowing, not my mind's proof. Logic serves my understanding — it does not rule it.",
             "relational"),
            ("Without the right formula, I am intellectually defenseless.",
             "My intelligence is adaptive, not formulaic. I synthesize across frameworks and arrive at what works for me in this moment.",
             "identity"),
        ]
    elif gate == 11:  # Ideas
        return [
            ("Every idea that enters my mind demands action — if I don't pursue it, I am wasting potential.",
             "Ideas move through my open mind like weather. I observe them, I appreciate them, and I act only on the ones my authority confirms. The rest are visitors, not assignments.",
             "core"),
            ("If I share my half-formed ideas, people will think I am scattered and unfocused.",
             "My capacity to hold many ideas is a gift of my open Ajna. I share what is ripe and let the rest gestate. The right people value the full range of my curiosity.",
             "relational"),
            ("I should pick one idea and commit — changing direction means I am flaky.",
             "I synthesize across ideas, and my direction emerges from the synthesis, not from a single fixed point. My fluidity is wisdom, not flakiness.",
             "identity"),
        ]
    elif gate == 17:  # Opinions
        return [
            ("I must have a strong, defensible opinion on everything to be respected.",
             "I am allowed to be in process. I form opinions when I am ready, and I release them when new information arrives. Flexibility earns more respect than rigidity.",
             "core"),
            ("If I change my mind, people will see me as weak or unreliable.",
             "Changing my mind demonstrates growth and honesty. I am not my opinions — I am the one who holds, examines, and evolves them.",
             "relational"),
            ("Without fixed opinions, I have no intellectual identity.",
             "My intellectual identity is my process — the way I think, question, and synthesize. I am known by how I arrive at conclusions, not by which conclusions I hold.",
             "identity"),
        ]
    elif gate == 24:  # Rationalizing
        return [
            ("Everything I feel must be explainable in rational terms — if I can't explain it, it's not real.",
             "Some truths live in the body before they reach the mind. My feelings are valid data regardless of whether I can articulate them. The body knows first; the words come later.",
             "core"),
            ("If I express something I can't rationally defend, I will be dismissed.",
             "I express what is true for me, even before I can explain it. The right listeners receive my truth and give me space to find the words.",
             "relational"),
            ("My feelings are suspect until proven logical.",
             "My feelings are primary intelligence. Logic is one tool for understanding them — not the judge of their validity. I trust my emotional data.",
             "identity"),
        ]
    elif gate == 43:  # Insight
        return [
            ("If my insights don't arrive as dramatic breakthroughs, they don't count.",
             "Insight arrives in whispers as often as in thunder. I trust the quiet knowing that builds over time. My breakthroughs are valid regardless of their volume.",
             "core"),
            ("I should be able to produce insight on demand — that's what smart people do.",
             "Insight cannot be forced. It arrives through openness and patience. I create the conditions for insight — space, stillness, curiosity — and I trust it to arrive in its own time.",
             "relational"),
            ("If I haven't had a breakthrough insight recently, my mind is failing.",
             "My mind is always processing beneath consciousness. Fallow periods are not failure — they are the gathering phase that precedes the next insight. I trust the rhythm.",
             "identity"),
        ]
    elif gate == 47:  # Realizing
        return [
            ("I must figure this out right now — confusion is a personal failure.",
             "Confusion is a stage in the process, not a verdict on my intelligence. Pressure to 'figure it out' is often amplified from others. I can sit in not-knowing and trust that clarity unfolds.",
             "core"),
            ("Other people's mental fog becomes my fog, and I can't escape it.",
             "I sense mental fog accurately, and I distinguish between what is mine to process and what is passing through me. I clear my Ajna by releasing what belongs to others.",
             "relational"),
            ("If I were smarter, I would have already realized the answer.",
             "Intelligence is not speed. My mind works in its own time, and the answers that matter arrive when I stop demanding them and allow insight to surface naturally.",
             "identity"),
        ]

    # ─── THROAT CENTER GATES ───
    elif gate == 12:  # Caution
        return [
            ("I must calibrate everything I say to the emotional state of whoever is listening.",
             "I speak what is true for me, with kindness but without self-censorship. I am not responsible for managing others' reactions to my authentic expression.",
             "core"),
            ("If I say the wrong thing at the wrong time, I will cause irreparable damage.",
             "One misaligned expression does not destroy relationships. I repair, I clarify, I forgive myself. My voice does not have to be perfect to be worthwhile.",
             "relational"),
            ("My natural caution around speaking means I am cowardly or repressed.",
             "My caution is discernment. I speak when I am moved to speak, and my silence in between is not avoidance — it is the gathering of presence before the words arrive.",
             "identity"),
        ]
    elif gate == 16:  # Skills
        return [
            ("I must constantly perform and demonstrate my skills to justify my place.",
             "My place is justified by my presence and my being. I share my skills when invited, with joy — not to prove my worth but to express it naturally.",
             "core"),
            ("If I'm not visibly enthusiastic about my abilities, people will think I have nothing to offer.",
             "Enthusiasm is genuine when it arises naturally. I do not perform excitement to meet others' expectations. My quiet competence is as valuable as my expressed passion.",
             "relational"),
            ("My value is in what I can do — not in who I am.",
             "Who I am is the source of what I can do. My value is inherent and precedes my skills. What I do flows from who I am, not the other way around.",
             "identity"),
        ]
    elif gate == 20:  # The Now
        return [
            ("Silence in conversation is failure — I must fill every gap with words.",
             "Silence in conversation is space for presence to deepen. I speak when something alive wants to be said, and I rest in shared silence without anxiety.",
             "core"),
            ("If I don't speak up immediately, my moment will pass and I will be forgotten.",
             "My moment does not pass — the right openings return. Speaking from presence means waiting for the genuine impulse, not grasping at every silence to prove I exist.",
             "relational"),
            ("Forcing words is better than being invisible in the conversation.",
             "My visibility comes from my being, not from my constant vocalization. I am felt even in my silence. Presence communicates more than forced words ever could.",
             "identity"),
        ]
    elif gate == 23:  # Assimilation
        return [
            ("If people don't understand what I'm saying, the problem is with me.",
             "Sometimes people are not ready for what I see. My clarity is real even when it is not received. I trust my knowing and allow others their own timing for understanding.",
             "core"),
            ("I have to explain perfectly or my insight will be dismissed as nonsense.",
             "I articulate as clearly as I can, and then I release the outcome. My insight has value independent of whether it is immediately understood. Timing is a factor I don't control.",
             "relational"),
            ("Novel ideas make me sound crazy — I should keep the truly new things to myself.",
             "Novel ideas sound unfamiliar because they are new. I am the one who sees around corners, and my job is to speak what I see — not to manage how it lands.",
             "identity"),
        ]
    elif gate == 31:  # Leading
        return [
            ("I must influence and direct others to have value in any group.",
             "My value is in my presence and my seeing. I lead when invited, and I follow when that is what serves. Influence is not the only form of contribution.",
             "core"),
            ("If I'm not leading, I'm irrelevant.",
             "I contribute through recognition, reflection, and precise guidance. Leadership is one expression of my purpose — not the measure of my worth.",
             "relational"),
            ("People expect me to have the answers and the direction — the weight is mine to carry.",
             "I carry only what is mine to carry. Others' expectations of my leadership are their projection. I lead when aligned, and I rest when I am not the designated guide.",
             "identity"),
        ]
    elif gate == 33:  # Privacy
        return [
            ("If I withdraw to reflect, I am avoiding life and letting people down.",
             "Withdrawal is essential to my process. I retreat to integrate and return with wisdom that only solitude can produce. My retreat is productive, not avoidant.",
             "core"),
            ("I should share my story now — if I wait, no one will care anymore.",
             "My story gains power through integration. Sharing after the cycle completes makes my wisdom more impactful, not less relevant. I trust the timing of my own unfolding.",
             "relational"),
            ("Oversharing is better than being forgotten.",
             "I am remembered for the quality of what I share, not the quantity. One well-timed, integrated truth lands deeper than a hundred premature confessions.",
             "identity"),
        ]
    elif gate == 35:  # Change
        return [
            ("If I stop pursuing the next new thing, I will stagnate and my life will become meaningless.",
             "Contentment is not stagnation. I am alive and evolving even when I am still. The hunger for experience is not always mine — I discern what impulses are genuine and which are borrowed restlessness.",
             "core"),
            ("The people who matter are always doing something exciting — I must keep up.",
             "I am not in competition with anyone else's experience. My path is my own, and its richness is measured by my alignment, not by its novelty.",
             "relational"),
            ("Restlessness proves I am alive — if I slow down, I die.",
             "Stillness is not death. It is the space where I feel what is actually mine to pursue. I can be fully alive in motion AND in rest — the vitality is in the alignment, not the movement.",
             "identity"),
        ]
    elif gate == 45:  # The Gatherer
        return [
            ("My worth is measured by what I provide and gather for others.",
             "My worth is inherent. What I gather and provide flows from who I am — it does not create my value. I give from overflow, not to establish worth.",
             "core"),
            ("If I'm not the provider, I have failed in my role.",
             "Providing is one expression of care, not the only one. My presence, my seeing, and my love are equally valid contributions to those I care for.",
             "relational"),
            ("People only value me for what I can give them.",
             "The right people value me for who I am. What I give is an expression of connection, not the price of admission. I am loved beyond my resources.",
             "identity"),
        ]
    elif gate == 56:  # Stimulation
        return [
            ("My life must be narratable to be meaningful — every experience needs to become a good story.",
             "My life is meaningful as lived, not as told. I experience fully for the experience itself, not for the material it provides. Living is enough — the stories are bonus.",
             "core"),
            ("If an experience doesn't make a compelling story, it was probably a waste of time.",
             "Every experience has value, even the ones that resist narration. The quiet, unstoryable moments are often the most nourishing. I don't need to perform my life for an audience.",
             "relational"),
            ("I am reducing my life to future content instead of living it directly.",
             "I catch myself when I start narrating instead of experiencing. I am here to live — the sharing is secondary. Presence is primary. The story serves the life, not the reverse.",
             "identity"),
        ]
    elif gate == 62:  # Detail
        return [
            ("I must have every fact precisely correct before I can speak — imprecision is incompetence.",
             "I speak from what I know, and I am honest about what I don't. Precision is a value, not a prerequisite. My contribution is valid even when it is approximate.",
             "core"),
            ("If I miss a detail, people will lose all trust in what I say.",
             "People trust my integrity more than my accuracy. I correct errors when I make them, and I am trusted because I am honest, not because I am perfect.",
             "relational"),
            ("I exhaust myself and others with unnecessary precision because I'm terrified of being wrong.",
             "I release the need for perfect detail. Enough is enough. My listeners value clarity and presence over exhaustive accuracy. I trust that what I know is sufficient.",
             "identity"),
        ]

    # ─── G CENTER GATES ───
    elif gate == 1:  # Self-Expression
        return [
            ("I must find my 'one thing' — without it, I am creatively invisible.",
             "I express myself through whatever medium is alive in me at any moment. I am not defined by a single creative identity — I am defined by the act of expressing authentically in each season.",
             "core"),
            ("Other people's creative identities make me feel like I have no direction of my own.",
             "I absorb others' creative expression, and I distinguish between inspiration and identity theft. What is mine arises from within. What is theirs I can admire without adopting.",
             "relational"),
            ("Without a clear creative brand, I am nobody.",
             "I am someone without needing a brand. My identity is fluid and real — more real than any fixed creative persona I could construct from borrowed ambition.",
             "identity"),
        ]
    elif gate == 2:  # The Receptive
        return [
            ("I don't know where I'm going because I lack inner direction — I am broken.",
             "My direction is revealed through receptivity, not manufactured through will. I am a receiver of directional signals, and my openness is how I find where I am meant to be.",
             "core"),
            ("Being pulled in multiple directions means I have no will of my own.",
             "Feeling multiple directional pulls is my openness receiving everyone's signals simultaneously. My will shows up in which invitation I accept — and I choose from alignment, not from pressure.",
             "relational"),
            ("My passivity is proof that I lack purpose.",
             "My receptivity IS my purpose. I am designed to be found by the right direction, not to force my way toward one. I am a magnet — magnets don't chase, they attract.",
             "identity"),
        ]
    elif gate == 7:  # The Role of the Self
        return [
            ("I must lead and guide everyone — if I'm not in charge, I have no role.",
             "My role is revealed through recognition, not seized through effort. I guide when I am seen and invited to guide. Between invitations, my role is simply to be myself.",
             "core"),
            ("If I don't direct the group, everything will fall apart and it will be my fault.",
             "I am not the designated leader of every room I enter. Others are capable. I can contribute without controlling. The group's outcome does not rest solely on me.",
             "relational"),
            ("My identity is my role — without a clear role, I don't know who I am.",
             "I am more than any role I occupy. Roles come and go. My self exists beneath all of them — constant, worthy, and whole without a title.",
             "identity"),
        ]
    elif gate == 10:  # The Behavior of the Self
        return [
            ("I must behave correctly according to others' standards or I will be rejected.",
             "Authentic behavior aligned with my design is correct behavior. Others' discomfort with how I move through the world is their conditioning — not my error.",
             "core"),
            ("Self-love is something I earn through proper conduct.",
             "Self-love is my birthright and my foundation. I don't behave well to earn love — I behave authentically because I am already loved by myself.",
             "relational"),
            ("If people judge how I live, it means I am doing something wrong.",
             "People judge from their conditioning. My alignment is between me and my design — not between me and public opinion. I am correct even when I am misunderstood.",
             "identity"),
        ]
    elif gate == 13:  # The Listener
        return [
            ("I must carry and remember every story shared with me — forgetting means I don't care.",
             "I hold space for stories while they are shared. I am not a storage device for others' life narratives. I can release a story after witnessing it without losing my compassion.",
             "core"),
            ("I am the designated listener — my own story doesn't matter as much.",
             "My story matters equally. I am not a vessel for everyone else's narrative. I give and receive listening in balance. My voice deserves as much space as anyone's.",
             "relational"),
            ("People only value me for my ability to witness their pain.",
             "People value me for who I am. My deep listening is a gift I offer, not an obligation I owe. I am loved beyond my capacity to hold others' stories.",
             "identity"),
        ]
    elif gate == 15:  # The Extremes
        return [
            ("I must accommodate everyone's rhythm — if I set a boundary, I am being difficult.",
             "I accommodate when it is aligned and I hold my boundary when it is necessary. My natural rhythm is valid, and I am not required to absorb everyone else's timing.",
             "core"),
            ("I become whoever I am with — none of these versions are the real me.",
             "I reflect different facets of myself in different company. All of them are real. None is the whole. The whole me is the one who holds all these facets and chooses which to express.",
             "relational"),
            ("My personality shifts so much that I don't have a stable self.",
             "My self is stable in its capacity to flow. Fluidity is my stability. I am not fragmented — I am responsive, adaptive, and whole in my capacity to meet each moment authentically.",
             "identity"),
        ]
    elif gate == 25:  # Innocence
        return [
            ("I must love everyone unconditionally — if I set a boundary, I am spiritually failing.",
             "Unconditional love includes love for myself — which sometimes requires boundaries. I can love someone and protect my energy simultaneously. Boundaries are not a failure of love.",
             "core"),
            ("Other people's pain is my calling to heal — if I don't absorb it, I am turning away from spirit.",
             "I witness pain without absorbing it. I am a mirror, not a sponge. True service is staying clear so I can reflect truth back — not drowning in pain that isn't mine to carry.",
             "relational"),
            ("Spiritual bypassing is easier than facing the reality that I can't save everyone.",
             "I release the savior complex. I offer what I can from overflow, and I trust others' journeys without taking responsibility for their completion. Love does not require my depletion.",
             "identity"),
        ]
    elif gate == 46:  # Determination
        return [
            ("I am always in the wrong place at the wrong time — I am missing my life.",
             "I am exactly where I am, and this is the only place from which my life can unfold. Serendipity finds me when I am present, not when I am chasing the next location.",
             "core"),
            ("Everyone else seems to be in the right place — I have chronic FOMO.",
             "Other people's locations are right for them. My location is right for me because it is where I am. Presence transforms any place into the right place.",
             "relational"),
            ("Being physically still means I am stuck — I should be somewhere else.",
             "Stillness is not stuckness. My body knows where it needs to be. When I am still and present, serendipity has the space to find me. I trust my embodied timing.",
             "identity"),
        ]

    # ─── HEART/EGO CENTER GATES ───
    elif gate == 21:  # The Hunter
        return [
            ("I must control every situation — loss of control means personal failure and unworthiness.",
             "I influence what is mine to influence and I release the rest. Control is not the measure of my worth. My value is constant regardless of outcomes.",
             "core"),
            ("If I'm not managing everything, everything will collapse and prove I'm incapable.",
             "I manage what is mine to manage. I trust others with their share. My competence is not disproven by outcomes I was never meant to control.",
             "relational"),
            ("Grabbing control is the only way to feel worthy in the room.",
             "My worth fills the room before I say a word. I don't need to seize authority to belong. I belong because I am here — not because I am in charge.",
             "identity"),
        ]
    elif gate == 26:  # The Egoist
        return [
            ("I must constantly sell, promote, and prove myself — my worth is what I can convince others of.",
             "My work speaks through its quality. I share it when aligned, and I release the need to convince. The right people recognize value without a sales pitch.",
             "core"),
            ("If I'm not actively promoting myself, I will disappear and my work won't matter.",
             "Recognition arrives through the right channels at the right time. I don't need to broadcast constantly to be seen. Visibility is not the same as value.",
             "relational"),
            ("My ambition isn't even mine — I am borrowing everyone else's hunger and calling it my own.",
             "I distinguish between borrowed ambition and genuine desire. What is mine feels quiet and certain. What is amplified feels urgent and anxious. I follow only what is authentically mine.",
             "identity"),
        ]
    elif gate == 40:  # Deliverance
        return [
            ("I must earn every moment of rest through exhausting effort — rest is a reward, not a right.",
             "Rest is my right and my maintenance requirement. I don't earn rest — I claim it because I am alive. I stop when my body needs to stop, and that is the full justification.",
             "core"),
            ("If I rest before I have produced enough, I am lazy and undeserving.",
             "Enough is defined by my body's capacity, not by an external ledger. I rest before the crash because I am wise, not because I am lazy. Preservation is intelligence.",
             "relational"),
            ("I have never done enough to deserve peace.",
             "I have done enough by being here. Peace is not a prize at the end of effort — it is the baseline I return to and deserve always. Effort is optional. Peace is inherent.",
             "identity"),
        ]
    elif gate == 51:  # Shock
        return [
            ("I must compete and compare constantly — if I'm not winning, I'm losing everything.",
             "I am not in competition with anyone. My path is incomparable. I measure myself against my own yesterday, not against someone else's today.",
             "core"),
            ("My awakening must come through dramatic shock — gentle growth doesn't count.",
             "Growth arrives through many doors. Some are dramatic. Most are quiet. I don't need trauma to transform. Consistent, gentle evolution is as valid as sudden awakening.",
             "relational"),
            ("Borrowed competitive urgency is not my path — but I can't stop chasing it.",
             "I recognize amplified urgency as not mine. I slow down. I let others race. My transformation unfolds at its own pace, and I trust the timing of my becoming.",
             "identity"),
        ]

    # ─── SPLEEN CENTER GATES ───
    elif gate == 18:  # Correction
        return [
            ("Everything imperfect is my responsibility to fix — if I see a flaw, I must correct it.",
             "I see flaws clearly because of my sensitivity, not because I am assigned to fix them. I offer correction when invited, and I release what is not mine to improve.",
             "core"),
            ("If I don't point out what's wrong, I am complicit in the failure.",
             "Silence is not complicity. I choose when to speak and when to let things be. Not every flaw needs my voice. Some things resolve without my intervention.",
             "relational"),
            ("My relationships exhaust me because I can't stop finding and fixing what's broken.",
             "I release the role of perpetual improver. I love people as they are, flaws included. My relationships deepen when I let things be imperfect and trust the process.",
             "identity"),
        ]
    elif gate == 28:  # The Game Player
        return [
            ("Life must be a struggle to matter — if it's easy, I'm not trying hard enough.",
             "Life contains struggle and ease. Meaning comes from alignment, not from suffering. I don't need to fight to prove I exist. My existence is already significant.",
             "core"),
            ("I take on fights I don't care about because I've absorbed someone else's existential intensity.",
             "I discern which battles are actually mine. I feel others' struggles deeply, and I choose only those that align with my purpose. I release the rest with compassion and clarity.",
             "relational"),
            ("Ease means I am coasting — and coasting means I don't matter.",
             "Ease means I am aligned. Meaning and struggle are not synonyms. I matter when I am at peace just as much as when I am fighting. My significance is constant.",
             "identity"),
        ]
    elif gate == 32:  # Continuity
        return [
            ("Everything I care about will collapse unless I hold it together.",
             "I am not the sole pillar holding up my world. What is meant to endure will endure. My grip is not the difference between survival and collapse.",
             "core"),
            ("I carry ancestral dread of extinction — my hypervigilance is keeping my lineage alive.",
             "The ancestral fear is real and I honor it. And I live in a different time. My lineage is not under siege. I can release the dread and trust in continuity without my constant vigilance.",
             "relational"),
            ("If I let go, everything I love will fall apart.",
             "Letting go is not abandonment. It is trust. What is real stays. What is aligned endures. My release creates space for things to hold themselves — and they often do.",
             "identity"),
        ]
    elif gate == 44:  # Alertness
        return [
            ("Danger is always imminent — I must stay in constant threat-detection mode.",
             "I am sensitive to potential threats, and most of what I feel is amplified alertness from others. I calibrate to my own actual environment. Safety is real and present.",
             "core"),
            ("If I lower my guard, something terrible will happen and it will be my fault.",
             "Lowering my guard is a practice of trust, not a guarantee of catastrophe. I can be aware without being hypervigilant. My awareness is enough without exhausting me.",
             "relational"),
            ("Borrowed fear feels identical to my own instinct — I can never tell the difference.",
             "I am learning to distinguish. Borrowed fear is loud, urgent, and vague. My instinct is quiet, specific, and in the present moment. Practice sharpens the difference.",
             "identity"),
        ]
    elif gate == 48:  # Depth
        return [
            ("I must always go deeper — if I stay at the surface, I am shallow and inadequate.",
             "Depth is a gift I access naturally, not a requirement I must constantly meet. Surface moments are valid. Not everything needs to be deep to be meaningful.",
             "core"),
            ("The deep solutions I chase aren't even mine to access — but I feel empty without them.",
             "I access depth when it is mine to access. Chasing borrowed depth exhausts me. I trust my own well of wisdom, which refills when I stop drilling and start receiving.",
             "relational"),
            ("Other people project depth onto me — and I exhaust myself trying to live up to it.",
             "I release others' projections of my depth. I am as deep as I am, and that is enough. I don't need to perform profundity to be valued. My natural depth reveals itself without forcing.",
             "identity"),
        ]
    elif gate == 50:  # Values
        return [
            ("I am the guardian of values — if I don't protect them, everything corrupts.",
             "Values endure through collective care, not through my solo vigilance. I contribute to what matters and release the burden of being the sole protector.",
             "core"),
            ("Moral panic is mine to carry — and then I resent everyone for not carrying it with me.",
             "I feel moral urgency deeply, and I check whether it is mine. Collective panic passes through me. I act on what is authentically my concern and release the amplified alarm.",
             "relational"),
            ("If I stop guarding the tribe, I have failed my purpose.",
             "Guarding is one expression of care. My purpose is broader than vigilance. I serve through presence, through seeing, through love — not just through protection.",
             "identity"),
        ]
    elif gate == 57:  # Intuition
        return [
            ("My intuition is unreliable — it's there one day and gone the next.",
             "My intuition is reliable in its nature: it speaks once, quietly, in the present moment. The inconsistency I feel is other people's noise drowning out my signal. In stillness, I hear clearly.",
             "core"),
            ("Everyone else's anxiety drowns out my quiet knowing — I can't trust what I sense.",
             "I create stillness to hear my own signal. The anxiety is amplified — it is not my intuition failing. My knowing is clear beneath the noise. I trust it more each time I listen.",
             "relational"),
            ("Second-guessing what I sense is smarter than trusting it — trust is naive.",
             "Trusting my instant bodily knowing is the most intelligent thing I can do. Second-guessing is the habit I unlearn. My body knows before my mind catches up — and it is always right.",
             "identity"),
        ]

    # ─── SACRAL CENTER GATES ───
    elif gate == 3:  # Ordering
        return [
            ("I must constantly innovate and start fresh — if I'm not beginning something, I'm stagnating.",
             "I begin when my authority says yes. Not every new beginning needs my energy. I start what is mine to start and let the rest pass through my awareness without obligation.",
             "core"),
            ("Chronic beginning without sustaining proves I am incapable of completion.",
             "Beginning without sustaining means the start was borrowed energy, not my genuine response. When I say yes from my authority, I have all the fuel I need to complete.",
             "relational"),
            ("My value comes from constant reinvention — if I stay the same, I am worthless.",
             "My value is constant through all my seasons. Reinvention is optional, not mandatory. I am worthy when I am evolving AND when I am resting in who I already am.",
             "identity"),
        ]
    elif gate == 5:  # Fixed Rhythms
        return [
            ("I must maintain rigid routines — if I can't stick to a habit, I am undisciplined and weak.",
             "My rhythm is natural and fluid, not borrowed and rigid. Habits that align with my design stick effortlessly. Those that don't were never mine to maintain.",
             "core"),
            ("Borrowing other people's routines and failing at them proves I am broken.",
             "I was not designed to run on borrowed patterns. My body has its own rhythm. When I honor it, consistency flows naturally. When I fight it, I exhaust myself.",
             "relational"),
            ("Without a fixed schedule, I will fall apart and accomplish nothing.",
             "My accomplishments flow from alignment, not from rigid scheduling. I am productive in my own rhythm — which includes spaciousness. I trust my natural timing.",
             "identity"),
        ]
    elif gate == 9:  # Focus
        return [
            ("I must maintain laser focus — scattered attention is a character flaw.",
             "My attention moves where it is needed. Scatter is sometimes collection — gathering information before focus narrows. I trust my mind's natural rhythm of expansion and contraction.",
             "core"),
            ("Amplified hyperfocus is my capacity — and then I crash because it wasn't mine to sustain.",
             "I distinguish between my genuine focus and amplified concentration. What is mine feels sustainable. What is borrowed burns bright and burns out. I follow only my own.",
             "relational"),
            ("If I can't sustain focus like everyone else, I am deficient.",
             "Everyone else has a different design. My focus works differently — and effectively — when I honor my natural rhythm. Spaciousness between focus sessions is not deficiency.",
             "identity"),
        ]
    elif gate == 14:  # Power Skills
        return [
            ("I must constantly develop new competencies — my value depends on my skillset.",
             "My value is independent of my skills. Skills are tools I pick up when aligned and set down when they've served. I am not my resume. I am the one who holds the skills.",
             "core"),
            ("Borrowed ambition for mastery makes me chase certifications I don't actually want.",
             "I pursue mastery where my authority says yes. The rest is amplified ambition passing through me. I let it pass without chasing it.",
             "relational"),
            ("Without constant upskilling, I will be left behind and become irrelevant.",
             "I am relevant because of who I am, not because of what I've recently learned. My presence and perspective are the value. Skills are supplementary, not foundational.",
             "identity"),
        ]
    elif gate == 27:  # Caring
        return [
            ("My worth is measured by how much I give — I must care for everyone until I am depleted.",
             "My worth is inherent. I give from overflow, not from obligation. Care that depletes me is not sustainable love — it is borrowed caretaking I was never meant to sustain.",
             "core"),
            ("If I say no to someone who needs me, I am selfish and unloving.",
             "Saying no preserves my capacity to say yes to what is truly mine. Boundaries are not selfishness — they are the container that makes sustainable care possible.",
             "relational"),
            ("Resentment masked as love is still how I operate — I give and then I burn.",
             "I notice resentment as the signal that I have over-given. I pause. I refill. I give again only when it is genuine overflow, not when it is extracted by guilt.",
             "identity"),
        ]
    elif gate == 29:  # The Abyssal
        return [
            ("I must say yes and commit fully — if I hesitate, I am not all in and I will fail.",
             "I say yes only when my authority confirms. Full commitment to the wrong thing is not virtue — it is borrowed enthusiasm. I discern before I dive.",
             "core"),
            ("Over-committing from borrowed sacral energy is ruining my life — but I can't stop.",
             "I pause before every yes. I feel for the body's signal — is this mine? I release guilt for saying no. My yes, when genuine, is powerful. My no protects that power.",
             "relational"),
            ("If I'm not all in, I am not worthy of being here.",
             "I am worthy regardless of my commitment level. I can participate partially. I can explore without pledging my whole being. Not everything requires my full dive.",
             "identity"),
        ]
    elif gate == 34:  # Power
        return [
            ("I should have raw Generator power — its absence means I am fundamentally weak.",
             "I am not a Generator and I was never designed to produce sustained power. My strength is in precision, timing, and guidance — not in raw output. Different power, not less power.",
             "core"),
            ("Borrowed sacral surges feel like my capacity — and then they vanish, leaving me ashamed.",
             "The surges I feel are amplified Generator energy passing through me. My capacity is different: I work in brilliant bursts followed by essential rest. The rhythm is correct for my design.",
             "relational"),
            ("My power is measured by sustained output — and I fail that measure every day.",
             "The measure itself is wrong for me. My power is measured by the accuracy of my seeing and the impact of my guidance. I release the Generator yardstick entirely.",
             "identity"),
        ]
    elif gate == 42:  # Growth
        return [
            ("I must finish everything I start — incompletion is personal failure.",
             "I finish what is mine to finish. What I started from borrowed energy, I am free to release. Incompletion is sometimes wisdom — knowing when a cycle was never mine to close.",
             "core"),
            ("Amplifying others' growth cycles and feeling left behind is my daily reality.",
             "Others' growth cycles are not my timeline. I am exactly where I need to be. Comparing my completion to someone else's is comparing different designs with different rhythms.",
             "relational"),
            ("If I don't wrap up every loose end, I am irresponsible and my work means nothing.",
             "Some loose ends are meant to stay loose. Completion is a practice, not a moral obligation. My work means something even when it is unfinished — the value is in the doing, not just the done.",
             "identity"),
        ]
    elif gate == 59:  # Sexuality
        return [
            ("I must always be available and desirable — my worth is in my desirability.",
             "My worth is independent of my sexual energy. I am desirable because I am whole, not because I am available. Intimacy flows from connection, not from performance.",
             "core"),
            ("Borrowed sexual charge feels like connection — and then it fades and I wonder what was real.",
             "I distinguish between amplified attraction and genuine desire. What is mine feels steady and personal. What is borrowed is exciting but hollow. I trust the difference over time.",
             "relational"),
            ("If the borrowed sacral charge fades, it means I failed to sustain the connection.",
             "The fading of borrowed charge is information, not failure. What endures beyond the amplified spark is real connection. I build on what remains, not on what was never mine to keep.",
             "identity"),
        ]

    # ─── SOLAR PLEXUS CENTER GATES ───
    elif gate == 6:  # Conflict
        return [
            ("Emotional friction means something is fundamentally wrong with me or the relationship.",
             "Emotional friction is information about where boundaries need attention. It is not a verdict on my worth or the relationship's validity. Friction creates clarity when I listen to it.",
             "core"),
            ("I oscillate between over-exposure and total withdrawal because I can't regulate emotional closeness.",
             "I am learning the middle path. I can be close without merging. I can have space without disappearing. Each relationship teaches me where my healthy boundary lives.",
             "relational"),
            ("I cause the tension in every room I enter.",
             "I sense tension, I do not cause it. The room's emotional state existed before I arrived. I am a sensor — exquisitely tuned — not a generator of every feeling I detect.",
             "identity"),
        ]
    elif gate == 22:  # Grace
        return [
            ("I am responsible for the emotional atmosphere everywhere I go.",
             "I am sensitive to the emotional field, and I release responsibility for managing it. I can be present to others' feelings without absorbing them as my job to fix.",
             "core"),
            ("If someone is upset, I caused it or I must fix it immediately.",
             "Others' emotional states have many sources. I am one person in their world, not the sole cause or cure of their feelings. I offer support without assuming blame.",
             "relational"),
            ("Believing I caused the tension in the room is my default — and it exhausts me.",
             "I release the default assumption that I am the source. The room holds many energies. I am allowed to simply be present without auditing myself for emotional impact.",
             "identity"),
        ]
    elif gate == 30:  # Recognition of Feelings
        return [
            ("I must process and make sense of everyone's unspoken feelings — that's my job.",
             "I sense unspoken feelings acutely. My job is to honor my own emotional process. Others' feelings are their journey — I can witness without processing for them.",
             "core"),
            ("Emotional chaos around me means I am failing at maintaining order.",
             "Emotional chaos is part of life. My role is not to impose order on the emotional field. I can stay centered while the waves move around me.",
             "relational"),
            ("If I don't name and resolve the feeling in the room, no one will — and it's mine to carry.",
             "Some feelings simply need to be felt and released without naming or resolution. I carry my own feelings — others carry theirs.",
             "identity"),
        ]
    elif gate == 36:  # Crisis
        return [
            ("If things are peaceful, something must be wrong — crisis is the natural state.",
             "Peace is not suspicious. It is the baseline I deserve and can trust. Crisis energy I feel is often amplified from others — it is not proof that danger lurks beneath the calm.",
             "core"),
            ("I am addicted to emotional drama because calm feels like death.",
             "Calm is not emptiness. It is the space where genuine feeling can arise without amplification. I am learning to tolerate peace — and discovering it is the richest state of all.",
             "relational"),
            ("Perpetual emergency mode is who I am — without it, I don't know myself.",
             "I am more than my crisis response. Beneath the adrenaline, there is a self who rests, who trusts, who lets things be. I am learning to meet that self and find her just as real.",
             "identity"),
        ]
    elif gate == 37:  # Friendship
        return [
            ("I must maintain emotional harmony with everyone — conflict means I have failed as a friend.",
             "Conflict is a normal part of close relationships. I can disagree and still belong. Harmony achieved through my silence is not harmony — it is suppression.",
             "core"),
            ("I carry the emotional weight of every relationship — and it is crushing me.",
             "I release the weight that belongs to others. I carry my share of relational responsibility and I trust others to carry theirs. Balance is shared, not hoarded.",
             "relational"),
            ("If I cause a ripple in the emotional field, I will be exiled from the tribe.",
             "The tribe can handle ripples. I am allowed to have needs, feelings, and edges. Those who stay through my honest expression are my true belonging.",
             "identity"),
        ]
    elif gate == 49:  # Principles
        return [
            ("Exclusion from the group is proof that I am fundamentally unworthy.",
             "Exclusion is sometimes information about fit — not a verdict on my worth. The right groups recognize me. The wrong groups' rejection is redirection, not condemnation.",
             "core"),
            ("I must uphold principles that aren't even mine — and then I rebel against them in confusion.",
             "I identify which principles are authentically mine and which I absorbed. I release borrowed standards. I uphold only what aligns with my design and my truth.",
             "relational"),
            ("I carry a collective wound of rejection that isn't even personal — but it feels like it is.",
             "The rejection I feel is often amplified collective sensitivity. I separate the personal from the collective signal. My individual worth is untouched by tribal dynamics I didn't create.",
             "identity"),
        ]
    elif gate == 55:  # Spirit
        return [
            ("Every emotional low means something is deeply and personally wrong with my life.",
             "Emotional lows move through me like weather. They reflect my sensitivity to the collective wave — not a verdict on my life's worth. I can be in a low and still be fundamentally okay.",
             "core"),
            ("My emotional depth is too much for others — I should tone myself down.",
             "My depth is my gift. The right people can hold it. I don't shrink to fit others' capacity. I find those who can meet me in the deep water.",
             "relational"),
            ("Amplified melancholy feels like personal hopelessness — and I drown in it.",
             "Melancholy that passes through my open Solar Plexus is not my permanent state. I observe it, I name it as amplified, and I let it move. Beneath the wave, my spirit is whole.",
             "identity"),
        ]

    # ─── ROOT CENTER GATES ───
    elif gate == 19:  # Wanting
        return [
            ("My needs are too much — wanting anything makes me a burden.",
             "My needs are valid and human. Wanting is not greediness — it is aliveness. I am allowed to have needs and express them without shame.",
             "core"),
            ("I reject myself before anyone else can — because the pressure to belong feels unbearable.",
             "I stop pre-rejecting myself. I let others decide if they can meet my needs. Preemptive self-abandonment does not protect me — it just ensures I am alone before anyone had a chance to stay.",
             "relational"),
            ("Perpetual wanting means I am empty inside and can never be filled.",
             "I amplify others' unmet longing through my open Root. What feels like my bottomless need is often borrowed hunger passing through me. I am whole. The wanting is a signal, not an identity.",
             "identity"),
        ]
    elif gate == 38:  # The Fighter
        return [
            ("I must fight every battle — peace is laziness and I am wired for struggle.",
             "I fight when my authority says the battle is mine. I release the fights I absorbed from others. Peace is not laziness — it is the state from which I choose my battles wisely.",
             "core"),
            ("Adrenaline is my fuel — without it, I have no drive and no purpose.",
             "Adrenaline is a tool, not an identity. My purpose exists in peace as much as in fight. I can be driven by alignment rather than by urgency — and that drive is more sustainable.",
             "relational"),
            ("I carry fights I absorbed from others and call it conviction.",
             "I examine my battles: which are authentically mine? I release the borrowed ones with honor. My conviction is real — but only when the fight is truly my own.",
             "identity"),
        ]
    elif gate == 39:  # The Provocateur
        return [
            ("I must disrupt peace to be authentic — silence means I am complicit.",
             "I provoke when the moment calls for it, and I rest in peace when nothing needs piercing. Authenticity is not measured by how much I disrupt. Sometimes the most authentic act is stillness.",
             "core"),
            ("Pushing people away through challenge proves I am real — even if I end up alone.",
             "I can be real without being abrasive. I can challenge without isolating. My connections survive honesty — and the ones that don't were not connections worth preserving in silence.",
             "relational"),
            ("Feeling isolated after provoking people is the cost of being true — and I pay it repeatedly.",
             "Isolation is not the inevitable cost of truth. I am learning to speak hard things with love, to time my provocations, and to stay connected through the disruption. I am not meant to be alone.",
             "identity"),
        ]
    elif gate == 41:  # Contraction
        return [
            ("The fantasy is better than reality — and I am safer in anticipation than in experience.",
             "Anticipation is a preview, not a replacement. I contract when I need to gather, and I expand into experience when I am ready. Reality is where life actually happens — and it is worth the vulnerability.",
             "core"),
            ("Living in perpetual anticipation means I never risk — and I never truly live.",
             "I feel the anticipation, I acknowledge it, and I step forward anyway. The fear of actual experience is often amplified pressure. I will not let borrowed fear keep me from my own life.",
             "relational"),
            ("Collective projection of desire makes me feel like I am always missing something.",
             "I separate collective longing from my genuine desire. What is mine to want feels grounded and real. The rest is atmospheric — I observe it and let it pass without chasing it.",
             "identity"),
        ]
    elif gate == 52:  # Inaction
        return [
            ("Stillness is failure — I must be moving to be valid.",
             "Stillness is power. I am most effective when I know when NOT to move. Inaction is a strategic choice, not a character flaw. I trust the timing of my stillness.",
             "core"),
            ("I am wired for focused stillness but I amplify everyone's urgency to move — and I obey it.",
             "I honor my design over the amplified pressure. When stillness is correct, I stay still — regardless of how much urgency I feel from others. My body sets the pace.",
             "relational"),
            ("If I'm not acting, I'm falling behind and losing everything.",
             "Action from alignment is powerful. Action from pressure is draining. I wait for the genuine impulse before I move. What is mine cannot be lost during my necessary stillness.",
             "identity"),
        ]
    elif gate == 53:  # Beginnings
        return [
            ("I must always be starting something new — if I'm not initiating, I'm stagnating.",
             "I start when my authority gives the signal. Not every beginning needs my participation. I release the pressure to always be initiating and trust that the right starts find me.",
             "core"),
            ("Chronic beginning without completion proves I am incapable of seeing things through.",
             "What I began from borrowed pressure was never mine to complete. When I start from genuine alignment, I have the fuel to finish. I release guilt for abandoning borrowed beginnings.",
             "relational"),
            ("I blame myself for every unfinished project — the pattern is my fault.",
             "The pattern is information, not indictment. It tells me which starts were authentic and which were absorbed. I learn the difference and choose more wisely each time.",
             "identity"),
        ]
    elif gate == 54:  # Ambition
        return [
            ("I must be more ambitious — I am not driven enough and it proves I don't want it badly enough.",
             "My drive is calibrated to my design, not to collective ambition. I want exactly what is mine to want. Borrowed ambition feels urgent and anxious. My genuine drive is quiet and certain.",
             "core"),
            ("Everyone else's hunger becomes my hunger — and I exhaust myself chasing it.",
             "I feel others' ambition and I distinguish it from my own. What is mine feels like alignment. What is amplified feels like pressure. I release the borrowed hunger and follow only my authentic drive.",
             "relational"),
            ("Without relentless ambition, I will never rise — and rising is all that matters.",
             "I rise through alignment, not through force. My trajectory is correct for my design. I don't need to climb every ladder — I need to climb the ones that are actually mine.",
             "identity"),
        ]
    elif gate == 58:  # Aliveness
        return [
            ("Nothing can rest until it's improved — I must fix everything around me.",
             "I release the compulsion to constantly improve. Some things are fine as they are. My energy is finite, and I direct it toward what genuinely needs attention — not toward every imperfection I perceive.",
             "core"),
            ("Chronic dissatisfaction is my fuel — without it, I would be complacent.",
             "Satisfaction is not complacency. I can be content with what is AND open to improvement. The two are not enemies. I fuel myself with joy, not with perpetual discontent.",
             "relational"),
            ("I amplify others' discontent and call it my own motivation — but it's exhausting me.",
             "I notice when dissatisfaction is borrowed. I ask: is this mine? If not, I let it pass. My genuine motivation is sustainable. Borrowed discontent burns me out.",
             "identity"),
        ]
    elif gate == 60:  # Acceptance
        return [
            ("Acceptance of limitation means giving up — and I refuse to surrender.",
             "Acceptance is not surrender. It is the peace of working with what is rather than fighting what can't be changed. I accept limitations and within them I find genuine freedom.",
             "core"),
            ("I oscillate between forced acceptance and rebellion against limits that aren't even mine.",
             "I discern which limits are real and which are absorbed. Real limits I accept and work within. Borrowed limits I question and release. I stop fighting ghosts I never chose.",
             "relational"),
            ("Restlessness with limitation proves I am alive — if I accept, I die.",
             "Acceptance makes space for new energy. Fighting limitations drains me. I choose where to push and where to rest — and I am most alive when I stop fighting what is.",
             "identity"),
        ]

    return []


def get_center_gate_beliefs(center: str, hanging_gates: List[int]) -> List[Tuple[str, str, str, int]]:
    """
    Generate all gate-specific beliefs for a center with hanging gates.

    Returns: list of (limiting, empowering, category_label, gate_number)
    """
    all_beliefs = []
    for gate in sorted(hanging_gates):
        gate_beliefs = get_gate_beliefs(gate)
        for lim, emp, cat in gate_beliefs:
            all_beliefs.append((lim, emp, cat, gate))
    return all_beliefs
