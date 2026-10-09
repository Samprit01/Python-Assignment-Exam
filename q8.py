'''
A college stores a student's roll number, name, course, and 
semester in a tuple. Write a function that displays 
each field separately and 
prints the complete student record.
'''

s_name = (2321206002011,"Samprit","MCA",4)


def student_print(x):
    id,name,course,sem = x
    print(f"Student Roll: {id}")
    print(f"Student Name: {name}")
    print(f"Course: {course}")
    print(f"Semester: {sem}")

student_print(s_name)
