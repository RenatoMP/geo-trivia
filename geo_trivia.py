# storing the answers in a key value pair to connect the question with the correct answer
questions = {"What is the third planet from the sun?": "A",
             "What is the largest country by territory? ": "B",
             "What is the largest country by population? ": "A",
             "Which desert covers much of northern Africa? ": "A",
             "What is the tallest mountain in the U.S.? ": "B",
             "What is the longest river in the world? ": "B",
             "What is the largest ocean in the world? ": "B",
             "What is the largest sea in the world? ": "B",
             "What largest river in the world by volume? ": "A",
             "Where can you find the Great Pyramids of Giza? ": "B",
             "In which country would you find the Eiffel Tower? ": "B",
             "In which country would you find Machu Picchu? ": "A"}

#created this to standardize the responses and make it easier to guess the right spelling and answer
answers = [["A. Earth", "B. Mars"], ["A. Canada", "B. Russia"], ["A. China", "B. India"], ["A. Sahara", "B. Namibia"],
           ["A. Mount Rainier", "B. Mount Denali"],
           ["A. Mississippi", "B. Nile"], ["A. Atlantic", "B. Pacific"], ["A. Dead Sea", "B. Caspian Sea"],
           ["A. Amazon", "B. Congo"],
           ["A. Mexico", "B. Egypt"], ["A. Nevada", "B. France"], ["A. Peru", "B. Colombia"]]

# define a function that runs the trivia game, shows the question and answers
def play_game():
    attempts = []
    correct_attempts = 0
    q_num = 0 # based on the index in the Dictionary

    for key in questions:
        print(key)  # this prints the questions in the dictionary
        for i in answers[q_num]:  # calls a specific index for the related answer to the question called in the for loop above
            print(i)
        attempt = input("Enter A or B then press the Enter key: ")
        attempt = attempt.upper() # ensures that all letters entered are in uppercase
        attempts.append(attempt)

        q_num += 1  # this increases the question to loop through the questions in the dictionary. I added this after I realized that it was not progressively moving through the questions
        correct_attempts += check_response(questions.get(key), attempt)  # adds the correct guesses 
        
    show_score(correct_attempts, attempts)

# define a function that checks the 
def check_response(answer, attempt):      
    if answer == attempt:
        print("You got it right! Great job.")
        print()
        return 1
    else:
        print("That's not quite right.")
        print()
        return 0


def show_score(correct_attempts, attempts):
    print("Results: ")
    print()

    print("Answers: ")
    for i in questions:
        print(questions.get(i))
    print()

    print("Guesses: ")
    for i in attempts:
        print(i)
    print()

    score = ((correct_attempts / len(questions))*100)
    score = int(score)
    print("Your score is: ", str(score), "percent!")


# Ask the player fi they want to play again
def play_again():
    again = input("Do you want to play again? ")
    again = again.lower()

    if again == "yes":
        return True
    if again == "no":
        print("Adios!")
    else:
        return False


play_game()

while play_again():
    play_game()