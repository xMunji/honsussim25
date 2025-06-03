import time
import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def type_print(text, delay=0.03):
    """Prints text with a typing effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# --- Scene 1: The Community Meeting ---
scene1_art_and_dialogue = """
==================================================================================
                  SIMULATING SUSTAINABLE PRACTICE - DEMO v2
==================================================================================

SCENE: Community Meeting - "The New Park Plaza Project" - A Full House

  +------------------------------------------------------------------------------+
  |                                MEETING ROOM                                  |
  |                                                                              |
  |  Dr. Andreas (Facil.)  Rev. Jackson (Obs.)     Mr. Develo (Developer) O      |
  |        O                     O                                     /|\     |
  |       /|\                   /|\                                    / \     |
  |       / \                   / \                                            |
  |                                                                              |
  |  Present: Pablo Diaz Albertt, Emma Tiller, Fred Ross, Viola B. Muse,         |
  |           Martina Curl, Ella Baker, Louise Stokes, Sylvia Woods,             |
  |           Oscar Heline, Akinabh Burbank, & Other Community Members           |
  |                                                                              |
  |                         -------------------------                            |
  |                        |    LARGE MEETING TABLE    |                           |
  |                         -------------------------                            |
  +------------------------------------------------------------------------------+
"""

dialogue_sequence_scene1 = [
    ("Dr. Andreas", "Welcome, everyone. The purpose of today's meeting is to facilitate a robust and open discussion on the proposed Park Plaza project."),
    ("Rev. Jackson", "Indeed. We encourage all present to express their truths, concerns, and perspectives authentically."),
    ("Mr. Develo", "Thank you. (Clears throat) Our vision for the Park Plaza is a vibrant, modern hub that will revitalize this area and bring benefits to all! (Gestures to a projected plan - not shown in ASCII)"),
    ("Pablo Diaz Albertt", "Benefit *whom*, specifically, Mr. Develo? Your 'vibrant hub' has the distinct aroma of displacement for the long-term residents and established communities!"),
    ("Emma Tiller", "And frankly, the environmental and socio-economic impact studies you've provided are insultingly vague. They gloss over the potential fallout for those whose roots are deepest here."),
    ("Martina Curl", "Ah, the perennial siren song of 'revitalization'! A most grandiloquent overture, yet I must inquire: beneath this gleaming veneer of progress, do we not discern the subtle, sorrowful cadence of livelihoods uprooted, of cultural narratives paved over by ambition's relentless, inexorable march?"),
    ("Ella Baker", "Collaboration, Mr. Develo, demands more than tokenistic consultation! It necessitates a genuine symphony of engagement, a polyphony where every instrument, every voice, from the most prominent to the most muted, contributes to a harmonious, equitable, and ultimately sustainable composition! Are Black and Indigenous voices truly amplified in this process?"),
    ("Viola B. Muse", "(Speaking softly but clearly) ...I see families, elders, small businesses. Their stability, their sense of belonging... that is my primary concern. This plan, as presented, it unsettles that foundation."),
    ("Louise Stokes", "My little bakery has been on Elm Street for thirty years. 'Vibrant hub' often translates to rent hikes we can't absorb. What about the existing fabric of this community, Mr. Develo? Where do *we* fit in your grand design?"),
    ("Oscar Heline", "(Enthusiastically) Now, come on, folks! A shiny new plaza! Sounds exciting to me! More foot traffic, more fun for everyone, right? I'm sure they've thought it all through. They wouldn't steer us wrong!"),
    ("Akinabh Burbank", "Yeah! I'm with Oscar! New things are good! Gotta keep up with the times! Some folks always find something to complain about, but I'm personally ready for a bit of an upgrade around here!"),
    ("Dr. Andreas", "(Nodding slowly) We have a wide range of perspectives here, which is valuable. All these inputs are being noted... and, in fact, fed into our demonstration tool.")
]

# --- Scene 2: The Simulation ---
scene2_header = """
==================================================================================
                  SIMULATING SUSTAINABLE PRACTICE - DEMO v2
==================================================================================

SCENE: Simulation Analysis - Complex Inputs

  +------------------------------------------------------------------------------+
  |                             SIMULATION OUTPUT                                |
  |                                                                              |
