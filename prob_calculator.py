import copy
from importlib.resources import contents
import random
# Consider using the modules imported above.

class Hat:
    def __init__ (self, **kwargs):
        self.contents=[]
        for key,value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, number):
        all=[]
        if (number>len(self.contents)):
            return self.contents
        for i in range(number):
            rem=self.contents.pop(random.randint(0,len(self.contents)-1))
            all.append(rem)
        return all

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    cnt=0
    for i in range(num_experiments):
      expected_copy=copy.deepcopy(expected_balls)
      hat_copy=copy.deepcopy(hat)
      colors=hat_copy.draw(num_balls_drawn)
      for color in colors:
        if (color in expected_copy):
          expected_copy[color]-=1        
        if (all(x<=0 for x in expected_copy.values())):
          cnt+=1
          break
    return cnt/num_experiments