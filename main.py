import time,os,random

char_hp = []
char_str = []
enemy_hp = []
enemy_str = []


lvlone = ['You encounter a goblin',
          'meet trader','find a shiny fruit',]
lvltwo = ['dungeon','gaurd merchant']

def roll(a,b):
  result = random.randint(a,b)
  return result


def build_char():
  print("Build your character\n")
  name = input("Name your Legend:\n")
  race = input("Character Type (Human, Elf,Beast, Orc):\n")
  class_type = input("choose your class(Warrior,Assassin,Archer,Mage):\n")
  print(name, "|", race,class_type)
  health = roll(8,15)
  char_hp.append(health)
  strength = roll(8,15)
  char_str.append(strength)
  print(f"HEALTH:",health)
  print(f"STRENGTH:",strength)

def level_one():
    rand = random.randint(0,2)
    encounter = lvlone[rand]
    encounter = encounter.split()
    for i in range(len(encounter)):
       if 'goblin' in encounter[i]:
          print('You encounter an angry goblin')
          gob_choice = input('Do you fight the goblin or run away:\n').lower()
          if input == 'fight':
            goblin()
          else:
             print("The goblin chases you but you eventually lose it and manage to get away")

       elif 'trader' in encounter[i]:
          print('You meet a suspicious trader')
          tra_choice = input

       elif 'fruit' in encounter[i]:
          print(" You find a shiny mysterious fruit ")
def goblin():
   gob_strength = roll(5,10)
   enemy_str.append(gob_strength)
   gob_health = roll(5,10)
   enemy_hp.append(gob_health)
   fight()



   
def fight():
         char_health = char_hp[0] 
         char_strength = (char_str[0] / float(2))
         enemy_strength = (enemy_str[0] / float(3))
         enemy_health = enemy_hp[0]
         while True:  
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
                  print('You have died\n')
                  exit()

build_char()
goblin()

