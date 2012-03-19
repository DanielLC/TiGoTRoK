﻿# This is a proof-of-concept K:BDH VN.

init:    

    image bg classroom = "Backgrounds/classroom.jpg"
    image bg hallway = "Backgrounds/hallway.png"
    image bg stairwell = "Backgrounds/stairwell.jpg"
    image bg stairwellbarrier = "Backgrounds/stairwellbarrier.jpg"
    image bg roof = "Backgrounds/roof.jpg"
    image bg roofclose = "Backgrounds/roofclose.jpg"
    image bg roofsky = "Backgrounds/roofsky.jpg"
    image bg roofright = "Backgrounds/roofright.jpg"
    image bg BeamOrange1 = "Backgrounds/BeamOrange1.jpg"
    image bg BeamOrange2 = "Backgrounds/BeamOrange2.jpg"
    image bg BeamOrange3 = "Backgrounds/BeamOrange3.jpg"
    image bg BeamOrange4 = "Backgrounds/BeamOrange4.jpg"
    image white = "#ffffff"
    image black = "#000000"
    image yukibackground = "#ccccff"
    image title0 = "Backgrounds/title0.png"
    image Barrier = "Backgrounds/barrier2.jpg"
    image Bluesword = "Backgrounds/bluesword1.png"
    image field = "Sprites/Effects/InterdictionField.png"
    image BarrierSmall = "Sprites/Effects/BarrierSmall.png"
    image BarrierSmall Bright = im.MatrixColor("Sprites/Effects/BarrierSmall.png",
                                       im.matrix.brightness(.5))
    image Knife1 = "Sprites/Effects/Knife1.png"
    image Knife2 = "Sprites/Effects/Knife2.png"
    image Knife3 = "Sprites/Effects/Knife3.png"
    image Spike1 = "Sprites/Effects/NetSpike1.png"
    image Spike2 = "Sprites/Effects/NetSpike2.png"
    image Spike3 = "Sprites/Effects/NetSpike3.png"
    image Spike4 = "Sprites/Effects/NetSpike4.png"
    image Spike5 = "Sprites/Effects/NetSpike5.png"
    image Haruhi Sup1 = "Sprites/Haruhi/HaruhiSideSurprised1.png"
    image Haruhi Ang1 = "Sprites/Haruhi/HaruhiSideAngry1.png"
    image Haruhi Ang2 = "Sprites/Haruhi/HaruhiSideAngry2.png"
    image Haruhi Ang3 = "Sprites/Haruhi/HaruhiSideAngry3.png"
    image Haruhi Hap1 = "Sprites/Haruhi/HaruhiSideHappy1.png"
    image Haruhi Hap2 = "Sprites/Haruhi/HaruhiSideHappy2.png"
    image Haruhi Hap3 = "Sprites/Haruhi/HaruhiSideHappy3.png"
    image Haruhi Hap4 = "Sprites/Haruhi/HaruhiSideHappy4.png"
    image Haruhi Pout1 = "Sprites/Haruhi/HaruhiSidePout1.png"
    image Haruhi Pout1 Bright = im.MatrixColor("Sprites/Haruhi/HaruhiSidePout1.png",
                                       im.matrix.brightness(.5))
    image Haruhi Eyeroll1 = "Sprites/Haruhi/HaruhiSideEyeroll1.png"
    image Haruhi Quest1 = "Sprites/Haruhi/HaruhiSideQuestion1.png"
    image Haruhi Grin1 = "Sprites/Haruhi/HaruhiSideGrin1.png"
    image Haruhi Worry1 = "Sprites/Haruhi/HaruhiSideWorry1.png"
    image Haruhi Smile1 = "Sprites/Haruhi/HaruhiSideSmile1.png"
    image Haruhi Smile2 = "Sprites/Haruhi/HaruhiSideSmile2.png"
    image Haruhi Smile3 = "Sprites/Haruhi/HaruhiSideSmile3.png"
    image Haruhi Sigh1 = "Sprites/Haruhi/HaruhiSideSigh1.png"
    image Kyon Ser1 = "Sprites/Kyon/KyonSerious1.png"
    image Kyon Ser2 = "Sprites/Kyon/KyonSerious2.png"
    image Kyon Ser2 Bright = im.MatrixColor("Sprites/Kyon/KyonSerious2.png",
                                       im.matrix.brightness(.5))
    image Kyon Sigh1 = "Sprites/Kyon/KyonSigh1.png"
    image Kyon Sigh2 = "Sprites/Kyon/KyonSigh2.png"
    image Kyon Neutral1 = "Sprites/Kyon/KyonNeutral1.png"
    image Kyon Neutral2 = "Sprites/Kyon/KyonNeutral2.png"
    image Kyon Ang1 = "Sprites/Kyon/KyonAngry1.png"
    image Kyon Pain1 = "Sprites/Kyon/KyonPained1.png"
    image Kyon Pain2 = "Sprites/Kyon/KyonPained2.png"
    image Kyon Smile1 = "Sprites/Kyon/KyonSmile1.png"
    image Kyon Worry1 = "Sprites/Kyon/KyonWorry1.png"
    image Kyon Puzzle1 = "Sprites/Kyon/KyonPuzzled1.png"
    image Skinsuit = "Sprites/Kyon/KyonSkinsuitTemplate.png"
    image Skinsuit Bright = im.MatrixColor("Sprites/Kyon/KyonSkinsuitTemplate.png",
                                       im.matrix.brightness(.5))
    image Coat Bright = im.MatrixColor("Sprites/Kyon/KyonCoat.png",
                                       im.matrix.brightness(.5))
    image Coat = "Sprites/Kyon/KyonCoat.png"
    image Asakura Smile1 = "Sprites/Asakura/AsakuraSmile1.png"
    image Asakura Smile2 = "Sprites/Asakura/AsakuraSmile2.png"
    image Asakura Smile3 = "Sprites/Asakura/AsakuraSmile3.png"
    image Asakura Sup1 = "Sprites/Asakura/AsakuraSurprise1.png"
    image Asakura Frown1 = "Sprites/Asakura/AsakuraFrown1.png"
    image Asakura Frown2 = "Sprites/Asakura/AsakuraFrown2.png"
    image Asakura Frown3 = "Sprites/Asakura/AsakuraFrown3.png"
    image Asakura Unhap1 = "Sprites/Asakura/AsakuraUnhappy1.png"
    image Asakura Sigh1 = "Sprites/Asakura/AsakuraSigh1.png"
    image Asakura Pain1 = "Sprites/Asakura/AsakuraPain1.png"
    image Asakura Pain2 = "Sprites/Asakura/AsakuraPain2.png"
    image Asakura Pain2 Bright = im.MatrixColor("Sprites/Asakura/AsakuraPain2.png",
                                       im.matrix.brightness(.5))
    image Yuki EyesClosed = "Sprites/Yuki/YukiSideEyesClosed1.png"
    image Yuki EyesClosed Bright = im.MatrixColor("Sprites/Yuki/YukiSideEyesClosed1.png",
                                       im.matrix.brightness(.5))
    image Yuki Side1 = "Sprites/Yuki/YukiSide1.png"
    image Yuki Side2 = "Sprites/Yuki/YukiSide2.png"
    image Yuki Talk1 = "Sprites/Yuki/YukiSideTalk1.png"
    image Yuki Talk2 = "Sprites/Yuki/YukiSideTalk2.png"

    image knifethrow = "Sprites/Effects/knifethrowlong.png"

    image Credits0 = "Backgrounds/credits0.png"
    image Credits1 = "Backgrounds/credits1.png"
    image Credits2 = "Backgrounds/credits2.png"
    image Credits3 = "Backgrounds/credits3.png"

    python: # TODO: figure out a way to quickly switch on/off the window show/hide statements below.
        basechar = Character(None, kind=nvl)
        kyon = Character("Kyon", kind=basechar, color="#777755")
        sister = Character("Nonoko", kind=basechar, color="#999977")
        yuki = Character("Nagato Yuki", kind=basechar, color="#aaaaff")
        narrator = Character(None, kind=basechar)
        irisoutfast = CropMove(0.2, "irisout")
        slowfadein = Fade(0.5, 0.5, 5)
        wipeleftfast = CropMove(0.3, "wipeleft")
        wiperightfast = CropMove(0.3, "wiperight")
        wipeupslow = CropMove(2, "wipeup")
        wipeupfast = CropMove(0.3, "wipeup")
        teleport = ImageDissolve("id_teleport.png", 1.0, 0)
        coatin = ImageDissolve("id_clouds.png", 1.0, 0)
        coatout = ImageDissolve("id_clouds.png", 1.0, 0, reverse=True)
        menu = nvl_menu
        style.nvl_window.background = "nvl_window.png"
        style.nvl_window.xpadding = 55
        style.nvl_window.ypadding = 55
        config.empty_window = nvl_show_core
        config.window_hide_transition = dissolve
        config.window_show_transition = dissolve
        renpy.music.set_volume(0.2, .5, channel="music")
        flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
        renpy.music.register_channel("sound2", "sfx", 0)
        _preferences.set_volume("sfx", 0.5)

        config.keymap['skip'].remove('K_LCTRL')
        config.keymap['skip'].remove('K_RCTRL')
        config.keymap['skip'].append('K_LALT')
        config.keymap['skip'].append('K_RALT')

