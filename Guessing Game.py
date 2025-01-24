import random 

print("Ready to play the guessing game! Choose a range.") 
start = int(input("Enter the starting value:"))
end =int(input("Enter the ending value:"))

if start >= end:
    print("Invalid range! Starting value must be less than the ending value")
else:
    guessing_game_number = random. randint (start, end)
    print (f"Guess the number between {start} and {end}. If you are too high I will tell you. If you are too low, I will tell you as well ")

guessing_game_range =range(start, end)
print(guessing_game_range)

while True:
    guess = int(input("Enter your guess"))
    if guess> guessing_game_number:
        print("Too high")
    elif guess< guessing_game_number:
        print("Too Low")
    else:
        print ("You win! The number was:", guessing_game_number)
        break

