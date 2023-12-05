import random
import art
import game_data
import os

compare_list = []
user_lives = 1
user_total = 0


def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def random_2_celeb():
    """To get random 2 celebrities"""
    return random.sample(game_data.data, 2)


current_celeb = None  # Variable to store the celebrity the user got right

while user_lives != 0:
    celebs = random_2_celeb()

    # If the user got the previous comparison right, use the second celebrity from the previous round
    if current_celeb:
        celeb1 = current_celeb
    else:
        celeb1 = celebs[0]

    celeb1_name = celeb1['name']
    celeb1_followers = celeb1['follower_count']
    celeb1_description = celeb1['description']
    celeb1_country = celeb1['country']

    print(art.logo)
    print(celeb1_name, celeb1_description, "and they are from", celeb1_country)

    # Accessing information about the second celebrity
    celeb2_name = celebs[1]['name']
    celeb2_followers = celebs[1]['follower_count']
    celeb2_description = celebs[1]['description']
    celeb2_country = celebs[1]['country']

    print(art.vs)
    print(celeb2_name, celeb2_description, "and they are from", celeb2_country)

    user_guess = input("Who has more followers, select 'higher' if the first celebrity has more or 'lower' if they "
                       "second one is more popular" + "\n").lower()

    if user_guess not in ['higher', 'lower']:
        print("Invalid input. Please enter 'higher' or 'lower'.")
        continue  # Skip the rest of the loop and restart

    if celeb1_followers > celeb2_followers and user_guess == 'higher':
        user_total += 1
        print(f"You are right, current score = {user_total}")
        clear_screen()
        current_celeb = celebs[1]  # Save the second celebrity for the next round
    elif celeb1_followers < celeb2_followers and user_guess == 'lower':
        user_total += 1
        print(f"You are right, current score = {user_total}")
        clear_screen()
        current_celeb = celebs[1]  # Save the second celebrity for the next round
    else:
        user_lives -= 1
        print(f"You lose: Your final score was {user_total}")
        current_celeb = None  # Reset to None if the user got it wrong
