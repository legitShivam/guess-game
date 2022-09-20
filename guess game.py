import random  # Importing Random module to generate random numbers


def path(path):
    var = path.replace("\\", "\\\\")
    return var


def caps(string):
    return ''.join((c.upper() if i == 0 or string[i-1] == ' ' else c) for i, c in enumerate(string))


def user(name):
    file = open("Database\score.txt", 'r+')
    fileContent = file.readlines()
    for userData in fileContent:
        user = userData.strip().split(' ')
        userName = user[0]
        userBestScore = user[1]
        if name.lower().strip() == userName:
            return f"Your Best Score is {userBestScore}"
        else:
            file.write(f"{name} {20}\n")
            return f"Your Best Score is {20}"
        file.close()


def fileWriting(name, score):
    file = open("Database\score.txt", 'r')
    fileContent = file.readlines()
    file.close()
    file = open("Database\score.txt", 'w')
    
    for userData in fileContent:
        user = userData.split(' ')
        userName = user[0]
        userBestScore = user[1]
        if score < int(userBestScore):
            user[1] = score
            print('writing')
        for writableLine in user:
            file.write(f"{user[0]} {user[1]}\n")
    file.close()


guessingNumber = 2  # random.randint(1, 101)
score = 1
print("\n--------------- Guessing Game ---------------\n\n")
name = input(">>> Enter your name\n    --> ")
while True:
    guess = int(input(">>> Guess the number:\n    -->"))
    if guess <= 100:
        if score < 20:
            if guess == guessingNumber:
                print(
                    f"\n>>> You guessed the number (*^▽^*)\n--- {caps(name)}'s Score is {score}\n")
                fileWriting(name, score)
                break
            elif guess > guessingNumber:
                print(
                    f"\n______________________________________________________________________________\n\n>>> Guess something smaller ⊙﹏⊙∥ {user(name)}\n______________________________________________________________________________\n")
            elif guess < guessingNumber:
                print(
                    f"\n_______________________________________________________________________________\n\n>>> Guess something bigger ⊙﹏⊙∥ {user(name)}\n_______________________________________________________________________________\n")
        else:
            print("\n>>> You lost the game")
    else:
        print(">>> Invalid Number")
    score += 1  # Increasing Total number of tries
