#higher or lower? by Samuel Lin 1/4/17
import easygui
import random

intro = easygui.msgbox("2 player game. First player enters a magic number. The second trys to guess the number. stay within 1-100 or we will choose a random number. Good luck.")

n = easygui.enterbox("Choose number 1-100.")
n = int(n)
if n > 100 or n < 1:
    n = random.randint(1, 100)

    

guess = easygui.enterbox("Guess the number")
guess = int(guess)

while guess != n:
    if guess > n:
        guess = int(easygui.enterbox("Wrong anwser. Try again! The magic number is lower."))
    elif guess < n:
        guess = int(easygui.enterbox("Wrong anwser. Try again! The magic number is higher."))

if guess == n:
    easygui.msgbox("You win!")


