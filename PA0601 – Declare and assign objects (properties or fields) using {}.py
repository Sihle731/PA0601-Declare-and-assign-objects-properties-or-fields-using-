'''Question 1

Create an object called student with:

name
studentNumber
course
yearLevel
'''

class Student:
   def __init__(self, name, studentNumber, course, yearLevel):
       self.name = name
       self.studentNumber = studentNumber
       self.course = course
       self.yearLevel = yearLevel

studentInfo = Student("Sihle Mkhwanazi", "214194027", "Data Science", 2)

print(studentInfo.name)  # Output: Sihle Mkhwanazi
print(studentInfo.studentNumber)  # Output: 214194027
print(studentInfo.course)  # Output: Data Science
print(studentInfo.yearLevel)  # Output: 2

'''
Question 2

Create an empty object called vehicle, then assign:

brand
colour
registrationNumber'''

# 1. Define an empty class
class Vehicle:
    pass

# 2. Create an object of the class
my_car = Vehicle()

# 3. Assign values directly to the object
my_car.brand = "Volkswagen"
my_car.colour = "Red"
my_car.registrationNumber = "XYZ789"

# 4. Access the values
print(my_car.brand)  # Output: Volkswagen   
print(my_car.colour)  # Output: Red
print(my_car.registrationNumber)  # Output: XYZ789
