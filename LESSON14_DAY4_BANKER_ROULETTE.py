print("Enter names: ")
names_string= input()
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
length=len(names)-1
import random
x = random.randint(0,length)
random_name= names[x]
print(f"{random_name} is going to buy the meal today!")
