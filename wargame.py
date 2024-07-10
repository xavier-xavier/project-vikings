from vikingsClasses import Soldier, Viking, Saxon, War
import random

def main():
    war = War()
    soldier_names = ["Albert", "Andres", "Archie", "Dani", "David", "Gerard", "German", "Graham", "Imanol", "Laura"]

    # Create 5 Vikings
    for i in range(5):
        name = random.choice(soldier_names)
        health = 100
        strength = random.randint(10, 100)
        viking = Viking(name, health, strength)
        war.addViking(viking)

    # Create 5 Saxons
    for i in range(5):
        health = 100
        strength = random.randint(10, 100)
        saxon = Saxon(health, strength)
        war.addSaxon(saxon)

    round_number = 0
    while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        print(f"Round {round_number + 1}")
        
        # Viking attack
        viking_attack_result = war.vikingAttack()
        print(viking_attack_result)
        
        # Saxon attack
        saxon_attack_result = war.saxonAttack()
        print(saxon_attack_result)

        # Print current status
        print(f"Viking army size: {len(war.vikingArmy)}")
        print(f"Saxon army size: {len(war.saxonArmy)}")
        print(war.showStatus())
        
        round_number += 1
        print()

    # Final status
    print(war.showStatus())

if __name__ == "__main__":
    main()