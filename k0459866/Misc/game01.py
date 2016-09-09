print """
Welcome to the game! When typing answers, please type in all lowercase.
Hint: choosing 'check inventory' will automatically use an item if appropriate.
"""
step01 = str(raw_input("""
You awaken in a strange land, you don't know how you go there and you don't know why.
A man appears, he says,
"Greetings traveller, you seemed to have come to our lands in a strange time."
He continues on for a few seconds longer, but he is then interrupted by a strange flash of light.
"I am sorry, but I must leave, here is a sword and a book of ancient knowledge."
He then tells you to navigate the forest infront of you to reach the nearest town.
The man then vanishes before your eyes.
You take a few steps forward, preparing to enter the strange forest.
The path continues for a few more feet, then seemingly stops.
You look around, and can't tell which direction you're facing.
The woods seems to shift and change.
You take a deep breath and prepare for the long trek through these forboding timbers.
There's no turing back now.
You look around, and find two clearings in the trees, do you want to go left or right?\n
"""))

if (step01 == "left"):
    print "You go left."
    step02l = str(raw_input("""
You walk for a good mile through the clearing.
It appears you've made the right choice.
You continues walking, only to come across a silent stream stream.
You have no choice, will you swim across, wait, or check your items?
    """))
    if (step02l == "swim"):
        print """
All of a sudden, the stream turns into a rushing waterfall.
You try to struggle and swim to an egde, but all of the edges seemingly vanish.
The waterfall swallows you, and everything goes black
        """
        print "Game over"
    if (step02l == "wait"):
        print """
You take a seat and wait for something to happen.
After a few hours, nothing seems to change.
It seems you're all alone in these woods...
Suddenly, a creature covered in shadow jumps from a bush.
You try to pull out your sword, but the creature is upon you.
Multiple shredding swipes move across your body.
There isn't much you can do.
The creature dissapears as quickly as it appeared.
You lie on the ground, bleeding out, unable to move.
Then, your vision goes fuzzy and everything fades to black.
        """
        print "Game over."
    if (step02l == "check items"):
        print """
You look over your items:
You have a sword, not anything special, but sharp enough to do the job.
You take a look inside the mysterious tome given to you earlier.
Flipping through the pages, your eyes seem to lock in on a specific page.
The page has a strange rune on it.
Coincidentally, the rune appears in front of a patch of dead grass.
Stepping towards the rune, a patch of ice forms across the stream.
There is now a path available.
You continue to walk for a good hour until you come across another path.
        """
        
        step03l = str(raw_input("You can go left or right.\n"))
        if (step03l == "left"):
            print """
You start to go left, but you're cut off by an invisible barrier.
You take a few steps back.
            """
            step03l = str(raw_input("You can go right.\n"))
            if (step03l == "left"):
                print """
You try to go left once again, but, again, you cannot proceed.
                """
                step03l = str(raw_input("You can go right.\n"))
                if (step03l == "left"):
                    print """
Against all odds, you try to go left once more.
Surprisingly, you are pushed back.
Fed up with the left path, you go right
                    """
                    step03l = str(raw_input("You can go right.\n"))
        if (step03l == "right"):
            print """
You go right.
The path winds around many strange trees and stones.
After a few curves in the road, a mile long stretch comes into view.
After walking for what seems like forever, something appears.
A strange figure, covered in shadow with flaming red eyes, equiped with a strange weapon.
It doesn't look friendly.
It immediately dashes towards you.
You have enough time to make a move.
            """
            print """
Combat works as follows:
You classify what attack you're making with your first word.
Your second word classifies what weapon you'll attack with.
If you simply type 'punch', you will punch your target.
For example: if you type 'stab sword', you'll stab with your sword.
Currently, you only know how to swing and stab.
You may have opportunities to learn additional moves.
            """
            
            step04l = str(raw_input("What move do you make?\n"))
            if (step04l == "stab sword"):
                print """
You attempt to stab the creature.
With your lack of sword training, you wildly stab at the creature.
The creature, with no hesitation, parries to the left and hits your sword out of your hand.
                """
                step04la = str(raw_input("""
It seems the creature is open to an attack.
Pity your sword was knocked away.
            """))
                if (step04la == "punch"):
                    print """
You attempt to punch the creature.
The creature dodges your punch, violently swinging upwards.
The creature's weapon catches you in the chest, moving upwards into your throat.
You fall to the ground, profusely bleeding from your neck.
You only sit their for a few more seconds before bleeding out.
                """
                print "Game over."
            if (step04l == "swing sword"):
                print """
As the creature approaches, you swing your sword.
The creature barely dodges the mighty swing of your sword.
The creature seems to have slipped in the dirt, dropping his weapon.
The creature lies on the ground, defenseless.
The creature pitifully begs for life.
                """
                step04lm = str(raw_input("Do you kill the creature? (yes/no)\n"))
                if (step04lm == "no"):
                    print """
The creature jumps up off the ground, thankful for your mercy.
The creature reveals some information to you.
He says:
"Although I serve the dark one, I value my life more."
When you prompt him about the dark one, he doesn't say anything.
When he starts to walk away, he falls to the ground, flailing his arms and legs screaming "NO!"
Shadowy tendrils have pierced the ground, they drag the creature down under the earth.
As the creature fully vanishes under the ground, a dark, malevolent voice booms in your head.
"I over-estimated your abilities, great one, but you shall know endless torment!"
You hear shuffling in the trees and bushes around you.
You ready yourself only to have a flurry of arrows fly at you from one side of the trees.
All of them seem to go inside your body.
The arrows burn like fire.
You simply sit there, unable to do anything, slowly bleeding out.
When everything goes black, you awaken.
You look around, magma pouring out of the walls, smelling of brimstone.
Strangest of all, you feel alive and dead at the same time.
A giant figure emerges from a curtain of fire.
You attempt to run away, but the figurelaughs at you and sets you aflame.
You had your doubts, but there's no denying it.
This is hell.
                    """
                    print """
Game over.
                    """
                if (step04lm == "yes"):
                    print """
You execute the creature without hesitation.
As the creature lies on the ground dead, the body begins to shift.
The corpse starts to melt into a black puddle, prompting you to place your sword into it.
                    """
                    
                    step05l = str(raw_input("Do you lay down your sword? (yes/no)\n"))
                    if (step05l == "no"):
                        print """
You deny this offering.
The puddle fades away, a booming voice manifests in your head.
"I under-estimated your abilities, great one, but you shall know endless torment!"
You hear shuffling in the trees and bushes around you.
You ready yourself only to have a flurry of arrows fly at you from one side of the trees.
All of them seem to go inside your body.
The arrows burn like fire.
You simply sit there, unable to do anything, slowly bleeding out.
When everything goes black, you awaken.
You look around, magma pouring out of the walls, smelling of brimstone.
Strangest of all, you feel alive and dead at the same time.
A giant figure emerges from a curtain of fire.
You attempt to run away, but the figure laughs at you and sets you aflame.
You had your doubts, but there's no denying it.
This is hell.
                        """
                        print """
Game over.
                        """
                    if (step05l == "yes"):
                        print """
After a moment of consideration, you place your weapon in the puddle.
The weapon suddenly jumps up, floating above the pool of liquid.
The sword pulses red, and absorbs the puddles beneath it.
The weapon changes from its traditional shape to that of cursed one.
The metal warps and become exeedingly strong.
It looks indestructible.
The blade beckons you to wield it once again.
It looks powerful.
You pick up the sword, and it seems to bond with your very soul.
New power courses through your veins, and a voice echo through your head.
'The pact has been made, forsake it, and suffer.'
There is no turning back now.
                        """
                        print """
You learned the ability 'torment'.
                        """
                        print """
'Torment works like the punch ability.
You only need to type 'torment' to use it.'
                        """
                        print """
You stand there for a moment, observing the blade.
You then press forward, moving to the end of the forest into a clearing.
As you step out of the forest, you see a sign that reads,
"Welcome to Fonick!"
This was the village the man was talking about.
There are many things you can do here.

As of now, you can:
talk
go to the inn
                        """
                        step06l = str(raw_input("What would you like to do?\n"))
                        if (step06l == "go to the inn"):
                            print """
The inn appears to be vacant at the moment.
You take a step back.
                            """
                            step06l = str(raw_input("What would you like to do?\n"))
                            if (step06l == "go to the inn"):
                                print """
The inn isn't open, maybe you should talk to the people.
                                """
                                step06l = str(raw_input("What would you like to do?\n"))
                        if (step06l == "talk"):
                            print """
You walk up to a group of villagers.
They greet you with a hearty "Hello".
                            """
                            step06lt = str(raw_input("What do you talk about?\n"))
                            print """
You can talk about:
history
directions
gossip
                            """
                            print """
You try to start a conversation with the villagers.
However, they notice your weapon.
They look at each other for a second and say they have to go make supper.
They quickly shuffle away from you.
Some lights turn on in the inn, maybe you should sleep for the night.
You enter the inn, and ask for a room.
The innkeeper, although hesitant, says it will be 15 pieces.
You don't have the money.
You could either threaten, persuade, or beg.
                            """
                            
                            step07li = str(raw_input("What do you do?\n"))
                            if (step07li == "persuade"):
                                print """
You speak to the innkeeper using some forms of persuasion.
Although she is interested in your words, she denies you.
                                """
                                step07li = str(raw_input("What do you do?\n"))
                                if (step07li == "persuade"):
                                    print """
You try to persuade her again, but she denies you.
                                    """
                                    step07li = str(raw_input("What do you do?\n"))
                                if (step07li == "persuade"):
                                    print """
You try to persuade her again, but she denies you.
                                    """
                                if (step07li == "beg"):
                                    print """
You pittifull beg the innkeeper for a room.
She laughs at you.
                                    """
                                    step07li = str(raw_input("What do you do?\n"))
                                    if (step07li == "beg"):
                                        print """
You try to beg again.
She laughs at you again.
You feel like an idiot for begging.
                                        """
                                        step07li = str(raw_input("What do you do?\n"))
                                        if (step07li == "beg"):
                                            print """
You already feel embaressed for begging twice, you don't want to do it again.
                                            """
                                            step07li = str(raw_input("What do you do?\n"))
                                            if (step07li == "beg"):
                                                print """
You already feel embaressed for begging twice, you don't want to do it again.
                                                """
                                    if (step07li = "threaten"):
                                        print """
You threaten the innkeeper.
You tell her that if she doesn't give you a room, you'll burn down the whole inn.
The innkeeper, fearful of her life, gives you a room.
You think you should feel bad, but you don't.

You've lost karma, your sword barely glows red.

You go up to your room.
                                        """
                                        print """
There are a couple things you could do before bed:
inspect sword
read book
look around
go to bed
                                        """
                                        
                                        step08l = str(raw_input("What will you do?\n"))
                                        if (step08l == "inspect sword"):
                                            print """
You take out your sword, looking over it.
The first thing you see are three runes etched into the sword.
They are barely glowing a menacing red.
The blade itself has started to fade into a darker color.
You don't see anything else interesting with the sword.
You sheathe your sword.
                                            """
                                            step08l = str(raw_input("What will you do?\n"))
                                            if (step08l == "inspect sword"):
                                                print """
You take out your sword, looking over it.
The first thing you see are three runes etched into the sword.
They are barely glowing a menacing red.
The blade itself has started to fade into a darker color.
You don't see anything else interesting with the sword.
You sheathe your sword.
                                                """
                                                step08l = str(raw_input("What will you do?\n"))
                                                if (step08l == "inspect sword"):
                                                    print """
You take out your sword, looking over it.
The first thing you see are three runes etched into the sword.
They are barely glowing a menacing red.
The blade itself has started to fade into a darker color.
You don't see anything else interesting with the sword.
You sheathe your sword.
                                                    """
                                        if (step08l == "read book"):
                                            print """
As you start to open the book, it tries to resist.
You force it open.
You flip through the pages of the book.
All of a sudden, the pages lock onto a specific page.
"THE END OF DAYS"
"...one of the omens of the end...a man with a cursed blade...
demons versus angels...champions will clash...
the Seraphim and the Harbinger will fight..."
The book then slams shut, when you try to open it back up, you can't.
                                            """
                                            step08l = str(raw_input("What will you do?\n"))
                                            if (step08l == "read book"):
                                                print """
You try to open the book, but it resists.
Maybe it rejects those with bad karma...
                                                """
                                                step08l = str(raw_input("What will you do?\n"))
                                                if (step08l == "read book"):
                                                    print """
You try to open the book, but it resists.
Maybe it rejects those with bad karma...
                                                    """
                                            if (step08l == "look around"):
                                                print """
You look around the room.
There's a bed in the corner, along with a end table with a candle on it.
There's also a wardrobe sitting against a wall, but it's empty.
There's a small table along with two chairs in the center of the room.
Nothing else interests you about the room.
                                                """
                                                step08l = str(raw_input("What will you do?\n"))
                                                if (step08l == "look around"):
                                                    print """
You look around the room.
There's a bed in the corner, along with a end table with a candle on it.
There's also a wardrobe sitting against a wall, but it's empty.
There's a small table along with two chairs in the center of the room.
Nothing else interests you about the room.
                                                    """
                                                    step08l = str(raw_input("What will you do?\n"))
                                            if (step08l == "go to bed"):
                                                print """
You climb into the bed and fall asleep.

You wake up to screams in the village.
You jump out of bed and grab your items.
The book is gone.

You rush out of the inn to see a giant hole in the ground.
You see many demons tormenting the villagers.
You charge at one of the demons and swing at one of them.
Your sword refuses your attempt.
The demons all look at you, they exclaim,
"That's him!"
One of the demons grab you and they all retreat down the hole.
The demons then stop at a gate, and utter a strange phrase, likely in their native tongue.
The gate swings open and they all rush in.
A giant figure emerges from a wall of fire, the demons run out of the room.
There's no doubt about it, this is hell.
And this is the devil.
He orders you to raise your sword.
                                                """
                                                step09l = str(raw_input("Raise your sword? (yes/no)\n"))
                                                if (step09l == "no"):
                                                    print """
The devil laughs at your incopitence, and orders you again.
                                                    """
                                                    step09l = str(raw_input("raise your sword? (yes/no)\n"))
                                                    if (step09l == "no"):
                                                        print """
The devil's face drops, and looks at you for a moment.
He then laughs and says,
"You are not the one I saw."
He then flicks his wrist and stalagmites fall from the ceiling, impaling you.
                                                        """
                                                        print """
Game over.
                                                        """
                                                if (step09l == "yes"):
                                                    print """
You raise your sword to the ceiling.
A smile creeps across the devil's face.
"Finally, my Harbinger has arisen!"
He starts to cast some sort of fireball at you, but your sword jumps infront of you.
Your sword seems to absorb all the power from the fireball.
The devil says,
"For eons I have waited, planning for this crucial moment. Take this sword.
This weapon was used by the great angel Archiel to battle the forces of hell.
When he was overrun by my forces, we took the sword, and twisted it.
It had become the most powerful weapon we've ever created.
The power of the angel's steel in a blade of darkness.
Its name..."
The blade whispers to you.
"...Xal'atath..."

The blade sits above the ground, hovering for you to take.
It looks more malevolent than ever.
The three runes on the blade now glow a bright red, almost flaming.
The blade itself seems to have shifted from its two sided self, to that of a one sided blade.
Its handle and hilt have formed black, spire like growths, seeming to drip blood.
The blade beckons you to take it.
"""
                                                    step10l = str(raw_input("Will you take it? (yes/no)\n"))
                                                        print """
Part of you resists, but regardless, you step forward.
As you reach for Xal'atath, you already feel its power.
If any blade could take down an army, it'd be this blade.
...and you'd be its wielder.
You grasp the grip of the blade, and something happens...
You immediately feel overwhelmed with power.
The power of every demon courses through your veins.

The devil gleefully looks upon you, his champion.
He says,
"Now, we take the fight to the heavens!
My forces are already storming the high gates in the sky.
Take this portal when you are ready."

As you approach the dark portal, the devil says,
"If you suceed, infinite power will be yours."
You step through the portal.

Your eyes are bombarded with a bright light, almost blinding.
You shrug it off, and press forward.
One of the angels spot you, they yell,
"He is here! The Harbinger has shown himself! Overwhelm him while you can!"
The angels charge you.
                                                        """
                                                        step11l == str(raw_input("How do you attack?\n"))
                                                        print """
The angels charge you, but you are the Harbinger.
You cataclysmically swing your sword at one of the angels.
He's instantly obliterated.
You've made a giant crack in the holy ground by the impact of Xal'atath.
One of the angels start to disintegrate before your eyes.
You feel no remorse.
Fire starts to rise from the ground.
The angels continue to charge you.
Hundreds of angels are upon you.
You are overwhelmed.

But...

None can challenge you.
They all fall to your might.
It seems you are winning.

After minutes of slaughtering countless angels, a voice erupts of of them.
"ENOUGH!"
A figure moves forward.
All of the angels fall to the ground, kneeling before this chosen angel.
"Harbinger, your pathetic crusade ends here!
The minions of hell should have been wiped out long ago, but no more!"
He swings his sword at you.
A sharp slash of light flys through the air.
He misses you by a couple feet, but he wasn't aiming for you.
All of the demons following you through are immediately destroyed.
The portal, being hit with the full beam of light, crumbles.
You are trapped in the heavens.

However...

This is the final battle.
The Seraphim versus the Harbinger.
You cannot fail, you must not fail.
You step forward.
The Seraphim steps forward.
Both of you lock eyes for what seems like an eternity.
Finally, both of you draw your swords.
                                                        """
                                                        step12l = str(raw_input("How will you attack the Seraphim?\n"))
                                                        if (step12l == "swing sword"):
                                                            print """
You dash towards the Seraphim and swing your sword.
The Seraphim dodges to the left, and swings back.
You move to parry his blow.
Your swords clash and you are both left at a stalemate.
                                                            """
                                                            step12l = str(raw_input("How will you attack the Seraphim?\n")
                                                
                            
                            
                            
                            