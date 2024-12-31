import random
import math

lower=int(input('Enter Lower Bound:-'))
upper=int(input('Enter Upper Bound:-'))

x=random.randint(lower,upper)
print('\n\tYou have only',round(math.log(upper-lower+1,2)),'Chances to guess the integer!\n')
count=0
while count<math.log(upper-lower+1,2):
    count+=1
    guess=int(input('Guess a number:-'))
    if x==guess:
        print('Congratulations you did it in',count,'try')
        break
    elif x>guess:
        print('You guessed too small')
    elif x<guess:
        print('You guessed too high!')

if count>=math.log(upper-lower+1,2):
    print('\nThe number is %d'%x)
    print("\nBetter Luck Next time!")