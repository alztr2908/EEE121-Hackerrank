guesses= []

n = int(input())
X = int(input())
i = 0

while (i < n):
  Y = int(input())
  if Y > X:
    guesses.append("Lower!")
  elif Y < X:
    guesses.append("Higher!")
  else:
    guesses.append("You win!")
    break
  if i == n-1:
    guesses.append(f"Sorry, better luck next time! The answer was {X}." )
    break
  i += 1


for i in guesses:
  print(i)