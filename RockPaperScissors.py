import random


print('Rock, Paper, Scissors')
print('=====================')
print("")


print('1) Rock ✊')
print('2) Paper ✋')
print('3) Scissors ✌️')
print("")


player = int(input('Pick a number: '))
cpu = random.randint(1,3)
win = 'You win :)'
lose = 'You lose :('


while player != 1 and player != 2 and player != 3:
  player = int(input('Invalid input - please choose 1, 2 or 3: '))
if player == 1:
  print('You chose: 1) Rock ✊ ')
elif player == 2:
  print('You chose: 2) Paper ✋')
elif player == 3:
  print('You chose: 3) Scissors ✌️')


print("")
if cpu == 1:
  print('Computer chose: 1) Rock ✊ ')
elif cpu == 2:
  print('Computer chose: 2) Paper ✋')
else:
  print('Computer chose: 3) Scissors ✌️')


print("")
if player == cpu:
  print ("It's a draw!")
elif player == 1 and cpu == 2:
  print(win)
elif player == 1 and cpu == 3:
  print (lose)
elif player == 2 and cpu == 1:
  print(win)
elif player == 2 and cpu == 3:
  print(lose)
elif player == 3 and cpu == 1:
  print (lose)
elif player == 3 and cpu == 2:
  print (win)