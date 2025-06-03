import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_print(text, delay=0.03, pause_after=0.5):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    time.sleep(pause_after)

def display_art(art_string, delay_after=1):
    print(art_string)
    time.sleep(delay_after)

# --- ASCII ART EXAMPLES (Replace with your choices!) ---
# From https://www.asciiart.eu/buildings-and-places/cities
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

# From https://www.asciiart.eu/computers/computers
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

# From https://www.asciiart.eu/people/faces
confused_face_art = """
          .--""--.
         /        \\
        |  O  O   |
        |   <     |
        |  `---'  |
         \ `--` /
          `----`
"""

# From https://www.asciiart.eu/signs/tick
checkmark_art = """
          .--.
         / \\  `
        |   \\  \\
         \\   \\ /
          `-- `
"""

# --- DIALOGUE & SCENES ---
# Word count target: ~350 words for dialogue (7 min * 50 WPM)

def run_humorous_demo():
    clear_screen()
    type_print("Welcome to: The Park Plaza Predicament!", delay=0.05, pause_after=1)
    display_art(city_skyline_art, delay_after=2)

    # --- SCENE 1: The Slowdown ---
    type_print("SCENE: The Community Meeting Room. Tensions are... palpable.", pause_after=1)

    type_print("Mr. Develo (Developer, nervously): So! The new 'Harmony Park Plaza'! A beacon of... uh... community! Any... thoughts?", pause_after=1) # ~16 words

    type_print("Pablo Diaz Albertt (Sternly): 'Thoughts'? My thought is this 'beacon' casts a rather long shadow of displacement, Mr. Develo. Franky, your proposal is an affront to established residents!", pause_after=1.5) # ~28 words

    type_print("Emma Tiller (Sharply): Indeed. The intellectual dishonesty in omitting long-term socio-economic impact studies for existing, particularly Black and Indigenous, communities is... glaring.", pause_after=1.5) # ~26 words

    type_print("Martina Curl (Grandly, hand gesturing): Ah, but consider, esteemed colleagues, the veritable cornucopia of contention! This project, a singular nexus, yet from it unfurls a magnificent, multifaceted miasma of municipal misgivings!", pause_after=2) # ~31 words
    display_art(confused_face_art, delay_after=1)

    type_print("Oscar Heline (Loudly): Miasma? Is that like... a good smell? I just hope there's a good hot dog stand! With extra relish!", pause_after=1.5) # ~23 words

    type_print("Ella Baker (Poignantly): Mr. Heline, while the culinary considerations are noted, the more pressing particulate matter is the *process*! True collaboration, a tapestry woven from every voice, not just a mayoral decree draped over dissenting whispers!", pause_after=2) # ~37 words

    type_print("Louise Stokes (Quietly but firmly): My family's bakery... 50 years. Will 'Harmony Park' have room for us? Or just for chains that can afford your 'beacon' rates?", pause_after=1.5) # ~26 words

    type_print("Dr. Lewis Andreas (Calmly): We're certainly hearing a... vibrant spectrum of opinions. This divergence is key to intragroup expression.", pause_after=1) # ~19 words

    type_print("Akinabh Burbank (Cheerfully oblivious): Spectrum's right! I think it sounds super! New is always better! More parking, maybe? For my big truck?", pause_after=1.5) # ~22 words

    type_print("Fred Ross (Thoughtfully, after a pause): The desire for 'new' often overlooks the value of 'established'. We must be decisive, but with care for what already thrives, however humbly.", pause_after=1.5) # ~29 words
    
    type_print("Rev. Jesse Jackson (Nodding): Brother Ross speaks truth. The expression of difference is vital, but so is finding common ground, however narrow it may initially seem.", pause_after=1.5) # ~26 words

    type_print("Mr. Develo (Wiping brow): So... many... valid... points. It's... a lot. This is taking much longer than anticipated.", pause_after=1) # ~16 words
    # Current word count: ~273 words

    # --- SCENE 2: The Simulation & Humorous Concession ---
    type_print("\nDr. Andreas: Perhaps our 'Sustainable Practice Simulator' can offer some perspective on this... rich tapestry.", pause_after=1)
    display_art(computer_art, delay_after=2)
    type_print("SIM (Monotone): Processing diverse, often contradictory, inputs... Calculating 'Project Hindrance Index'...", pause_after=1.5)
    type_print("SIM: Index: 98.7%. High probability of project stagnation due to extreme perspectival divergence.", pause_after=1.5)
    type_print("SIM: Key conflict: Grand Idealism vs. Pragmatic Fear vs. Culinary Priorities.", pause_after=2) # ~38 words

    type_print("Oscar Heline: Culinary Priorities! See! I told you the hot dogs were important!", pause_after=1) # ~12 words

    type_print("Mr. Develo (Exasperated, but a lightbulb goes off): Hot dogs... Heline, if I guarantee you the *best* artisanal, locally-sourced, ethically-raised, gluten-free-option-available hot dog stand this city has ever seen... with ALL the relishes...", pause_after=2) # ~33 words

    type_print("Pablo Diaz Albertt (Raises an eyebrow): ...And what precisely does this... 'hot dog detente' achieve for the substantive issues of displacement, Mr. Develo?", pause_after=1.5) # ~21 words

    type_print("Mr. Develo: It achieves... (thinks hard)... a WILLING CONCESSION! A starting point! If we can agree on gourmet hot dogs, maybe we can agree to *actually listen* to Mrs. Stokes about her bakery, and to your points about impact studies, Mr. Albertt!", pause_after=2) # ~39 words

    type_print("Emma Tiller (A tiny smile plays on her lips): Conceding on condiments to conquer community conflict? It's... unorthodox. And frankly, a bit absurd.", pause_after=1.5) # ~20 words

    type_print("Viola B. Muse (Chuckles softly): Absurd, perhaps. But if it breaks the ice for genuine dialogue about protecting our vulnerable communities... I'll take it. With mustard.", pause_after=1.5) # ~26 words
    display_art(checkmark_art, delay_after=1)

    type_print("Martina Curl: A most piquant proposal! From gastronomic appeasement to gradual accord! The narrative arc is... unexpectedly delightful!", pause_after=1.5) # ~20 words

    type_print("Rev. Jesse Jackson: (Smiling) Sometimes, my friends, the path to profound understanding begins with the seemingly profane. If a hot dog can open hearts and minds to the deeper needs of the community, then let us bless the hot dog!", pause_after=2) # ~37 words

    type_print("\nDr. Andreas: So, we have a... 'Hot Dog Accord' as a basis for further, more serious, multi-modal discussions? A humorous, yet willing, first step?", pause_after=1) # ~22 words

    # Total Dialogue Word Count: ~273 (Scene 1) + ~38 (SIM) + ~12 (Heline) + ~33 (Develo) + ~21 (Albertt) + ~39 (Develo) + ~20 (Tiller) + ~26 (Muse) + ~20 (Curl) + ~37 (Jackson) + ~22 (Andreas) = ~541 words
    # This is over the 350 target. Need to trim.

    # --- REVISED DIALOGUE FOR PACING (Aiming closer to 350-400 words) ---
    # We'll shorten some lines, remove some less critical ones.

    clear_screen()
    type_print("Welcome to: The Park Plaza Predicament! (Fast Forward Edition)", delay=0.05, pause_after=1)
    display_art(city_skyline_art, delay_after=1.5)

    type_print("SCENE: Community Meeting. Project: 'Harmony Park Plaza'.", pause_after=1)
    type_print("Mr. Develo (Developer): Thoughts on 'Harmony Park'?", pause_after=0.5) # 5

    type_print("Pablo Diaz Albertt: It screams 'displacement'!", pause_after=1) # 4
    type_print("Emma Tiller: And your impact studies are a joke!", pause_after=1) # 7

    type_print("Martina Curl: Oh, the glorious cacophony of civic concern!", pause_after=1.5) # 8
    display_art(confused_face_art, delay_after=1)

    type_print("Oscar Heline: Cacophony? I just want a hot dog stand!", pause_after=1) # 9

    type_print("Ella Baker: Process, people! We need true collaboration, not just top-down plans!", pause_after=1.5) # 12

    type_print("Louise Stokes: My bakery... will it survive 'Harmony'?", pause_after=1) # 7

    type_print("Dr. Andreas: Diverse views are emerging...", pause_after=0.5) # 5
    type_print("Akinabh Burbank: Sounds great! New is good!", pause_after=1) # 6
    # Scene 1 Word Count: 5 + 4 + 7 + 8 + 9 + 12 + 7 + 5 + 6 = 63 words (Much shorter!)

    type_print("\nDr. Andreas: Let's consult the 'Sustainable Practice Simulator'.", pause_after=1)
    display_art(computer_art, delay_after=1.5)
    type_print("SIM: Processing... 'Project Hindrance Index': 98.7%. Stagnation likely.", pause_after=1) # 9
    type_print("SIM: Key conflict drivers: Idealism vs. Fear vs. Culinary Desires.", pause_after=1.5) # 10
    # Sim Word Count: 9 + 10 = 19 words

    type_print("Oscar Heline: See! Culinary Desires! Hot dogs matter!", pause_after=1) # 7

    type_print("Mr. Develo (Exasperated): Alright, Heline! You get your dream hot dog stand – best in the city! ALL the relishes!", pause_after=1.5) # 20

    type_print("Pablo Diaz Albertt: And this... solves displacement how?", pause_after=1) # 7

    type_print("Mr. Develo: It's a WILLING CONCESSION! A start! If we agree on hot dogs, maybe we can agree to *really* talk about bakeries and impact studies!", pause_after=1.5) # 26

    type_print("Emma Tiller (Slight smile): Condiment diplomacy? Absurd, but... intriguing.", pause_after=1) # 7

    type_print("Viola B. Muse (Chuckles): If absurd gets us talking seriously about our community, I'm in. With mustard.", pause_after=1) # 16
    display_art(checkmark_art, delay_after=1)

    type_print("Martina Curl: From frankfurters to fraternity! A curious course!", pause_after=1) # 8

    type_print("Rev. Jesse Jackson: (Smiling) If a humble hot dog opens hearts to deeper needs, let's embrace it!", pause_after=1.5) # 16

    type_print("\nDr. Andreas: So, the 'Hot Dog Accord' it is? A humorous first step to real collaboration?", pause_after=1) # 16
    # Scene 2 Dialogue Word Count: 7 + 20 + 7 + 26 + 7 + 16 + 8 + 16 + 16 = 123 words

    # Total Dialogue words: 63 (S1) + 19 (SIM) + 123 (S2) = 205 words.
    # At 50 WPM, this is 205/50 = ~4.1 minutes of speaking.
    # Add time for ASCII art display (e.g., 4 arts * 1.5s = 6s), pauses between lines (e.g. 20 lines * 1s = 20s),
    # intro/outro type_print (few seconds).
    # This should bring it closer to 5-6 minutes, which is a good target. If you want exactly 7, you can expand some lines slightly or add one more exchange.

    type_print("\nAnd so, fueled by an unlikely allegiance to artisanal sausages, the community began the slow, arduous, but now slightly more optimistic journey towards sustainable practice.", delay=0.05, pause_after=1)
    type_print("The project was still slow, but now, at least, they were slowing down *together*, with a shared chuckle.", delay=0.05, pause_after=1)
    type_print("\n--- END OF DEMO ---", delay=0.05)

if __name__ == "__main__":
    run_humorous_demo()