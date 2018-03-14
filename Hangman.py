import random
answerlist = ["world","look","hello","goodbye"]
random.shuffle(answerlist)
answer = list(answerlist[0])

display = []
used = []

display.extend(answer)
used.extend(display)

for i in range(len(display)):
    display[i] = "_"
print(' '.join(display))
print()

count = 0
while count < len(answer):
    guess = input("Please guess a letter: ")
    guess = guess.lower()
    print(count)

    for i in range(len(answer)):
        if answer[i] == guess and guess in used:
            display[i] = guess
            count = count + 1
            used.remove(guess)

    if guess not in display:
        print("Sorry, wrong guess")

    print("You have guessed: ",count,"correct letters.")

    print(' '.join(display))
    print()

print("Well done, you guessed the word")