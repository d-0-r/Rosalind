class RabbitPair():
  def __init__(self):
    self.canReproduce = False
  
  def toggleReproduce(self):
    self.canReproduce = True
    
  def mayReproduce(self):
    return self.canReproduce
    
    
def fibRabbits(n, k):
  ''' solution to Rabbits and Recurrence Relations on Rosalind.info '''
  head = RabbitPair()
  rabbit_arr = [head]
  for _ in range(1, n):
    for pair in rabbit_arr[::-1]:
      if (pair.mayReproduce()):
        for _ in range(k):
          rabbit_arr.append(RabbitPair())
      else:
        pair.toggleReproduce()
  return len(rabbit_arr)

print("There were {} pairs of rabbits after {} generations".format(fibRabbits(34, 5), 34))