#1.Large Power
def large_power(base, exponent):
  if base**exponent>5000:
    return True
  else:
    return False

print(large_power(2, 13))
print(large_power(2, 12))
print("2----")
#2. Over Budget
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  if budget<(food_bill+electricity_bill
  +internet_bill+rent):
    return True
  else:
    return False

# should print False
print(over_budget(80, 20, 30, 10, 30))
print("3----")
#3. Twice as Large
def twice_as_large(num1, num2):
  if num1>2*num2:
    return True
  else:
    return False

print(twice_as_large(10, 5))
print(twice_as_large(11, 5))
print("4----")
#4. Divisible BY Ten
def divisible_by_ten(num):
  if num%10==0:
    return True
  else:
    return False

print(divisible_by_ten(20))
print(divisible_by_ten(25))
print("5----")
#5 NOt sum to ten
def not_sum_to_ten(num1, num2):
  if (num1+num2)!=10:
    return True
  else:
    return False

print(not_sum_to_ten(9, -1))
print(not_sum_to_ten(9, 1))
print(not_sum_to_ten(5,5))
print("6----")

#6. In range
def in_range(num, lower, upper):
  if num >=lower and num <=upper:
    return True
  else:
    return False

print(in_range(10, 10, 10))
print(in_range(5, 10, 20))
print("7----")

#7. Same Name
def same_name(your_name, my_name):
  if your_name==my_name:
    return True
  else:
    return False
print(same_name("Colby", "Colby"))
print(same_name("Tina", "Amber"))
print("8----")

#8. Always False
def always_false(num):
  if num>0 and num<0:
    return True
  else:
    return False

print(always_false(0))
print(always_false(-1))
print(always_false(1))
print("9----")

#9. Movie Reviex
def movie_review(rating):
  if rating <=5:
    return "Avoid at all costs!"
  elif rating <9:
    return "This one was fun."
  elif rating>=9:
    return "Outstanding!"

print(movie_review(9))
print(movie_review(4))
print(movie_review(6))

print("10----")

#10. Max Number
def max_num(num1, num2, num3):
  if num1>num2 and num1>num3:
    return num1
  elif num2>num1 and num2>num3:
    return num2
  elif num3>num1 and num3>num2:
    return num3
  elif num1==num2 or num1==num3 or num2==num3:
    return "It's a tie!"

print(max_num(-10, 0, 10))
print(max_num(-10, 5, -30))
print(max_num(-5, -10, -10))
print(max_num(2, 3, 3))