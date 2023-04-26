import numpy as np
#we are making game guess the number
number = np.random.randint(1, 101)#using numpy module we are turning on the function randomizer
count = 0

while True:
    count += 1
    predict_number = int(input('Guess the number from 1 to 100'))
   
    if predict_number > number:
        print('Your number must be smaller!')
   
    elif predict_number < number:
        print('Your number must be bigger!')    
    
    else:
        print(f'You naild it! The number was = {number}, you did it using {count} trys')    
        break #end of the game