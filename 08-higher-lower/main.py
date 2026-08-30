import art
import random
import game_data

def compare_followers(decision):
    if decision == "a" and first_famous["follower_count"] > second_famous["follower_count"]:
        winner = first_famous
        return 1

    elif decision == "b" and second_famous["follower_count"] > first_famous["follower_count"]:
        winner = second_famous
        return 1

    else:
        return 0

print(art.logo)
score = 0
in_game = True

while in_game:

    first_famous = random.choice(game_data.data)
    second_famous = random.choice(game_data.data)

    if first_famous in game_data.data:
        game_data.data.remove(first_famous)

    if second_famous in game_data.data:
        game_data.data.remove(second_famous)

    print(f"Compare A: {first_famous["name"]}, a {first_famous["description"]} from {first_famous["country"]}")
    print(art.vs)
    print(f"Compare B: {second_famous["name"]}, a {second_famous["description"]} from {second_famous["country"]}")

    decision = input("Who has more follower. Type 'A' or 'B': ").lower()
    comparation = compare_followers(decision)

    if comparation == 1:
        score += 1
        print(f"You are right!. Current score: {score}")

    else:
        print(f"Sorry that is wrong. Final score: {score}")
        in_game = False
        break

    keep_playing = True

    while keep_playing:
        first_famous = second_famous
        second_famous = random.choice(game_data.data)
        print(f"Compare A: {first_famous["name"]}, a {first_famous["description"]}, from {first_famous["country"]}")
        print(art.vs)
        print(f"Compare B: {second_famous["name"]}, a {first_famous["description"]} from {first_famous["country"]}")

        if second_famous in game_data.data:
            game_data.data.remove(second_famous)

        decision = input("Who has more follower. Type 'A' or 'B': ").lower()
        comparation = compare_followers(decision)

        if comparation == 1:
            score += 1
            print(f"You are right!. Current score: {score}")

        else:
            print(f"Sorry that is wrong. Final score: {score}")
            in_game = False
            keep_playing = False
