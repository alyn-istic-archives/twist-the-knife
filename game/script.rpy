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
define protag = "Alyn"
define s = "???"
define m = "Marlen"

transform bounce:
    pause .2
    yoffset 0
    easein .175 yoffset -20
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0

transform shake:
    linear 0.175 xoffset -2
    linear 0.175 xoffset +0
    linear 0.175 yoffset -2
    linear 0.175 yoffset +0
    repeat


default preferences.text_cps = 45
default preferences.afm_enable = False
default nonmeat = False
default orphan = False
#police experience, police funds, police transfer
default p_exp = False
default p_fund = False
default p_tran = False
default f_nick = False
default f_rel = False

#snooper core
#living room/powder room
default lr = False
default pr = False
#super secret room
default ssroom = False
#room "items"
default couch = False
default coffee = False
default tv = False
default magazine = False
default soap = False
default toilet = False
default towel = False
default sink = False

#oooh sleeping with anton
default bed = False
default b_anton = False


# stats such as affection, suspicion, murder rate (how likely u r to die)

default a_s = 0
default a_mr = 0
default a_a = 0

image sweetpotatoes:
    "images/potato1.png"
    pause.3
    "images/potato2.png"
    pause.15
    "images/potato2.2.png"
    pause.15
    "images/potato3.png"
    pause.3
    "images/potato3.5.png"
    pause.2
    "images/potato4.png"
    pause.3
    repeat

image soup:
    "images/soup1.png"
    pause.3
    "images/soup2.png"
    pause.2
    "images/soup3.png"
    pause.3
    "images/soup4.png"
    pause.2
    repeat


image door:
    "images/door1.png"
    pause.3
    "images/door2.png"
    pause.2
    "images/door3.png"
    pause.15
    "images/door3.1.png"
    pause.1
    "images/door3.2.png"
    pause.1


# The game starts here.

label start:

    scene bg anton jump
    pause.5
    scene blackscreen with dis
    pause.5
    scene bg anton jump at shake
    pause.5
    scene bg anton jumpo at bounce
    pause.5
    scene bg anton jumpo at shake

    if persistent.tw:
        "Trigger Warning: blood, gore, violence (specifically only bad endings so u should be fine)"
        "do you wanna disable this warning for future playthroughs (AKA CLOSING THE GAME RESETS UR PROGRESS TWIN)"
        menu:
            "yESSIR":
                $persistent.tw = False
            "AWH HELL NAH":
                $persistent.tw = True
        "Also make sure to keep the game open while playing over and over to unlock certain endings !!"

    with dis
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

    "The immediate silence that follows is nothing short of chilling. It's been three months since the [s] had brought a halt to his crimes."
    "However, it seems to have been extremely short-lived as he's back on the rise."

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
        "Your boss told you to and you just want to get paid at this point...":
            $a_a+=1
            jump bar
        "You want to see this horrid criminal brought to justice!":
            $a_mr+=5
            jump bar
        "You have the experience to do it right the first time. You're sure some other bumbling fool would fuck this up somehow.":
            $a_a+=2
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
    with dis

    "This is in the past. Back when things were easier. You need this flashback so you don't lose your mind."

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

    with dis
    scene bg bar empty
    with Dissolve(.65)
    show ant pouto at center

    a "W-What?!{w=0.2} Why can't I go?"

    show ant pout 

    "He stutter indignantly, affronted by the exclusionary practice."

    pc "Perch will stay with you." 
    
    "You glance over at one of the older, grayer members. He's stocky, onset eyes that lock with yours before sending over a slow nod in your direction. You pat Anton on the back, offering him a cautious grin."

    show ant worry
    
    pc "It's probably nothing, Anton. Don't fuss. Enjoy your night."
    
label cont:

    scene bg desk 
    with Dissolve(0.5)

    "It was NOT nothing."

    "24 hours later, you're running on no sleep, leading a team of people you've known for either as long as five years or as little as three months trying to catch a violent,{w=0.2} destructive{w=0.2} murderer."
    "One victim is all you know of so far, but it's not long until your 'very professional' boss tells you that the corpse is HOW OLD-- and that there's probably MORE VICTIMS--"

    scene bg desk

    "And now you're back. In the present. With that stupid killer."

    "Your head sinks into your hands in your cubicle, awaiting for the results of your database searches to finalize based off of what little information of the victim you have."

    "The only comfort you had, was what litle 'battery acid' you and Marlen snuck to the back to create. An amalgamation of coffee, sour candies, energy drinks, and a bit of sugar packets from the break room. It had lasted you pretty long, you'll admit."
    
    hide item
    with dis
    show item empty mug

    "But even that had ran out, much like your patience. Your eyes rove over to the now-empty cup, wistfully."

    hide item with dis

    "Maybe you should have gotten another drink at the pub.{w=.2} A stronger, alcholic one. Anything to make the strain of this stupid case dissipate."

    scene bg slam desk with vpunch

    "Your head falls, nearly banging on the hard of your desk, vision blurring as you hear worried mutters from those around you. You're so... {b}so{/b} done."

    "It's the hesitant footfalls against the linoleum floor that slowly gets your attention of the white of your computer screen."
    
    show item freemoney
    
    "The five dollar bill slipped under the cross of your arm renders you suddenly perking up."

    hide item freemoney with vpunch

    scene bg desk

    "Anton's firm and broad shoulders come into view, stiffening at the immediate reaction, pulled tight to avoid laughing as he slowly retracts the bill."

    show ant worryo

    a "Sorry, Sarge. You looked like you needed a pick-me-up."

    show item mug with zoomin

    show ant fond

    "Before you have any time to complain or interject or assure him you're fine (like a good superior), he slides you a mug of... something."

    show ant worry

    a "Tea. It's chamomile."

    show ant pout

    "He clarifies, pointedly looking away, as he awkwardly explains himself."

    show ant worryo
    
    a "Ah-- is it too rude of me to offer? I can take it away--"

    show ant worry

    pc "You're fine."
    
    "You grin back at the gesture, basking in the warmth of the mug."
    menu:
        "(Take a sip.)":
            $a_a+=3
            hide item mug 
            show item tea mug
            "It's... good."
            show ant fond 
            show item empty mug with dis
            "Really good."
            hide item


            jump tea_sip

          #  menu:
          #  "Some people just... maybe need help, you suppose.":
          #  "Good fucking riddance.":
        "(Don't drink it, but thank him.)":
            $a_a+=2
            hide item with dis
            jump tea_dont_sip

    
    label tea_sip:
    

    scene bg slam desk with pixellate
    pause.2
    with zoomin

    "You fall asleep promptly at your desk a couple minutes later. 6 hours later, you wake up to your own coat covering your shoulders. He should get a raise."

    scene bg desk with dis

    "That morning, Anton had finished external research and networking, before presenting it with some information that just... clicks with what you were working on!"
    "You approach Marlen with this new evidence and ask if he could go with you on a stakeout later that day."
    "He readily agrees, his wife having scolded him last night for his absence and he is ready to be done with this quick but cruel case."

    scene night office bg with dis

    "Dusk arrives and the two of you are all but rushing out of the door, barely missing the forlorn look Anton shoots your way."
    "You both arrive on sight, just to see the suspect arguing with, what you assume is a business partner, before he pulls out what seems to be the {u}exact same weapon used on the victims {/u}!"
    "Marlen calls in backup before heading towards the man, hidden by the sunset cover. You support him from behind, trailing far enough to be able to step in, should he need it."

    "The takedown is swift and easy. Aside from the already-bloodied knife, coated in the previous victim's blood, the suspect (white, late 20s, jealous ex-boyfriend) practically breaks down and confesses everything in front of Marlen's body camera."

    "It's the weight of the blood on his hands that has him pleading guilty in front of the court, not even properly hiring a lawyer."
    "And he claims he couldn't stop killing? Because it became addictive? Uh...."
    "You don't get paid enough for this."
    
    jump dinner_inv

    label tea_dont_sip:
    
    hide ant worry
    "Hours pass just sat in front of your computer. Some of your coworkers check in on you."
    "It's really boring. You take several small power naps."
    pause.25
    "You scroll past another seemingly boring lead. Unless."
    
    pc "What--!" with vpunch
    
    "It's perfect."
    "Somehow this dead end is enough to locate the original drop site of the murder, and luckily enough, you manage to find the weapon! It's a typical murder, stab and ditch."
    show item knife
    "You catch the guy (white, early-to-mid 30s, businessman with a grudge) and he's promptly sent to jail after he pleads guilty, feeling the weight of his crimes heavy on him."
    hide item knife
    "Evidence shows he had a hit-list to take out by the end of the week. And he'd get paid--"
    
    "{cps=60}HOW MUCH-!!"with vpunch
    "Man, you would kill for that much too."
    jump dinner_inv

label dinner_inv:

    scene bg office doors
    with dis

    "You're finally clocking out of your shift. God forbid."
    "This case has been nothing but a pain in your ass these past couple days. Not weeks, thankfully. But you definitely could have seen it getting that extreme."

    "You're finally honing it to that far door, you're so close--"

    show ant worryo with hpunch
    
    a "Uh, hi boss?"

    show ant neutral

    "...Something in his hand smells... delicious. Goddamn it, you're starving."
    "And in record time, your stomach growls equally as loud. You've technically missed every word he's said since, but the growing smile on his face..."
    
    show ant grin
    "does NOT go unremarked."
    show ant grino

    a "You, uh, hungry, sarge?"
    show ant fond
    
    "He manages, a cheeky undertone pulling at his tired voice."
    pc "No."
    
    show ant neutralo
    a "Really now? I think something else disagrees."
    show ant grin

    "And if on cue, your stomach growls again. Sure, you had eaten earlier. {w=0.5} Earlier this week, at least."
    pc "What is it to you if I am? Are you offering to deal with it?"

    show ant grin
    pause.25
    show ant neutralo

    a "Sure! I usually make a mean pulled pork sandwich, or at least I have the leftovers here with me right now."
    a "But back at home, I've got like a large dinner set up for me and everything, if you'd like to join me!"

    show ant grin

    "That sounds... really good considering you don't have any food already prepped..."

    menu:
        "Hm. Sure.":
            menu:
                "Do you have any non-meat food? Meat's not a personal preference.":
                    $nonmeat = True
                    $a_mr = -100
                    #aka ur not dying any time soon
                    #not cause he hates you, but because like,, youre a vegan, you cna't eat humans
                    #vro draws the line at religion my chevre my beloved son  <3
                    show ant shocko
                    a "Oh!"
                    show ant worryo
                    a "Sorry, I didn't know that!{w} I don't have anything on me at the ready..."
                    show ant worry
                    pause.25
                    show ant shocko
                    a "I actually do!"
                    show ant grino
                    a "I was planning on a quaint meal tonight, nothing too heavy or anything. I'm so glad to have you join me!"
                    a "Appetizer, entree, dessert, etc. Except I'm not huge on dessert so it's another entree. If you don't mind."
                    show ant neutralo
                    a "I don't mind making some quick alternatives, but most of it is a little meat-heavy... But I've got alternatives, so don't you worry!"
                    jump car
                "Sounds great.":
                    jump car
        "No thanks.":
            pc "I'll pass tonight."
            "His smile falters, but he wishes you well."
            a "Ah, it's fine. I figured I'd just offer."
            "Neutral Ending: So you're no fun?"
            if "No Dinner For You :(" not in persistent.endings:
                $persistent.endings.append("No Dinner For You :(")
            return

