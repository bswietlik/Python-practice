#1. append size
def append_size(lst):
  lenght=len(lst)
  lst.append(lenght)
  return lst

print(append_size([23, 42, 108]))

print("2-----")

#2. Append sum
def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst

print(append_sum([1, 1, 2]))
print("3-----")

#3. Larger List
def larger_list(lst1, lst2):
  if len(lst1)>=len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

print("4-----")

#4. MOre than N
def more_than_n(lst, item, n):
  if lst.count(item)>n:
    return True
  else:
    return False

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

print("5-----")
#5. Combine SOrt
def combine_sort(lst1, lst2):
  lst=lst1+lst2
  return sorted(lst)


print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

print("6-----")
#6. Every Three Numbers
def every_three_nums(start):
  list=[]
  for i in range(start,101, 3):
    list.append(i)
  return list

print(every_three_nums(91))
print("7-----")

#7. Remove Middle
def remove_middle(lst, start, end):
  lst1=lst[:start]
  lst2=lst[end+1:]
  return lst1+lst2

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

print("8-----")
#8. MOre Frequent Item
def more_frequent_item(lst, item1, item2):
  if lst.count(item1)>=lst.count(item2):
    return item1
  else:
    return item2

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
print("9-----")

#9. Double Index
def double_index(lst, index):
  if index>=len(lst):
    return lst
  else:
    new_list=lst[0:index]
    new_list.append(lst[index]*2)
    second_list=lst[index+1:]
    return new_list+second_list


print(double_index([3, 8, -10, 12], 2))

print("10-----")

#10. Middle Item
def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

print(middle_element([5, 2, -10, -4, 4, 5,]))