# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  print(student_heights)
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
height_sum = 0
for height in student_heights:
  print(height)
  height_sum += height
student_number = 0
for student in student_heights:
  student_number += 1
  
#print(student_number)
#print(student_heights)
#print(height_sum)
height_average = round(height_sum/student_number)
print(height_average)
