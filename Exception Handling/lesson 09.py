# Gladiator Armour Exception Handling

class ArmourError(Exception):
    """Custom Exception for Armour Errors"""
    pass

class Gladiator:
    def __init__(self, armour):
        self.armour = armour

    def wear_armour(self):
        try:
            if self.armour == "broken":
                raise ArmourError("The armour is broken! Cannot wear it.")
            elif self.armour == "no_armour":
                raise ArmourError("No armour to wear!")
            else:
                print("The gladiator is wearing the armour!")
        except ArmourError as e:
            print(f"Error: {e}")

# Example 1: Gladiator has broken armour
gladiator1 = Gladiator("broken")
gladiator1.wear_armour()

# Example 2: Gladiator has no armour
gladiator2 = Gladiator("no_armour")
gladiator2.wear_armour()

# Example 3: Gladiator has valid armour
gladiator3 = Gladiator("steel")
gladiator3.wear_armour()

# Pakistani Lore Example - Handling with a mystical sword

class SwordError(Exception):
    """Custom Exception for Sword Errors"""
    pass

class Warrior:
    def __init__(self, sword):
        self.sword = sword

    def wield_sword(self):
        try:
            if self.sword == "broken":
                raise SwordError("The sword is broken! Cannot use it.")
            elif self.sword == "no_sword":
                raise SwordError("No sword to wield!")
            else:
                print("The warrior wields the sword with great strength!")
        except SwordError as e:
            print(f"Error: {e}")

# Example 4: Warrior has a broken sword
warrior1 = Warrior("broken")
warrior1.wield_sword()

# Example 5: Warrior has no sword
warrior2 = Warrior("no_sword")
warrior2.wield_sword()

# Example 6: Warrior has a legendary sword
warrior3 = Warrior("legendary_sword")
warrior3.wield_sword()