label car:
    show ant grin
    pause.25
    show ant grino
    a "Fantastic! We'll take my car!"
    show ant neutral
    "Silently, you raise an eyebrow in his direction. He quickly scatters following up with his reasoning."
    show ant worryo
    a "Well, uhm, you look really tired, Sarge. You shouldn't be driving if you're that fatigued."
    a "Least I can do for you."
    a "If you don't mind..."
    show ant worry
    "You let out a grudging sigh. You've told him not to call you that before."
    show ant shocko
    pc "You can refer to me by name, Anton. {w=0.25} We're coworkers, not employer-employee."
    show ant worry
    pause.25
    show ant shyo
    a "I will if you let me drive you?"
    "..."

    scene bg car with Dissolve(0.5)
    show ant car1

    "The car ride isn't spectacular or anything, still on edge from spending countless nights at your desk. It's a couple moments later that you're hesitantly speaking up."

    menu:
        "So... Sandwiches, am I right?":
            $a_a+=1
            a "Yes! I love making them. They're easy to put together and they aren't anything to heavy. Something you can finish anywhere if need be!"
            a "Gotta be ready whenever on the job!"
            jump cont_car1
        "Multiple entrees... are quaint?":
            "He chuckles nervously."
            a "Is it not? I like to eat a lot, I'm afraid."
            a "I hope it's not something you mind?"
            menu:
                "Nah, I eat a lot too.":
                    $a_a+=2
                    "He beams back at you in full force."
                    a "Now here's someone who shares the same dedication I do!"
                    jump cont_car1
                "Um... it's whatever, I guess.":
                    $a_mr+=5
                    a "That's good."
                    "He hums to himself absentmindedly as the next song plays on the radio."
                    jump cont_car1
                "Big back ahhh":
                    $a_mr+=10
                    $a_s+=2
                    "Silence fills the air as his face freezes."
                    "Stiltedly, he coughs."
                    jump cont_car1
        "(I like the silence...)":
            jump cont_car

    label cont_car1:
        menu:
            "So. How have you been these past couple days?":
                $a_a+=1
                a "Ah, it's been a little rough."
                a "It's busy. The whole office was working. Really hard."
                a "I mean, not to imply you weren't too. "
                a "It was this whole thing. Everyone was scared, and tired, and mad."
                pc "Having a serial killer on the streets, will do that sometimes."
                a "Yeah. It just.{w=0.2} Feels odd."
                a "It feels like there's more to this whole thing. The guy didn't even confess to the rest of the murders."
                a "And the methodology doesn't line up either."
                "..."
                pc "It's... over. We shouldn't have to think more about it."
                "The air is tense. You can't tell if you've misspoken or if he had."
                "Something about his choice in words just unnerves you. Simple as that."
                jump cont_car
            "So where'd you learn to cook? Your parents?":
                $orphan = True
                "His arm stiffens, fingers curling around the steering wheel."
                "With a strained laugh, he manages to reply."
                a "I, uh, didn't have parents growing up."
                pc "Oh, I'm so sorry-"
                $a_a+=1
                a "No, it's fine.{w=0.2} Really."
                a "Even if I had, they wouldn't have been great."
                "Subconciously, you raise an eyebrow."
                a "Really. What most people consider family, I would've never had anyway."
                a "I learned to cook because I had to."
                a "Born of necessity, if you will."
                "Ah."
                jump cont_car
    
    label cont_car:
        "The rest of the ride is filled with a neutral silence, the brief humming of the car, and whatever was playing on the radio."
        "A couple minutes later, you pull up into the parking lot of a... house???"
        pc "What the..."
        "You're... flabbergasted."
        "He's what... 27 to 28? At most, 30?"
        "And he has... a wholeass HOUSE?"
        "Nah... This isn't real."

        "As if catching your flabbergasted stare with amusement, he parks the car before heading around and opening your door."
        a "It is my house. If you're that curious, why not come in and actually take a look, Sarge?"
        "You scoff at the endearment with a grin."
        pc "You know I'm not actually your work superior."
        "You make your way outside the car."
        pc "I just trained you cause the real boss asked me to instead."

label house_01:

    scene bg kitchen with dis

    "You follow him to the entrance of Anton's house. He fiddles with his keys, before the door swings open with little to no fanfare."
    "He has you put your shoes on a shoe rack and hang up your coat in the closet."
    "You awkwardly trail behind him as he gives you a quick introduction around his primary living space."

    show kitchen ant grino with dis

    "He tells you to get settled at the island bar as you watch him get to cooking. Grinning, he boasts, tying the apron around his waist."
    a "I promise that everything I'm gonna serve is gonna be like nothing you've ever had before."
    "He pauses."
    a "Well, there's a good chance it'll be something you've had before. But better!"

    menu:
        "(Watch him make the first course.)":
            $a_a+=1
            if nonmeat:
                jump vegancourse01
            else:
                jump course01
        "(Take a look around from where you're sitting.)":
            $a_mr+=5
            $a_s+=1
            "It's not like you were expecting much. But still."
            "His house is a lot more bare bones than you were expecting it to be."
            "It lacks... emotion. Wherever you look, it's hard to find a trace of, well, Anton."
            "No personal or family photos, no evidence that the house is really lived in."
            jump serve01
        

label course01:
    "You watch him pull a bowl of... buttermilk(?) out of the fridge."
    show kitchen ant grin
    "And there it was in front of you."
    "...?"
    pc "Is that... actually, no, what is that?"
    show kitchen ant grino
    a "Gizzard! Have you heard of it before?"
    "This didn't answer any questions. This actually gave you more questions."
    menu:
        "Um... no.":
            jump what_gizzard
        "Yeah, it seems pretty cool!":
            $a_a+=1
            show kitchen ant shocko
            a "Really now? I don't think I've met a lot of people who know what it is!"
            show kitchen ant grino
            a "That's super cool!"
            jump yes_gizzard
        "Um, ew, unfortunately. And you think I'm eating that?":
            jump no_gizzard

    label what_gizzard:
        show kitchen ant fond
        pc "What's gizzard?"
        show kitchen ant neutralo
        a "Well, I don't actually have a real definition for you. But it's part of the chicken's stomach!"
        show kitchen ant grino
        a "It also tastes really similar to other dark meat!"
        a "And if you know what giblets are, they're part of that sub-group."
        show kitchen ant fond
        "You subtly grab your phone and type in gizzards and giblets into your search bar."
        "Giblets... Giblets are... edible internal organs? And gizzards happen to be those. So... gizzards are uysed to grind the food of chickens? They're muscles?"
        pc "Why do chickens need to grind their food."
        show kitchen ant neutralo
        a "They don't have teeth. I guess their beaks don't do all of that."
        show kitchen ant neutral
        pc "So, uh, why's it soaking in all that?"
        show kitchen ant neutralo
        a "Well, I'm guessing it said something about the gizzards being a muscle. And usually, muscles don't have the best texture."
        a "Buttermilk has acidic properties that let it break those muscle fibers."
        show kitchen ant grino
        a "It also tenderizes the meat!"
        show kitchen ant fondo
        a "I let these guys sit for about 20 hours to tenderize them. I could slow cook them, but I prefer to have something already ready to cook when I get home."
        show kitchen ant worry
        pc "Especially with that psycho on the loose."
        show kitchen ant fondo
        a "Correction, having *been* on the loose. Off the streets now, thank god."
        show kitchen ant neutral
        jump yes_gizzard

    label yes_gizzard:
        show kitchen ant neutral
        "He moves aside, preparing two bowls of a beaten egg mixture and another bowl that he adds flour, salt, garlic and onion powder, and some paprika to."
        "Generously, he coats each individual piece in the egg wash and then the flour."
        "His hands stiffen in the bowl, as if remembering a question."
        show kitchen ant worryo
        a "Oh. Sorry, does the idea of eating these bother you?"
        menu:
            "A little...":
                a "I can offer you something else to eat then! I have a more... vegan course prepared if you'd like?"
                "He... hadn't known you were coming. How would he have prepared all that?"
                menu:
                    "Yeah, I'd rather that.":
                        show kitchen ant fond
                        a "Yeah. Yeah, of course!"
                        show kitchen ant neutral
                        "He quickly washes his hands, moving to put the gizzard in the fridge and bringing out a different bowl."
                        "Water sloshes around the rim as you lean in."
                        jump vegancourse01
                    "Oh, no, it's fine.":
                        jump yay_gizzard
            "Not at all!":
                $a_a+=3
                jump yay_gizzard
        label yay_gizzard:
        show kitchen ant worry
        "Something about the sudden assumption makes you feel a bit defensive."
        "Your hands raise up to your shoulders in defense. It's not as if you cared that much."
        pc "It doesn't bother me! Really!"
        show kitchen ant fond 
        "His shoulders relax at the assurance."
        show kitchen ant fondo
        a "As long as you're sure. I wouldn't want to scare away my guest now."
        show kitchen ant fond
        "Silence follows the end of the conversation as Anton begins frying the gizzard pieces in the oil expertly."
        with dis
        jump serve01

    label no_gizzard:
        $a_a-=2
        $a_mr+=10
        show kitchen ant angry
        "He winces at your tone and diction. If almost wounded by your harshness."
        show kitchen ant worryo
        a "Ouch, alright, I get it."
        show kitchen ant neutralo
        a "I can prepare you something else."
        jump vserve01

