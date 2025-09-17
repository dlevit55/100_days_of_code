
import art, game_data, random
print(art.logo)

keep_playing = True
count = 0
while keep_playing:

    random_value_a = random.randint(0,len(game_data.data) - 1)
    random_value_b = random.randint(0, len(game_data.data) - 1)
    count_a = game_data.data[random_value_a]["follower_count"]
    count_b = game_data.data[random_value_b]["follower_count"]

    print(f"Compare A: {game_data.data[random_value_a]["name"]}, {game_data.data[random_value_a]["description"]}, from {game_data.data[random_value_a]["country"]}")
    print(count_a)
    print(art.vs)
    print(f"Compare B: {game_data.data[random_value_b]["name"]}, {game_data.data[random_value_b]["description"]}, from {game_data.data[random_value_b]["country"]}")
    print(count_b)
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if user_choice == "A" and count_a > count_b or user_choice == "B" and count_b > count_a:
        count += 1
        print(f"You're right! current score: {count}")
    elif user_choice == "B" and count_b < count_a or user_choice == "A" and count_a < count_b:
        print(f"Sorry, that's wrong.final score :{count} ")
        keep_playing = False


