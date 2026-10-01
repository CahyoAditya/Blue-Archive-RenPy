# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define kei = Character("Kei", color="#ffffff", who_bold=True)
image BG_Iron Continent = im.Scale("BG_IronContinent.jpg", 1920, 1080)
image Kei_Prototype_Idle = "Kei_Prototype_Idle.png"
image Kei_Prototype_Sweat = "Kei_Prototype_Sweat.png"
image Kei_Prototype_Openmouth_Eyesclosed = "Kei_Prototype_Openmouth_Eyesclosed.png"
image Kei_Prototype_question = "Kei_Prototype_question.png"
image Kei_Prototype_smile = "Kei_Prototype_03.png"
image Kei_Prototype_AngryBlushed = "Kei_Prototype_13.png"


# Animation shake left and right for .1s and repeat until duration went out
transform shake(times=5):
    block:
        xoffset -5
        pause 0.05
        xoffset 5
        pause 0.05
        repeat times
    xoffset 0

# MAIN STORY =====================================
# The game starts here.
# ================================================
label start:
    play music "Track_267.ogg.mp3"

    # Startup scene / animation
    scene BG_Iron Continent
    pause 1.0
    show Kei_Prototype_Idle at middle_kei_prototype, take, silhouette_in, idle
    pause 2.0

    # Text ... kei
    hide Kei_Prototype_Idle
    show Kei_Prototype_Sweat at middle_kei_prototype, idle
    play sound "SE_Appear_02b.wav.mp3" volume 1.5
    kei ".{nw=0.5}"
    play sound "SE_Appear_02b.wav.mp3" volume 1.5
    extend ".{nw=0.5}"
    play sound "SE_Appear_02b.wav.mp3" volume 1.5
    extend "."

    menu:
        "...":
            pass

    # Text What? Why are you staring at me like that? kei
    hide Kei_Prototype_Sweat
    show Kei_Prototype_Idle at middle_kei_prototype, shake(), idle
    kei "What? Why are you staring at me like that?"

    # Text Is there something on my face? Oh, there's not? I knew that. I checked a mirror before we came out here. kei
    hide Kei_Prototype_Idle
    show Kei_Prototype_Openmouth_Eyesclosed at middle_kei_prototype
    kei "Is there something on my face? Oh, there's not? I knew that. I checked a mirror before we came out here."

    menu:
        "No, I just...":
            pass


    hide Kei_Prototype_Openmouth_Eyesclosed
    show Kei_Prototype_question at middle_kei_prototype
    kei "...Just?"

    menu:
        "...I just thought everything turned out well.":
            pass

    hide Kei_Prototype_question
    show Kei_Prototype_smile at middle_kei_prototype
    kei "...Of course it did."

    menu:
        "And...Kei-Kei looks really cute.":
            pass
        "And...Mommy really cute":
            pass

    hide Kei_Prototype_smile
    play sound "SE_Cartoon_01.wav.mp3" volume 2.5
    show Kei_Prototype_AngryBlushed at middle_kei_prototype, jump()
    kei "Why is that all you ever want to talk about?"

    return