label vegancourse01:
        show sweetpotatoes
        "It's... sweet potatoes? They look fairly fresh and they've already been peeled."
        "He begins cutting them into cubes, hands nimble before he looks back up at you."
        a "Do you like sweet potatoes?"
        menu:
            "Well, if you didn't you're eating them now.":
                pc "Uh... I like them enough!"
                a "Ahh, sorry. I'll remember for next time."
                "...?"
                "There's going to be a next time?"
                "Ambitious, you guess."
            "Yes!":
                pc "I love sweet potatoes. Really delicious. And like the name suggests, sweet."
                a "Fantastic!"
        "It's not really a moment later until he's quickly scribbling something down on a sheet of paper."
        a "Here's the line-up for tonight. I figured I should give you a heads-up on what you're eating!"
        "Appetizer - Cubed Sweet Potato."
        "First Course - Tomato Soup with a side of Garlic Bread."
        "Palate Cleanser - Tea Time | Wine and Dine."
        "Entree - Tofu Tomahawk."
        menu:
            "This isn't as... professional as you made it sound.":
                a "I'm just a man! Not a three-star Michelin chef."
                jump vc1cont
            "This sounds... delicious!":
                $a_a+=2
                a "Thank you! I try my best to make meals I'll enjoy and ones that actually feed me well enough!"
                jump vc1cont
            "Anton, what is a tomahawk.":
                a "A tomahawk is a type of steak! So it's moreso just a tofu steak."
                a "Specifically a ribeye cut!"
                a "Gots lot of marbling, tenderness, and flavor. Delicious."
                pause.25
                a "But yours is completely tofu, don't worry."
                if not nonmeat:
                    a "I know you just changed from the gizzard, but the whole menu changes if you change the gizzard. Sorry."

        label vc1cont:
        scene bg kitchen with dis
        "He pours the cubes all into a pot, letting it boil on the stove for 4-10 minutes before letting them cool and drying them gently."
        "The potatoes are all lumped into one bowl of oil and spices, shaken around until even coating."
        "Anton makes quick work of the sweet potatoes, expertly frying them in the built-in deep fryer (?!!?!) in his kitchen before he grabs a seperate package from his fridge."
        menu:
            "What's that?":
                "His body stiffens before he awkwardly chuckles."
                a "I'm just preferential to meat. Sorry."
                if not nonmeat:
                    a "Sweet potatoes and gizzards can taste great together, but I prefer red meat over white in this case."
                    a "Plus, you aren't huge on the gizzards, I won't make you uncomfortable like that."
                "He carefully peels a thin sheet of red out of the package."
                a "It's wonderfully marbled beef. And nothing tastes better than fried beef."
                "He grins sheepishly, before apologizing."
                if not nonmeat:
                    a "Sorry, I didn't tell you this was another option. But I don't think I have enough for two servings of beef anyway."
                if nonmeat:
                    a "I know it's not your thing but I hope you don't mind."
                    pc "As long as you aren't feeding it to me."
                    a "What?! I would never do that!"
                    "It's an immediate knee-jerk response, as if he's almost hurt at the suggestion."
                    pc "Ahaha... I was just. Joking."
                    a "Oh. Sorry. I would never feed someone something they aren't comfortable without asking first!"
                    a "You just scared me, that's all."
                pc "Eh. It's fine, don't stress too much."
                jump serve01
            "How do you know when to take them out of the fryer?":
                a "Huh?"
                a "Oh, you mean the food?"
                a "It's pretty easy for the sweet potatoes."
                a "You just wait between 10-14 minutes depending on how crispy (or burnt) you want them to be."
                a "Or you keep an eye on the colour if you're panfrying them! {w=0.2} For about 7-10 minutes though.    "
                pc "Hmm... Sounds a bit more easy than you make it look."
                a "I do tend to do that."
                jump serve01

label vserve01:
    scene bg kitchen with dis
    show kitchen ant neutral
    "Everything is done quickly, with a subtle layer of quiet finesse to it. You're not sure how often he cooks for himself."
    "But his apparent talent is clear."
    "He gestures to his dining table as you watch him clean the cutting boards, washing them under running water."
    show kitchen ant neutralo
    a "You can go make yourself comfortable if you'd like?"
    show kitchen ant grin
    menu:
        "Oh. Yeah, sure.":
            $a_a+=2
            show kitchen ant grino
            a "Alright, the table should already be set and everything!"
            jump vserve1cont
        "Can I do anything to help you with?":
            a "Ah, you could set the table? You just need to grab your preferred cutlery. Top drawer."
            "He gestures to his left."
            menu:
                "(Open the top drawer.)":
                    scene bg cutlery
                    "With little fanfare, you choose your desired cutlery before heading to the dinner table,"
                    jump vserve1cont
                "(Open the second drawer.)":
                    $a_mr+=5
                    scene bg cutlery with dis
                    "You slide open the second drawer with a clatter, hearing metal scrape as you quickly glance to your right as Anton's eyes narrow on you."
                    a "No--" with hpunch
                    a "{cps=70} What. {w=.2}Are. {w=.2}You.{w=.2} Doing."
                    pc "I--"
                    menu:
                        "Tell the truth.":
                            pc "I just wanted to check out the other drawers!"
                            pc "Is that so wrong?"
                            "Stilted anger courses through his words."
                            a "Yes? I was pretty obvious when I said {b}top{/b} drawer."
                            "Your eyebrow twitches at the sudden anger."
                            pc "I made a mistake. My bad. No need to be so aggressive."
                            "He lets out a frustrated sigh before his face takes on a more common expression."
                            a "...Sorry. {w=0.2} Could you just go sit down at the table?"
                            pc "Fine."
                            "Fuck you too."
                            $a_s += 5
                            jump vserve1cont
                        "Lie.":
                            pc "Oh, sorry. Opened the wrong drawer."
                            "..."
                            a "Just be careful next time."
                            a "Ok?"
                            pc "...Okay."
                            "Well. That was weird."
                            "He's giving you the stink eye now... so I guess it's best to go sit down then."
                            $a_s += 5
                            jump vserve1cont
    label vserve1cont:
        scene meal ant neutral
        "You sit down at the table."
        "It's a couple moments later that Anton is accompanying you, a hot plate of fresh deep fried potatoes in front of you."
        if (a_s>0):
            show meal ant neutralo
            a "I'm sorry. About... earlier."
            show meal ant neutral
            pause.5
            show ant neutralo
            a "It was... uncalled for."
        show meal ant neutralo
        a "Wait a couple minutes and it should be good to cool down."
        "The question that's been lingering on the tip of your tongue escapes your traitorous mouth."
        pc "So how do you afford this?"
        "Ouch."
        pc "Er... {w=0.5} Let me rephrase-"
        show meal ant neutralo
        a "It's fine!"
        show meal ant angryo
        a "I had an interesting... childhood."
        if orphan:
            a "I told you a bit about it in the car."
        a "But basically. I was in a really, really bad place growing up."
        a "I didn't have the support I needed. And I did really bad things."
        show meal ant angryo
        a "Like. Really bad."
        show meal ant happyo
        a "And it was a rookie cop that saved my life."
        show meal ant neutralo
        a "I'm no paragon of perfection now."
        a "But they saved me when I had nothing. And it made me realize that my life has... value. Has potential."
        show meal ant neutral
        "That sounds... vaguely familiar."
        a "And so I changed things around. Got a job, moved cities, got another job. And then eventually, I got into police school."
        show meal ant happyo
        a "I want to be able to make change. Like that officer had done for me."
        show meal ant happy
        pc "Wow... That's really..."
        show meal ant neutralo
        a "It's a lot. I know."
        pause.5
        show meal ant happyo
        a "But you know what you can do to make me feel better?"
        show meal ant happy
        "Er... well, not really something you wanna do but can't hurt..."
        show meal ant happyo
        a "Eat your food?"
        show meal ant happy
        "Oh yeah. It's definitely cooled down by now."      
    
    #    a "My parents weren't very stable. In any way, shape, or form."
    #    a "And then, I got tossed."
    #    show meal ant neutralo
     #   a "I was alone, for a very long time. And being alone at a young age, it... does something to you."
  #  #    a "But someone saved me from that... that despair."
   #     a "And if I could be saved, there's probably a bunch of others who need saving."
   #     a "So I enrolled in police school. I want to be able to save others just like I had been."
   #     pc "That's... a lot."
   #     a "Yeah. Sorry."
    #    pc "Is there... anything I can say? Like. An apology feels insufficient."
 #       a "Eh, I've been over it for a while..."
  #   #   pause.2
   #     a "But you know what you can do to make me feel better?"
    #    "Er... well, not really something you wanna do but can't hurt..."
     #   show ant grin
        "You gingerly take a piece in between your thumb and pointer, the thin layer batter crumbling under your fingers."
        "!!!" with vpunch
        "This is really good !!"
        "The sweet potatoes are so... {w} sweet! The inside is so soft and fluffy, it practically melts on your tongue."
        "The batter is crispy and light in a way that doesn't take away from the flavors of the starch."
        "Breaking your spell of satiation, Anton coughs into his hand."
        show meal ant happyo
        a "I'll take that it tastes good?"
        show meal ant happy
        pc "Fantastic! Really!" 
        pc "I know that they're easy to make taste good. But I mean it!"
        pc "You could pursue a career in food."
        show meal ant happyo
        a "That means a lot to me, thank you, boss."
        pc "How's your beef?"
        show meal ant neutralo
        a "Huh?"
        show meal ant neutral
        "You gesture to his plate, that he hasn't really taken a bite out of."
        show meal ant neutralo
        a "Oh! {w} It's good! Thanks for asking!" 
        "As if emphasizing, he goes in to take a bite before looking back up at you."
        show meal ant happyo
        a "It really is. This was an excellent cut, good on me! {w} Props to the butcher!"
        "It's a brief silence that has him pushing back out of his chair after eating a bit of the food. He takes the empty plate with him."
        show meal ant neutralo
        a "I'll start on the soup. It's mainly just returning it to the stovetop."
        pc "I can-"
        show meal ant happyo
        a "You can help stir it if you'd like?"
        "Huh. How'd he guess that?"
        show meal ant neutralo
        a "You're a very open person to read, boss."
        "I guess that explains it."  
        jump course02

