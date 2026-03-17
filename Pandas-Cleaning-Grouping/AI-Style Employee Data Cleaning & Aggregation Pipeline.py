import pandas 
import numpy 

if __name__ == "__main__":
    
    data = {
        "Employee": [
            "Amit", "Neha", "Rahul", "Sneha",
            "Vikram", "Priya", "Arjun", "Divya"
        ],
        "Department": [
            "IT", "HR", "IT", "Finance",
            "HR", "Finance", "IT", "HR"
        ],
        "Salary": [
            600000, 500000, numpy.nan, 700000,
            520000, numpy.nan, 650000, 480000
        ],
        "Temporary_Notes": [
            "On probation", "Contract",
            "Pending docs", "Verified",
            "Intern", "New joiner",
            "On leave", "Temporary role"
        ]
    }

    
    df = pandas.DataFrame(data)

    print("Original DataFrame:")
    print(df)
    print("\nMissing values per column:")
    print(df.isna().sum())

    
    mean_salary = df["Salary"].mean()
    df["Salary"] = df["Salary"].fillna(mean_salary)

    print("\nDataFrame after filling missing Salary with mean:")
    print(df)

    
    df = df.drop(columns=["Temporary_Notes"])

    
    df = df.rename(columns={"Salary": "Annual_Salary"})

    
    summary = df.groupby("Department").agg(
        Mean_Annual_Salary=("Annual_Salary", "mean"),
        Employee_Count=("Employee", "count")
    ).reset_index()

    print("\nFinal summary table (by Department):")
    print(summary)