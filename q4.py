'''

Question 4: Employee Salary Analysis
A company stores employee salaries in a list. 
Write a function to calculate the average salary, 
display salaries above the average, and increase every salary by 10%.



'''

salary = [10000,20000,30000,40000,34000,76000,87000]

def salary_mod(x):
    avg = sum(x)/len(x)
    sal_avg = [_ for _ in x if _>avg]
    sal_avg_inc = [_+(_*0.1) for _ in x if _>avg]
    print(f"Average Salary: {avg} \nSalary above average: {sal_avg} \nIncreased Salary above Average: {sal_avg_inc}")

salary_mod(salary)