label serve01:
    show kitchen ant neutral
    "Everything is done quickly, with a subtle layer of quiet finesse to it. You're not sure how often he cooks for himself."
    "But his apparent talent is clear."
    "His plate sits in front of you, pouring you a glass of water in a wineglass, the lemon pitcher resting nearby."
    "He gestures to his dining table as you watch him clean the cutting boards, wash them under running water."
    show kitchen ant fondo
    a "You can go make yourself comfortable if you'd like?"
    menu:
        "Oh. Yeah, sure.":
            show kitchen ant grino
            a "Alright, the table should already be set and everything!"
            jump vserve1cont
        "Can I do anything to help you with?":
            $a_a+=2
            show kitchen ant grino
            a "Ah, you could set the table? You just need to grab your preferred cutlery. Top drawer."
            "He gestures to his left."
            ## scene bg cutlery01
            menu:
                "Open the top drawer.":
                    scene bg cutlery
                    "With little fanfare, you choose your desired cutlery before heading to the dinner table,"
                    jump vserve1cont
                    menu:
                        "Chopsticks":
                            jump serve1cont
                        "Fork":
                            jump serve1cont
                "Open the second drawer.":
                    # blur of action or sum with hpunch
                    "You slide open the second drawer with a clang, hearing metal crash against one another as you quickly glance to your right, Anton's figure quickly moving."
                    show kitchen ant angryo
                    a "{cps=70}What. {w=.2}Are. {w=.2}You.{w=.2} Doing." with hpunch
                    show kitchen ant angry
                    pc "I--"
                    menu:
                        "Tell the truth.":
                            pc "I just wanted to check out the other drawers!"
                            pc "Is that so wrong?"
                            "Stilted anger courses through his words."
                            show kitchen ant angryo
                            a "Yes? I was pretty obvious when I said {b}top{/b} drawer."
                            show kitchen ant angry
                            "Your eyebrow twitches at the sudden anger."
                            pc "I made a mistake. My bad. No need to be so aggressive."
                            "He lets out a frustrated sigh before his face takes on a more common expression."
                            show kitchen ant neutralo
                            a "...Sorry. {w=0.2} Could you just go sit down at the table?"
                            show kitchen ant worry
                            pc "Fine."
                            "Fuck you too."
                            $a_s += 5
                            jump serve1cont
                        "Lie.":
                            pc "Oh, sorry. Opened the wrong drawer."
                            "..."
                            show kitchen ant worry
                            pause.25
                            show kitchen ant neutralo
                            a "Just be careful next time."
                            a "Ok?"
                            show kitchen ant neutral
                            pc "...Okay."
                            show kitchen ant angry
                            "Well. That was weird."
                            "He's giving you the stink eye now... so I guess it's best to go sit down then."
                            $a_s += 5
                            jump serve1cont
    label serve1cont:
        scene meal ant angry
        "You sit down at the table."
        if (a_s >= 5):
            "You were just curious. You didn't get the big deal. Why in the world is he so mad?"
            "It's not your fault, really."
            "And it was just an accident!"
            "Whatever."
            $a_s+=1
            "Jerk."
        "It's a couple moments later that Anton is accompanying you, a hot plate of fresh deep fried gizzards in front of you."
        if (a_s>0):
            show meal ant neutralo
            a "I'm sorry. About... earlier."
            show meal ant neutral
            pause.5
            show meal ant neutralo
            a "It was... uncalled for."
        show meal ant neutralo
        a "Wait a couple minutes and it should be good to cool down."
        show meal ant happy
        "The question that's been lingering on the tip of your tongue escapes your traitorous mouth."
        pc "So how do you afford this?"
        show meal ant neutral
        "Ouch."
        pc "Er... {w=0.5} Let me rephrase-"
        show meal ant happy
        pause.2
        show meal ant neutralo
        a "It's fine!"
        show meal ant neutral
        pause.25
        show meal ant neutralo
        a "I had a... rough childhood."
       ## if orphan:
         ##   a "You know I didn't have parents."
           ## a "And so I was alone for a long time."
         ##   pc "Surely there was adoptive and foster care?"
           ## a "I mean, have you heard more good stories than bad about the foster system?"
            ##"I mean, the gap can't be that bad."
         ##   a "Okay, I might be wrong there."
          ##  a "But that system did jackshit for me."
          ##  a "I was failed. And I had almost nowhere to go."
           ## a "And a couple years ago, I was saved."
          ##  a "I mean, it's nothing too big or anything. Just like these kids were ganging up on me."
          ##  a "So I was having a bad day overall. And then this rookie cop ended up saving my life."
           ## a "I'm pretty sure they would have killed me."
           ## "You wince at the idea."
           # pc "Really?"
  #      else:
    #        a "I was alone for a good amount of my life."
     #       "Oh."
     #       a "No. {w=0.5} Don't give me that look."
       #     "He sighs, as if resetting his emotions."
    ##        a "Sorry."
         #   a "As I was saying though. I was alone. Homeless at one point."
      ##      a "I had nowhere to go, no money, nothing."
       #     a "But then a cop saved my life. Like. Literally."
        #    "Your heart drops in your chest."
       #     pc "You- You don't have to tell me this. If you're uncomfortable."
     #       a "No, no. It's fine. I really should."
        if orphan:
            a "I told you a bit about it in the car."
        a "But basically. I was in a really, really bad place growing up."
        a "I didn't have the support I needed. And I did really bad things."
        show meal ant angryo
        a "Like. Really bad."
        show meal ant neutralo
        a "And it was a rookie cop that saved my life."
        show meal ant neutral
        pause.25
        show meal ant neutralo
        a "I'm no paragon of perfection now."
        a "But they saved me when I had nothing. And it made me realize that my life has... value. Has potential."
        "That sounds... vaguely familiar."
        show meal ant happyo
        a "And so I changed things around. Got a job, moved cities, got another job. And then eventually, I got into a police program."
        a "I want to be able to make change. Like that officer had done for me."
        show meal ant happy
        pc "Wow... That's really..."
        show meal ant neutralo
        a "It's a lot. I know."
        pause.5
        show meal ant happyo
        a "But you know what you can do to make me feel better?"
        show meal ant happy
        "Er... well, not really something you wanna do but can't hurt..."
        show meal ant happyo
        a "Eat your food?"
        show meal ant happy
        "Oh yeah. It's definitely cooled down by now."  
        "You gingerly take a piece in between your thumb and pointer, the batter flaking away as you do."
        "!!!" with vpunch
        "This is really good !!"
        "The outer coating of the gizzard bites are crunchy and flaky, crackling with each bite you take."
        "The flesh is tender and meaty, practically falling apart with each chew of your incisors (?)."
        "Some parts are more thicker than others, you note mildly, but it's not unpleasant!"
        "Breaking your spell of satiation, Anton coughs into his hand."
        show meal ant happyo
        a "I'll take that it tastes good?"
        show meal ant neutral
        pc "Fantastic! It's a lot better than I was expecting?"
        show meal ant neutralo
        a "Oh? Really now? {w} And what were you expecting?"
        show meal ant happy
        "..."
        pc "Nothing this great really... Uh."
        pause.2
        show meal ant happyo
        a "You wound me!"
        show meal ant happy
        pc "But seriously. This is really good, Anton."
        pc "You could genuinely pursue a career in food."
        show meal ant happyo
        a "That means a lot to me, thank you, boss."
        show meal ant happy
        "It's a brief silence that has him pushing back out of his chair after eating a bit of the food. He takes the empty plate with him."
        show meal ant neutralo
        a "I'll start on the soup. It's mainly just returning it to the stovetop."
        pc "I can-"
        show meal ant happyo
        a "You can help stir it if you'd like?"
        show meal ant happy
        "Huh. How'd he guess that?"
        show meal ant happyo
        a "You're a very open person to read, boss."
        show meal ant happy
        "I guess that explains it."
        jump course02

