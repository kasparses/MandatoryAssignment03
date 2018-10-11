
def getRootOfCube(cube, epsilon, squaredNumber):
    
    num_guesses  =  0
     
    low  =  0    
    high  =  cube
    guess  =  (high  +  low)/2.0
         
    while  abs(guess ** squaredNumber  -  cube)  >=  epsilon:
#         print('guess', guess, 'high', high, 'low', low)
        if  guess ** squaredNumber  <  cube  :
            low  =  guess
        else:
            high  =  guess
        guess  =  (high  +  low)/2.0
        num_guesses  +=  1
        
    print (guess, 'is close  to  the  cube  root  of', cube)
    return num_guesses
        

num_guesses = getRootOfCube(1000000, 0.00001, 2)
print(num_guesses)

num_guesses = getRootOfCube(1000000, 0.00001, 4)
print(num_guesses)