from classes.game import bcolors, Person

magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 10, "dmg": 124},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "An Enemy Attacks" + bcolors.ENDC)

while running:
    print("==========================")
    player.choose_action()
    choice = input("Choose Action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for ", dmg, " points of damage. Enemy HP: ", enemy.get_hp())

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemey attacks for ", enemy_dmg, " Player HP: ", player.get_hp())

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your Enemy Has defeated you" + bcolors.ENDC)
        running = False
    # running = False
