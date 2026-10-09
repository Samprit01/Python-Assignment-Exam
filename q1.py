'''
Question 1: Student Marks Analysis
A college stores students' marks in a list. 
Write a function that accepts a list of marks and 
displays the highest mark, lowest mark, average mark, 
and number of students who passed (marks of 40 or above).
'''


def analyze_marks(x):
    c=0
    max_num = max(x)
    min_num = min(x)
    avg_num = sum(x)/len(x)
    for _ in x:
        if _ >40: c+=1
    print (f"Max marks: {max_num} \nMin marks:  {min_num} \nAverage marks: {avg_num} \nCount of student passes: {c}")



marks = [84,90,36,54,32,40]
analyze_marks(marks)