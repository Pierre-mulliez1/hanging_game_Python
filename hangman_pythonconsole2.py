# -*- coding: utf-8 -*-
"""
Created on Mon May  6 20:05:46 2019

@author: Pierre Mulliez
"""

secret = input("Secret word: ")
print('\n')
chances = input("Number of chances: ")
print('\n'*30)
hang = "\|o||||_"
guessed = ''
counter = 0
counter0 = -1
list1 = []
guesses = ''

for letter in secret:
        list1.append(' _ ')
print(list1)        
print('\n')
for var in range(0, int(chances)):
    var = input("Enter your guess: ")
    guesses += ' ' + var + ' '
    for l in secret:
        counter0 += 1
        if l == var:
            list1[counter0] = (' ' + var + ' ')
            guessed += (' ')
    
    print(list1)
    print('\n'* 2)
    print('Your letters ' + guesses)
    
    if len(guessed) == len(secret):
        print("YOU WON")
        break   
    
    print('')
    print(' Your hangstate is:')   
    print('')   
    
    if all(letter != var for letter in secret) == True: 
        counter += 1
        
    for iteration in range(0,counter):   
        print(hang[iteration])
    
    counter0 = -1
        
    continue
 
  
