print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("what does cpu stand for? ")

if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect! ")

answer = input("what does GPU stand for? ")

if answer.lower() == "graghics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect! ")

answer = input("what does RAM stand for? ")

if answer.lower() == "random acces memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect! ")

answer = input("what does PSU stand for? ")

if answer.lower() == "power supply unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect! ")

print("You got " + str(score) + " questions correct! ")
print("You got " + str((score / 4)*100) + "%. ")