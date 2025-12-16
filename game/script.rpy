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

default preferences.text_cps = 45
default preferences.afm_enable = False
default nonmeat = False
default orphan = False
#police experience, police funds, police transfer
default p_exp = False
default p_fund = False
default p_tran = False


# stats such as affection, suspicion, murder rate (how likely u r to die)

default a_s = 0
default a_mr = 10
default a_a = 0

image sweetpotatoes:
    "images/potato1.png"
    pause.3
    "images/potato2.png"
    pause.3
    repeat

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

    hide item
    with dis

    "Maybe you should have gotten another drink at the pub.{w=.2} A stronger, alcholic one. Anything to make the strain of this stupid case dissipate."

    scene bg slam desk
    with vpunch

    "Your head falls, nearly banging on the hard of your desk, vision blurring as you hear worried mutters from those around you. You're so... {b}so{/b} done."

    "It's the hesitant footfalls against the linoleum floor that slowly gets your attention of the white of your computer screen."
    
    show item freemoney
    
    "The five dollar bill slipped under the cross of your arm renders you suddenly perking up."

    hide item freemoney
    with vpunch

    scene bg desk

    "Anton's firm and broad shoulders come into view, stiffening at the immediate reaction, pulled tight to avoid laughing as he slowly retracts the bill."

    show ant neutral

    a "Sorry, Sarge. You looked like you needed a pick-me-up."

    show item mug
    with zoomin

    show ant fond

    "Before you have any time to complain or interject or assure him you're fine (like a good superior), he slides you a mug of... something."

    a "Tea. It's chamomile."

    "He clarifies, pointedly looking away, as he awkwardly explains himself."

    show ant worryo
    
    a "Ah-- is it too rude of me to offer? I can take it away--"

    show ant worry

    pc "You're fine."
    
    "You grin back at the gesture, basking in the warmth of the mug."
    menu:
        "Take a sip.":
            hide item mug 
            show item tea mug
            "It's... good."
            show ant fond
            with dis
            show item empty mug
            "Really good."
            hide item


            jump tea_sip

          #  menu:
          #  "Some people just... maybe need help, you suppose.":
          #  "Good fucking riddance.":
        "Don't drink it, but thank him.":
            hide item
            jump tea_dont_sip

    
    label tea_sip:
    

    scene bg slam desk
    with pixellate
    pause.2
    with zoomin

    "You fall asleep promptly at your desk a couple minutes later. 6 hours later, you wake up to your own coat covering your shoulders. He should get a raise."

    scene bg desk
    with dis

    "That morning, Anton had finished external research and networking, before presenting it with some information that just... clicks with what you were working on!"
    "You approach Marlen with this new evidence and ask if he could go with you on a stakeout later that day."
    "He readily agrees, his wife having scolded him last night for his absence and he is ready to be done with this quick but cruel case."

    scene night office bg
    with dis

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
    
    with vpunch
    pc "What--!"
    
    "It's perfect."
    "Somehow this dead end is enough to locate the original drop site of the murder, and luckily enough, you manage to find the weapon! It's a typical murder, stab and ditch."
    show item knife
    "You catch the guy (white, early-to-mid 30s, businessman with a grudge) and he's promptly sent to jail after he pleads guilty, feeling the weight of his crimes heavy on him."
    hide item knife
    "Evidence shows he had a hit-list to take out by the end of the week. And he'd get paid--"
    with vpunch
    "HOW MUCH-!!"
    "Man, you would kill for that much too."
    jump dinner_inv

label dinner_inv:

    scene bg office doors
    with dis

    "You're finally clocking out of your shift. God forbid."
    "This case has been nothing but a pain in your ass these past couple days. Not weeks, thankfully. But you definitely could have seen it getting that extreme."

    "You're finally honing it to that far door, you're so close--"

    with hpunch
    show ant worryo
    
    a "Uh, hi boss?"

    show ant neutral

    "...Something in his hand smells... delicious. Goddamn it, you're starving."

    "And in record time, your stomach growls equally as loud. You've technically missed every word he's said since, but the growing smile on his face..."
    

    show ant grin
    "does NOT go unremarked."
    
    show ant happyo

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
                    $a_mr = -100000
                    #aka ur not dying any time soon
                    #not cause he hates you, but because like,, youre a vegan, you cna't eat humans
                    #vro draws the line at religion my chevre my beloved son  <3
                    show ant shocko
                    a "Oh!"
                    show ant worryo
                    a "Sorry, I didn't know that! I don't have anything on me at the ready..."
                    pause.2
                    show ant shocko
                    a "I actually do!"
                    show ant neutralo
                    a "I was planning on a quaint four course meal tonight, nothing too heavy or anything. I'm so glad to have you join me!"
                    a "I don't mind making some quick alternatives, but most of it is a little meat-heavy... But I've got alternatives, so don't you worry!"
                    jump car
                "Sounds great.":
                    jump car
        "No thanks.":
            pc "I'll pass tonight."
            "His smile falters, but he wishes you well."
            a "Ah, it's fine. I figured I'd just offer."

            "Neutral Ending: So you're no fun?"
            if "Neutral" not in persistent.endings:
                $persistent.endings.append("No Dinner For You :(")
            return