transform center_left:
    xalign 0.1 yalign 1.0
    
transform HalfRight:
    xalign 0.75 yalign 1.0
transform HalfLeft:
    xalign 0.25 yalign 1.0
    
transform KyonRightFast:
    xalign 0.0 yalign 1.0
    linear 0.15 xalign 1.0   

label start:
    stop music fadeout 1
    scene title0 with slowfadein
    
    pause
    play sound "SE/Pageflip3.mp3" 

    nvl clear
    scene bg classroom with fade:
        size (800,600)
    "Class had started innocently enough that day, but he'd long ago given up on expecting that to mean anything."
    "With each passing moment after lunch, he grew more and more anxious, stealing glances behind him to make certain that she was still there—{w=.4}still safe."
    "And every time their eyes met, she smirked knowingly and quickly looked outside, trying to pretend eye contact was never made."
    "He was absolutely certain that if his sense of anxiety weren't imagined, she was the one behind it — one way or another." 
    "When the fifth period bell rang, he was prepared."    
    nvl clear
    play music "Music/Gouin.mp3" fadein 1
    $ renpy.music.set_volume(0.2, .5, channel="music")
    "In a way, he'd always wanted to do this; exact that one tiny bit of revenge upon her for all the times she'd done it to him."
    "So when she rose, turned in one smooth motion, and made to bolt out of the room—"
    nvl clear
    "—he was there first, seizing the decorative ties of her sailor uniform's neckerchief and making for the door at top speed." 
    nvl clear
    scene bg hallway with fade:
        size (800,600)
    show Haruhi Sup1 at left
    show Kyon Ser1 at center
    "\"Bwa!\" she protested, arms waving frantically as she dashed to keep up, or risk the knot being pulled out." 
    show Haruhi Ang2 at left
    "\"What the hell do you think you're doing!?\""
    show Haruhi Sup1 at left
    scene bg hallway with None:
        xanchor .5 yanchor .5
        xpos .5 ypos .5
        linear .5 rotate 360
    hide Haruhi
    hide Kyon  
    pause .5
    nvl clear
    scene bg stairwell with fade:
        size (800,600)
    "Naturally, he said nothing to her during the entire mad dash to the remote stairwell where she had first hauled him by his own tie, so long ago."
    "He released her at the top of the steps after looking around to ensure that no one else was nearby."
    "Her momentum carried her forward, resulting in him pressing one hand flat against her chest, just below her neck."
    "Her eyes quickly sharpened, her features fixed into a scowl."
    nvl clear
    show Haruhi Ang3 at center_left
    "\"What the hell, Kyon!?\""
    show Kyon Ser1 at right
    "He held up one hand and said, \"Something's up.\""
    show Haruhi Hap3 at center_left
    "Her irritation vanished instantly, replaced with wide-eyed excitement. She clapped her hands together and hopped from foot to foot."
    show Haruhi Hap4 at center_left
    "\"Yes!\" she cheered. \"It's been so boring lately!\""
    nvl clear
    "\"This better not be your fault!\""
    show Kyon Sigh1 at right
    "He shook his head in irritation, then patted his left coat pocket. Then right, then both pants pockets, then the back of each hand."
    "After that, he traced the fingertips of his right hand above his ear, eyes distant, and pulled his cell phone from one pocket."
    nvl clear
    show Haruhi Ang1 at center_left
    "\"What is it?\" she asked, when he spent a long minute studying the screen."
    show Kyon Neutral1 at right
    "\"Maybe a false alarm,\" he admitted, shifting his shoulders.{nw} "
    show Kyon Ang1 at right
    extend "\"Are you messing with me?\""   
    show Haruhi Ang2 at center_left
    "\"I should be asking you that! But whatever! You hauled me all the way out here—by my shirt, I might add!—so tongues are going to wag! If you're going to do this, then you know what I want!\""
    show Haruhi Hap1 at center_left
    nvl clear
    show Kyon Sigh2 at right
    "\"Haruhi....\""
    show Haruhi Hap2 at center_left
    "\"Do it!\" she said, bouncing on the balls of her feet in excitement. \"I want to see it!\""
    show Kyon Neutral2 at right
    "\"Is now really the time? Break's going to be over soon—\""
    show Haruhi Hap3 at center_left
    "\"Get it out now! I want to see!\""
    nvl clear
    show Kyon Sigh1 at right
    "Heaving the sigh of the eternally doomed, he put his phone away and muttered underneath his breath."
    show Haruhi Hap4 at center_left
    "\"Do that voice, too! You know the one? Like from a movie voice-over guy? I love that! Do it! Come on!\""
    show Kyon Ser1 at right
    "\"Fine,\" he grumbled.{nw}"
    show Kyon Sigh2 at right
    extend " \"But you come up with the excuse for class.\""
    nvl clear
    show Haruhi Hap4 at center_left
    "\"Student council president,\" she said without hesitation. \"Blame him.\""
    show Kyon Sigh2 at right
    "\"Ahem,\" he coughed, shooting her a dark look.{nw}"
    show Kyon Ser1 at right
    stop music fadeout 1
    extend " \"Take a step back, I don't want to catch you in the interdiction field again.\""
    show Haruhi Hap4 at center_left
    "She nodded and stepped backwards, against the wall."
    show Haruhi Hap4:
        xalign 0.1 yalign 1.0
        linear 0.4 xalign 0.0
    pause 0.4
    nvl clear
    play music "music/YukiAsakuraFight.mp3" fadein 1
    show Kyon Ser2 at right
    pause 1
    play sound "SE/DunDun.mp3"
    "Standing perfectly straight, hands at his sides, he closed his eyes, and began speaking in his best faux movie announcer voice-over."
    "\"Skinsuit active,\" "
    play sound "SE/Sizzle2.mp3"
    show Skinsuit at right with wipeupslow
    extend "as something that looked like nothing so much as black paint suddenly engulfed his entire body beneath his uniform."
    nvl clear
    play sound "SE/NanoRepair.mp3"
    "\"Gravimetric stabilizers and secondary gyrometrics online,\" as ridged metal studs appeared on the back of each knuckle, and beneath his uniform pants, metallic vertical rails were described in the skinsuit."
    nvl clear
    "\"Greatcoat thermoptic stealth disengaged,\" "
    play sound "SE/CloakOff.mp3"
    show Coat at right with coatin
    extend "as a knee-length tan greatcoat coalesced, covering his shoulders with a thick mantle."
    show Haruhi Hap3 at left
    "\"Doesn't that get hot?\" Her smile had only grown, her eyes shining with anticipation."
    nvl clear
    show Kyon Neutral2 at right
    "\"We had environmental conditioning added last night, since the weather's heating up,\" he said in a normal voice."
    show Kyon Ser2 at right
    "Switching back, he said, \"Primary weapons check.\""     
    nvl clear
    play sound "SE/lowswoosh.mp3"
    pause .02
    play sound "SE/lowswoosh.mp3"
    pause .02
    play sound "SE/lowswoosh.mp3"
    "He pulled a fifty centimeter long glittering metal cylinder from within the greatcoat, releasing it to spin on its axis in midair to one side, announcing, \"Long range precision and high yield weaponry is at full charge.\""
    play sound "SE/Barrier2.mp3"
    show Kyon Ser2 Bright at right
    show Skinsuit Bright at right
    show Coat Bright at right
    show field at right with dissolve
    pause .1
    hide field at right
    show Kyon Ser2 at right
    show Skinsuit at right 
    show Coat at right
    with dissolve
    "A circle of light appeared on the floor around him, a simple white ring with glittering sparks chasing around in either direction, sending brilliant flashes to streak upwards."
    nvl clear
    "Another cylinder, wider but shorter than the last was released to float next to the first."
    "\"Mid- and short-range crowd-control weaponry is at ... ninety seven percent capacity and charging,\" he continued, squinting at the featureless gunmetal tube."
    nvl clear
    play sound "SE/clink.mp3"
    "Pulling a well-crafted sword hilt with no cross-guard or blade from one pocket, he released it horizontally, and it hung before him between the other weapons. \"Beam saber is at full capacity.\""
    show Kyon Ser1 at right
    "After pulling his cell phone from one pocket, he brushed his fingertips over his ear, revealing three dull metal studs in the skinsuit."
    "\"All systems nominal; no proximity alarms—\""
    nvl clear
    show Kyon Ang1 at right
    "He broke off suddenly, scowling. \"Okay,\" he said in his normal voice. \"My mistake. We've got incoming.\""
    show Haruhi Hap4:
        xalign 0.0 yalign 1.0
        linear 0.1 xalign 0.1
    "\"God damn it Kyon, you're so cool when you do this,\" Haruhi gushed, clapping her hands together. \"What is it?\""
    nvl clear
    show Kyon Neutral1 at right
    "\"I'm not sure,\" he said, as a cold, familiar chuckle echoed."
    show Kyon Ser1 at right
    "One eyebrow twitched and he stowed his weapons, banishing the ring of light and flinging his phone at Haruhi."
    show Kyon Ser2 at right
    "\"Speed dial two,\" he snapped. \"Stay in the circle.\""
    show Haruhi Pout1:
        xalign 0.1 yalign 1.0
        linear 0.4 xalign 0.0
    pause 0.4
    play sound "SE/Barrier1.mp3"
    show Haruhi Pout1 Bright at left
    show field at left with dissolve
    pause .1
    hide field at left with dissolve
    show Haruhi Pout1 at left with dissolve
    "She pouted, but did as she was told, the ring of light reappearing on the floor around her this time."
    nvl clear
    hide Kyon 
    hide Skinsuit
    hide Coat
    hide Haruhi
    play sound "SE/footsteps5.mp3" 
    pause 5
    show Asakura Smile2 at center with wipeup
    pause 1
    play sound "SE/DunDun.mp3"
    show Asakura Smile1 at center
    "\"Kyon-kun~!\" someone caroled up the stairwell, the echoing click of their shoes sounding as they climbed the stairs."
    show Asakura Smile2 at center
    "\"It's been a while, hasn't it?\""
    show Asakura Sup1 at center
    play sound "SE/saberon.mp3"
    show Bluesword with wipeupfast
    pause 1
    hide Bluesword with dissolve
    "The school bell chimed just as she rounded the landing, and he activated the beam saber. The blade made a crackling, whirring buzz and shed a soft, pale blue light."
    show Asakura Frown1 at center
    "\"Y...you....\" she began, before she frowned, blinking, staring at the energy weapon."
    nvl clear
    show Asakura Frown1 at left
    show Kyon Ang1 at right
    show Skinsuit at right
    show Coat at right
    "\"Long time no see,\" he said, switching stance to the long-sword style, Ni-Ten Ichi Ryu."
    show Asakura Frown2 at left
    "\"Um.... Hm. This is different. You've certainly changed, Kyon-kun.\""
    nvl clear
    show Kyon Ser2 at right
    "\"That's funny, Asakura-san, because you haven't.\""
    # stop music fadeout 1
    # scene black with fade
    # # The hardpause calls are necessary because otherwise Ren'py wants to skip over all the pause statements on a single press of the key.
    # show Credits0 with dissolve
    # pause
    # $ renpy.pause(.1, hard=True)
    # show Credits1 with dissolve
    # pause
    # $ renpy.pause(.1, hard=True)
    # show Credits2 with dissolve
    # pause
    # $ renpy.pause(.1, hard=True)
    # show Credits3 with dissolve
    # pause
