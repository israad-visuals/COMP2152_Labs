# Lab 04: Loops and Functions Practice
# Student Name: Ismail
# Student ID: 101580272
# Date: February 2026

# Import the random library to use for the dice later
import random

# Hero's Attack Functions
def hero_attacks(combat_strength, m_health_points):
    ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                  
      @              @                  
      """
    print(ascii_image)
    print("Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    if combat_strength >= m_health_points:
        m_health_points = 0
        print("You have killed the monster")
    else:
        m_health_points -= combat_strength
        print("You have reduced the monster's health to " + str(m_health_points))
    return m_health_points


# Monster's Attack Function
def monster_attacks(m_combat_strength, health_points):
    ascii_image2 = """                                                                 
           @@@@ @                           
      (     @*&@  ,                         
    @               %                       
     &#(@(@%@@@@@*   /                      
      @@@@@.                                
               @       /                    
                %         @                 
            ,(@(*/           %              
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
             """
    print(ascii_image2)
    print("Monster's Claw (" + str(m_combat_strength) + ") ---> Hero (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        health_points = 0
        print("You have killed the monster")
    else:
        health_points -= m_combat_strength
        print("The monster has reduced your health to " + str(health_points))
    return health_points


# Game
# Define The number of lives for the Hero and Monster
numLives = 10  # number of player's lives remaining
mNumLives = 12  # number of monster's lives remaining

# Define the Dice
diceOptions = list(range(1, 7))
# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Print out the weapons using a for loop
for weapon in weapons:
    print(weapon)

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
good_loot_options = ["Health Potion", "Leather Boots"]
bad_loot_options = ["Poison Potion"]

# Define the number of stars awarded to the Player
num_stars = 0

# Use a While Loop to get valid input for Hero and Monster's Combat Strength
i = 0

while i in range(5):
    combat_strength = input("Enter your combat Strength (1-6): ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    # Validate input: Check if the string inputted is numeric
    if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
        # If one of the inputs are invalid, print error message and halt
        print("One or more invalid inputs. Player needs to enter integer numbers for Combat Strength")
        i = i + 1
        continue

    # Note: Now safe to cast combat_strength to integer
    # Validate input: Check if the string inputted is a number between 1-6
    elif (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength)) not in range(1, 7):
        print("Enter a valid integer between 1 and 6 only")
        i = i + 1
        continue

    # Break out of while loop if input was valid
    else:
        break

# Input was valid - broke out of while loop
combat_strength = int(combat_strength)
m_combat_strength = int(m_combat_strength)

# Roll for weapon
input("Roll the dice for your weapon (Press enter)")
weaponRoll = random.choice(diceOptions)

# Max out the combat strength at 6
combat_strength = min(6, (combat_strength + weaponRoll))
print("The hero\'s weapon is " + str(weapons[weaponRoll - 1]))

# Weapon Roll Analysis
input("Analyze the Weapon roll (Press enter)")
if weaponRoll <= 2:
    print("--- You rolled a weak weapon, friend")
elif weaponRoll <= 4:
    print("--- Your weapon is meh")
else:
    print("--- Nice weapon, friend!")

# If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
if weapons[weaponRoll - 1] != "Fist":
    print("--- Thank goodness you didn't roll the Fist...")

# Roll for player health points
input("Roll the dice for your health points (Press enter)")
health_points = random.choice(diceOptions)
print("Player rolled " + str(health_points) + " health points")

# Roll for monster health points
input("Roll the dice for the monster's health points (Press enter)")
m_health_points = random.choice(diceOptions)
print("Player rolled " + str(m_health_points) + " health points for the monster")

input("Analyze the roll (Press enter)")
# Compare Player vs Monster's strength
print("--- You are matched in strength: " + str(combat_strength == m_combat_strength))

# Check the Player's overall strength and health
print("--- You have a strong player: " + str((combat_strength + health_points) >= 15))

# Loop while the monster and the player are alive. Call fight sequence functions
print("You meet the monster. FIGHT!!")
while m_health_points > 0 and health_points > 0:

    input("You strike first (Press Enter)")
    m_health_points = hero_attacks(combat_strength, m_health_points)
    if m_health_points == 0:
        num_stars = 3
    else:
        input("The monster strikes (Press Enter)")
        health_points = monster_attacks(m_combat_strength, health_points)
        if health_points == 0:
            num_stars = 1
        else:
            num_stars = 2

stars = "*" * num_stars
print("Hero gets <" + stars + "> stars")


# ============================================
# Question 1: Robot Return to Origin
# ============================================

def robot_returns_to_origin(moves):
    # Initialize starting position
    x = 0
    y = 0

    # Loop through each move and update x, y
    for move in moves:
        if move == "U":
            y += 1
        elif move == "D":
            y -= 1
        elif move == "R":
            x += 1
        elif move == "L":
            x -= 1

    # Return True if back at origin, False otherwise
    if x == 0 and y == 0:
        return True
    else:
        return False

# Test cases
test_moves = ["UD", "LL", "UDLR", "LDRRLRUULR"]

for moves in test_moves:
    result = robot_returns_to_origin(moves)
    print("Moves '" + moves + "': Returns to origin? " + str(result))


# ============================================
# Question 2: Two Sum
# ============================================

# Part A: Brute Force with Nested Loops
def two_sum_brute_force(numbers, target):
    # Use nested loops to find the pair
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (i, j)
    return None

# Part B: Optimized with Dictionary
def two_sum_optimized(numbers, target):
    seen = {}  # Dictionary to store {number: index}
    # Loop through numbers, check if needed value exists in seen
    for i in range(len(numbers)):
        needed = target - numbers[i]
        if needed in seen:
            return (seen[needed], i)
        seen[numbers[i]] = i
    return None

# Test cases
test_cases = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6),
    ([1, 5, 3, 8, 2], 10)
]

print("=== Part A: Brute Force (Nested Loops) ===")
for numbers, target in test_cases:
    result = two_sum_brute_force(numbers, target)
    print("Numbers: " + str(numbers) + ", Target: " + str(target))
    print("Result: " + str(result))
    print()

print("=== Part B: Optimized (Dictionary) ===")
for numbers, target in test_cases:
    result = two_sum_optimized(numbers, target)
    print("Numbers: " + str(numbers) + ", Target: " + str(target))
    print("Result: " + str(result))
    print()


# ============================================
# Question 3: Shuffle the Array
# ============================================

def shuffle_array(nums, n):
    # Step 1: Split into two halves using slicing
    first_half = nums[:n]
    second_half = nums[n:]

    # Step 2: Create empty result list
    result = []

    # Step 3: Interleave using a for loop
    for i in range(n):
        result.append(first_half[i])
        result.append(second_half[i])

    return result

# Test cases
test_cases_shuffle = [
    ([2, 5, 1, 3, 4, 7], 3),
    ([1, 2, 3, 4, 4, 3, 2, 1], 4),
    ([1, 1, 2, 2], 2)
]

for nums, n in test_cases_shuffle:
    print("Original: " + str(nums))
    print("n = " + str(n))

    # Show the slices
    print("First half (nums[:" + str(n) + "]): " + str(nums[:n]))
    print("Second half (nums[" + str(n) + ":]): " + str(nums[n:]))

    # Get result
    result = shuffle_array(nums, n)
    print("Shuffled: " + str(result))
    print()


# ============================================
# Question 4: First Unique Character
# ============================================

# Helper function: Count all characters in a string
def count_characters(s):
    counts = {}
    # Loop through string and count each character
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

# Main function: Find first unique character
def first_unique_character(s):
    # Step 1: Get character counts using helper function
    char_counts = count_characters(s)

    # Step 2: Loop through string with index to find first unique
    for i in range(len(s)):
        if char_counts[s[i]] == 1:
            return i

    # Step 3: Return -1 if no unique character found
    return -1

# Test cases
test_strings = ["leetcode", "loveleetcode", "aabb", "python", "aabbcc"]

for s in test_strings:
    index = first_unique_character(s)

    if index != -1:
        print("First unique character in '" + s + "': index " + str(index) + " (character: '" + s[index] + "')")
    else:
        print("First unique character in '" + s + "': index -1 (no unique character)")

    # Show the character counts for understanding
    counts = count_characters(s)
    print("  Character counts: " + str(counts))
    print()