#1. count unique letters
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  counter=0
  for letter in letters:
    if letter in word:
      counter+=1
  return counter


print(unique_english_letters("mississippi"))
print(unique_english_letters("Apple"))
print("2--------")
#2. count X
def count_char_x(word, x):
  counter=0
  for letter in word:
    if letter==x:
      counter+=1
  return counter


print(count_char_x("mississippi", "s"))
print(count_char_x("mississippi", "m"))
print("3--------")
#3. Count Multi X
def count_multi_char_x(word, x):
  splits = word.split(x)
  return(len(splits)-1)

print(count_multi_char_x("mississippi", "iss"))
print(count_multi_char_x("apple", "pp"))
print("4--------")
#4. Substring Between
def substring_between_letters(word, start, end):
  a=word.find(start)
  b=word.find(end)
  if a > -1 and b > -1:
    return(word[a+1:b])
  return word

print(substring_between_letters("apple", "p", "e"))
print(substring_between_letters("apple", "p", "c"))
print("5--------")
#5. X lenght
def x_length_words(sentence, x):
  words=sentence.split()
  for word in words:
    if len(word) >= x:
      return True
    else:
      return False

print(x_length_words("i like apples", 2))
print(x_length_words("he likes apples", 2))

print("6--------")
#6. Check Name
def check_for_name(sentence, name):
  if name.lower() in sentence.lower():
    return True
  else:
    return False

print(check_for_name("My name is Jamie", "Jamie"))
print(check_for_name("My name is jamie", "Jamie"))
print(check_for_name("My name is Samantha", "Jamie"))
print("7--------")

#7.EVERY OTHER LETTER
def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other

print(every_other_letter("Codecademy"))
print(every_other_letter("Hello world!"))
print(every_other_letter(""))

print("8.--------")
#8. Reverse
def reverse_string(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse

print(reverse_string("Codecademy"))
print(reverse_string("Hello world!"))
print(reverse_string(""))

print("9.--------")
#9. Make Spoonerism
def make_spoonerism(word1, word2):
  return word2[0]+word1[1:]+" "+word1[0]+word2[1:]

print(make_spoonerism("Codecademy", "Learn"))
print(make_spoonerism("Hello", "world!"))
print(make_spoonerism("a", "b"))

print("10.--------")
#10. Add Exclamation
def add_exclamation(word):
  new_word=word+ ""
  while len(new_word)<20:
    new_word+="!"
  return new_word

print(add_exclamation("Codecademy"))
print(add_exclamation("Codecademy is the best place to learn"))