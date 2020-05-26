import random

options = ["rock", "paper", "scissors"]


def get_random_option():
    random_value = int(random.random() * len(options))
    return options[random_value]


def does_user_win(user_option, cpu_option):
    user_option_idx = options.index(user_option)

    # next element beats user value
    beats_user = options[(user_option_idx + 1) % 3]

    return cpu_option != beats_user


def main():

    while True:
        print("\nRock paper scissors")
        response = input("Type: rock, paper or scissors. Q - quit\n")

        if response.lower() == "q":
            break
        elif response in options:
            cpu_option = get_random_option()
            print("Cpu option: " + cpu_option)
            if response == cpu_option:
                print("Draw!")
            elif does_user_win(response, cpu_option):
                print("You won!")
            else:
                print("Cpu won!")


if __name__ == "__main__":
    main()
