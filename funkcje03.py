#Insurance cost function

def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost=250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated insurance cost for " + name+  " is "+ str(estimated_cost)+ " dollars.")
  return estimated_cost


# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost(name = "Maria", age = 28, sex = 0, bmi = 26.2, num_of_children = 3, smoker = 0)


# Estimate Omar's insurance cost

omar_insurance_cost = calculate_insurance_cost(name = "Omar", age = 35, sex = 1, bmi = 22.2, num_of_children = 0, smoker = 1)

beata_insurance_cost=calculate_insurance_cost(name = "Beata", age = 31, sex = 0, bmi = 22.2, num_of_children = 2, smoker = 0)


def difference_cost(cost1, cost2):
  difference=cost1-cost2
  return "The difference in insurance cost is "+ str(difference)+  " dollars."

print(difference_cost(6789, 5467))

#Extended Version of Tgis project with control flow statement

def analyze_smoker(smoker_status):
  if smoker_status == 1:
     print("To lower your cost, you should consider quitting smoking.")
  else:
     print("Smoking is not an issue for you.")

def analyze_bmi(bmi_value):
  if bmi_value >30:
    print("Your BMI is in the obese range. To lower your cost, you should significantly lower your BMI.")
  elif bmi_value >= 25 and bmi_value <= 30:
    print("Your BMI is in the overweight range. To lower your cost, you should lower your BMI")
  elif bmi_value >= 18.5 and bmi_value < 25:
    print("Your BMI is in a healthy range.")
  elif bmi_value < 18.5:
    print("Your BMI is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health")


# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  analyze_bmi(bmi)
  return estimated_cost

keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, bmi = 26.2, num_of_children = 3, smoker = 1)

beata_insurance_cost=estimate_insurance_cost(name = 'Beata', age = 31, sex = 0, bmi = 23.2, num_of_children = 2, smoker = 0)