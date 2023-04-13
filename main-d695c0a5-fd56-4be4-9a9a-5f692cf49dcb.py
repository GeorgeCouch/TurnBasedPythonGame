# Import for random number generation
from numpy.random import randint

# Import time for simulating enemy thinking
import time

# Import Tkinter for outcome display
from tkinter import *

# Global vars
remainingPartyMembers = 0
remainingFriendlyPartyMembers = 0
remainingEnemyPartyMembers = 0
friendlyPartyMembers = []
enemyPartyMembers = []
items = []

# Classes
# Base class for every party member
class PartyMember():
    def __init__(self, name: str, health: int, damage: int, mana: int, hasTakenTurn: bool):
        self.name = name
        self.health = health
        self.damage = damage
        self.mana = mana
        self.hasTakenTurn = hasTakenTurn
        # Add to total remaining party members on initialization
        global remainingPartyMembers
        remainingPartyMembers += 1

    # Method for attacking
    def attack(self):
        return int(self.damage)

# Classes that inherrit from PartyMember class
# Base class for every friendly party member
class FriendlyPartyMember(PartyMember):
    def __init__(self, name: str, health: int, damage: int, mana: int, hasTakenTurn: bool):
        super().__init__(name, health, damage, mana, hasTakenTurn)
        # Append to friendlyPartyMembers list on initialization
        friendlyPartyMembers.append(self)
        # Add to total remaining friendly party members on initialization
        global remainingFriendlyPartyMembers
        remainingFriendlyPartyMembers += 1

# Base class for every enemy party member
class EnemyPartyMember(PartyMember):
    def __init__(self, name: str, health: int, damage: int, mana: int, hasTakenTurn: bool):
        super().__init__(name, health, damage, mana, hasTakenTurn)
        # Append to enemyPartyMembers list on initialization
        enemyPartyMembers.append(self)
        # Add to total remaining enemy party members on initialization
        global remainingEnemyPartyMembers
        remainingEnemyPartyMembers += 1

# Classes that inherrit from FriendlyPartyMember Class
# Each one has a useSpell funciton that subtracts mana and deals damage, if not enough mana return 0
class Warrior(FriendlyPartyMember):
    def __init__(self, name: str, health: int, damage: int, mana: int, hasTakenTurn: bool):
        super().__init__(name, health, damage, mana, hasTakenTurn)

    def useSpell(self):
        print("\nWarrior uses Berserker's Rage!")
        tmpMana = self.mana
        self.mana -= 70
        if (self.mana <= 0):
            self.mana = tmpMana
            print("Not enough mana to cast spell!")
            return 0
        else:
            return 80

class Mage(FriendlyPartyMember):
    def __init__(self, name: str, health: int, damage: int, mana: int, hasTakenTurn: bool):
        super().__init__(name, health, damage, mana, hasTakenTurn)

    def useSpell(self):
        print("\nMage uses Black Fireball!")
        tmpMana = self.mana
        self.mana -= 40
        if (self.mana <= 0):
            self.mana = tmpMana
            print("Not enough mana to cast spell!")
            return 0
        else:
            return 50

class Archer(FriendlyPartyMember):
    def __init__(self, name: str, health: int, damage: int, mana: int, hasTakenTurn: bool):
        super().__init__(name, health, damage, mana, hasTakenTurn)

    def useSpell(self):
        print("\nArcher uses Piercing Shot!")
        tmpMana = self.mana
        self.mana -= 30
        if (self.mana <= 0):
            self.mana = tmpMana
            print("Not enough mana to cast spell!")
            return 0
        else:
            return 40

# Classes that inherrit from EnemyPartyMember Class
# Each one has a useSpell funciton that subtracts mana and deals damage, if not enough mana return 0
class Dog(EnemyPartyMember):
    def __init__(self, name: str, health: int, damage: int, mana: int, hasTakenTurn: bool):
        super().__init__(name, health, damage, mana, hasTakenTurn)

    def useSpell(self):
        print("\nDog uses Deafening Howl!")
        tmpMana = self.mana
        self.mana -= 60
        if (self.mana <= 0):
            self.mana = tmpMana
            print("Not enough mana to cast spell!")
            return 0
        else:
            return 20

class Pirate(EnemyPartyMember):
    def __init__(self, name: str, health: int, damage: int, mana: int, hasTakenTurn: bool):
        super().__init__(name, health, damage, mana, hasTakenTurn)

    def useSpell(self):
        print("\nPirate uses Kracken's Fury!")
        tmpMana = self.mana
        self.mana -= 90
        if (self.mana <= 0):
            self.mana = tmpMana
            print("Not enough mana to cast spell!")
            return 0
        else:
            return 70

