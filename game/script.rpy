# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    persistent.confessions = 0
    persistent.last_confess = []
    persistent.endings = []
    persistent.tw = True

define dis = { "master" : Dissolve(0.5) }

define a = "Anton"
define pc = "You"
define s = "???"
define m = "Marlen"


# The game starts here.

label start:

    if persistent.tw:
        "Trigger Warning: blood, gore, violence (specifically only bad endings so u should be fine)"
        "do you wanna disable this warning for future playthroughs (AKA CLOSING THE GAME RESETS UR PROGRESS TWIN)"
        menu:
            "yESSIR":
                $persistent.tw = False
            "AWH HELL NAH":
                $persistent.tw = True
        "Also make sure to keep the game open while playing over and over to unlock certain endings !!"

    with Dissolve(1)
    scene bg cork wall

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.


    "You find yourself standing to a tall cork wall, thumbtacks embedded into it with red string woven around each base. You watch your associates pile into the room slowly, single file, muttering as they enter."
    "All chatter stops as you knock on the hard surface of the board."

    pc "Attention."

    "Your lips purse as the words form in your head, lips late to catching up with your thoughts."

    pc "He's struck again."

    "The immediate silence that follows is nothing short of chilling. It's been three months since the [s] had brought a halt to his crimes. However, it seems to have been extremely short-lived as he's back on the rise."

    pc "The victim is aged 24, female, identified as Annalisse Intar."
    
    show a neutral
    with dis

    "You specifically point to a photo of a quite happy, satisfied, blonde on the corkboard."

    hide a neutral
    with dis

    pc "Now, forensics has identified her primarily by the... teeth left at the scene where she was last seen. Aside from that, we have very little evidence."

    "Someone scoffs."

    s "As usual."
    
    "Someone immediately slaps the back of their head, grumbling."
    
    s "Shh--!"

    "You've been on this wild goose chase for a year now, you can't blame them. You too tire of this mundanity. But you've taken up the mantle because:"

    menu:
        "your boss told you to and you just want to get paid at this point...":
            jump bar
        "you want to see this horrid criminal brought to justice!":
            jump bar
        "you have the experience to do it right the first time. you're sure some other bumbling fool would fuck this up somehow.":
            jump bar

    label bar:

    "You sigh. Regardless of motive, you have little to no choice in this whole ordeal. He's a criminal, a murderer -- and you're a homicidal specialist detective."
    "And unfortunately, this makes it exclusively your job to handle this criminal and get him off the streets -- for good."

    "Some conclusions that you and the team (or specifically, your rookie) have come to are the following: he's likely a man between the ages of 25 and 30, relatively built (at the very least lean) to be able to incapacitate his victims,"
    "and very, {i} very {/i} skilled at what he does."
    "(Which is murder, if you're not sure.)"

    "The cruelties started a couple months into your latest hire, Anton, who had been directly trained under your guidance (in place of your boss), when the killer first emerged."
    "You had been working under this investigative force for a while, more of a special case detective rather than a consistent one."
    "Only extreme end cases are sent to you -- the completely mundane or the completely distressing. It's the efficacy in which you can handle both that lets other officers handle smaller investigations to fry the big fish..."
    "While you interview old ladies about purse muggers."
    "(Or catch serial killers.)"

    "But it's fine. You get paid enough to make up for the occasional stress and/or boredom."

    "Fortunately, that nuance is what lands you prime investigator of that criminal's folder. The only one to have a clear enough head and enough department history to lead the case, your boss claims."
    "Fuck your boss, is what you claim."
    pause.25
    "In your head."
    "Obviously."

    "Anton's young, about as young as you were when you first joined the force. A little wet behind the ears, but that's to be expected from his first year as detective."
    "Sure he's undergone bare minimum policing training and being a beat cop, but he trained at Delta..."

    "Your nose wrinkles at the very thought of Delta unit, stomach twisting as you do. You push it down, as that unfortunately led to you having to do supplemental teaching. Leave it to Delta Precinct to fuck up, as usual."

    show bg bar zoom1

    "The first case rolled around three months into Anton's successful integration to the team. You're off hours, having a drink, your arm casually wrapped around his back, grinning down at him as he offers a crooked, earnest smile back to you."
    "The rest of the team is toasting together, hell even Marlen is chiming in."
    "All of you receive a simultaneous, familiar chime on your phone -- save for Anton. You groan, frustrated. Anton's wary eyes meet yours, lips pursing in an unsaid question."

    "You chew on your lip. Do you tell him?"

    pc "It's... nothing."

    "You barely manage to blurt it out before Marlen derisively scoffs, turning to you with a soured and sordid look on his face."

    m "If nothing means some pain in the ass business in your books, Lawrence, then it's a whole bunch of nothing."
    "He grumbles, downing the last remnants of his tall glass of beer."

    "{i}What a roundabout way of saying I'm bullshitting him.{/i}"

    show bg bar 

    "You sigh, pulling yourself out of your chair. You eye the way Anton rises with you, following suit, even pulling his jacket on before your hand steadies him and pushes him back into his seat."

    pc "You're staying here. You're new, and we don't know what the hell the boss could be presenting."

    with Dissolve(.25)
    scene bg bar empty
    with Dissolve(.65)
    show a_pouto at center


    a "W-What?! Why can't I go?"

    show a_pout 

    "He stutter indignantly, affronted by the exclusionary practice."

    pc "Perch will stay with you." 
    
    "You glance over at one of the older, grayer members. He's stocky, onset eyes that lock with yours before sending over a slow nod in your direction. You pat Anton on the back, offering him a cautious grin."

    show a_worry
    
    pc "It's probably nothing, Anton. Don't fuss. Enjoy your night."

    "It was NOT nothing."

    "24 hours later, you're running on no sleep, leading a team of people you've known for either as long as five years or as little as three months trying to catch a violent, destructive murderer."
    "One victim is all you know of so far, but it's not long until your 'very professional' boss tells you that the corpse is HOW OLD-- and that there's probably MORE VICTIMS--"

    "Your hand sinks into your hands at your desk, waiting for the results of your database searches to finalize based off of what little information of the victim you have."


    "The only comfort you had, was what litle 'battery acid' you and Marlen snuck to the back to create. An amalgamation of coffee, sour candies, energy drinks, and a bit of sugar packets from the break room. It had lasted you pretty long, you'll admit."

    "But even that had ran out, much like your patience. Your eyes rove over to the now-empty cup, wistfully."

    "Maybe you should have gotten another drink at the pub. A stronger, alcholic one. Anything to make the strain of this stupid case dissipate."

    "Your head falls, nearly banging on the hard of your desk, vision blurring as you hear worried mutters from those around you. You're so... {b} so {/b} done."

    "It's the hesitant footfalls against the linoleum floor that slowly gets your attention of the white of your computer screen. The five dollar bill slipped under the cross of your arm renders you suddenly perking up."
    "Anton's firm and broad shoulders come into view, stiffening at the immediate reaction, pulled tight to avoid laughing as he slowly retracts the bill."

    a "Sorry, Sarge. You looked like you needed a pick-me-up."

    "Before you have any time to complain or interject or assure him you're fine (like a good superior), he slides you a mug of... something."

    a "Tea. It's chamomile."

    "He clarifies, pointedly looking away, as he awkwardly explains himself."
    
    a "Ah-- is it too rude of me to offer? I can take it away--"

    pc "You're fine."
    
    "You grin back at the gesture, basking in the warmth of the mug."
    menu:
        "Take a sip.":
            jump tea_sip

          #  menu:
          #  "Some people just... maybe need help, you suppose.":
          #  "Good fucking riddance.":
        "Don't drink it, but thank him.":
            jump tea_dont_sip

    
    label tea_sip:
    "You fall asleep promptly at your desk a couple minutes later. 6 hours later, you wake up to your own coat covering your shoulders. He should get a raise."
    "That morning, Anton had finished external research and networking, before presenting it with some information that just... clicks with what you were working on!"
    "You approach Marlen with this new evidence and ask if he could go with you on a stakeout later that day. He readily agrees, his wife having scolded him last night for his absence and he is ready to be done with this quick but cruel case."

    "Dusk arrives and the two of you are all but rushing out of the door, barely missing the forlorn look Anton shoots your way."
    "You both arrive on sight, just to see the suspect arguing with, what you assume is a business partner, before he pulls out what seems to be the {u}exact same weapon used on the victim {/u}!"
    "Marlen calls in backup before heading towards the man, hidden by the sunset cover. You support him from behind, trailing far enough to be able to step in, should he need it."

    "The takedown is swift and easy. Aside from the already-bloodied knife, coated in the previous victim's blood, the suspect (white, late 20s, jealous ex-boyfriend) practically breaks down and confesses everything in front of MArlen's body camera."

    "It's the weight of the blod on his hands that has him pleading guilty in front of the court, not even properly hiring a lawyer."

    label tea_dont_sip:
    "You make progress int he case, able to locate the original drop site of the murder, and luckily enough, you manage to find the weapon! It's a typical murder, stab and ditch."
    "You catch the guy (white, early-to-mid 30s, businessman with a grudge) and he's promptly sent to jail after he pleads guilty, feeling the weight of his crimes heavy on him."







    a "so... you come round here often?"

    a "or we're just balling with ts"

    


    # This ends the game.

    return
