import random
class player:
    health = 10
    damage = 1
    level = 1
    weapon = 'no weapon'
class RegularEnemy:
    health = 10
    damage = 1
    level = 1
class MolagVaal:
    health = 1000
    damage = 100
    level = 666
def mainmenu():
    print("------------------")
    print("your level - ", player.level)
    print("your health - ", player.health)
    print("your damage - ", player.damage)
    print("your weapon - ", player.weapon)
    print("------------------")

def battle(npc):
    global runflag
    print(f"You're battling a level {npc.level} {npc.__name__}!")
    print(f"npc health = {npc.health}")
    print(f"npc damage = {npc.damage}")
    print()
    while npc.health>0:
        print("player health - ", player.health)
        print("npc health - ", npc.health)
        print("[1] - atack!")
        print("[2] - heal yourself")
        print("[3] - run away")
        option = input()
        while option == '':
            option = input()
        option = int(option)
        if option == 3:
            runflag = 1
            break
        if option == 1:
            npc.health-=player.damage
            if npc.health==0:
                print("you won!")
                break
        if option == 2:
            player.health+=5
        player.health-=npc.damage
        if player.health <=0:
            print("you lost")
            break

weapon_prefix = ['mighty', 'shitty', 'braindead', 'cursed', 'golden', 'shiny']
weapon_suffics = ['sword', 'longsword', 'spear', 'dagger', 'katana', 'morgenstar']

runflag = 0
print("Welcome to the game!. Press enter to start")
input()
while True:
    print("[1] - main menu")
    print("[2] - to battle")
    print("[3] - EXIT")
    if player.health<9+player.level:
        print("[4] - meditate and heal yourself")
    print("[666] - Battle The Molag Vaal (extremely hard)")
    print()
    option = input()
    while option=='':
        option = input()
    option = int(option)
    if option == 1:
        mainmenu()
    if option == 2:
        RegularEnemy.level = random.randint(player.level, player.level + 3)
        RegularEnemy.health = random.randint(player.health - 6, player.health + 3)
        RegularEnemy.damage = random.randint(1 + RegularEnemy.level, RegularEnemy.level + 5)
        battle(RegularEnemy)
        if player.health > 0 and runflag==0:
            player.level+=1
            player.damage+=1
            player.health+=1
        drop = random.randint(1, 10)
        if drop == 5:
            weapon = weapon_prefix[random.randint(0,5)] + " " +weapon_suffics[random.randint(0,5)]
            print(f'You got a new weapon - {weapon}')
            print("[1] - equip")
            print("[2] - discard")
            option = input()
            while option == '':
                option = input()
            option = int(option)
            if option == 1:
                player.weapon = weapon
            if option == 2:
                continue
    runflag = 0
    if option==3:
        break
    if option == 4:
        if player.health<9+player.level:
            player.health = 9 + player.level
            print("you meditate and are now at full health!")
        else:
            print("Error! Already at full health")
    if option==666:
        battle(MolagVaal)
        if player.health > 0 and runflag == 0:
            player.level += 100
            player.damage += 100
            player.health += 100
            print("Congratulations! You completed my game. Thanks for playing!")