label course02:
    scene bg kitchen
    "You watch him haul a big pot out of his fridge that he says basically just needs to be reheated and stirred for a bit."
    show soup with dis
    "You, of course, then move to the stovetop."
    "He fiddles with the notches and the buttons on his stovetop before settling and leaving you to stir."
    a "I'll just cut up some garlic bread."
    "Grabbing a long baguette loaf, he gingerly slices it behind you. You can hear the bread knife rocking through it."
    menu:
        "Ask about work.":
            jump interrogation
        "Ask about you." if a_a>=10:
            jump checkup
        "Stay silent.":
            jump c2cont

    label checkup:
        menu:
            "Why do you call me boss?" if not f_nick:
                jump friend_nickname
            "What are we?" if not f_rel:
                jump friend_relationship
                    
        label friend_nickname:
            $f_nick = True
            $a_a+=1
            pc "So why do you call me that?"
            a "Huh?"
            pc "Boss, sarge, whatever."
            pc "Like, we both know I'm not your actual boss."
            pc "I trained you, but so did half the people at the station."
            a "Oh."
            a "Uh, I guess I just thought it was nice to have a nickname for you."
            a "You were the first one to teach me."
            a "And the first one to sound like you appreciated me outside of my work."
            pc "I mean.{w} We do work together. Your performance affects how you're perceived."
            a "Valid, but not what I meant, I guess?"
            a "It feels like...{w} you see me as a real person.{w} I don't know."
            a "You're the only one who's ever really tried to understand me as a person."
            a "Not just a coworker, but me on my own."
            if f_nick and f_rel:
                jump c2cont
            else:
                jump checkup

        label friend_relationship:
        $a_a+=2
        $f_rel = True
        pc "What are we?"
        "You belatedly can hear Anton choke before briefly cursing."
        a "{cps=70} Shit!{w}{cps=45} I accidentally cut myself!{w} The bread is fine though." with hpunch 
        "You continue stirring the pot, occasionally glancing over your shoulder to see him cleaning up the mess."
        pc "Er... I didn't mean it in a weird way.{w} Sorry?"
        a "No, no! You're good. Just...{w} caught me off guard."
        pc "Sorry."
        a "Really, you're good."
        a "Huh. It's a good question...{w} I know you don't mean anything by it."
        pc "Like, do you think of me as your coworker? Or your friend?"
        a "Well,{w} they're basically the same thing to me."
        a "But I would like to be your friend if you let me?"
        a "I've technically thought we were friends for a while."
        a "But if we haven't been, and you don't want to be, then coworkers is fine."
        menu:
            "I've thought we were friends too!":
                a "Really?! That's great."
                pc "I wasn't sure if I was overstepping or not with the question."
                a "Yeah, you're good, don't worry!"
                jump fr_cont
            "Yeah, we can be friends, if you'd like.":
                a "Great!{w} That's awesome to hear!"
                a "I'd love nothing more!"
                pc "So...{w} friends?"
                a "Friends."
                jump fr_cont
            "I'd like to keep this strictly professional.":
                a "Oh."
                a "Sorry for the assumption."
                "Stilted silence fills the air.{w} Well, that's awkward."
                jump fr_cont
        label fr_cont:
        if f_nick and f_rel:
            jump c2cont 
        else:
            jump checkup

    label interrogation:
        menu:
            "So uh. How were your trainee years?" if not p_exp:
                jump police_years
            #"How'd you get the money for the academy?" if not p_fund: 
            #    jump police_funds
            "Why'd you transfer here?" if not p_tran:
                jump police_transfer

        label police_years:
            $p_exp = True
            a "I, uh, I'm not sure if you read my file. Or if the big boss let you."
            "You did. You know he transferred from Delta. God forbid."
            a "But I came from Delta. And they don't have the best reputation.{w} Should my memory serve me right."
            pc "You'd be right, unfortunately."
            pc "We know them as local scumbags. Like the worst of the worst."
            "Anton makes a choked noise from behind you."
            pc "Uh....{w} not that you're as bad as them...{w} Of course..."
            "He lets out a lighthearted chuckle at that."
            a "It's fine. Really."
            a "I know how bad they are."
            "Gah! {w} Of course he would, he actually worked with them."
            "Nice going, dumbass."
            a "They're not bullies, they didn't pick on me. But the list of what they didn't do is very short."
            a "They're elitist, ironic considering how they act."
            "You let out a short snicker at his remark."
            if p_exp and p_tran:
                jump c2cont
            else:
                jump interrogation

        #label police_funds:
        #    $p_fund = True

        label police_transfer:
            $p_tran = True
            a "Delta. You know how they are."
            a "They're {b} very hard {/b} to be around on a constant basis."
            a "They can't get along with anyone because they're all vying to be better than one another."
            a "It's tiring. Really."
            "..."
            pc "... Sorry I asked?"
            a "No! {w} No, you're fine."
            a "I don't talk a lot about them, just because of how... {w}much{w} it was dealing with them."
            a "Plus, I can't say I was a lot better."
            "Now, that's a surprise."
            a "Hey! I can practically hear you thinking from over there!"
            a "I'm not as sketchy! {w} I swear!"
            pc "Yeah? Care to elaborate?"
            a "Everyone does some bad things in life. I just happen to be better than those I left behind."
            pc "Sounds a little biased."
            if a_s>0:
                a "You mean to tell me, you've never done anything bad either?"
                "You stiltedly remember how he caught you checking his other drawer despite his insistence not to."
                pc "... {w} Fair point."
                "He gracefully moves on."
            a "Everyone's a little biased at the end of the day."
            a "It's not like I could tell you what I've done to make me feel better about what happened."
            pc "I mean, you could."
            "The silence that fills makes it obvious he has no intentions of doing so."
            "He lets out a quite chuckle at your remark."

            if p_exp and p_tran:
                jump c2cont
            else:
                jump interrogation

    label c2cont:
    if (a_s>=5):
        menu:
            "Ask about the second drawer.":
                "You can almost feel the way he stops in place, the cuts of the knife no longer audible."
                $a_s+=5
                $a_mr+=2
                a "Why do you want to know?{w} Why can't you just leave it alone?"
                pc "I-" with vpunch
                a "It's not important, boss."
                a "Stop asking."
                "He's mad.{w} You don't know why.{w} It feels uncanny.{w} But not unfamiliar."
                jump c2cont1
            "Say the food tasted off.":
                "The floor squeaks under the weight of his feet as he turns to you."
                "You pointedly avoid the glare you can feel burn under your skin."
                a "...{w}What?"
                $a_s+=2
                $a_mr +=5
                a "Could you{w} repeat that...?"
                pc "Nothing...{w}! Maybe I don't have an elevated palette."
                "You can hear him scoff."
                "Is he mad? Insulted?"
                "...{w} Regardless. Maybe you shouldn't have said that."
                jump c2cont1
            "Keep quiet.":
                $a_a+=3
                jump c2cont1

    label c2cont1:
        "He gingerly slides the tray of garlic bread in the toaster oven for a bit before turning to you with a bottle of wine in hand."
        a "Would you like some?"
        menu:
            "Sure.":
                "He pours you a wine glass to the side whilst you continue stirring the pot."
                a "It's Chianti."
                "You chuckle lightly."
                pc "That means nothing to me."
                a "It's bright and fruity. It'll mirror the tang of the soup."
                a "Harmonize. They're nice complements."
                jump c2cont2
            "Do you have anything else?":
                a "I have some tea?"
                "He shelves the wine from wherever he got it before pulling out a teapot and steeping some leaves in it."
                "It blossoms into this wonderful bright red shade."
                a "It's rose rooibos. A red tea, if you will."
                a "A personal mix of mine. It's smooth and earthy."
                a "The richness should complement the acidity of the tomatoes."
                jump c2cont2
    label c2cont2:
        "You occasionally take small sips of your drink. Not overindulging, but just enough to be missing the taste of the soup."
        "The sweet aroma fills the air and you glance in Anton's direction."
        a "It should be ready to eat as soon as-"
        "{size=+15}DING !!!{/size}" with hpunch
        a "Ok... so that's done."
        jump serve02

label serve02:
    show meal ant neutral
    "You sit down across from Anton as he quietly arranges the dish in front of you."
    show meal ant neutralo
    a "So it's a tomato soup with some balsamic and basil. Would you like any parmesan?"
    show meal ant neutral
    menu:
        "Sure!":
            jump s2cont
        "No thanks.":
            $parm = True
            jump s2cont
    label s2cont:
    "You pick up the spoon of soup, gently blowing on it before hesitantly bringing it to your lips."
    "Wow.{w} Wow!" with vpunch
    show meal ant happy
    "He genuinely can't stop surprising you."
    "The sauce is thicker than it looked when you were mindlessly stirring it to no end."
    "You can taste a different depth to it, with every velvety bite you take."
    "It's smooth on your tongue, warm in your mouth."
    "The both of you sit in quiet silence for a couple minutes, taking an occasional sip of your drink as you do."
    "A couple moments later, Anton looks at your expression appraisingly before pulling out of his chair."
    show meal ant neutral
    menu:
        "Where are you going?":
            show meal ant neutralo
            a "The next meal just requires a bit more extensive prepping."
            show meal ant happyo
            a "Don't worry too much about it!"
            show meal ant happy
            pc "Ah, okay."
            jump c3meal
        "Oh, ok. Go ahead." if a_s>=10:
            "And he does so with little to no fanfare."
            "Raising from the table, pulling a package out of the fridge as you continue making your way through the soup."
            "He's gone however.{w} A fact you notice almost instantaneously."
            jump c3investigation
        "You're not staying to eat?" if a_a>=5:
            show meal ant happyo
            a "Oh!"
            a "I'm just going to prepare the next meal!"
            a "It's a bit more tedious than the other two."
            show meal ant happy
            pc "Oh. Uh.{w} I can help!"
            show meal ant neutralo
            a "No, you've helped plenty enough! At least let me do the entree!"
            menu:
                "Ok...":
                    jump c3meal
                "Insist." if a_a>=10:
                    jump c3prep

