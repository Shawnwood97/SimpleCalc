class Addition:
  numbers = []
  result = 0

  def __init__(self, *nums):
    counter = 0
    for num in nums:
      self.numbers += num

    for number in self.numbers:
      counter = counter + 1
      print(f'Step {counter}: {self.result} + {number} = {self.result + number}')
      self.result += number

    print(f'Result: {self.result}')
