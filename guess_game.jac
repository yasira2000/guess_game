import:py from random, randint;

walker GuessGame{
    has correct_number:int;

    can start_game with entry `root;
    can process_guess(guess: int)
}

node turn{
    has guess:int;

    can check(guess:int) with entry GuessGame;
}

with entry {
    print("Random number ", randint(0, 100));
}