label course03:
    label c3prep:
        scene bg kitchen
        show kitchen ant neutral
        if nonmeat:
            jump vc3prep
        "You cautiously hover around the island as Anton works, his back to you as he does."
        "Silence fills the air before you decide to ask him something."
        menu:
            "...Are we friends?" if p_exp:
                show kitchen ant shocko
                pc "Urk-"
                show kitchen ant fond
                pc "Uh, just wondering. Cause a multi-course meal doesn't really sound like just coworkers."
                pc "Or I'm overthinking."
                show kitchen ant grino
                a "No, no! I'd love nothing more than to be friends!"
                show kitchen ant shyo
                a "I've actually been too shy to work up the nerve and ask you, so maybe that's on me."
                a "I wasn't sure. So you really took a weight off my shoulders!"
                show kitchen ant fond
                jump serve03
            "You're too casual outside work events." if p_tran:
                show kitchen ant shocko
                "You're not sure how you feel about this sudden bout of closeness."
                show kitchen ant angry
                "It's almost out of the blue. You don't know him."
                show kitchen ant worry
                "And you don't really care to."
                show kitchen ant neutralo
                $a_mr+=2
                a "Ah... sorry?"
                show kitchen ant worry
                jump serve03
            "Why don't we hang out more?" if f_nick:
                show kitchen ant shocko
                $a_a+=1
                "You rarely see him outside the office, even less with your fellow coworkers."
                "And it's not like they treat him poorly or anything else like that."
                show kitchen ant neutralo
                a "Hmm...{w} I guess I just don't get along very well with them."
                show kitchen ant worry
                "That's... odd. The rest of them really like Anton. Like teasing-a-younger-junior kind of like."
                show kitchen ant worryo
                a "They just feel... overbearing."
                show kitchen ant grino at bounce
                a "Not you, of course!"
                show kitchen ant neutralo
                a "Just...{w} they can be a lot."
                show kitchen ant fond
                "Hmm... He was right, to be fair."
                "Marlen has been strung tight with every night he's had to take away from his family."
                "To be fair, being a police officer tends to require that type of dedication regardless."
                "Perch is quiet. He doesn't talk much but maybe he's intimidated?"
                "Anton's voice interrupts your perusal of reasons he might feel overwhelemed by the team."
                show kitchen ant worryo
                a "You look worried, it's fine. Really."
                show kitchen ant grino
                a "I'm sure they'll grow on me. Eventually."
                show kitchen ant neutral
                pc "Yeah...{w} If it's Marlen, he'll be less of a jerk soon, promise. He just needs a couple days off."
                show kitchen ant worryo
                a "...{w} I'm sure."
                show kitchen ant neutral
                jump serve03
            "We should hangout more." if f_rel:
                $a_a+=3
                show kitchen ant grin
                "You can practically feel the smile that worms its way onto his face."
                show kitchen ant grino
                a "...{w} We should. That'd be fun."
                show kitchen ant fond
                "Letting out an awkward cough, you voice a tentative suggestion."
                pc "Maybe you shouldn't have to cook all the time though."
                show kitchen ant smirk
                "You can hear a lilting chuckle from behind you."
                show kitchen ant grino
                a "Really now? Here I thought you liked my cooking?"
                show kitchen ant smirk
                pc "It's not that I don't! I just... feel a bit guilty."
                show kitchen ant fond
                pause.5
                show kitchen ant grino
                a "Don't worry, I like cooking!{w} Are you gonna deprive me of my one and only vice?"
                jump serve03
            "We have a nice casual relationship, don't we?" if a_a>=20:
                $a_a+=5
                show kitchen ant neutral
                pause.2
                show kitchen ant shocko at bounce
                a "O-Oh!" with vpunch
                "You hear a metal clang behind you and you almost whip your head around at neckbreaking speeds."
                a "{cps=75}Don't!{w} Don't look at me right now!"
                "It's a strained sound that his throat makes before you pointedly follow his demand."
                pc "Are...{w} Are you alright?"
                show kitchen ant worryo
                a "{size=-15}Fuck... this is embarassing.{w}{size=-30} Why...? Why would they?"
                show kitchen ant shyo
                a "Yeah. Yeah, I'm good." 
                show kitchen ant fond
                "...{w}"
                pc "So as I was saying..."
                pc "It's nice, isn't it?"
                show kitchen ant grin
                "Er... {w}well...{w} that feels unfinished."
                pc "Like, being close to someone, without being uncomfortable?"
                show kitchen ant fond
                pc "You make talking to you easy.{w}{cps=60} I don't know.{w}{cps=80} Maybe I'm wrong..."
                show kitchen ant shyo
                a "No!{cps=60}{w} I know what you mean!" with vpunch
                show kitchen ant fondo
                a "It's nice. Being able to talk with you. It's...{w} good."
                show kitchen ant fond
                pc "Yeah, it's casual, nonchalant even."
                show kitchen ant grino
                a "{size=-20}{cps=100}We could be more if you want..."
                pc "Huh?"
                show kitchen ant shocko at bounce
                pause.2
                show kitchen ant worryo
                a "Ack!{w} Nothing!" with vpunch
                show kitchen ant neutral
                "Huh. Wonder what he said."
                jump serve03
            "Stay quiet.":
                jump serve03

    label c3meal:
        if nonmeat:
            jump vc3meal
        show meal ant neutral
        "It's only a couple moments later until the both of you are sat down face to face at the table once more."
        "Your eyes move down towards the steak placed in front of you as you carefully glide through the soft, wavering flesh and the perfect crust."
        "The juices of the steak ooze around the bottom, forming a small accumulation on the surface of the ceramic plate."
        "You note, while slicing through the tender meat, that it's a lot easier to cut than you've ever had to."
        "Maybe it's very marbled?"
        "You tentatively take a small bite."
        show meal ant happy
        "!!!" with vpunch
        "The meat practically melts on your tongue, rendered fat and lack of muscle leaving a soft, smooth, silken taste!"
        "There's an undertone of smokiness that you could probabaly attribute to the long bone inside it, but it's subtle and unique."
        "It does taste reminiscent of pork, despite Anton mentioning it was beef."
        "Odd."
        pc "Is this pork?"
        show meal ant neutralo
        a "If that's a problem with your religion, it's not! Don't worry."
        show meal ant happy
        "You hum, satisfied with the answer, before you continue diving into the meal."
        if (a_a>=10):
            "You belatedly look back up every now and then to see Anton staring at you."
            "Normally, he stares at you with an air of curiosity, eager to learn and ask more questions at work."
            "Tonight, it feels... {w}different. Still curious."
            jump c3meal
        if (a_mr>=10): 
            show meal ant neutral
            "You belatedly look back up every now and then to see Anton staring at you."
            "Normally, he stares at you with an air of curiosity but this is blatantly disregard for you."
            "He masks it well. But not well enough."
            "Something about it scares you."
            show meal ant happy
            "But he recovers quickly enough to act like nothing had happened."
            jump c3meal
        if (a_s>=5):
            show meal ant neutral
            "You belatedly look back up every now and then to see Anton staring at you."
            "Normally, he stares at you with an air of curiosity but there's something darker in his eyes tonight."
            "It sets you on edge."
            "Because you've seen that look in other eyes before."
            show meal ant angry
            "Specifically, other criminals."
            jump c3meal
        else:
            show meal ant happy
            "The two of you sit in awkward silence as you both indulge in your food."
            jump c3meal

    label c3investigation:
        "...So he's gone. Finally."
        "Something has felt off this whole time. The ease at which he approached you. How easily you listened."
        "It's too...{w} uncanny."
        "And you're going to figure out why."
        label c3i:
        menu:
            "Search the living room." if (not lr):
                jump c3i_lr
            "Search the powder room." if (not pr):
                jump c3i_pr
            "Check out '[???]'" if (pr and lr) and (a_s>=5):
                jump c3i_room
        label c3i_lr:
                scene bg livingroom
                $lr = True
                menu:
                    "Check the couch." if not couch:
                        $couch = True
                        "The couch is made of stiff dark leather."
                        "It compresses under your touch, but not easily."
                        "The upholstery is barely lived in."
                        if couch and coffee and tv and magazine:
                            "You've seen everything here."
                            jump c3i
                        else:   
                            jump c3i_lr
                    "Check the coffee table." if not coffee:
                        $coffee = True
                        "There's a stack of coasters on the coffee table, but no visible signs of usage."
                        "It says 'Happy Birthday Kael!'."
                        "Who's Kael?"
                        if couch and coffee and tv and magazine:
                            "You've seen everything here."
                            jump c3i
                        else:   
                            jump c3i_lr
                    "Check the TV." if not tv:
                        $tv = True
                        "You hear clattering in the kitchen and take the oppurtunity to turn on the television, muting it."
                        "You glance to the kitchen and nothing is there."
                        "Good."
                        "The TV flickers alive and you see a brief weather report on exerting caution."
                        "That's odd."
                        if couch and coffee and tv and magazine:
                            "You've seen everything here."
                            jump c3i
                        else:   
                            jump c3i_lr
                    "Check the magazines." if not magazine:
                        $magazine = True
                        "WOAH WOAH WOAH !!!" with vpunch
                        "Anton, what is THAT ?!"
                        "Oh wait. Nevermind this isn't interesting. It's just some boring dumb magazine from the 2000s."
                        if couch and coffee and tv and magazine:
                            "You've seen everything here."
                            jump c3i
                        else:   
                            jump c3i_lr
                    "Leave." if not couch or not coffee or not tv or not magazine:
                        jump c3i
        label c3i_pr:
                scene bg bathroom
                $pr = True
                menu:
                    "Check the soap." if not soap:
                        $soap = True
                        "You gingerly squirt a bit of the capped soap he has on the counter."
                        "You lave your hands under a running stream of cool water."
                        "You note that your hands smell like cherry blossoms now."
                        if soap and toilet and towel and sink:
                            "You've seen everything here."
                            jump c3i
                        else:   
                            jump c3i_pr
                    "Check the toilet." if not toilet:
                        $toilet = True
                        "Just, uh, a normal toilet here."
                        "Why are you investigating here? You're probably gonna get jumpscared."
                        if soap and toilet and towel and sink:
                            "You've seen everything here."
                            jump c3i
                        else:   
                            jump c3i_pr
                    "Check the towels." if not towel:
                        $towel = True
                        "You grasp the towels in your hands."
                        "So... fluffy.{w} So... warm."
                        "They must be freshly washed, they feel so nice..."
                        if soap and toilet and towel and sink:
                            "You've seen everything here."
                            jump c3i
                        else:   
                            jump c3i_pr
                    "Check the sink." if not sink:
                        $sink = True
                        "You stare down the sink, noticing a pinkish tint to it."
                        "You grab some of the toilet paper, and swipe at it."
                        "It's not fresh, and you're not sure how to feel about that."
                        if soap and toilet and towel and sink:
                            "You've seen everything here."
                            jump c3i
                        else:   
                            jump c3i_pr
                    "Leave." if not soap or not toilet or not towel or not sink:
                        jump c3i_pr
        label c3i_room:
            "You tiptoe down the hall, to a room across the powder room."
            "Faintly, you remember Anton saying it's a guest room that he hasn't cleaned out yet."
            "And to stay out of it. But something smells foul here."
            "... And ew, all of a sudden that is literally speaking."
            "What is he hiding?{w} It smells like melted steel."
            "You glance to your right, no one there."
            "Slowly, you creak the door open..."
            show door
            pc "What the-" with vpunch
            "..."
            a "I told you to stay out."
            a "How{w} stupid{w} are{w} you?"
            with dis
            "Bad Ending: You have got to be more nonchalant..."
            if "Vro is not slick" not in persistent.endings:
                $persistent.endings.append("Vro is not slick")
            return
    

