emp_name = input("Enter employee name: ")
basic = float(input("Enter basic pay (Rs.): "))
ot_hours = float(input("Enter overtime hours: "))
incentive = float(input("Enter performance incentive (Rs.): "))

if basic <= 0 or ot_hours < 0 or incentive < 0:
    print("Invalid salary details entered.")
else:
    hra = basic * 0.20
    da = basic * 0.15
    ot_pay = ot_hours * 250.0
    gross = basic + hra + da + ot_pay + incentive

    pf = basic * 0.12
    if gross <= 30000:
        tax = 0.0
    elif gross <= 60000:
        tax = (gross - 30000) * 0.10
    else:
        tax = (30000 * 0.10) + (gross - 60000) * 0.20

    total_deductions = pf + tax
    net_salary = gross - total_deductions

    print("\n========================================")
    print("        EMPLOYEE SALARY STATEMENT       ")
    print("========================================")
    print(f"Employee Name    : {emp_name}")
    print(f"Basic Pay        : Rs. {basic:.2f}")
    print(f"HRA (20%)        : Rs. {hra:.2f}")
    print(f"DA (15%)         : Rs. {da:.2f}")
    print(f"Overtime Pay     : Rs. {ot_pay:.2f}")
    print(f"Incentive        : Rs. {incentive:.2f}")
    print("----------------------------------------")
    print(f"Gross Salary     : Rs. {gross:.2f}")
    print(f"PF Deduction     : Rs. {pf:.2f}")
    print(f"Income Tax       : Rs. {tax:.2f}")
    print("----------------------------------------")
    print(f"Net Salary       : Rs. {net_salary:.2f}")
    print("========================================")
