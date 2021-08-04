def isMatched(s):
  group = ["[","{","(","]","}",")"]

  # This is stack ADT implemented in an array
  stack = []
  counter = 0
  temp = 0

  for letter in s:
    # Check if letter is a grouping symbol
    if letter in group:
      # Get the index
      pointer = group.index(letter)

      # If open grouping symbol
      if pointer < 3:
        stack.append(letter)
      # If close grouping symbol
      else:
        # Check first if stack is empty since we can't pop 
        # if there are no elements inside the stack
        if len(stack) == 0:
          temp = counter
          return temp
        # If the closing is different from the opening symbol
        # They must be the same since you can't close a group with
        # different symbol
        elif group[pointer-3] != stack[-1]:
          temp = counter
          return temp
        # Normal case 
        else:
          stack.pop()
    
    # Counter keeps track of every "letter" on the string
    counter += 1 
  
  # When the loop ends and there are still elements inside the stack
  if len(stack) != 0:
    return counter

  # When there are no elements inside the stack since closing symbol acts as 
  # an indicator that stack must pop the last opening element
  return -1

print(isMatched(input()))