"""
simulation_processing_lines = [
    ("SIM", "Analyzing diverse, multi-modal inputs: Formal proposal, passionate testimonies, pragmatic concerns, grandiloquent expressions, and statements of contentment..."),
    ("SIM", "         [▓▓▓▓░░░░░░░░░░░░░░░░] Processing Varied Language Models..."),
    ("SIM", "         [▓▓▓▓▓▓▓▓░░░░░░░░░░░░] Assessing Complex Argumentative Nature..."),
    ("SIM", "         [▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░] Translating Nuanced Sentiments & Differing Viewpoints..."),
    ("SIM", "         [▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░] Aggregating Disparate Viewpoints & Concerns..."),
    ("SIM", "         [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░] Identifying Sentiment Polarity, Intensity & Cultural Inclusiveness Gaps..."),
    ("SIM", "         [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░] Evaluating Potential Conflict Zones & Systemic Injustice Markers..."),
    ("SIM", "         [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓] Cross-referencing Historical Precedents for Similar Developments...")
]

scene2_results_and_dialogue = """
  |                                                                              |
  |   SIM (Prediction & Analysis):                                               |
  |   ---------------------------                                                |
  |   * Predicted 'Argumentative Nature' Score: VERY HIGH (9.1/10)               |
  |     - High emotional load, strong intellectual disagreement, & divergent values detected. |
  |   * Key Concern Clusters (Equal Starts, Differing Viewpoints):               |
  |     - Displacement & Gentrification (Albertt, Tiller, Muse, Stokes)          |
  |     - Cultural/Historical Erasure & Lack of Indigenous/Black Voice (Curl, Baker) |
  |     - Economic Impact on Small, Local Businesses (Stokes, Muse)              |
  |     - Lack of Genuine, Multi-Modal Community Involvement (Baker, Albertt)    |
  |   * Contrasting Sentiments Noted:                                            |
  |     - Superficial Enthusiasm/Uncritical Acceptance (Heline, Burbank) - low depth, |
  |       potentially overlooking systemic risks due to lack of direct negative impact. |
  |   * 'Community Appreciation' (Lottery Outcome - Current Plan): VERY LOW (15%)|
  |     - Weighted by depth of concern and potential for negative, non-visual outcomes. |
  |   * 'Distrust' Metric (Exclusion of Deep/Marginalized Concerns): CRITICAL (95%)|
  |     - Indicates that crucial viewpoints feel unheard or undervalued.          |
  |   * Systemic Injustice Risk (Simulating possibilities): HIGHLY PROBABLE      |
  |     - Based on predicted outcomes if current plan proceeds without addressing|
  |       core concerns from multiple, deeply invested community segments.       |
  |                                                                              |
  |   SIM (Recommendation for Regulated Solutions): "Current trajectory suggests |
  |                         severe community fragmentation and probable systemic |
  |                         injustice. Recommend immediate, structured, multi-modal|
  |                         dialogue focusing on mitigating displacement, preserving |
  |                         local culture, & ensuring economic safeguards for    |
  |                         existing entities. The 'content' voices (Heline,     |
  |                         Burbank) may not grasp the depth of potential negative |
  |                         impacts on others; their perspective, while valid for  |
  |                         them, should not overshadow evidence of potential harm."|
  +------------------------------------------------------------------------------+
"""

dialogue_sequence_scene2_reaction = [
    ("Dr. Andreas", "The simulation's analysis of this... rich and, at times, strained discussion is quite sobering."),
    ("Rev. Jackson", "It certainly underscores the chasm that can exist between stated intent and perceived, potential impact. The importance of ensuring all voices, especially Black and Indigenous voices, are not just heard but *heeded* is paramount."),
    ("Pablo Diaz Albertt", "(Scoffs) See! Even the machine gets it! 'Highly probable systemic injustice'! Maybe now they'll listen!"),
    ("Emma Tiller", "The distinction between 'superficial enthusiasm' and 'deep concerns' is crucial. It highlights how easily dissenting, critical voices can be dismissed if one isn't looking for nonvisual outcomes."),
    ("Oscar Heline", "(Looking a bit deflated) Oh. Uh. I... I genuinely just thought a new park would be nice for everyone... I didn't think about all that other stuff..."),
    ("Akinabh Burbank", "Yeah, guess it's a lot more complicated than just wanting 'new stuff' then, huh? Maybe there's more to it than what's on the surface."),
    ("Viola B. Muse", "(Nods slowly) Perhaps this tool can help us find a path that respects everyone's start, even with our differing views."),
    ("Ella Baker", "Indeed. If this simulation can help translate community sentiments and demonstrate how equal starts can lead to regulated, equitable solutions, then it is a powerful aid to sustainable practice.")
]


# --- Main Demo Execution ---
def run_demo():
    clear_screen()
    print(scene1_art_and_dialogue)
    time.sleep(2) # Pause to read the setup

    for speaker, line in dialogue_sequence_scene1:
        type_print(f"\n{speaker}: ", delay=0.02)
        type_print(f'"{line}"', delay=0.04)
        time.sleep(1.5) # Pause between speakers

    input("\n\nPRESS [ENTER] TO FEED THIS DIVERSE DATA TO THE SIMULATION...")
    clear_screen()

    print(scene2_header)
    time.sleep(1)
    for speaker, line in simulation_processing_lines:
        if speaker == "SIM":
            type_print(f"  {line}", delay=0.02)
        else: # for the initial line
             type_print(f"  {speaker}: \"{line}\"", delay=0.02)
        time.sleep(0.8) # Pause for each processing step

    print(scene2_results_and_dialogue)
    time.sleep(2) # Pause to read results

    for speaker, line in dialogue_sequence_scene2_reaction:
        type_print(f"\n{speaker}: ", delay=0.02)
        type_print(f'"{line}"', delay=0.04)
        time.sleep(1.5)

    print("\n\nWhat next?")
    print("  1. Initiate structured dialogue workshops based on SIM's key concern clusters.")
    print("  2. Form a task force with diverse representation (including Albertt, Baker, Muse, Stokes) to revise the proposal.")
    print("  3. Mr. Develo dismisses SIM, attempts to push plan (High risk of backlash & injustice).")

    while True:
        choice = input("> ")
        if choice in ['1', '2', '3']:
            if choice == '1':
                type_print("\nOutcome: Workshops initiated. Focus on genuine multi-modal community involvement and co-designing solutions. Path to regulated, more sustainable practice chosen.")
            elif choice == '2':
                type_print("\nOutcome: Task force formed. Diverse viewpoints now directly shaping the project. Simulation helped bridge communication gap.")
            elif choice == '3':
                type_print("\nOutcome: Developer proceeds, ignoring warnings. Simulation predicts significant community distrust, protests, and long-term systemic issues. (The path your paper warns against)")
            break
        else:
            type_print("Invalid choice. Please enter 1, 2, or 3.")

    print("\n\n--- End of Demo ---")

if __name__ == "__main__":
    run_demo()