label car:
    show ant grin
    pause.25
    show ant neutralo
    a "Fantastic! We'll take my car!"
    show ant neutral
    "Silently, you raise an eyebrow in his direction. He quickly scatters following up with his reasoning."
    show ant worryo
    a "Well, uhm, you look really tired, Sarge."
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

    scene bg car
    with Dissolve(0.5)
    show ant car1

    "The car ride isn't spectacular or anything, still on edge from spending countless nights at your desk. It's a couple moments later that you're hesitantly speaking up."

    menu:
        "So... Sandwiches, am I right?":
            a "Yes! I love making them. They're easy to put together and they aren't anything to heavy. Something you can finish anywhere if need be!"
            a "Gotta be ready whenever on the job!"
            jump cont_car1
        "Four courses... is quaint?":
            "He chuckles nervously."
            a "Is it not? I like to eat a lot, I'm afraid."
            a "I hope it's not something you mind?"
            menu:
                "Nah, I eat a lot too.":
                    "He beams back at you in full force."
                    a "Now here's someone who shares the same dedication I do!"
                    jump cont_car1
                "Um... it's whatever, I guess.":
                    a "That's good."
                    "He hums to himself absentmindedly as the next song plays on the radio."
                    jump cont_car1
                "Big back ahhh":
                    "Silence fills the air as his face freezes."
                    "Stiltedly, he coughs."
                    jump cont_car1
        "(I like the silence...)":
            jump cont_car

    label cont_car1:
        menu:
            "So. How have you been these past couples days?":
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

    scene bg kitchen
    with dis

    "You follow him to the entrance of Anton's house. He fiddles with his keys, before the door swings open with little to no fanfare."
    "He has you put your shoes on a shoe rack and hang up your coat in the closet."
    "You awkwardly trail behind him as he gives you a quick introduction around his primary living space."

    show kitchen ant happyo
    with dis

    "He tells you to get settled at the island bar as you watch him get to cooking. Grinning, he boasts, tying the apron around his waist."
    a "I promise that everything I'm gonna serve is gonna be like nothing you've ever had before."
    "He pauses."
    a "Well, there's a good chance it'll be something you've had before. But better!"

    menu:
        "Watch him make the first course.":
            if nonmeat:
                jump vegancourse01
            else:
                jump course01
        "Take a look around from where you're sitting.":
            "It's not like you were expecting much. But still."
            "His house is a lot more bare bones than you were expecting it to be."
            "It lacks... emotion. Wherever you look, it's hard to find a trace of, well, Anton."
            "No personal or family photos, no evidence that the house is really lived in."
            jump serve01
        

