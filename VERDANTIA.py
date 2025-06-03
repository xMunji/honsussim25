import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_print(text, speaker_delay=0.02, line_delay=0.04, pause_after=0.7):
    if ":" in text:
        speaker, line = text.split(":", 1)
        for char_s in speaker + ":":
            print(char_s, end='', flush=True)
            time.sleep(speaker_delay)
        for char_l in line:
            print(char_l, end='', flush=True)
            time.sleep(line_delay)
    else:
        for char in text:
            print(char, end='', flush=True)
            time.sleep(line_delay)
    print()
    time.sleep(pause_after)

def display_art(art_string, delay_after=1):
    print(art_string)
    time.sleep(delay_after)

# --- ASCII ART (Keep your chosen art here) ---
city_skyline_art = """
          |    |    |    |    |    |    |    |    |    |    |
 _   _   _|_  _|_  _|_  _|_  _|_  _|_  _|_  _|_  _|_  _|_  _|_   _   _   _
        (#)  (#)  (#)  (#)  (#)  (#)  (#)  (#)  (#)  (#)  (#)
    (#)                                                            (#)
        _____________________________________________________________
   |||||                                                             |||||
   |||||                                                             |||||
   |||||_____________________________________________________________|||||
       /                                                             \\
      /_______________________________________________________________\\
      |                                                               |
      |                                                               |
 """
computer_art = """
        _________________________
       |.-----------------------.|
       ||                       ||
       ||      SIMULATION       ||
       ||        RUNNING        ||
       ||                       ||
       ||_______________________||
       '-------------------------'
          /TRONICS CO  C1200/
         /-------------------/
        /___________________/
          """
confused_face_art = """
          .--""--.
         /        \\
        |  O  O   |
        |   <     |
        |  `---'  |
         \ `--` /
          `----`
"""
checkmark_art = """
          .--.
         / \\  `
        |   \\  \\
         \\   \\ /
          `-- `
"""
# --- DIALOGUE & SCENES ---