label vcourse03:
    label vc3prep:
        "You cautiously hover around the island as Anton works, his back to you as he does."
        "Silence fills the air before you decide to ask him something."
        menu:
            "...Are we friends?" if p_exp:
                show kitchen ant shocko
                pc "Urk-"
                show kitchen ant fond
                pc "Uh, just wondering. Cause a multi-course meal doesn't really sound like just coworkers."
                pc "Or I'm overthinking."
                show kitchen ant grino
                a "No, no! I'd love nothing more than to be friends!"
                show kitchen ant shyo
                a "I've actually been too shy to work up the nerve and ask you, so maybe that's on me."
                a "I wasn't sure. So you really took a weight off my shoulders!"
                show kitchen ant fond
                jump vc3meal
            "You're too casual outside work events." if p_tran:
                show kitchen ant shocko
                "You're not sure how you feel about this sudden bout of closeness."
                show kitchen ant angry
                "It's almost out of the blue. You don't know him."
                show kitchen ant worry
                "And you don't really care to."
                show kitchen ant neutralo
                $a_mr+=2
                a "Ah... sorry?"
                show kitchen ant worry
                jump vc3meal
            "Why don't we hang out more?" if f_nick:
                show kitchen ant shocko
                $a_a+=1
                "You rarely see him outside the office, even less with your fellow coworkers."
                "And it's not like they treat him poorly or anything else like that."
                show kitchen ant neutralo
                a "Hmm...{w} I guess I just don't get along very well with them."
                show kitchen ant worry
                "That's... odd. The rest of them really like Anton. Like teasing-a-younger-junior kind of like."
                show kitchen ant worryo
                a "They just feel... overbearing."
                show kitchen ant grino at bounce
                a "Not you, of course!"
                show kitchen ant neutralo
                a "Just...{w} they can be a lot."
                show kitchen ant fond
                "Hmm... He was right, to be fair."
                "Marlen has been strung tight with every night he's had to take away from his family."
                "To be fair, being a police officer tends to require that type of dedication regardless."
                "Perch is quiet. He doesn't talk much but maybe he's intimidated?"
                "Anton's voice interrupts your perusal of reasons he might feel overwhelemed by the team."
                show kitchen ant worryo
                a "You look worried, it's fine. Really."
                show kitchen ant grino
                a "I'm sure they'll grow on me. Eventually."
                show kitchen ant neutral
                pc "Yeah...{w} If it's Marlen, he'll be less of a jerk soon, promise. He just needs a couple days off."
                show kitchen ant worryo
                a "...{w} I'm sure."
                show kitchen ant neutral
                jump vc3meal
            "We should hangout more." if f_rel:
                $a_a+=3
                show kitchen ant grin
                "You can practically feel the smile that worms its way onto his face."
                show kitchen ant grino
                a "...{w} We should. That'd be fun."
                show kitchen ant fond
                "Letting out an awkward cough, you voice a tentative suggestion."
                pc "Maybe you shouldn't have to cook all the time though."
                show kitchen ant smirk
                "You can hear a lilting chuckle from behind you."
                show kitchen ant grino
                a "Really now? Here I thought you liked my cooking?"
                show kitchen ant smirk
                pc "It's not that I don't! I just... feel a bit guilty."
                show kitchen ant fond
                pause.5
                show kitchen ant grino
                a "Don't worry, I like cooking!{w} Are you gonna deprive me of my one and only vice?"
                jump vc3meal
            "We have a nice casual relationship, don't we?" if a_a>=20:
                $a_a+=5
                show kitchen ant neutral
                pause.2
                show kitchen ant shocko at bounce
                a "O-Oh!" with vpunch
                "You hear a metal clang behind you and you almost whip your head around at neckbreaking speeds."
                a "{cps=75}Don't!{w} Don't look at me right now!"
                "It's a strained sound that his throat makes before you pointedly follow his demand."
                pc "Are...{w} Are you alright?"
                show kitchen ant worryo
                a "{size=-15}Fuck... this is embarassing.{w}{size=-30} Why...? Why would they?"
                show kitchen ant shyo
                a "Yeah. Yeah, I'm good." 
                show kitchen ant fond
                "...{w}"
                pc "So as I was saying..."
                pc "It's nice, isn't it?"
                show kitchen ant grin
                "Er... {w}well...{w} that feels unfinished."
                pc "Like, being close to someone, without being uncomfortable?"
                show kitchen ant fond
                pc "You make talking to you easy.{w}{cps=60} I don't know.{w}{cps=80} Maybe I'm wrong..."
                show kitchen ant shyo
                a "No!{cps=60}{w} I know what you mean!" with vpunch
                show kitchen ant fondo
                a "It's nice. Being able to talk with you. It's...{w} good."
                show kitchen ant fond
                pc "Yeah, it's casual, nonchalant even."
                show kitchen ant grino
                a "{size=-20}{cps=100}We could be more if you want..."
                pc "Huh?"
                show kitchen ant shocko at bounce
                pause.2
                show kitchen ant worryo
                a "Ack!{w} Nothing!" with vpunch
                show kitchen ant neutral
                "Huh. Wonder what he said."
                jump vc3meal
            "Stay quiet.":
                jump vc3meal

    label vc3meal:
        "It's only a couple moments later until the both of you are sat down face to face at the table once more."
        "Your eyes move down towards the tofu steak placed in front of you as you carefully glide through the soft, wavering flesh and the perfect crust."
        "The juices of the tofu ooze around the bottom, forming a small accumulation on the surface of the ceramic plate."
        "The brown sauce that coats over the ridges, "
        "You note, while slicing through the tender meat, that it's a lot easier to cut than you've ever had to."
        "Maybe it's very marbled?"
        "You tentatively take a small bite."
        show meal ant happy
        "!!!" with vpunch
        "The tofu is still firm, slightly bouncy but still tender. The material melts on your tongue slowly."
        "There's an undertone of smokiness and sweetness that can easily be attributed to the sauce that is heavily melded into the grooves of the tofu."
        if (a_a>=10):
            "You belatedly look back up every now and then to see Anton staring at you."
            "Normally, he stares at you with an air of curiosity, eager to learn and ask more questions at work."
            "Tonight, it feels... {w}different. Still curious."
            jump serve03
        if (a_mr>=10): 
            show meal ant neutral
            "You belatedly look back up every now and then to see Anton staring at you."
            "Normally, he stares at you with an air of curiosity but this is blatantly disregard for you."
            "He masks it well. But not well enough."
            "Something about it scares you."
            show meal ant happy
            "But he recovers quickly enough to act like nothing had happened."
            jump serve03
        if (a_s>=5):
            show meal ant neutral
            "You belatedly look back up every now and then to see Anton staring at you."
            "Normally, he stares at you with an air of curiosity but there's something darker in his eyes tonight."
            "It sets you on edge."
            "Because you've seen that look in other eyes before."
            show meal ant angry
            "Specifically, other criminals."
            jump serve03
        else:
            show meal ant happy
            "The two of you sit in awkward silence as you both indulge in your food."
            jump serve03

    label vc3investigation:
        "...So he's gone. Finally."
        "Something has felt off this whole time. The ease at which he approached you. How easily you listened."
        "It's too...{w} uncanny."
        "And you're going to figure out why."
        label vc3i:
        menu:
            "Search the living room." if (not lr):
                jump vc3i_lr
            "Search the powder room." if (not pr):
                jump vc3i_pr
            "Check out '[???]'" if (pr and lr) and (a_s>=10):
                jump vc3i_room
        label vc3i_lr:
                scene bg livingroom
                $lr = True
                menu:
                    "Check the couch." if not couch:
                        $couch = True
                        "The couch is made of stiff dark leather."
                        "It compresses under your touch, but not easily."
                        "The upholstery is barely lived in."
                        if couch and coffee and tv and magazine:
                            "You've seen everything here."
                            jump vc3i
                        else:   
                            jump vc3i_lr
                    "Check the coffee table." if not coffee:
                        $coffee = True
                        "There's a stack of coasters on the coffee table, but no visible signs of usage."
                        "It says 'Happy Birthday Kael!'."
                        "Who's Kael?"
                        if couch and coffee and tv and magazine:
                            "You've seen everything here."
                            jump vc3i
                        else:   
                            jump vc3i_lr
                    "Check the TV." if not tv:
                        $tv = True
                        "You hear clattering in the kitchen and take the oppurtunity to turn on the television, muting it."
                        "You glance to the kitchen and nothing is there."
                        "Good."
                        "The TV flickers alive and you see a brief weather report on exerting caution."
                        "That's odd."
                        if couch and coffee and tv and magazine:
                            "You've seen everything here."
                            jump vc3i
                        else:   
                            jump vc3i_lr
                    "Check the magazines." if not magazine:
                        $magazine = True
                        "WOAH WOAH WOAH !!!" with vpunch
                        "Anton, what is THAT ?!"
                        "Oh wait. Nevermind this isn't interesting. It's just some boring dumb magazine from the 2000s."
                        if couch and coffee and tv and magazine:
                            "You've seen everything here."
                            jump vc3i
                        else:   
                            jump vc3i_lr
                    "Leave." if not couch or not coffee or not tv or not magazine:
                        jump vc3i
        label vc3i_pr:
                scene bg bathroom
                $pr = True
                menu:
                    "Check the soap." if not soap:
                        $soap = True
                        "You gingerly squirt a bit of the capped soap he has on the counter."
                        "You lave your hands under a running stream of cool water."
                        "You note that your hands smell like cherry blossoms now."
                        if soap and toilet and towel and sink:
                            "You've seen everything here."
                            jump vc3i
                        else:   
                            jump vc3i_pr
                    "Check the toilet." if not toilet:
                        $toilet = True
                        "Just, uh, a normal toilet here."
                        "Why are you investigating here? You're probably gonna get jumpscared."
                        if soap and toilet and towel and sink:
                            "You've seen everything here."
                            jump vc3i
                        else:   
                            jump vc3i_pr
                    "Check the towels." if not towel:
                        $towel = True
                        "You grasp the towels in your hands."
                        "So... fluffy.{w} So... warm."
                        "They must be freshly washed, they feel so nice..."
                        if soap and toilet and towel and sink:
                            "You've seen everything here."
                            jump vc3i
                        else:   
                            jump vc3i_pr
                    "Check the sink." if not sink:
                        $sink = True
                        "You stare down the sink, noticing a pinkish tint to it."
                        "You grab some of the toilet paper, and swipe at it."
                        "It's not fresh, and you're not sure how to feel about that."
                        if soap and toilet and towel and sink:
                            "You've seen everything here."
                            jump vc3i
                        else:   
                            jump vc3i_pr
                    "Leave." if not soap or not toilet or not towel or not sink:
                        jump vc3i_pr
        label vc3i_room:
            "You tiptoe down the hall, to a room across the powder room."
            "Faintly, you remember Anton saying it's a guest room that he hasn't cleaned out yet."
            "And to stay out of it. But something smells foul here."
            "... And ew, all of a sudden that is literally speaking."
            "What is he hiding?{w} It smells like melted steel."
            "You glance to your right, no one there."
            "Slowly, you creak the door open..."
            "images/door3.1.png"
            pc "What the-" with vpunch
            "..."
            pause.4
            a "I told you to stay out."
            a "How{w} stupid{w} are{w} you?"
            with dis
            "Bad Ending: You have got to be more nonchalant..."
            if "Vro is not slick (vegan edition)" not in persistent.endings:
                $persistent.endings.append("Vro is not slick (vegan edition)")
            return


