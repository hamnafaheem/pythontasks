import random
import matplotlib.pyplot as plt

def roll_dice(num_dice, num_sides):
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    return rolls

def display_roll_history(rolls):
    print("Roll History:")
    for i, roll in enumerate(rolls, start=1):
        print(f"Roll {i}: {roll}")

def calculate_total_sum(rolls):
    return sum(rolls)

def calculate_probability_analysis(rolls, num_sides):
    counts = [0] * num_sides
    for roll in rolls:
        counts[roll - 1] += 1
    probabilities = [count / len(rolls) for count in counts]
    return probabilities

def display_probability_analysis(probabilities):
    print("\nProbability Analysis:")
    for i, probability in enumerate(probabilities, start=1):
        print(f"Probability of rolling {i}: {probability:.2f}")

def display_dice_visualization(rolls, num_sides):
    frequencies = [rolls.count(i) for i in range(1, num_sides + 1)]
    plt.bar(range(1, num_sides + 1), frequencies)
    plt.xlabel('Dice Face')
    plt.ylabel('Frequency')
    plt.title('Dice Roll Frequency Visualization')
    plt.xticks(range(1, num_sides + 1))
    plt.grid(axis='y')
    plt.show()  # Display the plot

def main():
    print("Welcome to the Dice Rolling Simulator!")

    num_dice = int(input("Enter the number of dice to roll: "))
    num_sides = int(input("Enter the number of sides on each die: "))
    num_rolls = int(input("Enter the number of rolls: "))

    all_rolls = []
    for _ in range(num_rolls):
        rolls = roll_dice(num_dice, num_sides)
        all_rolls.append(rolls)
        print(f"\nRoll Result: {rolls}")
    
    display_roll_history(all_rolls)

    total_sum = calculate_total_sum([sum(rolls) for rolls in all_rolls])
    print("\nTotal Sum of all Rolls:", total_sum)

    probabilities = calculate_probability_analysis([item for sublist in all_rolls for item in sublist], num_sides)
    display_probability_analysis(probabilities)

    display_dice_visualization([item for sublist in all_rolls for item in sublist], num_sides)

if __name__ == "__main__":
    main()
