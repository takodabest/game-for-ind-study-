import time,os,random

#list to store our character hp and str and the enemys hp and str for cross 
#function across our program.
char_hp = []
char_str = []
enemy_hp = []
enemy_str = []

#list of our random encounters for each level
lvlone = ['You encounter a goblin',
          'meet trader','find a shiny fruit',]
lvltwo = ['dungeon','guard merchant']
lvlthree = ['Raziel', 'Dragon']
# dice roll randomizer(not restricted to 1-6)
def roll(a,b):
  result = random.randint(a,b)
  return result

#function that builds our character based on the users choice of options
def build_char():
  print("Build your character\n")
  name = input("Name your Legend:\n")
  race = input("Character Type (Human, Elf,Beast, Orc):\n")
  class_type = input("choose your class(Warrior,Assassin,Archer,Mage):\n")
  print(name, "|", race,class_type)
  health = roll(8,15)
  char_hp.append(health)#stores our randomized health into the list
  strength = roll(8,15)
  char_str.append(strength)#stores our randomized strength
  print("HEALTH:",health)
  print("STRENGTH:",strength)
  print()
  time.sleep(2)
  os.system('clear')

def level_one():
   print('You enter into a dense, eerie forest. Peering through the trees enveloped by foliage and vegetation of an intense green, you traverse further and further until you hear a noise from the tall bushes. \n')
   time.sleep(1)
   rand = random.randint(0,2)#choose random index 
   encounter = lvlone[rand]#chooses that scenario from lvl one 
   encounter = encounter.split()#splits up string into its own seperate list
   for i in range(len(encounter)):#goes through each list/index in our new list
      if 'goblin' in encounter[i]:#looks for the key words to begin that randomized scenario
         print('You encounter an angry goblin. While unassuming for its small stature and no armor, it does wield a makeshift weapon in its hand. \n')
         gob_choice = input('Do you fight the goblin or run away:\n').lower()
         if gob_choice == 'fight':
            goblin()
         else:
            print("The goblin chases you but you eventually lose it and manage to get away\n")

      elif 'trader' in encounter[i]:
         print('You meet a suspicious trader. Dressed from heads to toe in a matte black leather cloak, he reaches inside his cloak to grab a sword. \n')
         trader()
      elif 'fruit' in encounter[i]:
         print(" You find a shiny mysterious fruit fallen from a nearby tree. \n")
         fruit()
   print("That was an interesting encounter you had. But you mustn't stop now, who knows if there are any lurking creatures around, or worse, other wicked humans. \n")
   print('You eventually find your way out of the forest, after walking out you see the massive sign stating, "ADVENTURER GUILD", and you begin to walk through its doors. \n')
     
    

   
          
def goblin():#our goblin
   gob_strength = roll(5,10)
   enemy_str.append(gob_strength)
   gob_health = roll(5,10)
   enemy_hp.append(gob_health)
   fight()
   enemy_hp.clear()
   enemy_str.clear()



   
def fight():#function which controls battles not restricted to one character
         char_health = char_hp[0] #chooses first index for our hp and str to put into variables
         char_strength = (char_str[0] / float(2))
         enemy_strength = (enemy_str[0] / float(3))
         enemy_health = enemy_hp[0]
         while True:#rolls a random number 1-6    
            char_roll = roll(1,6)
            if char_roll == 6 or char_roll == 4 or char_roll == 2 or char_roll == 1:
               print("You attack the enemy\n")
               time.sleep(2)
               enemy_health -= char_strength
               print(f"enemy has {enemy_health} health left\n")
               time.sleep(2)
               if enemy_health <= 0:
                  print("You have defeated the enemy\n")
                  time.sleep(2)
                  os.system("clear")
                  break
            else:
               print('You have been struck\n')
               time.sleep(2)
               char_health -= enemy_strength
               print(f"You have {char_health} health left\n")
               time.sleep(2)
               if char_health <= 0:
                  print('You have died: GAME OVER\n')
                  exit()


def trader():
   tra_choice = input("Trader offers you a sword, no strings attached do you accept it?:\n").lower()
   if tra_choice == 'yes':
       print("The trader gives you the sword\n")
       print(".........\n")
       time.sleep(1)
       sword = roll(1,3)
       if sword == 1 or sword == 2:
         print("You got a very powerful sword(+20 strength)\n")
         sword_str = char_str[0] + 20
         char_str.clear()
         char_str.append(sword_str)
       elif sword == 3:
            print("You grab the sword and suddenly start to feel weaker\n")
            print("The sword is cursed(-5 strength)\n")
            print("You turn to see the trader running away, cackling in delight of your foolishness. \n")
            sword_str = char_str[0] - 5
            char_str.clear()
            char_str.append(sword_str)
            print("You now have",char_str,'strength\n')
   else:
      print("You turn to away from the trader. Suspicious of what kind of man this mysterious trader is, and what kind of business you would get yourself into. \n")
      time.sleep(1)
      print('You then suddenly feel a sharp pain from back... You were stabbed from behind with a sword. \n')
      time.sleep(1)
      print('Trader: "HOW DARE YOU REJECT MY OFFER"\n')
      time.sleep(1)
      print("You bleed out to death: GAME OVER\n")
      exit()


