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

def level_one():
   print('You spawn into a forest\n')
   time.sleep(1)
   rand = random.randint(0,2)#choose random index 
   encounter = lvlone[rand]#chooses that scenario from lvl one 
   encounter = encounter.split()#splits up string into its own seperate list
   for i in range(len(encounter)):#goes through each list/index in our new list
      if 'goblin' in encounter[i]:#looks for the key words to begin that randomized scenario
         print('You encounter an angry goblin\n')
         gob_choice = input('Do you fight the goblin or run away:\n').lower()
         if gob_choice == 'fight':
            goblin()
         else:
            print("The goblin chases you but you eventually lose it and manage to get away\n")

      elif 'trader' in encounter[i]:
         print('You meet a suspicious trader\n')
         trader()
      elif 'fruit' in encounter[i]:
         print(" You find a shiny mysterious fruit\n")
         fruit()
   print("That was an interesting encounter you had\n")
   print('You find your wat out of the forest, after walking out you see the massive sign "ADVENTURER GUILD" and you begin to walk towards it\n')
     
    

   
          
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
            print("You turn to see the trader running away, laughing\n")
            sword_str = char_str[0] - 5
            char_str.clear()
            char_str.append(sword_str)
            print("You now have",char_str,'strength\n')
   else:
      print("You turn to away from the trader\n")
      time.sleep(1)
      print('You then suddenly feel a sharp pain from back... You got stabbed with a sword\n')
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
   print()    

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

      
    
os.system('clear')
print("WELCOME TO: DND RIP-OFF")
build_char()
level_one()
level_two()
