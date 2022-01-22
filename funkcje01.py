#1. Tenth power
def tenth_power(num):
  return num**10
print(tenth_power(1))
print(tenth_power(0))
print(tenth_power(2))

#2. Square root
def square_root(num):
  return num**(1/2)
print(square_root(16))
print(square_root(100))

#3. WIn percentage
def  win_percentage(wins, losses):
  full=wins+losses
  return (wins/full)*100
print(win_percentage(5, 5))
print(win_percentage(10, 0))

#4. Average
def average(num1, num2):
  return (num1+num2)/2

print(average(1, 100))
print(average(1, -1))

#5. Remainder
def remainder(num1, num2):
  return (2*num1)%(1/2*num2)
print(remainder(15, 14))
print(remainder(9, 6))
