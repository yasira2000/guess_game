import:py from random, randint;

walker GuessGame{
    has correct_number:int = randint(0, 100);

    can start_game with `root entry;
    can process_guess(guess: int);
}

node turn{

    can check with GuessGame entry;
}

#========================== implementation ==============================

:walker:GuessGame:can:start_game{
    end = here;
    for i=0 to i<10 by i+=1{
        end ++> (end := turn());
    }

    visit [-->];
}

:walker:GuessGame:can:process_guess(guess:int){
    if guess == self.correct_number{
        print("Congratulations !!! you have guessed the number correct.");
        disengage;
    }elif guess < self.correct_number{
        print("Too Low");
    }else{
        print("Too high");
    }

    
}

:node:turn:can:check{
    guess = input("Enter the number: ");

    if guess.isdigit(){
        here.process_guess(int(guess));
    }else{
        print("Enter a valid number.");
    }
    visit [-->];
}

with entry{
    GuessGame() spawn root;
}
