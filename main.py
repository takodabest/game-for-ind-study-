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
lvltwo = ['dungeon','gaurd merchant']
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
  print(f"HEALTH:",health)
  print(f"STRENGTH:",strength)
  print()

def level_one():
    rand = random.randint(0,2)#choose random index 
    encounter = lvlone[rand]#chooses that scenario from lvl one 
    encounter = encounter.split()#splits up string into its own seperate list
    for i in range(len(encounter)):#goes through each list/index in our new list
       if 'goblin' in encounter[i]:#looks for the key words to begin that randomized scenario
          print('You encounter an angry goblin')
          gob_choice = input('Do you fight the goblin or run away:\n').lower()
          if input == 'fight':
            goblin()
          else:
             print("The goblin chases you but you eventually lose it and manage to get away\n")

       elif 'trader' in encounter[i]:
          print('You meet a suspicious trader\n')
          trader()
       elif 'fruit' in encounter[i]:
          print(" You find a shiny mysterious fruit ")
          






def goblin():#our goblin
   gob_strength = roll(5,10)
   enemy_str.append(gob_strength)
   gob_health = roll(5,10)
   enemy_hp.append(gob_health)
   fight()



   
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
         print("You got a very powerful sword(+10 strength)\n")
         str = char_str[0]
         sword_str = str + 10
         char_str.clear()
         char_str.append(sword_str)
       elif sword == 3:
            print("You grab the sword and suddenly start to feel weaker\n")
            print("The sword is cursed(-5 strength)\n")
            print("You turn to see the trader running away, laughing\n")
            str = char_str[0]
            sword_str = str - 5
            char_str.clear()
            char_str.append(sword_str)
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
   fruit_choice = input("Do you eat the fruit or leave it?")

       
      
        
os.system('clear')
print("WELCOME TO: DND RIP-OFF")
build_char()
