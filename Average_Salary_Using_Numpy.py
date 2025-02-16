import numpy as np

def calcualte_average_salary():
    salaries = []
    for job in collection.find():
        if job['salary'] != "N/A":
            salary = job['salary'].replace('$', '').replace(',', '').strip()
            salaries.append(float(salary))

        if salaries:
            average_salary = np.mean(salaries)
            print(f"Average Salary: ${average_salary:.2f}")
        else:
            print("No salary data available.")
            