class Vampire(EnemyPartyMember):
    def __init__(self, name: str, health: int, damage: int, mana: int, hasTakenTurn: bool):
        super().__init__(name, health, damage, mana, hasTakenTurn)

    # This function also heals the vampire
    def useSpell(self):
        print("\nVampire uses Blood Sacrifice!")
        tmpMana = self.mana
        self.mana -= 70
        if (self.mana <= 0):
            self.mana = tmpMana
            print("Not enough mana to cast spell!")
            return 0
        else:
            self.health += 30
            return 80

# Function for selecting intended party member from party members that have not taken their turn
def selectPartyMember(numSelected, partyMembersWaiting):
    numSelected -= 1
    # Print results for party member selected
    print("\nSelected: " + partyMembersWaiting[numSelected].name)
    print("Current Health: ", partyMembersWaiting[numSelected].health)
    print("Current Mana: ", partyMembersWaiting[numSelected].mana)
    # return party member
    return partyMembersWaiting[numSelected]

def friendlyPartyMemberAction(partyMember):
    # Get global vars
    global remainingEnemyPartyMembers
    global remainingPartyMembers
    # Prompt user for action
    print("\nWhat would you like this party member to do?: ")
    print("1 - Attack")
    print("2 - Use Spell")
    print("3 - Use Item")
    partyMemberActionChoice = input("\nEnter the corresponding number for the action you'd like to select: ")
    partyMemberActionChoice = int(partyMemberActionChoice)
    
    # Ask user what party member they would like to attack
    if (partyMemberActionChoice == 1):
        print("\nYou have chosen attack!")
        print("\nWhich enemy party member would you like to attack?")
        # Get all living enemy party members
        i = 1
        for x in enemyPartyMembers:
            print(i, "-", x.name)
            i += 1
        partyMemberChoice = input("\nEnter the corresponding number for the party member you'd like to select: ")
        partyMemberChoice = int(partyMemberChoice)
        partyMemberChoice -= 1
        # Subtract health from attacked enemy
        enemyPartyMembers[partyMemberChoice].health -= partyMember.attack()
        # Set health to 0 if it falls below 0
        if (enemyPartyMembers[partyMemberChoice].health < 0):
            enemyPartyMembers[partyMemberChoice].health = 0
        # Print update to user
        print("\n" + enemyPartyMembers[partyMemberChoice].name + " has", enemyPartyMembers[partyMemberChoice].health, "health remaining!")
        # Remove enemy from living members if no health remaining
        if (enemyPartyMembers[partyMemberChoice].health <= 0):
            enemyPartyMembers.remove(enemyPartyMembers[partyMemberChoice])
            # Subtract party members remaining
            remainingEnemyPartyMembers -= 1
            remainingPartyMembers -= 1
    
    # Ask user what party member they would like to use a spell on
    if (partyMemberActionChoice == 2):
        print("\nYou have chosen to cast a spell!")
        print("\nWhich enemy party member would you like to use a spell on?")
        # Get all living enemy party members
        i = 1
        for x in enemyPartyMembers:
            print(i, "-", x.name)
            i += 1
        partyMemberChoice = input("\nEnter the corresponding number for the party member you'd like to select: ")
        partyMemberChoice = int(partyMemberChoice)
        partyMemberChoice -= 1
        # Subtract health from enemy which spell was used on
        enemyPartyMembers[partyMemberChoice].health -= partyMember.useSpell()
        # Set health to 0 if it falls below 0
        if (enemyPartyMembers[partyMemberChoice].health < 0):
            enemyPartyMembers[partyMemberChoice].health = 0
        # Set mana to 0 if it falls below 0
        if (partyMember.mana < 0):
            partyMember.mana = 0
        # Print update to user
        print("\n" + partyMember.name + " has", partyMember.health, "health and", partyMember.mana, "mana remaining!")
        print("\n" + enemyPartyMembers[partyMemberChoice].name + " has", enemyPartyMembers[partyMemberChoice].health, "health remaining!")
        # Remove enemy from living members if no health remaining
        if (enemyPartyMembers[partyMemberChoice].health <= 0):
            enemyPartyMembers.remove(enemyPartyMembers[partyMemberChoice])
            # Subtract party members remaining
            remainingEnemyPartyMembers -= 1
            remainingPartyMembers -= 1

    # Ask user to select an item if they haven't used all of them already
    if (partyMemberActionChoice == 3):
        print("\nYou have chosen to use an item!")
        if (len(items) == 0):
            print("\nThere are no more items! You took too long looking for one wasted your turn!")
        else:
            print("\nWhich item would you like to use?")
            # Get existing items as options
            i = 1
            for x in items:
                print(i, "-", x)
                i += 1
            partyMemberChoice = input("\nEnter the corresponding number for the item you'd like to select: ")
            partyMemberChoice = int(partyMemberChoice)
            partyMemberChoice -= 1
            # Print for formatting
            print()
            # Remove item based on value found
            if (items[partyMemberChoice] == "Health Potion"):
                # Add health, print, remove health potion
                partyMember.health += 50
                print(partyMember.name + " now has", partyMember.health, "health!")
                items.remove("Health Potion")
            elif (items[partyMemberChoice] == "Mana Potion"):
                # Add mana, print, remove mana potion
                partyMember.mana += 50
                print(partyMember.name + " now has", partyMember.mana, "mana!")
                items.remove("Mana Potion")
            elif (items[partyMemberChoice] == "Strength Potion"):
                # Add damage, print, remove strength potion
                partyMember.damage += 50
                print(partyMember.name + " now deals", partyMember.damage, "damage!")
                items.remove("Strength Potion")

    # Set turn taken to true so that you can't perform more actions with this party member until enemy turn is complete
    partyMember.hasTakenTurn = True

