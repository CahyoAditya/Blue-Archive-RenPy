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

# ANIMATION ================================================
# This block is purely for animation purposes.
# ==========================================================

# Animation black -> its color in default 1 sec
transform blackfx(duration=1.0):
    # Start as completely black
    matrixcolor TintMatrix("#000000")

    # Smoothly fade in opacity and restore color
    ease duration matrixcolor TintMatrix("#ffffff")

# Animation shake left and right for .1s and repeat until duration went out
transform shake(times=5):
    block:
        xoffset -5
        pause 0.05
        xoffset 5
        pause 0.05
        repeat times
    xoffset 0

# Animation shake up down like jumping
transform jump(times=5):
    ease 0.1 yoffset -40
    pause 0.05
    ease 0.05 yoffset 5
    pause 0.05
    ease 0.1 yoffset 0

# TRANSFORM ================================================
# This block is for defining transforms used in the game.
# ==========================================================

# Set transform to the middle of screen
transform middle:
    xalign 0.5
    yalign 0.5
    yoffset 400
    zoom 1.3

# Set transform to the middle of screen for Kei prototype
transform middle_kei_prototype:
    xalign 0.3
    yalign 0.5
    yoffset 400
    zoom 1.3

# The game starts here.
label start:
    play music "Track_267.ogg.mp3"

    # Startup scene / animation
    scene BG_Iron Continent
    pause 1.0
    show Kei_Prototype_Idle at middle_kei_prototype, blackfx(2.0)
    pause 2.0

    hide Kei_Prototype_Idle
    show Kei_Prototype_Sweat at middle_kei_prototype
    play sound "SE_Appear_02b.wav.mp3"
    kei ".{nw=0.5}"
    play sound "SE_Appear_02b.wav.mp3"
    extend ".{nw=0.5}"
    play sound "SE_Appear_02b.wav.mp3"
    extend "."

    menu:
        "...":
            pass

    hide Kei_Prototype_Sweat
    show Kei_Prototype_Idle at middle_kei_prototype, shake()
    kei "What? Why are you staring at me like that?"

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

    hide Kei_Prototype_smile
    play sound "SE_Cartoon_01.wav.mp3"
    show Kei_Prototype_AngryBlushed at middle_kei_prototype, jump()
    kei "Why is that all you ever want to talk about?"

    return
