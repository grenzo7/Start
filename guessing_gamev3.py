import random
comp_choice=random.randint(1,100)
# print(comp_choice)
guesses=0
user_choice=None
while (user_choice!=comp_choice):
    user_choice=int(input("Enter your guess\n"))
    guesses+=1
    if comp_choice>user_choice:
        print("Wrong. Try greater value")
    elif comp_choice<user_choice:
        print("Wrong. Try smaller value")
print(f"Correct. You got it right at {guesses} guesses  ")

with open("hiScore.txt","r") as f:
    hiScore=int(f.read())
if guesses<hiScore:
    with open("hiScore.txt", "w") as f:
        f.write(guesses)
