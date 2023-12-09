print("The Love Calculator is calculating your score...")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

low_name1=name1.lower()
low_name2=name2.lower()
name=low_name1+low_name2
x=name.count('t')+name.count('r')+name.count('u')+name.count('e')
y=name.count('l')+name.count('o')+name.count('v')+name.count('e')
love_score=10*x+y
if love_score<10 or love_score>90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")

elif love_score>40 and love_score<50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")

