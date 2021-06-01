import traceback
from exceptions import CalculatorInputError

class Addition:
  numbers = []
  result = 0

  def __init__(self, *nums):
    counter = 0
    print(nums)
    self.result = float(nums[0][0])
    for num in nums[0]:
      try:
        self.numbers.append(float(num))
      except ValueError:
        raise CalculatorInputError()

    for number in self.numbers:
      counter = counter + 1
      if (counter > 1):
        last_result = self.result
        self.result += number
        if(self.result.is_integer()):
          self.result = int(self.result)
        print(f'Step {counter - 1}: {str(last_result)} + {str(number)} = {str(self.result)}')

    print(f'Result: {self.result}')
