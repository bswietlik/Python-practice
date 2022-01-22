#1.  First Three Multiples.  For this function, we are going to print out the first three multiples of a number
# and return the third multiple.
def  first_three_multiples(num):
  print(num)
  print(num*2)
  print(num*3)
  return num*3
first_three_multiples(10)
first_three_multiples(0)

#2. We can create a function to easily calculate the amount to tip based on the total cost of the food and a percentag
def tip(total, percentage):
  return (total*percentage)/100
print(tip(10, 25))
print(tip0, 100))

#3. Our function is going to concatenate strings together in order to replace James Bond’s name with whatever name we want.

def introduction(first_name, last_name):
  return last_name+ ', '+ first_name+ ' '+ last_name

print(introduction("James", "Bond"))
print(introduction("Maya", "Angelou"))

#4. create a function which calculates a dog’s age in dog years!
def dog_years(name, age):
  dog_age=age*7
  return name+', you are '+str(dog_age)+ " years old in dog years"
print(dog_years("Lola", 16))
print(dog_years("Baby", 0))

#5. we are going to perform multiple mathematical operations on multiple inputs to the function.
def lots_of_math(a, b, c, d):
  A=a+b
  B=c-d
  C=(a+b)*(c-d)
  print(A)
  print(B)
  print(C)
  return C%a

print(lots_of_math(1, 2, 3, 4))
print(lots_of_math(1, 1, 1, 1))