label serve03:
    scene bg kitchen with dis
    show kitchen ant neutral
    "20 minutes pass and with the empty plates, you both move to the island sink."
    show kitchen ant fondo
    a "It's been wonderful having you over, boss."
    show kitchen ant grin
    pc "Yeah. Thanks for having me."
    pc "But I should really get going now."
    show kitchen ant worryo
    pause.5
    show kitchen ant neutralo
    a "Ah, yes, of course! And I can drive you back to the office."
    show kitchen ant fond
    pc "Sure."
    "..."
    show ant worry
    "Or at least thats what you thought."
    "Before there was a crazy SNOWSTORM EVERYWHERE ??" with pixellate
    "..."
    show ant shocko
    a "Uh... that definitely throws a wrench into things...{w} Is there any chance I could convince you into staying the night?"
    show ant worryo
    a "I'm not fond of driving on the snow, gotten into a couple accidents lately."
    show ant worry
    pause.25
    show ant neutralo
    a "And this looks... really bad."
    menu:
        "Yeah sure!" if (a_s<10):
            jump house02
            #good end
        "No thanks..." if (a_s>10)and (a_mr<10):
            #you arent close anymore, you figured smth was up
            show ant worryo
            a "Oh. Okay."
            show ant worry
            "Something about his voice sounds strained. You're more grateful he isn't crashing out."
            "You have this feeling that if you had made him mad, he would retaliate...{w} poorly."
            scene bg car with dis
            show ant car2
            "The car ride back is quiet. You can't tell how he feels. But you're not sure you want to."
            scene bg office doors with dis
            pause.2
            scene night office bg with dis
            "Neutral Ending: Survival of the Fittest"
            if "not hunted, still pursued" not in persistent.endings:
                $persistent.endings.append("not hunted, still pursued")
            return
        "Fuck no." if (a_mr>=10):
            pc "No. You've been acting up this whole time."
            pc "Don't think I haven't noticed, Anton."
            "You take a step backwards from him, the snow melting as it lands on your skin."
            "Your heart skips a beat traitorously as he takes a step towards you, face dark."
            show ant angryo
            a "...{w} Care to elaborate, boss?"
            show ant angry
            #show ant evil at bounch
            pc "Don't call me that!" with vpunch
            show ant worry
            "Hurriedly, you take more and more steps back, eyes trained on his approaching figure."
            show ant worryo
            a "We can talk this out, sarge...!{w} {cps=80}{size=-10} Please..."
            show ant angry
            pc "No. You're hiding something. I know you are. And I don't care to find out what."
            "Stealthily, you pull out your phone, dialing a familiar three-digit number."
            show ant worry
            "Unfortunately, the receiver is far from stealthy."
            s "{size=30}Hello!{w} Police Station #0001, how can I help you?" with vpunch
            "...Fuck."
            show ant angry
            "Anton grabs the phone out of your hand, glaring at you."
            "You try to run but he trips you with a quick movement of his leg." with hpunch
            show ant shyo
            a "Hi, sorry, I misdialed."
            show ant angry
            s "Oh! All good! Be careful tonight!"
            "How is that receiver that stupid...?"
            show ant angryo
            a "I can't believe you...{w} I trusted you..."
            ## dramatic snow bg
            "You see a glint of silver in your peripheral."
            pc "A-Anton... wait. We can{w}... we can talk about this."
            show ant worry
            "As if unable to hear your strained voice, he drags the knife along your clothes. Threads fray in its wake as he continues."
            show ant worryo
            a "I...{w}I thought you were different.{w} Better."
            show ant fondo
            a "I thought you could be like me.{w} Thought you could like me too."
            show ant angry
            pc "Anton--" with vpunch
            show ant angryo
            a "Shut it."
            show ant worryo
            a "I... Where did I go wrong? You should be fine. You should be good."
            show ant angryo
            a "But you're not."
            show ant angryo at bounce
            a "You're... You're just as bad as the rest of them!"
            "Belatedly, you can feel the knife that he stabs into your chest, tears pooling in his eyes as he does."
            "He repeatedly mumbles something to himself, but all you can feel is the bite of the cold."
            "Has the winter always been this freezing?"
            #you get slimed out

            "Bad Ending: Ripe for the Slaughter"
            if "ragebait 5000" not in persistent.endings:
                $persistent.endings.append("ragebait 5000")
            return

label house02:
    scene bg kitchen with dis
    show kitchen ant neutral with dis
    "The both of you find your way back to the kitchen island at the revelation, Anton continuing to clean plates."
    pc "Of COURSE it's snowing. I should have just driven in my own car."
    show kitchen ant fond
    "As if you would've driven in this weather..."
    pc "Sorry for imposing more than I already have."
    show kitchen ant grino
    a "Oh, you're all good, don't worry!"
    menu:
        "Complain about the situation.":
            pc "This blows. Are you joking right now?"
            pc "I know it's winter, but a whole snowstorm?"
            pc "This is ridiculous."
            show kitchen ant neutralo
            "Anton sighs from in front of you."
            a "You can say that again."
            show kitchen ant shyo
            a "Here, go take a shower and warm up."
            show kitchen ant neutralo
            a "I know I have good heating but you look like you could use some downtime."
            show kitchen ant grin
            "...You know what?"
            "Sure."
            pc "Thanks."
            jump shower
        "Help him clean up.":
            pc "Here, let me--"
            show kitchen ant neutralo at bounce
            a "No, no, I couldn't. Let me clean this up."
            show kitchen ant worryo
            a "You can take a shower, I'm sure you're exhausted!"
            show kitchen ant fond
            pc "I-"
            show kitchen ant fondo
            a "Really, go ahead."
            show kitchen ant grin
            "... You could use one."
            pc "...{w} Alright."
            jump shower
    label shower:
        scene bg bathroom
        "The shower slowly creaks to life, hot water raining against the tiled floor."
        "You step into the shower, feeling the water wash over your strained shoulders."
        "It's not as if you haven't showered since the beginning of the case, it's simply that you were too exhausted to enjoy one."
        "The tension slips from your back, as you hum to yourself."
        "You borrow the shampoo and conditioner available in the washroom."
        "Unfortunately, it's as you shut off the faucet that you starkly realize you have no clothes."
        "Well, other than you're old ones."
        menu:
            "Ask Anton for some clothes.":
                $a_a+=2
                "You creak the door open, opening your mouth, but you look down and see a small folded pile of clothes."
                "Huh."
                pc "Thanks for the clothes."
                a "Oh!{w} It's no problem."
                jump showercont
            "Wear your old clothes.":
                "You quickly get dressed, the towel around your shoulders still damp as droplets fall from your hair."
                "You open the door, and see a pile of clothes."
                "Awkwardly, you change into clothes a second time."
                jump showercont
        label showercont:
            "It's a pair of sweatpants and a loose t-shirt."
            "You skulk into the living room with little to no fanfare."
            scene bg livingroom with dis
            show ant fond with dis
            a "Hi! Take a seat."
            "The couch is an L-shape, and Anton pats to the left of the cushion."
            scene bg shittytv with dis
            "You watch as he nimbly flicks through an array of channels, choosing a new show to put in the background."
            "You quietly remark a movie adaptation of one of your favorite books!"
            "Huh. You didn't know they uploaded that yet."
            scene bg shittytv solo with dis
            show ant grin with dis
            pc "'Bloodborne'?"
            show ant grino
            a "Oh? Do you know it?"
            show ant grin
            "Chuckling, you wistfully think back to the book series."
            show ant shocko
            pc "More than know it, I read it fervently as of late."
            show ant neutralo
            a "I didn't know this was your type of book?"
            pc "It was reccommended to me by a friend, it's pretty good."
            pc "Wonder if they did a faithful rendition of it."
            "The two of you fall into a quiet and easy silence as you bore into the show."
            a "You can take the bed, by the way.{w} For the night."
            menu:
                "Oh, really? Great.":
                    $bed = True
                    "peak" 
                "(Fight for the couch.)":
                    $bed = True
                    pc "Or... I could take the couch. I'm the guest here."
                    a "Exactly! Which is why you should take the bed."
                    pc "No, it's your house. You deserve to at least have the bed."
                    a "It's not as if you chose to be snowed in today!"
                    show ant shyo
                    a "No can do, boss."
                    a "I'll take the couch.{w} And that's final."
                    "Letting out a small huff, you resign yourself to your fate."
                    jump movie
                "(... Share the bed.)" if (a_a >=15):
                    $bed = True
                    if nonmeat:
                        show ant shyo
                        a "No can do, boss."
                        a "I'll take the couch.{w} And that's final."
                        "Letting out a small huff, you resign yourself to your fate."
                        jump movie
                    else:
                        $b_anton
                        show ant shocko
                        pause.5
                        show ant shyo
                        a "I-I mean...{w} Sure?"
                        "His voice nearly cracks at the last unsure word."

            
        label movie:
            scene bg shittytv
            "The two of you find a comfortable silence in watching the show 'Bloodborne'."
            "It's nothing eventful, and Anton remarks several times the inaccuracies compared to the book."
            "You find yourself agreeing with some points and disagreeing with others."
            "It's not much later until you find yourself yawning."
            scene bg shittytv solo with dis
            show ant worryo with dis
            a "Are you ready to head to bed?"
            pc "I think so... Ugh..."





        

    





return
