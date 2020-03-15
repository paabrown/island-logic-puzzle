from .game import Game


def main():
    print("Welcome to the island! See https://xkcd.com/blue_eyes.html")
    num_blue_eyed = int(input("How many blue-eyed meeple should be on the island?"))
    game = Game(num_blue_eyed=num_blue_eyed)

    print("The guru tells everyone that at least one person has blue eyes")
    game.run_guru()

    day = 1
    while game.base_universe.blue_eyed_meeple:
        print(f"Day {day}")
        num_left = game.advance_one_day()
        print(f"{num_left} meeple left the island")
        input("Press enter to continue")
        day += 1


if __name__ == "__main__":
    main()
