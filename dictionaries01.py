#Python Dictionaries: Medical Insurance Project-
# You have been asked to create a program that organizes and updates medical records efficiently.

medical_costs={}
medical_costs["Marina"]=6607.0
medical_costs["Vinay"]=3225.0
medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})
#print(medical_costs)
medical_costs["Vinay"]=3325.0
print(medical_costs)

#calculate average cost od each patient
total_costs=0
for cost in medical_costs.values():
  total_costs+= cost
average_cost=total_costs/len(medical_costs)
print("Average Insurance Costs: "+ str(average_cost))

#create new dictionray zip name and age
names=["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages=[27, 24, 43, 35, 52]
zipped_ages=zip(names, ages)
names_to_ages={names:ages for names, ages in zipped_ages}
print(names_to_ages)
marina_age=names_to_ages.get("Marina")
print("Marina's age is "+ str(marina_age))

#create 3 dictionary to represent a database od medical records
medical_records={}
medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records["Isaac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}
print(medical_records)

print("Connie's insurance cost is "+str(medical_records["Connie"]["Insurance_cost"])+ " dollars.")

medical_records.pop("Vinay")

for name, record in medical_records.items():
   print(name + " is a " + str(record["Age"]) + \
  " year old " + record["Sex"] + " " + record["Smoker"] \
  + " with a BMI of " + str(record["BMI"]) + \
  " and insurance cost of " + str(record["Insurance_cost"]))