def fruit():
   fruit_choice = input("Do you eat the fruit or leave?\n").lower()
   if fruit_choice == "yes":
      print("You eat the fruit\n")
      print(".........\n")
      time.sleep(1)
      fruit = roll(1,5)
      if fruit == 1:
         print("You gained (+10 HP) from the Fruit\n")
         hp = char_hp[0] + 10
         char_hp.clear()
         char_hp.append(hp)
      elif fruit == 2:
         print("You gained (+10 strength) from the fruit\n")
         str = char_str[0] + 10
         char_str.clear()
         char_str.append(str)
      elif fruit == 3:
         print("You lose (-3 HP) from the Fruit\n")
         hp = char_hp[0] - 3
         char_hp.clear()
         char_hp.append(hp)
      elif fruit == 4:
         print("You lose (-3 strength) from the Fruit\n")
         str = char_str[0] - 3
         char_str.clear()
         char_str.append(str)
      elif fruit == 5:
         print()
   elif fruit_choice == 'leave':
      print("you turn and walk away, as you walk away you bear jumps out of the bushes as attacks you\n")
      bear()

def bear():
   bear_strength = roll(20,30)
   enemy_str.append(bear_strength)
   bear_health = roll(20,30)
   enemy_hp.append(bear_health)
   fight()
   enemy_hp.clear()
   enemy_str.clear()


def level_two():
   print('You walk in through the entrance of the Adventurer Guild\n')
   print('you talk to the guild receponist and she welcomes you, she says theres a mission that just came in this morning\n')
   time.sleep(1)
   rand = random.randint(0,1)#choose random index 
   encounter = lvltwo[rand]#chooses that scenario from lvl one 
   encounter = encounter.split()#splits up string into its own seperate list 
   for i in range(len(encounter)):
      if 'merchant' in encounter[i]:
         guard_merchant()
      elif 'dungeon' in encounter[i]:
         print()


def guard_merchant():
   print("The guild receponist tells you your missison is guard a merchant as he deliveres goods through a forest\n")
   time.sleep(2)
   print("Before you leave the receponist gives you a new sword and chestplate(+45 hp and str)\n")
   time.sleep(2)
   hp = char_hp[0] + 45
   char_hp.clear()
   char_hp.append(hp)
   str = char_str[0] + 45
   char_str.clear()
   char_str.append(str)
   time.sleep(2)
   print('You meet the merchant and you begin the mission but as you are halfway through the forest a group of bandits ambushes you\n')
   choice = input('Do you fight off the bandits or do you run away and give up the merchants\n').lower()
   if choice == 'fight':
      time.sleep(2)
      print("You begin to fight the bandits. Three lower level bandits and the bandit group leader\n")
      bandit()
      bandit()
      bandit()
      bandit_leader()
   elif choice == 'run':
      print("you get away and later find out the merchant got killed and all his good stolen\n")
      print("The guild revoked your license to adventure and you are now forever a failure: GAME OVER\n")
      exit()

def dungeon():
   print('The receponist says your mission is to raid a dungeon and bring back the group of adventurers that got lost inside\n')
   time.sleep(2)
   print("Before you leave the receponist gives you a new sword and chestplate(+45 hp and str)\n")
   time.sleep(2)
   hp = char_hp[0] + 45
   char_hp.clear()
   char_hp.append(hp)
   str = char_str[0] + 45
   char_str.clear()
   char_str.append(str)
   time.sleep(2)
   print('You make your way inside the dungeon which is within a cave. You kill a couple of skeletons and goblins and then find a big wooden door\n')
   time.sleep(2)
   print('you open the door and find a big open room and their you find the missing advenurers you go up to check on them and then the big door behind closes and large skelton giant appears behind you\n')
   time.sleep(2)
   print('The skeleton giant is ready to attack you have to fight to survive\n')
   skeleton()
   print("You defeated the skeleton and then help the travelers get out of the dungeon but on  your way out of the boss room you notice and shiny new chestplate(+50 health)\n")
   hp = char_hp[0] + 50
   char_hp.clear()
   char_hp.append(hp)

def skeleton():
   skel_strength = roll(50,55)
   enemy_str.append(skel_strength)
   skel_health = roll(80,90)
   enemy_hp.append(skel_health)
   fight()
   enemy_hp.clear()
   enemy_str.clear()

def bandit():
   ban_strength = roll(40,45)
   enemy_str.append(ban_strength)
   ban_health = roll(45,50)
   enemy_hp.append(ban_health)
   fight()
   enemy_hp.clear()
   enemy_str.clear()

def bandit_leader():
   ban_strength = roll(50,60)
   enemy_str.append(ban_strength)
   ban_health = roll(60,65)
   enemy_hp.append(ban_health)
   fight()
   enemy_hp.clear()
   enemy_str.clear()  

      
    

