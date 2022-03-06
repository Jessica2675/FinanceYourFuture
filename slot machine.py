#!/usr/bin/env python
# coding: utf-8

# In[1]:


pension = input('Pension:')


# In[2]:


def token_bonus (pension):
    return int(int(pension)/100)


# In[10]:


import random as rn
symbols = ['€','£','$']

tokens = 10 + token_bonus(pension)
print('Welcome to the slot game!')

while tokens > 0:
    print('You have', tokens, 'tokens.')
    try:
        bet = int(input('Bet amount:')) 
    except:
        print('Please enter a whole number of tokens.')
        continue
    if bet > tokens:
        print('Not enough tokens.')
    elif bet < 1:
        print('Please enter a positive number of tokens.')
    else:
        tokens -= bet
        sq_one, sq_two, sq_three = rn.choices(symbols, weights=[1,1,2])[0], rn.choices(symbols, weights=[1,2,1])[0], rn.choices(symbols, weights=[2,1,1])[0]
            
        print() 
        print('|', sq_one, '|', sq_two, '|', sq_three, '|')
        print()
            
        if sq_one == sq_two and sq_two == sq_three:
            amountwon = bet*10
            print("Congratulation! You have won £", amountwon, '.')
            pension = int(pension) + amountwon
        else:
            print('You lost this time.')
print('You are out of tokens.')
print('Your current pension is £', pension)


#  
