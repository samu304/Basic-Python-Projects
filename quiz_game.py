print("Welcome to the Quiz Game !!! \n")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Ok! Let's Play \n")
score = 0

ans = input("What does CPU stand for? \n")
if ans.lower() == "central processing unit":
    print("Correct ✅ ")
    score += 1
else:
    print("Incorrect ❌ ")

ans = input("What does RAM stand for? \n")
if ans.lower() == "random access memory":
    print("Correct ✅ ")
    score += 1
else:
    print("Incorrect ❌ ")

ans = input("What does ROM stand for? \n")
if ans.lower() == "read only memory":
    print("Correct ✅ ")
    score += 1
else:
    print("Incorrect ❌ ")

ans = input("What does WWW stand for? \n")
if ans.lower() == "world wide web":
    print("Correct ✅ ")
    score += 1
else:
    print("Incorrect ❌ ")

ans = input("What does GUI stand for? \n")
if ans.lower() == "graphical user interface":
    print("Correct ✅ ")
    score += 1
else:
    print("Incorrect ❌ ")

print("You scored: " + str(score))

print("Your percentage: " + str((score / 5 ) * 100) )
