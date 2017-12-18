


def increased_salary(salary):
    return salary + 0.23*salary


old_salary = [15000, 20000, 17000, 18900, 30000]
print("Total salary of employee after increase in salary by 23% are : \n")

for each_salary in old_salary:
    temp = increased_salary(each_salary)
    print("{:.3f}\n".format(temp))

