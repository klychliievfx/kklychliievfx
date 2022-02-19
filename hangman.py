from random_word import RandomWords
import os
from rich.console import Console


console = Console(width=200)


pics = ['''
        +---+
        |   |
            |
            |
            |
            |
            |
            |
            |
      =========''', '''
        +---+
        |   |
        |   |
            |
            |
            |
            |
            |
            |
      =========''', '''
        +---+
        |   |
        |   |
        |   |
            |
            |
            |
            |
            |
      =========''', '''
        +---+
        |   |
        |   |
        |   |
        |   |
      (•_•) |
            |
            |
            |
      =========''', '''
        +---+
        |   |
        |   |
        |   |
        |   |
      (•_•) |
        |   |
            |
            |
      =========''', '''
        +---+
        |   |
        |   |
        |   |
        |   |
      (•_•) |
        |\  |
            |
            |
      =========''', '''
        +---+
        |   |
        |   |
        |   |
        |   |
      (•_•) |
       /|\  |
            |
            |
      =========''', '''
        +---+
        |   |
        |   |
        |   |
        |   |
      (•_•) |
       /|\  |
       /    |
            |
      =========''', '''
        +---+
        |   |
        |   |
        |   |
        |   |
      (•_•) |
       /|\  |
       / \  |
            |
      =========''', '''
        +---+
        |   |
        |   |
        |   |
        |   |
      (+_+) |
       /|\  |
       / \  |
            |
      ========='''
        ]


def play_again():

    response = console.input(
        "[green]Would you like to play again? (y/n) : [/green]").lower()
    if response == 'y':
        os.system("clear")
        game_run()
    else:
        os.system("clear")
        console.print("See you next time!",
                      style="bold navy_blue on white", justify="center")


def game_run():

    print()
    console.print("Welcome to the Hangman Game! The computer will randomly choose a word and you will try to guess what the word is. If you need a hint, type 'need a hint'. ",
                  style="bold navy_blue on white", justify="center")

    r = RandomWords

    random_word = r().get_random_word()
    word = str(random_word)

    reversed_pics = pics[::-1]
    letters_guessed = []
    tries = 10
    print()
    alphabet = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's',
                'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

    for letter in word:
        if letter in alphabet:
            console.print('[purple]_ ', end="")
        elif not letter.isalpha():
            console.print(f"[purple]{letter } ", end="")

    while tries > 0:

        user_guess = console.input(
            f"[red]Guess a letter {alphabet} (quit): [red]")
        print()

        for letter in alphabet:
            if user_guess == letter:
                index = alphabet.index(letter)
                alphabet[index] = " "

        if user_guess == "need a hint":
            letters_list = list(word)     
            letter_position = int(
                input("Enter a position of the letter you want to be revealed: "))
            x = letters_list[letter_position - 1]
            console.print(
                f"\n[red]{x}[/red] is the letter under index {letter_position}. Now you can insert it into your word!\n")
            continue

        if user_guess in word:
            console.print("[magenta]Correct! Choose another letter. \n ")

        if len(user_guess) != 1 or not "need a hint":
            console.print("[magenta]Enter one letter only please: \n")
            continue

        if user_guess not in word or not "need a hint":
            tries -= 1
            console.print(
                f"[magenta]Incorrect. There are no {user_guess} in the secret word. You have {tries} tries left. \n")
            print(reversed_pics[tries])

        letters_guessed += user_guess
        wrong_count = 0

        for letter in word:
            if letter in letters_guessed:
                console.print(f"[purple]{letter} ", end="")
            elif not letter.isalpha():
                console.print(f"[purple]{letter } ", end="")
            else:
                console.print("[purple]_ ", end="")
                wrong_count += 1

        if wrong_count == 0:
            console.print(
                f"\n\nYou won!\nThe answer was {word}.\n", style="bold italic green", justify="center")
            break
    else:
        console.print(
            f"\n\nYou lost!\nThe answer was {word}.\n", style="bold italic red", justify="center")

    play_again()


game_run()