def enemyPartyMemberAction(partyMember):
    # Get global vars
    global remainingFriendlyPartyMembers
    global remainingPartyMembers
    # Print enemy name and wait for 2.5 seconds
    print("\nThe " + partyMember.name + " is selecting an action...")
    time.sleep(2.5)
    # Generate number between 0 and 1
    enemyAction = randint(2)
    
    # Attack if generated 0
    if (enemyAction == 0):
        # Generate random number to select enemy target
        enemyTarget = randint(len(friendlyPartyMembers))
        # Subtract health from enemy target using enemy damage
        friendlyPartyMembers[enemyTarget].health -= partyMember.attack()
        # Set enemy target health to 0 if it falls below 0
        if (friendlyPartyMembers[enemyTarget].health < 0):
            friendlyPartyMembers[enemyTarget].health = 0
        # Print update for user
        print("\n" + partyMember.name + " attacked " + friendlyPartyMembers[enemyTarget].name)
        print("\n" + friendlyPartyMembers[enemyTarget].name + " has", friendlyPartyMembers[enemyTarget].health, "health remaining!")
        # Remove enemy target from list if health falls below or equal to 0 so that it won't be targetted anymore
        if (friendlyPartyMembers[enemyTarget].health <= 0):
            friendlyPartyMembers.remove(friendlyPartyMembers[enemyTarget])
            # Subtract party members remaining
            remainingFriendlyPartyMembers -= 1
            remainingPartyMembers -= 1
    
    # Use spell if generated 1
    if (enemyAction == 1):
        # Generate random number to select enemy target
        enemyTarget = randint(len(friendlyPartyMembers))
        # Subtract health from enemy target using spell damage
        friendlyPartyMembers[enemyTarget].health -= partyMember.useSpell()
        # Set enemy target health to 0 if it falls below 0
        if (friendlyPartyMembers[enemyTarget].health < 0):
            friendlyPartyMembers[enemyTarget].health = 0
        # set enemy mana to 0 if it falls below 0
        if (partyMember.mana < 0):
            partyMember.mana = 0
        # Print update for user
        print(partyMember.name + " used a spell on " + friendlyPartyMembers[enemyTarget].name)
        print("\n" + partyMember.name + " has", partyMember.health, "health and", partyMember.mana, "mana remaining!")
        print("\n" + friendlyPartyMembers[enemyTarget].name + " has", friendlyPartyMembers[enemyTarget].health, "health remaining!")
        # Remove enemy target from list if health falls below or equal to 0 so that it won't be targetted anymore
        if (friendlyPartyMembers[enemyTarget].health <= 0):
            friendlyPartyMembers.remove(friendlyPartyMembers[enemyTarget])
            # Subtract party members remaining
            remainingFriendlyPartyMembers -= 1
            remainingPartyMembers -= 1

    # Set turn taken to true so that you can't perform more actions with this party member until enemy turn is complete
    partyMember.hasTakenTurn = True