def run_verdantia_lockin_demo():
    clear_screen()
    type_print("Welcome to: The Verdantia Lock-In!", speaker_delay=0.05, pause_after=1)
    type_print("A city beautiful, yet... stuck.", pause_after=1)
    display_art(city_skyline_art, delay_after=1.5)

    type_print("SCENE: Community Meeting. Project: 'Harmony Park Plaza'.", pause_after=1)
    type_print("Dr. Andreas: Welcome. Today we discuss the Park Plaza, and Verdantia's path forward.", pause_after=0.5) # 14
    type_print("Mr. Develo: (Nervously) Yes! Harmony Park! For a... harmonious Verdantia!", pause_after=0.5) # 9

    # --- Lock-in Group 1: Car-Centric Transportation ---
    type_print("Fred Ross: Mr. Develo, before 'harmony,' let's address Verdantia's car-centric lock-in. This plaza design seems to worsen it, harming pedestrians and air quality.", pause_after=1) # 26
    type_print("Akinabh Burbank: Hey, I need my truck! More parking is good! Old patterns work for me!", pause_after=1) # 16
    type_print("Louise Stokes: My customers need parking, but the constant traffic jams and delivery truck fumes? It's a nightmare for local health, especially the elderly.", pause_after=1.2) # 27

    # --- Lock-in Group 2: Fossil Fuel Infrastructure ---
    type_print("Pablo Diaz Albertt: And will this 'Harmony' be powered by Verdantia's dirty, outdated fossil fuel grid? We're locked into pollution that disproportionately harms marginalized communities!", pause_after=1.2) # 30
    type_print("Sylvia Woods: Exactly! The substation near my predominantly Black neighborhood is a relic! We need investment in clean energy, not more strain on failing systems that poison us.", pause_after=1.2) # 33

    # --- Lock-in Group 3: Exclusive Housing & Zoning ---
    type_print("Emma Tiller: Then there's housing. Verdantia's exclusionary zoning locks out affordable options, fueling gentrification. This park, without safeguards, will displace more low-income families and people of color.", pause_after=1.2) # 36
    type_print("Viola B. Muse: (Quietly, firmly) Many facing displacement have nowhere to go. Our city is stuck in policies that prioritize profit over people, especially the vulnerable.", pause_after=1.2) # 26

    # --- Lock-in Group 4: Aging Water/Energy Systems ---
    type_print("Ella Baker: And what of our crumbling water and energy lines? They fail most often in poorer districts! True harmony requires equitable infrastructure for all, not just patching for the privileged!", pause_after=1.2) # 35
    type_print("Oscar Heline: Water comes out my tap, lights are on! If it ain't broke for me, why the big fuss? Sounds expensive!", pause_after=1) # 23 (Shows resistance)

    type_print("Martina Curl: (Grandly) Behold! Verdantia, a magnificent mosaic of municipal malaise! Interlocking systems, each ensnared in antiquity's embrace, crying out for innovation, yet resisting transformation's touch!", pause_after=1.5) # 34
    display_art(confused_face_art, delay_after=1)
    # Word Count Scene 1: ~305 words. At 50WPM = ~6.1 mins. This is already long. We need to be very concise from here.

    type_print("Mr. Develo: (Overwhelmed) So many... deep... systemic... lock-ins! This is more than just a park!", pause_after=1) # 13

    type_print("\nDr. Andreas: Indeed. Let's see what our 'Sustainable Practice Simulator' makes of this.", pause_after=0.5)
    display_art(computer_art, delay_after=1.5)
    type_print("SIM: Analyzing Verdantia's Systemic Lock-Ins... Car-dependency, Fossil Fuels, Exclusionary Zoning, Aging Infrastructure...", pause_after=1) # 16
    type_print("SIM: 'Project Hindrance & Systemic Stagnation Index': CRITICAL (99.2%).", pause_after=1) # 9
    type_print("SIM: Resistance Points: Burbank (Cars), Heline (Infrastructure Complacency), Entrenched Interests (Implied).", pause_after=1.2) # 13
    type_print("SIM: Injustice Amplification: High. Current trajectory harms low-income, POC, disabled, and elderly populations most severely.", pause_after=1.5) # 19

    type_print("Oscar Heline: Okay, okay! Maybe my tap water isn't everyone's tap water... So, what if... just spitballing... we made sure the new park had REALLY good hot dogs? Like, REALLY good?", pause_after=1.5) # 36 (Humorous intervention attempt)

    type_print("Mr. Develo: (A desperate spark) Hot dogs! Heline, if this 'Harmony Park' features a solar-powered, locally-sourced, union-staffed, universally accessible gourmet hot dog emporium... a beacon of delicious, equitable sustenance...", pause_after=2) # 35

    type_print("Pablo Diaz Albertt: (Scoffs) We're talking systemic injustice, and you offer... artisanal wieners?", pause_after=1) # 12

    type_print("Viola B. Muse: (A thoughtful smile) Perhaps... Mr. Albertt, if agreeing on an 'equitable hot dog' helps us find common ground to *start* unlocking these other systems... if it shows a *willingness* to concede something small for a bigger dialogue...", pause_after=2) # 39
    display_art(checkmark_art, delay_after=1)

    type_print("Emma Tiller: A 'Hot Dog Accord' as an enabling condition for tackling exclusionary zoning? It's preposterous... but Verdantia needs *something* to break the inertia.", pause_after=1.5) # 25

    type_print("Fred Ross: If this... culinary compromise... can pave the way for real talk on bike lanes, better transit, and cleaner air, I'll bring the (vegan) buns.", pause_after=1.5) # 26

    type_print("Rev. Jesse Jackson: (Chuckles) From frankfurters to freedom from fossil fuels! Sometimes, the most profound changes begin with the simplest acts of shared humanity – or a shared snack. This could be the new narrative Verdantia needs!", pause_after=2) # 39

    type_print("\nDr. Andreas: So, an unorthodox strategy for change emerges. The 'Hot Dog Accord' – a small, humorous step to enable dialogue on Verdantia's deep-seated lock-ins. The challenges are immense, requiring funding, true community support, and overcoming significant resistance.", pause_after=1.5) # 46

    type_print("SIM: Enabling Conditions for 'Unlock': Cross-sector collaboration, participatory budgeting for infrastructure, zoning reform champions, visible community benefits from initial small wins (e.g., the hot dog stand's success).", pause_after=2) # 34
    # Word count Scene 2 & SIM: ~333 words.
    # Total words: ~305 + ~333 = ~638 words. At 50WPM = ~12.76 minutes. Still too long.

    # --- MAJOR TRIM REQUIRED ---
    # We need to be ruthless. Assume the audience gets the lock-in from the character's first line.
    # The humor needs to come fast.

    clear_screen()
    type_print("Welcome to: Verdantia's Un-Lock-In! (Speed Run!)", delay=0.05, pause_after=0.5) # 7
    display_art(city_skyline_art, delay_after=1)

    type_print("SCENE: Verdantia Community Meeting. Topic: 'Harmony Park Plaza' & City's Many Stuck Systems.", pause_after=0.5) # 14
    type_print("Mr. Develo: Harmony Park! Good for Verdantia?", pause_after=0.5) # 6

    type_print("Fred Ross (Cars): This plaza worsens car lock-in!", pause_after=0.3) #7
    type_print("Akinabh Burbank (Cars): More parking! Cars good!", pause_after=0.3) #5
    type_print("Pablo D. Albertt (Fossil Fuels): Powered by dirty energy again?", pause_after=0.3) #8
    type_print("Sylvia Woods (Fossil Fuels): Our air is bad enough near old plants!", pause_after=0.3) #10
    type_print("Emma Tiller (Housing): More gentrification from bad zoning!", pause_after=0.3) #7
    type_print("Viola B. Muse (Housing): Where do displaced families go?", pause_after=0.3) #7
    type_print("Ella Baker (Infrastructure): Old pipes fail the poor most!", pause_after=0.3) #8
    type_print("Oscar Heline (Infrastructure): My lights work! What's the fuss?", pause_after=0.3) #8
    # Initial complaints: 60 words. (~1.2 mins)

    type_print("Martina Curl: Verdantia! Stuck in a magnificent mess!", pause_after=0.5) #7
    display_art(confused_face_art, delay_after=0.5)
    type_print("Mr. Develo: (Panicked) So many lock-ins!", pause_after=0.5) #5
    # Transition: 12 words

    type_print("Dr. Andreas: Simulator, help!", pause_after=0.3)
    display_art(computer_art, delay_after=1)
    type_print("SIM: Verdantia's Lock-Ins: Severe. Stagnation Index: CRITICAL.", pause_after=0.5) #8
    type_print("SIM: Injustice Amplification: HIGH for marginalized groups.", pause_after=0.5) #7
    # SIM: 15 words

    type_print("Oscar Heline: Okay, what if... the park had AMAZING hot dogs?", pause_after=0.5) #10
    type_print("Mr. Develo: (Hopeful) Solar-powered, accessible, gourmet hot dogs for ALL?", pause_after=0.5) #10
    type_print("Pablo D. Albertt: Hot dogs vs. Systemic Injustice? Really?", pause_after=0.5) #8
    type_print("Viola B. Muse: If hot dogs START real talks on housing... maybe?", pause_after=0.5) #11
    display_art(checkmark_art, delay_after=0.5)
    type_print("Emma Tiller: Absurd... but zoning reform needs *some* catalyst.", pause_after=0.5) #8
    type_print("Fred Ross: If it helps get bike lanes, I'm in.", pause_after=0.5) #10
    type_print("Rev. Jesse Jackson: From franks to freedom! A new narrative!", pause_after=0.5) #9
    # Accord: 66 words (~1.3 mins)

    type_print("Dr. Andreas: The 'Hot Dog Accord'! A quirky strategy for change, unlocking dialogue on Verdantia's systemic issues.", pause_after=0.5) # 18
    type_print("SIM: Enabling Conditions: Community support, new narratives (like this one!), funding for pilot projects (e.g., The Equitable Hot Dog Stand).", pause_after=0.5) # 20
    # Conclusion: 38 words.

    # TOTAL WORDS: 7+14+6+60+12+3+15+66+38 = 221 words.
    # At 50 WPM = 221 / 50 = ~4.42 minutes of pure speaking.
    # With pauses for ASCII art (4 * 1s = 4s), intro/outro (5s), and inter-line pauses (generously, 30 lines * 0.5s = 15s).
    # Total time: ~4.42 min (265s) + 4s + 5s + 15s = ~289 seconds = ~4.8 minutes.

    # To reach ~7 minutes, we can:
    # 1. Add slightly longer pauses (`pause_after` in `type_print`).
    # 2. Slightly expand a few key lines for each character to better land their lock-in point.
    # 3. Let Martina Curl have one more slightly longer poetic line.
    # 4. Add a line or two about "resistance" more explicitly in the SIM or Andreas's wrap-up.

    type_print("\nNarrator: And so, Verdantia, teetering on the brink of delicious diplomacy, began to consider if a shared love for processed meats could indeed pave the way for systemic upheaval. Resistance from entrenched interests protecting old patterns would be fierce, but for the first time in ages, there was a sliver of (mustard-covered) hope.", delay=0.05, pause_after=1) # 59 words
    # New total: 221 + 59 = 280 words. ~5.6 minutes speaking. Add ~1.4 mins (84s) of pauses and art. This should hit close to 7 mins.

    type_print("\n--- END OF THE VERDANTIA UN-LOCK-IN! (SPEED RUN) ---", delay=0.05)

if __name__ == "__main__":
    run_verdantia_lockin_demo()