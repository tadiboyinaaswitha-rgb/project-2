# PROJECT 2 – EMPLOYEE PAYROLL AND DEDUCTION ANALYSIS

## About the Project
The Employee Payroll and Deduction Analysis project is designed to compute an employee's monthly salary from basic pay, allowances, overtime hours, and performance incentives. It applies Provident Fund and progressive income tax deductions to generate a clean, formatted salary statement.

## Technologies Used
- **Python** – Used to build the payroll calculation and payslip generator.
- **Conditional Statements** – Used to validate inputs and apply progressive tax slabs.
- **Arithmetic Operators** – Used to calculate allowances, overtime wages, deductions, and net pay.
- **String Formatting** – Used to format the final salary statement cleanly.

## Main Features
- Accepts employee name, basic pay, overtime hours, and incentive amount.
- Validates that basic pay is positive and overtime/incentives are non-negative.
- Calculates HRA (20% of basic), DA (15% of basic), and overtime pay (Rs. 250/hour).
- Computes gross salary and applies PF (12% of basic) plus progressive income tax.
- Displays a structured salary statement with gross pay, deductions, and net salary.

## Algorithm
1. Start the program.
2. Read employee name, basic pay, overtime hours, and performance incentive.
3. Check that basic pay is greater than zero and other values are non-negative.
4. Calculate HRA (20%), DA (15%), and overtime pay (`ot_hours * 250`).
5. Compute gross salary by summing basic pay, allowances, overtime, and incentive.
6. Calculate PF deduction (12% of basic pay).
7. Calculate income tax according to gross salary slabs.
8. Subtract total deductions (PF + tax) from gross salary to get net salary.
9. Display the formatted employee salary statement.
10. Stop the program.

## Sample Output
Enter employee name: Karthikeya
Enter basic pay (Rs.): 40000
Enter overtime hours: 10
Enter performance incentive (Rs.): 5000

========================================
        EMPLOYEE SALARY STATEMENT       
========================================
Employee Name    : Karthikeya
Basic Pay        : Rs. 40000.00
HRA (20%)        : Rs. 8000.00
DA (15%)         : Rs. 6000.00
Overtime Pay     : Rs. 2500.00
Incentive        : Rs. 5000.00
----------------------------------------
Gross Salary     : Rs. 61500.00
PF Deduction     : Rs. 4800.00
Income Tax       : Rs. 3300.00
----------------------------------------
Net Salary       : Rs. 53400.00
========================================

## Conclusion
This project automates employee salary computation and deduction handling in a clear payslip format. It demonstrates Python concepts such as conditional statements, arithmetic operators, and formatted output.
