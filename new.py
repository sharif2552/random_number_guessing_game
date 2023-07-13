import random 


def random_number_guessing_game():
    corect_answer=int(random.randrange(1,51))
    print("Enter value between 0 and 50 ")

    win = 0
    for i in range(5):
        print("You have "+str(5-i)+" chances left")
        user_input = int(input("Enter a number: "))
        if(user_input == corect_answer ):
            win = 1
            print("You Win!")
            break
        elif(user_input>corect_answer):
            print("Correct answer is smaller!")
        elif(user_input<corect_answer):
            print("Correct answer is greater!")

    if(win==0):
            print("You lose! ")

    if(input("Type start to continue...: ")=="start"):
         random_number_guessing_game()


    

print("Random number guessing game!")
a = input("Type start to strat the game: ")
if(a =="start"):
    random_number_guessing_game()