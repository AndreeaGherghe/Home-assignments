# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SQYohBECDz-YAv4Z8CQuJ3Qrn3i8GiEr
"""

import random 
myName=input("Hello! What is your name?")
print("Well,"+myName+"I am thinking of a number between 1 and 10.")
guess=int(input("Take a guess."))
number=random.randint(1,10)
if guess==number:3
print("Good job, " +myName + "!You guessed my number")