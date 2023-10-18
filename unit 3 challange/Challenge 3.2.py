'''
Implement a function called sort_students that takes a list of student objects as input and sorts the 
list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object 
has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function 
with different input lists of students.
''' 

class Student:
    
  def __init__(self, name, roll_number, cgpa):
        self.name = name 
        self.roll_number = roll_number
        self.cgpa = cgpa


def sort_students(student_list):
#Sort the list of students in decenending order of cgpa 
   sorted_students = sorted(student_list, 
                         key=lambda student: student.cgpa, 
                         reverse=True)
# synta-lambada arg:exp
   return sorted_students 


# example usage:
students = [
    Student("Alice", "A123", 3.8),
    Student("Bob", "B456", 3.9),
    Student("Charlie", "C789", 3.7),
    Student("Dave", "D012", 3.6),
    Student("Eve", "E345", 3.5),
]
sorted_students = sort_students(students)

#print the sorted list of students
for student in sorted_students:
    print("Name:{},roll_number:{}, cgpa:{}".format(student.name, 
                                                   student.roll_number, 
                                                   student.cgpa))
 