def level_three():
   rand = random.randint(0,1)
   encounter = lvlthree[rand]
   encounter = encounter.split()
   for i in range(len(encounter)):
     if 'Raziel' in encounter[i]:
       print("You proceed through the creeping hallways and enter a large hollowed chamber with a marble slab table at its center. You see what appears to be an apparition wearing a white cloak, suspended above the table. \n")
       time.sleep(3)
       print("You proceed towards it with caution. As you come close to it, you meet face-to-face with the being. Standing in awe you try to take in what you are seeing, but the creature mutters out an incomprehensible language that startles you. Then it moves. \n")
       Boss1Actions()
     elif 'Dragon' in encounter[i]:
       print("Progressing through a colossal cave of dirt and stone, you come into contact with a uncountable amount of gold and treasure laying all around you in the edges of the room. At the very center lays rest' an enormous, scaled beast. Coiled in its own body it slumbers asleep. Upon closer inspection, you realize that the beast is none other than a great dragon.")
       time.sleep(3)
       print("You notice a pathway on the opposite side of the room behind the giant monster, but a cold sweat washes down your whole body. The thought of awakening the behemoth is an instant death sentence. But you can't turn back now, not with how far you've gotten, how close you are towards the end.")
       
def Boss1Actions():
  RazielActions = roll(1,2)
  if RazielActions == 1:
    BossFight1()
  elif RazielActions == 2:
    RazielSpeak()

def BossFight1():
  print("The figure begins to hover towards you slowly, before plunging into the ground. The figure speaks to your once more, and although you still can't seem to make out what its saying, you do hear it say the word Raziel. \n")
  time.sleep(2)
  print("Suddenly, it clasp its hands and begins drawing them outwards, creating a large spear-like weapon of regal design and structure. Then assumes a fighting stance. \n")
  choice = input("Do you wish to fight Raziel or flee?: \n").lower()
  if choice == 'fight':
    time.sleep(2)
    print("You draw your weapon and steel yourself for the incoming battle. \n")
    Raziel()

def RazielSpeak():
   print("The figure begins to hover towards you slowly, before plunging into the ground. It looks up at you and articulates a foreign language unknown to the ears, but understandable to the soul. You feel yourself in the presence of Raziel, the Anoited God. \n")
   time.sleep(3)
   print("Suddenly, it snaps it fingers and you being to feel the world around you reform. The ground you stand on feels non-existent, the air you breathe feels almost pleasurable and fresh, you begin to understand everything around you but you don't know why. \n")
   time.sleep(3)
   print("Then, Raziel walks towards you. It vocalizes a question, inquiring the reason for your presence here. \n")
   time.sleep(3)
   choice = input("Do you answer truthfully or lie?: \n").lower()
   if choice == 'truth':
     os.system('clear')
     time.sleep(2)
     print("You tell Raziel about your adventures through the dungeon and of the many monsters and people you've met. Raziel stands idle as if listening to you speak. It then points to the forked hallway behind it.")
     choice = input("Do you head left or right?: \n")
     if choice == 'left':
       print()
     else:
       print()
   elif choice == 'lie':
     os.system('clear')
     time.sleep(2)
     print("You fabricate a story about your triumphs, accomplishments, and how special of a person you are. You brazzenly demand that Raziel must let you through in the name of glory. Raziel stands idle as if listening to you speak. It then points to the spiral staircase that leads downward to the unknown abyss and the other that leads upward to a blinding light too overwhelming to look at. \n")
     choice = input("Do you head up or down?: \n")
     if choice == 'up':
       print()
     else:
       print()
     
def BossFight2A():
  print("As you attempt to move around the dragon as quietly as possible, you hear the sound of scrapping stone and cluttering gold coins move beside you. Thinking that the beast has awoken you quickly turn around to see a plume of dirt, dust, and debris. Emerging from that smog you witness the sheer scale of this dragon. Standing on its four legs and barring teeth larger than yourself, you come to understand that death is inevitable. \n")
  time.sleep(4)
  print("All the memories throughout your life flash through your mind, but the earth-shattering roar of Yttriox brings you back into the cruel reality of life. Knowing that you were doom from the start, you draw your weapon in an absurd endevour to fight for your life to the bitter end. \n")
  time.sleep(3)
  Dragon()

def BossFight2B():
  print("Stealthfully operating around the cave, you evade the mess of coins sprawled along the dirt floor as to not make any sudden noise. Getting closer and closer to the end of the cave you feel a sense of unparalleled delight, believing that you truly are about to make it out alive. However, the unexpected rumbling of the ground forces you to hide. So you stow away inside a nearby opened treasure chest.")
  time.sleep(4)
  print("Peeking through the slit you see the dragon shaking the dust off itself and peering around the room, investigating the location of what woke it up. ")


def Raziel():
  raz_strength = roll(250, 300)
  enemy_str.append(raz_strength)
  raz_health = roll(300, 400)
  enemy_hp.append(raz_health)
  fight()
  enemy_hp.clear()
  enemy_str.clear()

def Dragon():
  drag_strength = roll(300, 350)
  enemy_str.append(drag_strength)
  drag_health = roll(250, 300)
  enemy_hp.append(drag_health)
  fight()
  enemy_hp.clear()
  enemy_str.clear()

os.system('clear')
print("WELCOME TO: DND RIP-OFF")
build_char()
level_one()
level_two()
level_three()