label course01:
    "You watch him pull a bowl of... buttermilk(?) out of the fridge."
    "And there it was in front of you."
    "...?"
    pc "Is that... actually, no, what is that?"
    a "Gizzard! Have you heard of it before?"
    "This didn't answer any questions. This actually gave you more questions."
    menu:
        "Um... no.":
            jump what_gizzard
        "Yeah, it seems pretty cool!":
            a "Really now? I don't think I've met a lot of people who know what it is!"
            a "That's super cool!"
            jump yes_gizzard
        "Um, ew, unfortunately. And you think I'm eating that?":
            jump no_gizzard

    label what_gizzard:
        pc "What's gizzard?"
        a "Well, I don't actually have a real definition for you. But it's part of the chicken's stomach!"
        a "It also tastes really similar to other dark meat!"
        a "And if you know what giblets are, they're part of that sub-group."
        "You subtly grab your phone and type in gizzards and giblets into your search bar."
        "Giblets... Giblets are... edible internal organs? And gizzards happen to be those. So... gizzards are uysed to grind the food of chickens? They're muscles?"
        pc "Why do chickens need to grind their food."
        a "They don't have teeth. I guess their beaks don't do all of that."
        pc "So, uh, why's it soaking in all that?"
        a "Well, I'm guessing it said something about the gizzards being a muscle. And usually, muscles don't have the best texture."
        a "Buttermilk has acidic properties that let it break those muscle fibers."
        a "It also tenderizes the meat!"
        a "I let these guys sit for about 20 hours to tenderize them. I could slow cook them, but I prefer to have something already ready to cook when I get home."
        pc "Especially with that psycho on the loose."
        a "Correction, having *been* on the loose. Off the streets now, thank god."
        jump yes_gizzard

    label yes_gizzard:
        "He moves aside, preparing two bowls of a beaten egg mixture and another bowl that he adds flour, salt, garlic and onion powder, and some paprika to."
        "Generously, he coats each individual piece in the egg wash and then the flour."
        "His hands stiffen in the bowl, as if remembering a question."
        a "Oh. Sorry, does the idea of eating these bother you?"
        menu:
            "A little...":
                a "I can offer you something else to eat then! I have a more... vegan course prepared if you'd like?"
                "He... hadn't known you were coming. How would he have prepared all that?"
                menu:
                    "Yeah, I'd rather that.":
                        a "Yeah. Yeah, of course!"
                        "He quickly washes his hands, moving to put the gizzard in the fridge and bringing out a different bowl."
                        "Water sloshes around the rim as you lean in."
                        jump vegancourse01
                    "Oh, no, it's fine.":
                        jump yay_gizzard
            "Not at all!":
                jump yay_gizzard
        label yay_gizzard:
        "Something about the sudden assumption makes you feel a bit defensive."
        "Your hands raise up to your shoulders in defense. It's not as if you cared that much."
        pc "It doesn't bother me! Really!"
        "His shoulders relax at the assurance."
        a "As long as you're sure. I wouldn't want to scare away my guest now."
        "Silence follows the end of the conversation as Anton begins frying the gizzard pieces in the oil expertly."
        with dis
        jump serve01

    label no_gizzard:
        "He winces at your tone and diction. If almost wounded by your harshness."
        a "Ouch, alright, I get it."
        a "I can prepare you something else."
        jump vserve01

