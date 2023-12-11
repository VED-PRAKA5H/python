student_heights=input("enter heights in one row with space\n")
student_heights=student_heights.split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

number_of_student=0
total_height =0
n=0
for i in student_heights:
  toatal_height += student_heights[n]
  n +=1
  number_of_student += 1

print(f"total student_heights = {total_height}\nnumber of students = {n}\naverage student_heights = {round(average_height/n)}")



                                  #MEETHOD 2👇

student_heights = input('Input a Python list of student heights').split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Your code below this row 👇
total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")
  
