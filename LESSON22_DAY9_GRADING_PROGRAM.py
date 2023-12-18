# Instructions👇
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.
# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.
# The final version of the student_grades dictionary will be checked
# DO NOT write any print statements.
# This is the scoring criteria:
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}
for student in student_scores:
  score = student_scores[student]
  if score >=91 and score <= 100:
    grade = "Outstanding"
  elif score >= 81 and score <= 90: 
    grade = "Exceeds Expectations"
  elif score >= 71 and score <= 80:
    grade = "Acceptable"
  elif score <= 70:
    grade = "Fail"
  student_grades[student] = grade
  
print(student_grades)