label vegancourse01:
        show sweetpotatoes
        "It's... sweet potatoes? They look fairly fresh and they've already been peeled."
        "He begins cutting them into cubes, hands nimble before he looks back up at you."
        a "Do you like sweet potatoes?"
        menu:
            "(Well, if you didn't you're eating them now.)":
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
        "Dessert - Velvet Mousse."
        menu:
            "This isn't as... professional as you made it sound.":
                a "I'm just a man! Not a three-star Michelin chef."
                jump vc1cont
            "This sounds... delicious!":
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
        scene bg kitchen
        with dis
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
    "Everything is done quickly, with a subtle layer of quiet finesse to it. You're not sure how often he cooks for himself."
    "But his apparent talent is clear."
    "His plate sits in front of you, pouring you a glass of water in a wineglass, the lemon pitcher resting nearby."
    "He gestures to his dining table as you watch him clean the cutting boards, washing them under running water."
    a "You can go make yourself comfortable if you'd like?"
    menu:
        "Oh. Yeah, sure.":
            a "Alright, the table should already be set and everything!"
            jump vservecont
        "Can I do anything to help you with?":
            a "Ah, you could set the table? You just need to grab your preferred cutlery. Top drawer."
            "He gestures to his left."
                ## scene bg cutlery01
            menu:
                "Open the top drawer.":
                ## scene bg cutlery02, the cutlery is spoon knife chopstick butterknife etc.
                ## $ cutlery = whatever they choose
                    "PEAK"
                    jump vservecont
                "Open the second drawer.":
                        # blur of action or sum with hpunch
                    "You slide open the second drawer with a clatter, hearing metal scrape as you quickly glance to your right as Anton's eyes narrow on you."
                    with hpunch
                    a "No--"
                    a "What. {w=.2}Are. {w=.2}You.{w=.2} Doing."
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
                            $a_s += 10
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
        if orphan:
            a "I told you a bit about it in the car."
        a "But basically. I was in a really, really bad place growing up."
        a "I didn't have the support I needed. And I did really bad things."
        a "Like. Really bad."
        a "And it was a rookie cop that saved my life."
        a "I'm no paragon of perfection now."
        a "But they saved me when I had nothing. And it made me realize that my life has... value. Has potential."
        "That sounds... vaguely familiar."
        a "And so I changed things around. Got a job, moved cities, got another job. And then eventually, I got into police school."
        a "I want to be able to make change. Like that officer had done for me."
        pc "Wow... That's really..."
        a "It's a lot. I know."
        pause.5
        a "But you know what you can do to make me feel better?"
        "Er... well, not really something you wanna do but can't hurt..."
        show ant grin
        a "Eat your food?"
        "Oh yeah. It's definitely cooled down by now."      
        "You sit down at the table."
        if (a_s > 5):
            "You were just curious. You didn't get the big deal. Why in the world is he so mad?"
            "It's not your fault, really."
            "And it was just an accident!"
            "Whatever."
            "Jerk."
        "It's a couple moments later that Anton is accompanying you, a hot plate of fresh deep fried gizzards in front of you."
        if (a_s>0):
            show ant worryo
            a "I'm sorry. About... earlier."
            show ant neutral

            pause.5

            show ant worryo
            a "It was... uncalled for."
        a "Wait a couple minutes and it should be good to cool down."
        "The question that's been lingering on the tip of your tongue escapes your traitorous mouth."
        pc "So how do you afford this?"
        "Ouch."
        pc "Er... {w=0.5} Let me rephrase-"
        a "It's fine!"
        a "I had an interesting... childhood."
        a "My parents weren't very stable. In any way, shape, or form."
        a "And then, I got tossed."
        a "I was alone, for a very long time. And being alone at a young age, it... does something to you."
        a "But someone saved me from that... that despair."
        a "And if I could be saved, there's probably a bunch of others who need saving."
        a "So I enrolled in police school. I want to be able to save others just like I had been."
        pc "That's... a lot."
        a "Yeah. Sorry."
        pc "Is there... anything I can say? Like. An apology feels insufficient."
        a "Eh, I've been over it for a while..."
        pause.2
        a "But you know what you can do to make me feel better?"
        "Er... well, not really something you wanna do but can't hurt..."
        show ant grin
        a "Eat your food?"
        "Oh yeah. It's definitely cooled down by now."
        "You gingerly take a piece in between your thumb and pointer, the thin layer batter crumbling under your fingers."
        with vpunch
        "!!!"
        "This is really good !!"
        "The sweet potatoes are so... {w} sweet! The inside is so soft and fluffy, it practically melts on your tongue."
        "The batter is crispy and light in a way that doesn't take away from the flavors of the starch."
        "Breaking your spell of satiation, Anton coughs into his hand."
        a "I'll take that it tastes good?"
        pc "Fantastic! Really!" 
        pc "I know that they're easy to make taste good. But I mean it!"
        pc "You could pursue a career in food."
        show ant happyo
        a "That means a lot to me, thank you [protag]."
        pc "How's your beef?"
        a "Huh?"
        "You gesture to his plate, that he hasn't really taken a bite out of."
        a "Oh! {w} It's good! Thanks for asking!" 
        "As if emphasizing, he goes in to take a bite before looking back up at you."
        a "It really is. This was an excellent cut, good on me! {w} Props to the butcher!"

        "It's a brief silence that has him pushing back out of his chair after eating a bit of the food. He takes the empty plate with him."
        a "I'll start on the soup. It's mainly just returning it to the stovetop."
        pc "I can-"
        a "You can help stir it if you'd like?"
        "Huh. How'd he guess that?"
        a "You're a very open person to read, boss."
        "I guess that explains it."  

