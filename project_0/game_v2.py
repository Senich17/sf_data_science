import numpy as np

def random_predict(number:int=1) -> int:
        """Rundomly guessing the number
    Args:
         number (int, optional): hidden number. Defaults to 1.
    Returns:
        int: count of attempts
    """
        count = 0
        
        while True:
            count += 1
            predict_number = np.random.randint(1, 100)
            if number == predict_number:
                break
        return(count)    

def score_game(random_predict) -> int:
    """For how many attempts on average out of 1000 approaches does our algorithm guess
    Args: 
        random_predict ([type]): guess function
    Returns:
        int: average number of attempts
    """
    count_try = []#list for count attempts
    np.random.seed(1)#fixating seed for reproducing
    random_array = np.random.randint(1, 101, size=(1000))#list of hidden numbers
    
    for number in random_array:
        count_try.append(random_predict(number))
        
    score = int(np.mean(count_try))#the average count of attempts
    
    print(f'Your algorithm guesses the number on average for: {score} attempts')    
    return(score)

#RUN
score_game(random_predict)
    
    
    
    