def main():
    # Objects for Friendly Party Members
    warrior = Warrior("Warrior", 100, 20, 100, False)
    mage = Mage("Mage", 100, 10, 100, False)
    archer = Archer("Archer", 100, 25, 100, False)

    # Objects for Enemy Party Members
    dog = Dog("Dog", 100, 40, 100, False)
    pirate = Pirate("Pirate", 100, 20, 100, False)
    vampire = Vampire("Vampire", 100, 10, 100, False)

    # Add items to item list
    global items
    items.append("Health Potion")
    items.append("Mana Potion")
    items.append("Strength Potion")

    # Intro Message
    print("\n\n***Defeat the enemy party before they defeat yours!***\n")

    # While loop to continue game so long as both parties have at least one member with health above 0
    friendlyMembersLiving = True
    enemyMembersLiving = True
    while friendlyMembersLiving and enemyMembersLiving:
        # Print the current game state
        print("Current game state:\n")
        print("Total party members remaining:", remainingPartyMembers)
        print("\nFriendly Party members remaining:", remainingFriendlyPartyMembers)
        for x in friendlyPartyMembers:
            print(x.name + ": Health:", x.health, ", Mana:", x.mana)
        print("\nEnemy Party members remaining:", remainingEnemyPartyMembers)
        for x in enemyPartyMembers:
            print(x.name + ": Health:", x.health, ", Mana:", x.mana)
        # Var for counting if every party member has taken their turn
        friendlyTurnsTaken = 0
        # While loop that breaks when every party member has taken their turn
        while friendlyTurnsTaken < len(friendlyPartyMembers) and len(enemyPartyMembers) > 0:
            # Reset var and list
            friendlyTurnsTaken = 0
            partyMembersWaiting = []
            # Display party members that still haven't taken their turn
            print("\nSelect a party member!")
            i = 1
            for x in friendlyPartyMembers:
                # Append to list if party member has not taken their turn
                if (x.hasTakenTurn == False):
                    partyMembersWaiting.append(x)
                    print(i, "-", x.name)
                    i += 1
            # Ask for user to select party member
            partyMemberChoice = input("\nEnter the corresponding number for the party member you'd like to select: ")
            partyMemberChoice = int(partyMemberChoice)
            # Use function to return party member selected
            selectedPartyMember = selectPartyMember(partyMemberChoice, partyMembersWaiting)
            # Use function to choose an action for the party member
            friendlyPartyMemberAction(selectedPartyMember)
            # Check if all party members have taken a turn, if so break while loop
            for x in friendlyPartyMembers:
                if x.hasTakenTurn == True:
                    friendlyTurnsTaken += 1
        # Var for counting if every enemy party member has taken their turn
        enemyTurnsTaken = 0
        # While loop that breaks when every enemy party member has taken their turn
        while enemyTurnsTaken < len(enemyPartyMembers) and len(friendlyPartyMembers) > 0:
            # Reset var and list
            enemyTurnsTaken = 0
            partyMembersWaiting = []
            # Create list of party members waiting to take their turn
            for x in enemyPartyMembers:
                if (x.hasTakenTurn == False):
                    partyMembersWaiting.append(x)
            print("\nThe enemy is selecting a party member...")
            time.sleep(2.5)
            # if else to select party member that hasn't taken turn yet
            if (len(partyMembersWaiting) > 1):
                # Generate number between 0 and length of partyMembersWaiting - 1
                enemyChoice = randint(len(partyMembersWaiting))
            else:
                enemyChoice = 0

            # Use function to return party member selected
            selectedPartyMember = selectPartyMember(enemyChoice, partyMembersWaiting)
            # Use function to choose action for party member
            enemyPartyMemberAction(selectedPartyMember)
            # Check if all party members have taken a turn, if so break while loop
            for x in enemyPartyMembers:
                if x.hasTakenTurn == True:
                    enemyTurnsTaken += 1

        # Check if both teams still have living members
        healthCheck = 0
        # Loop through and determine if any members have health above 0
        for x in friendlyPartyMembers:
            if (x.health > 0):
                healthCheck = x.health
        # If no members had health above 0, set friendlyMembersLiving to false
        if (healthCheck == 0):
            friendlyMembersLiving = False
        # Reset healthCheck
        healthCheck = 0
        # Same check above but for enemies
        for x in enemyPartyMembers:
            if (x.health > 0):
                healthCheck = x.health
        if (healthCheck == 0):
            enemyMembersLiving = False

        # Reset all turns taken to false
        for x in friendlyPartyMembers:
            x.hasTakenTurn = False
        for x in enemyPartyMembers:
            x.hasTakenTurn = False

        # Delay before game state displays
        time.sleep(2.5)

    
    # Create widget to display outcome
    widget = Tk()
    widget.title("Battle Outcome!")
    widget.geometry("500x500")
    
    # Print results after one party wins
    if (friendlyMembersLiving == False):
        print("You Lost!")
        widget.config(bg="#D2042D")
        lb1 = Label(widget, bg="#D2042D", font= (24))
        lb1.config(text="You Lost!")
        lb1.pack(expand=True)
        widget.mainloop()
    else:
        print("You Won!")
        widget.config(bg="#AAFF00")
        lb1 = Label(widget, bg="#AAFF00", font= (24))
        lb1.config(text="You Won!")
        lb1.pack(expand=True)
        widget.mainloop()

if __name__ == "__main__":
    main()