label serve01:
    "Everything is done quickly, with a subtle layer of quiet finesse to it. You're not sure how often he cooks for himself."
    "But his apparent talent is clear."
    "His plate sits in front of you, pouring you a glass of water in a wineglass, the lemon pitcher resting nearby."
    "He gestures to his dining table as you watch him clean the cutting boards, wash them under running water."
    a "You can go make yourself comfortable if you'd like?"
    menu:
        "Oh. Yeah, sure.":
            a "I mean you don't have to!"
        "Can I do anything to help you with?":
            a "Ah, you could set the table? You just need to grab your preferred cutlery. Top drawer."
            "He gestures to his left."
            ## scene bg cutlery01
            menu:
                "Open the top drawer.":
                    ## scene bg cutlery02, the cutlery is spoon knife chopstick butterknife etc.
                ## $ cutlery = whatever they choose
                    menu:
                        "Chopsticks":
                            jump servecont
                        "Fork":
                            jump servecont
                "Open the second drawer.":
                    # blur of action or sum with hpunch
                    "You slide open the second drawer with a clang, hearing metal crash against one another as you quickly glance to your right, Anton's figure quickly moving."
                    with hpunch
                    a "What. {w=.2}Are. {w=.2}You.{w=.2} Doing."
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
                            $a_s += 10
                            jump serve1cont
                        "Lie.":
                            pc "Oh, sorry. Opened the wrong drawer."
                            "..."
                            a "Just be careful next time."
                            a "Ok?"
                            pc "...Okay."
                            "Well. That was weird."
                            "He's giving you the stink eye now... so I guess it's best to go sit down then."
                            $a_s += 5
                            jump serve1cont
    label serve1cont:
        "You sit down at the table."
        if (a_s > 5):
            "You were just curious. You didn't get the big deal. Why in the world is he so mad?"
            "It's not your fault, really."
            "And it was just an accident!"
            "Whatever."
            "Jerk."
        "It's a couple moments later that Anton is accompanying you, a hot plate of fresh deep fried gizzards in front of you."
        if (a_s>0):
            show ant worryo
            a "I'm sorry. About... earlier."
            show ant neutral

            pause.5

            show ant worryo
            a "It was... uncalled for."
        show ant neutralo
        a "Wait a couple minutes and it should be good to cool down."
        show ant fond
        "The question that's been lingering on the tip of your tongue escapes your traitorous mouth."
        pc "So how do you afford this?"
        show ant worry
        "Ouch."
        pc "Er... {w=0.5} Let me rephrase-"
        show ant fond
        pause.2
        show ant neutralo
        a "It's fine!"
        show ant worry
        pause.25
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
        a "Like. Really bad."
        a "And it was a rookie cop that saved my life."
        a "I'm no paragon of perfection now."
        a "But they saved me when I had nothing. And it made me realize that my life has... value. Has potential."
        "That sounds... vaguely familiar."
        a "And so I changed things around. Got a job, moved cities, got another job. And then eventually, I got into a police program."
        a "I want to be able to make change. Like that officer had done for me."
        pc "Wow... That's really..."
        a "It's a lot. I know."
        pause.5
        a "But you know what you can do to make me feel better?"
        "Er... well, not really something you wanna do but can't hurt..."
        show ant grin
        a "Eat your food?"
        "Oh yeah. It's definitely cooled down by now."  
        "You gingerly take a piece in between your thumb and pointer, the batter flaking away as you do."
        with vpunch
        "!!!"
        "This is really good !!"
        "The outer coating of the gizzard bites are crunchy and flaky, crackling with each bite you take."
        "The flesh is tender and meaty, practically falling apart with each chew of your incisors (?)."
        "Some parts are more thicker than others, you note mildly, but it's not unpleasant!"
        "Breaking your spell of satiation, Anton coughs into his hand."
        a "I'll take that it tastes good?"
        pc "Fantastic! It's a lot better than I was expecting?"
        show ant neutralo
        a "Oh? Really now? {w} And what were you expecting?"
        show ant grin
        "..."
        pc "Nothing this great really... Uh."
        pause.2
        show ant happyo
        a "You wound me!"
        show ant grin
        pc "But seriously. This is really good, Anton."
        show ant fond
        pc "You could genuinely pursue a career in food."
        show ant happyo
        a "That means a lot to me, thank you [protag]."
        "It's a brief silence that has him pushing back out of his chair after eating a bit of the food. He takes the empty plate with him."
        a "I'll start on the soup. It's mainly just returning it to the stovetop."
        pc "I can-"
        a "You can help stir it if you'd like?"
        "Huh. How'd he guess that?"
        a "You're a very open person to read, boss."
        "I guess that explains it."
        jump course02



label course02:
    scene bg kitchen
    "You watch him haul a big pot out of his fridge that he says basically just needs to be reheated and stirred for a bit."
    "You, of course, then move to the stovetop."
    "He fiddles with the notches and the buttons on his stovetop before settling and leaving you to stir."
    a "I'll just cut up some garlic bread."
    "Grabbing a long baguette loaf, he gingerly slices it behind you. You can hear the bread knife rocking through it."

label interrogation:
    menu:
        "So uh. How were your trainee years?" if not p_exp:
            jump police_years
        #"How'd you get the money for the academy?" if not p_fund: 
        #    jump police_funds
        "Why'd you transfer here?" if not p_tran:
            jump police_transfer
        "Stay quiet.":

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

    if police_years and police_transfer:
        jump cont
    else:
        jump interrogation

return