#     
    nvl clear
    hide Asakura
    show Kyon Ser2 at right
    show Skinsuit at right
    show Coat at right
    show Haruhi Hap3 at left
    "Haruhi bounced on her heels with a wide grin, holding Kyon's cell phone in both hands as she remained in the center of the glowing circle."
    show Haruhi Hap4 at left
    "\"I knew it!\" she cheered.{nw} "
    show Haruhi Hap1 at left
    extend "\"There was something off about Asakura! What is it?\""
    nvl clear
    hide Kyon
    hide Coat
    hide Skinsuit
    hide Haruhi
    show Asakura Unhap1 at center
    "\"Um...\" the onetime class representative said, frowning."
    hide Asakura
    show Kyon Sigh2 at right
    show Skinsuit at right
    show Coat at right
    "\"She's alien,\" Kyon volunteered.{nw} "
    show Kyon Neutral2 at right
    extend "\"From the same place as Yuki-chan and Kimidori, but she tried to kill me once.\""
    show Haruhi Sup1 at left
    "\"Whaaaat? What did you do to make her mad?\" Haruhi asked, looking at him in bemusement."
    nvl clear
    hide Kyon
    hide Coat
    hide Skinsuit
    hide Haruhi
    show Asakura Frown3 at center
    "\"Er,\" Asakura said, crossing her arms beneath her chest."
    show Asakura Frown2 at center
    "\"Evidently my information requires an update. I was sent to dispatch Kyon-kun, because he's become an undesirable element for my superiors.\""
    show Asakura Sup1 at center
    nvl clear
    "\"Really, I'd hoped to see a new state, maybe even provoke it with his death."
    show Asakura Smile2 at center
    "\"But, those toys seem to say that's already happened! So disappointing ... I suppose if I'd been more patient, I could see it anyway?\""
    show Kyon Sigh1 at right
    show Skinsuit at right
    show Coat at right
    "\"I personally like to see it as a lesson on the effects of {i}randomly stabbing people,{/i}\" Kyon muttered."
    nvl clear
    show Asakura Smile1 at center
    "\"Oh, it wasn't random,\" she countered.{nw} "
    show Asakura Smile2 at center
    extend "\"It was highly specific! I put a whole two hours of thought into it, you know. For us, that's quite a while!\""
    show Kyon Ser2 at right
    "\"I'm touched,\" he said dryly."
    nvl clear
    show Asakura Smile1 at center
    hide Kyon
    hide Coat
    hide Skinsuit
    hide Asakura
    show Haruhi Eyeroll1 at left
    "\"Blah blah blah,\" Haruhi muttered, crossing her arms over her chest and rolling her eyes."
    show Haruhi Ang1 at left
    "\"Skip the speeches — if I don't know the complete back story, it's all meaningless to me. I think it's about time we get down to business, right?\""
    nvl clear
    hide Haruhi
    stop music
    play music "Music/AsakuraTheme.mp3" fadein 1
    play sound "SE/horror.mp3"
    scene bg stairwellbarrier with teleport:
        size (800,600)
    show Asakura Smile2 at center
    "\"Happy to oblige!\" Asakura said brightly, as their surroundings pulsed, the window turning into a gunmetal gray steel barrier, strange patterns coalescing across the walls."
    play sound "SE/powerdown.mp3"
    "The circle on the floor around Haruhi abruptly winked out."
    nvl clear
    "\"Now, I've converted the entire space of this stairwell into-\""
    hide Asakura
    "Kyon spun on one foot, crying out with a great, \"Ki-yah!\" "
    play sound "SE/lowswoosh.mp3"
    pause (0.2)
    play sound "SE/impact.mp3"
    with vpunch
    pause (0.2)
    play sound "SE/glassbreak1.mp3"
    with hpunch
    extend "and kicking the door halfway across the roof."
    show Haruhi Sup1 at left
    pause (.01)
    show Kyon Ser1 at left behind Haruhi
    show Skinsuit at left behind Haruhi
    show Coat at left behind Haruhi
    with moveinright
    pause (0.5)
    hide Kyon
    hide Haruhi
    hide Skinsuit
    hide Coat
    with moveoutleft
    "Sparing no more time, he swept Haruhi up in one arm and dashed through the opening."
    scene bg roof with wiperight
    nvl clear
    "\"Waaah!\" she protested.{fast} \"Why are you running away!?\""
    show Haruhi Sup1 at left
    show Kyon Ser1 at right
    show Skinsuit at right
    show Coat at right
    with moveinleft
    "\"Confined spaces,\" he answered, sliding to a halt in the middle of the roof and setting her down.{fast} \"Speed dial two again.\""
    nvl clear
    show Haruhi Pout1 at left
    pause .4
    play sound "SE/Barrier1.mp3"
    show Haruhi Pout1 Bright at left
    show field at left with dissolve
    pause .1
    hide field at left with dissolve
    show Haruhi Pout1 at left with dissolve
    "\"Right, right,\" she mumbled, reactivating the circle of light."
    show Haruhi Quest1 at left
    "\"So, what's so great about this if she can just turn it off, anyway?\""
    nvl clear
    show Kyon Ser1 at right
    play sound "SE/SaberOn.mp3"
    "\"It's a barrier and emergency help function,\" he answered, reactivating the beam saber and reassuming a defensive stance."
    show Kyon Ser2 at right
    "\"Unless she seals this space off —{w=0.5} again — {w=0.5}she can't disable it.\""
    nvl clear
    hide Kyon 
    hide Haruhi
    hide Skinsuit
    hide Coat
    scene bg roofclose
    show Asakura Sigh1 at center with wipeup
    "Asakura gave a pained sigh as she stepped through the jagged distortion between her controlled dataspace and the rooftop. "
    show Asakura Frown2 at center
    "\"You shouldn't be able to manipulate data like that,\" she said reprovingly."
    show Asakura Smile2 at center
    "\"I suppose that means it's time to stop holding back.\""
    nvl clear
    show Knife1 at center
    play sound "SE/clink.mp3"
    play sound "SE/clink.mp3"
    pause (0.3)
    show Knife2 at center
    play sound "SE/clink.mp3"
    play sound "SE/clink.mp3"
    pause (0.3)
    show Knife3 at center
    play sound "SE/clink.mp3"
    play sound "SE/clink.mp3"
    pause (0.8)
    play sound "SE/DunDun.mp3"
    show Asakura Smile3 at center
    "She clapped her hands together before her and drew them apart, flinging a fan of dozens of identical knives outward."
    hide Asakura
    play sound "SE/lowswoosh.mp3"
    scene black with fade
    show knifethrow with moveinleft
    scene bg roof with fade
    show Kyon Ang1 at right
    show Skinsuit at right
    show Coat at right    
    "Kyon maintained his guard position, his free hand already clenched into a fist, the metal ridges of his skinsuit facing outward."
    nvl clear
    play sound "SE/Barrier1.mp3"
    show BarrierSmall at HalfRight with dissolve
    pause 0.5
    show BarrierSmall Bright at HalfRight
    play sound "SE/block.mp3"
    pause (0.1)
    show BarrierSmall at HalfRight
    pause (0.1)
    show BarrierSmall Bright at HalfRight
    play sound "SE/block.mp3"
    pause (0.1)
    show BarrierSmall at HalfRight
    pause (0.1)
    show BarrierSmall Bright at HalfRight
    play sound "SE/block.mp3"
    pause (0.1)
    show BarrierSmall at HalfRight
    pause (0.1)
    show BarrierSmall Bright at HalfRight
    play sound "SE/block.mp3"
    pause (0.1)
    show BarrierSmall at HalfRight
    pause (0.1)
    show BarrierSmall at HalfRight
    pause (0.1)
    show BarrierSmall Bright at HalfRight
    play sound "SE/block.mp3"
    pause (0.1)
    show BarrierSmall at HalfRight
    pause (0.1)
    show BarrierSmall at HalfRight
    pause (0.1)
    show BarrierSmall Bright at HalfRight
    play sound "SE/block.mp3"
    pause (0.1)
    show BarrierSmall at HalfRight
    pause (0.1)
    play sound "SE/GlassBreak3.mp3"
    hide BarrierSmall with dissolve
    "The knives adjusted their course, most homing in on him to suddenly be halted by a semi-circular barrier of glowing blue force before shattering into nothingness, but a handful stopping suddenly in the space over the circle around Haruhi."
    nvl clear
    play sound "SE/lowswoosh.mp3"
    show Asakura Smile3 at left
    show Asakura Smile3:
        xalign 0.0 yalign 1.0
        linear 0.1 xalign 0.6
    show Kyon Pain1 at right
    pause (0.1)
    play sound "SE/slash2.mp3"
    "He opened his mouth to retort, but Asakura was already within his guard, driving yet another blade into his stomach."
    scene bg roofright
    play sound "SE/lowswoosh.mp3"
    pause (0.1)
    show Kyon Pain1 at KyonRightFast
    show Skinsuit at KyonRightFast
    show Coat at KyonRightFast
    pause (0.1)
    play sound "SE/touhoudead.wav"
    hide Kyon
    hide Skinsuit
    hide Coat
    "The inner carbon-nano-weave of the greatcoat and the force field of the skinsuit beneath it converted the stabbing force into a distributed shock wave, so instead of being pierced, Kyon was merely hit with the force of a speeding minivan, flying clear across the roof with a choked grunt."
    nvl clear
    scene bg roof
    show Asakura Smile1 at right
    "\"In the end,\" Asakura remarked, watching his form tumble off the edge of the school building,{fast} \"all those toys are pretty silly if you don't actually know how to use them.\""
    show Haruhi Hap1 at left
    "\"You have to give him credit, though,\" Haruhi said, peering very closely at the knives frozen over her barrier, not even glancing back to where Kyon had vanished."
    show Haruhi Grin1 at left
    "\"He comes up with one hell of a distraction ploy, doesn't he?\""
    nvl clear
    show Asakura Sup1 at right
    "The blue-haired interface cocked her head to one side, blinking."
    stop music fadeout 1
    "\"What?\""
    nvl clear
    hide Haruhi
    hide Asakura
    scene bg roofsky with fade
    play music "SE/lowwind.mp3" 
    "The sensation of being hit with a force that would crush a mid-sized car into a work of modern art was not entirely new, but was without a doubt extremely unpleasant."
    "His skinsuit did what it could to distribute the kinetic force evenly across his body, so the crushing pain was at least perfectly uniform in infliction."
    "The balancing gizmos gave up the ghost on keeping him upright, and struggled to guarantee he wouldn't land wherever he flew head-first."
    "His gravity manipulation defenses all strained to bleed the inertia of his impact off without even {i}more{/i} pain, but the end result was that he didn't slow appreciably until after he passed the edge of the five story rooftop."
    nvl clear
    "Not what he'd hoped for by a long shot."
    "All of the \"toys\" would keep him mobile, even if he was afraid he'd need to be {i}poured{/i} out of the skinsuit when it was over."
    "He'd have to beg Nagato or Haruhi to help him out and repair things later, but there was just too damn much to keep track of with all the attack vectors, defensive capabilities...."
    "\"It started off such a nice day, too,\" he mumbled, as his forward momentum was arrested and he began the downward plummet in earnest."
    nvl clear
    "How had it come to this, anyway...?"
    stop music fadeout 1
    nvl clear
    scene black with dissolve
    "Dev note: In the story this switches to the past, with Kyon going to meet Yuki. In the interest of asset re-use though, I'm focusing on finishing the fight scene. - Oroboro"
    nvl clear
    scene bg roofclose with fade
    show Asakura Sup1 at center
    "\"Hmm,\" Ryouko mused, turning slowly around, to where her sealed space in the stairway had been breached."
    show Asakura Frown1 at center
    "\"It was broken from the outside, somehow? I wonder—\""
    nvl clear
    play music "Music/Justice.ogg"
    play sound "SE/Barrier2.mp3"
    play sound2 "SE/Laser1.mp3"
    scene bg BeamOrange1 with flashbulb
    "The shrill buzz of a brilliant energy beam licked out from the roof of the tiny structure that housed the stairwell."
    show Asakura Pain1 at center
    "Ryouko was struck in the chest dead-center of mass, her entire body glowing white for a second before she staggered—"
    play sound "SE/Laser1.mp3"
    play sound2 "SE/Barrier1.mp3"
    scene bg BeamOrange2
    show Asakura Pain2 Bright at center
    with flashbulb
    "Instantly another beam shot out from the same location, lighting slightly to one side, near the girl's left shoulder."
    nvl clear
    play sound "SE/Laser1.mp3"
    play sound2 "SE/Slash3.mp3"
    scene bg BeamOrange4
    show Asakura Pain2 Bright at center
    with flashbulb
    "A third, though not as brightly glowing shot was somewhat lower, near her stomach, {nw}"
    scene bg roofclose
    show Asakura Unhap1
    play sound "SE/impact.mp3"
    with dissolve
    extend "and Ryouko dropped to her knees, eyes widened."
    "\"High yield neutron flare?\" she asked. \"Quantum entanglement to disrupt my connection....\""
    scene bg roofright
    pause (0.01)
    play sound "SE/CloakOff.mp3"
    show Kyon Ser1 at right
    show Skinsuit at right
    show Coat at right
    with coatin
    "De-stealthing, Kyon stood from his hiding place atop the stairwell housing, his greatcoat billowing behind him."
    nvl clear
    "The end of his weapon was glowing orange with discharge, the shape changed from a simple cylinder to a much thinner meter-long construction of sturdy rails and curving hand guards."
    "He slung it over his shoulder and ignored it, pulling the second cylinder from his coat and leaping the twenty meter distance between himself and Ryouko."
    play sound "SE/lowswoosh.mp3"
    scene bg roofclose with wiperightfast
    nvl clear
    show Asakura Unhap1 at center
    pause (0.3)
    play sound "SE/guncock.mp3"
    "Beneath him, a widening circle of dust marked where he leapt from, and while in midair he flipped over, a sequence of touch-points converting the unadorned cylinder into a stocky, blunt, two-handed gun."
    play sound "SE/netlaunch.mp3"
    pause (1)
    play sound "SE/stake1.mp3"
    show Spike1 at center
    pause (0.1)
    play sound "SE/stake2.mp3"
    show Spike2 at center
    pause (0.1)
    play sound "SE/stake3.mp3"
    show Spike3 at center
    pause (0.1)
    play sound "SE/stake1.mp3"
    show Spike4 at center
    pause (0.5)
    hide Spike1
    hide Spike2
    hide Spike3
    hide Spike4
    show Spike5 at center
    play sound "SE/elec1.mp3"
    "It fired with a rasping cough, launching a ring of metallic spikes to burrow into the rooftop around Ryouko, and then a grid of crackling brissant energy raked between each of the spikes, snaring the girl in a glowing, shuddering net."
    nvl clear
    "\"Ah,\" she said, her voice disappointed as Kyon's repulsor and gravimetric systems flared his momentum and spread it evenly across the entire rooftop, landing him near Haruhi, at Ryouko's side."
    show Asakura Sigh1 at center
    "\"I failed again.\""
    nvl clear
    hide Asakura
    hide Spike5
    scene bg roof
    show Haruhi Ang1 at left   
    "\"Is that going to hurt her?\" Haruhi asked, crossing her arms over her chest and raising an eyebrow at Kyon in concern."
    show Kyon Ser2 at right
    show Skinsuit at right
    show Coat at right
    nvl clear
    "\"Hurt her?\" he asked, somewhat indignantly."
    show Kyon Ang1 at right
    "\"Haruhi, she's tried to kill me. Three times, now, and you just saw one of them! Your primary concern is that I not hurt her?\""
    show Kyon Sigh1 at right
    play sound "Guncock.mp3"
    "He muttered to himself beneath his breath, folding away his firearm into storage."
    nvl clear
    show Haruhi Ang3 at left
    nvl clear
    "Haruhi tapped a toe impatiently, still staring at him."
    show Kyon Neutral1 at right
    "Pulling a phone identical to the one Haruhi was holding from one pocket, he punched a key. \"Nagato should be here shortly,\" he added, shaking his head."
    show Kyon Ser1 at right
    nvl clear
    "\"This is all up to you. I already know you'll take care of things just fine.\""
    show Haruhi Hap4 at left
    "\"Yes!\" she said, pumping one fist in the air. \"I get to do something! "
    show Haruhi Hap1 at left
    extend "Hey, how's the future?\""
    nvl clear
    show Kyon Sigh1 at right
    "\"It's awesome,\" he said, annoyed. "
    show Kyon Ser2 at right
    extend "\"Try and have some pity for the me that nearly got murdered off a building, huh?"
    show Kyon Neutral1 at right
    "\"Anyway, just so you know, she's programmed to try and kill me; she won't do anything to you.\""
    nvl clear
    show Kyon Neutral2 at right
    "\"And you won't see me tomorrow at school, because I'm going to be ... well. You'll find out.\""
    show Haruhi Pout1 at left
    "\"Okay,\" she agreed, frowning. "
    show Haruhi Quest1 at left
    extend "\"But, hey, why aren't you going to be around?\""
    nvl clear
    show Kyon Ser1 at right
    "\"Further information is not available here,\" he warned, shaking his head."
    show Kyon Smile1 at right
    "\"Now, when you see that other me, tell him I said 'hi', like I always do.\""
    show Kyon Ser1 at right
    "He paused before glancing at his phone again with a grimace."
    play sound "SE/CloakOn.mp3"
    hide Kyon
    hide Skinsuit
    hide Coat
    with coatout
    "\"My time's up,\" he announced, re-engaging his stealth field and vanishing from sight."
    stop music fadeout 1
    nvl clear
    scene bg roofclose
    show Asakura Sup1 at center
    show Spike5 at center
    "\"What?\"Ryouko asked, still trapped in the containment field. "
    show Asakura Smile3 at center
    extend "\"He just abandoned me here with you?\""
    play music "Music/NagatoTheme.mp3"
    scene bg roofright
    pause (0.5)
    play sound "SE/impact.mp3"
    show Kyon Pain1 at right
    show Skinsuit at right
    show Coat at right
    with wipeup
    "\"Damn it,\" Kyon groaned, from where he was just climbing over the edge of the building, breathing hard. "
    show Kyon Sigh1 at right
    extend "\"I hate when I have to rely on time-travel to take care of things.\""
    nvl clear
    scene bg roof
    show Haruhi Hap1 at left
    "\"Oh!\" Haruhi said cheerfully. \"Future-you says 'hi', like always!\""
    scene bg roofright
    show Kyon Sigh2 at right
    show Skinsuit at right
    show Coat at right
    "\"Yeah? That guy always annoys me. Probably almost as much as I'm annoyed by having to save past-me.\""
    nvl clear
    scene bg roof
    show Haruhi Hap1 at left
    pause (0.5)
    play sound "SE/Barrier1.mp3"
    show Yuki EyesClosed Bright  at center
    show field at center
    with flashbulb
    show Yuki EyesClosed at center
    hide field with dissolve
    "There was a flash of light and a warping of space, and then Nagato appeared at Haruhi's side."
    show Yuki Side1 at center
    "The circle of illumination around Haruhi's feet had vanished."
    scene bg roofclose with wipeup
    show Asakura Sigh1 at center
    show Spike5 at center
    show Yuki Side1 at HalfLeft with moveinleft
    "While Nagato knelt to examine Ryouko, Haruhi dashed to Kyon's side and helped him stand."
    nvl clear
    scene bg roofright
    show Kyon Pain2 at right
    show Skinsuit at right
    show Coat at right
    show Haruhi Worry1 at center with moveinleft
    "\"How bad was it, anyway? Future-you seemed to think you weren't very tough, and that you were hurt pretty badly.\""
    show Kyon Pain1 at right
    "\"I think I've got some internal bleeding,\" he said, wincing, one hand pressed to his abdomen. "
    show Kyon Pain2 at right
    extend "\"And some of my gear is messed up from the impact and overload. While this is fun for you, I wouldn't mind some medical assistance.\""
    nvl clear
    show Haruhi Hap3 at center
    "\"Sure!\" she said cheerfully, clapping one hand on his shoulder. "
    play sound "SE/impact.mp3"
    show Kyon Pain1 at right
    extend "\"Happy, healing, all-better thoughts!\""
    scene bg roofclose
    show Asakura Sigh1 at center
    show Spike5 at center
    show Yuki Talk1 at HalfLeft
    "\"Medical program loaded,\"Nagato added helpfully from where she was studying the other interface. "
    show Yuki Talk2 at HalfLeft
    extend "\"Permission to proceed?\""
    scene bg roofright
    show Kyon Pain1 at right
    show Skinsuit at right
    show Coat at right
    show Haruhi Worry1 at center
    "\"Granted.\" Kyon said, {nw}"
    play sound "SE/heal1.wav"
    show field at right
    show Kyon Ser2 Bright at right
    show Skinsuit Bright at right
    show Coat Bright at right
    with dissolve
    pause .1
    hide field at right
    show Kyon Sigh2 at right
    show Skinsuit at right
    show Coat at right
    with dissolve
    extend "straightening up as a sparkle of green and white lights suffused up from the rooftop beneath him, flowing through his body and undoing the damage."
    nvl clear
    show Kyon Smile1 at right
    "\"Oh, that feels so much better! Thank you; that probably saved my life.\""
    show Kyon Neutral2 at right
    "\"And for future reference, you can probably assume that I'm okay with that one being used.\""
    "\"Acknowledged,\" Nagato agreed."
    nvl clear
    show Haruhi Smile2 at left with move
    "\"Hmm, hey, Kyon, you know, you're going to have to really step up your game,\" Haruhi said suddenly, tossing his cell phone back to him."
    show Kyon Ser1 at right
    play sound "SE/woosh.mp3"
    hide Skinsuit with wipedown
    play sound "SE/CloakOn.mp3"
    hide Coat with coatout
    "He scowled, pocketed it, and then banished all of his equipment, the greatcoat taking the longest to phase out of view."
    show Kyon Ser2 at right
    "\"What's that supposed to mean?\" he asked in irritation."
    nvl clear
    show Haruhi Sigh1 at left
    "\"Well, this is fun and all, but you can hardly expect me to take your lectures on using power responsibly seriously when you're always relying on your future self to save you,\"she warned, raising one finger and waggling it at him."
    show Kyon Sigh2 at right
    "\'He sighed and hung his head. \"You know, I really am trying my hardest,\""
    show Kyon Worry1 at right
    show Haruhi Worry1 at left
    extend " he muttered, crossing his arms over his chest and looking away towards the sea."
    nvl clear
    show Kyon Ser1 at right
    "\"But I can't just leave you alone, and Nagato can't handle another interface right now.\""
    scene bg roofclose
    show Asakura Smile2  at center
    show Spike5 at center
    show Yuki Side1 at HalfLeft
    "\"And you did such a great job!\" Ryouko encouraged from beneath her energy net."
    show Asakura Smile1 at center
    "\"Time travel, is it? Now that's one tool you seem to know how to use well.\""
    nvl clear
    show Yuki Talk1 at HalfLeft
    "\"It's fine,\" Nagato said tonelessly."
    show Yuki Talk2 at HalfLeft
    "\"Asakura Ryouko is isolated and confined; she is limited to her organic functions at this moment.\""
    show Yuki Talk1 at HalfLeft
    "\"After she is dispatched, I will retrieve defenses to protect against further interference.\""
    nvl clear
    scene bg roofright
    show Haruhi Sup1 at left
    show Kyon Ser1 at right
    "\"Waaaait!\" Haruhi yelled, stomping one foot and spinning to face Yuki."
    show Haruhi Ang2 at left
    "\"Dispatched'? I don't think so! If you need something from her, there's got to be a way to do it without killing her!\""
    show Haruhi Ang1 at left
    "\'What's the point of running into another alien, just to kill them?\""
    nvl clear
    show Kyon Sigh1 at right
    "\"But the fighting is fine,\" Kyon observed, stretching his arms above his head, then swiveling his hips and stretching his spine out."
    show Kyon Ang1 at right
    "\"After all, no one of any importance was smashed off a building.\""
    show Haruhi Eyeroll1 at left
    "\'Kyon!\""
    show Kyon Sigh2 at right
    "\'Alright,\" he said, shaking his head."
    nvl clear
    show Kyon Ser1 at right
    "\"I don't really want Asakura to die either. But if her body were destroyed, she'd just go back to the place she came from.\""
    show Kyon Worry1 at right
    "\"At least, as I understand it.\" He shot a questioning glance towards Nagato."
    nvl clear
    "She didn't meet his eyes."
    nvl clear
    show Haruhi Hap1 at left
    "\"Good!\" Haruhi nodded decisively, grinning again."
    show Haruhi Smile3 at left
    "\'Yuki, let's come up with a backup plan. Something that will let you get your power-up and let us reform Ryouko. Can we do that?\""
    scene bg roofclose
    show Asakura Frown1  at center
    show Spike5 at center
    show Yuki Side1 at HalfLeft
    "Nagato stared intently at Ryouko, then gave a decisive nod. "
    show Yuki Talk1 at HalfLeft
    extend "\"Awaiting program,\" she announced."
    nvl clear
    show Haruhi Ang3 at left with moveinleft
    show Kyon Ser1 at right with moveinright
    show Yuki Side1
    "\"Hmm,\" Haruhi mused, narrowing her eyes and peering intently at Ryouko, who merely watched back curiously."
    show Haruhi Ang2 at left
    "\"Um ... some kind of second chance ... a chance to start over, prove herself, and ... let's see, realize she doesn't want to kill Kyon at all.\""
    nvl clear
    show Haruhi Smile2 at left
    "\"And she gets to give Yuki what she needs to make her equal to the next interface that comes along.... But no brainwashing, that's not cool.\""
    show Haruhi Smile3 at left
    "\"So, maybe an 'evil' module or something like that, which Yuki can purify and use for good, letting Ryouko learn how to become a nicer person?\""
    nvl clear
    show Haruhi Hap3 at left
    "\"Yeah! That sounds very good! Let's do that.\""
    nvl clear
    show Asakura Frown3 at center
    pause (0.4)
    show Asakura Frown1 at center
    "The pinned interface blinked several times, then turned her eyes to Kyon from beneath the glowing energy net."
    show Asakura Frown2 at center
    "\"None of this has been reported to my superiors,\" she commented."
    show Asakura Smile2 at center
    "\"It's entirely possible that this new knowledge could change their perceptions; there's no reason to be hasty!\""
    nvl clear
    show Yuki Talk1 at HalfLeft
    "\'Program loaded,\" Nagato replied."
    show Yuki Talk2 at HalfLeft
    "\'Permission to proceed?\""
    nvl clear
    show Asakura Pain1 at center
    "\'We can be reasonable!\ Ryouko protested."
    show Kyon Sigh1 at right
    "\"You're probably the most reasonable person I've ever had try to kill me,\" Kyon agreed."
    show Kyon Ang1 at right
    "\"But I remember that time you did stab me all too well.\""
    show Haruhi Ang1 at left
    "\"No stabbing!\" Haruhi said in a chastising tone. "
    show Haruhi Ang2 at left
    extend "\"Bad Ryouko! No class rep votes for you!\""
    nvl clear
    show Kyon Neutral1 at right
    "\"...you don't really think that's her prime concern, do you? Aside from which, did you even vote last time?\""
    show Asakura Frown1 at center
    "\"It isn't,\" Ryouko agreed. \"And no, she didn't. "
    show Asakura Smile2 at center
    extend "But, about being reasonable...\""
    show Kyon Puzzle1 at right
    "\"Anything that I should know about this program, Nagato?\" Kyon asked, quirking one eyebrow higher."
    nvl clear
    show Yuki Talk1 at HalfLeft
    "\"It will be beneficial to all involved,\" Nagato assured him, while Haruhi nodded knowingly."
    show Kyon Sigh2 at right
    "\"Okay,\" he sighed, shaking his head."
    show Kyon Ser1 at right
    "\"Granted.\""
    nvl clear
    show Yuki Side2 at HalfLeft
    "The smaller girl turned her gaze back to Ryouko's bound form, the faintest hint of a smile coming to her lips."
    nvl clear
    scene black
    stop music
    "\"I will not let you harm him again.\""
    
    
    
