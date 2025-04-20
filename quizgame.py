#python quiz game
print("Welcome to my computer quiz!")

playing = input("Do you want to play? (yes/no) : ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? : ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score +=1
else:
    print('Incorrect!')

answer = input("What do you mean by os? : ")
if answer.lower() == "operating system":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("How many bones are there in our body? : ")
if answer.lower() == "207":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What is the meaning of color black? : ")
if answer.lower() == "darkness and power":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print(f"You got {score} questions correct!")
print(f"You got {((score / 4) * 100) }%.")






