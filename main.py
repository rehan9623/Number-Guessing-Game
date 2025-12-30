import random
n = random.randint(1, 100) 
a = -1
guesses = 1
while(a != n):
    a = int(input("Guess the number: ")) 
    if(a >n):
        print("Lower number please")
        guesses +=1
    elif(a<n):
        print("Higher number Please")
        guesses +=1
percentage = round(100 / guesses, 2)
print(f"You have guessed the number {n} correctly in {guesses} attempts with a winning percentage of {percentage}%")
