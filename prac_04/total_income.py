"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

def print_report(months, incomes):
    """Print income report for a given number of months."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

def main():
    """Get and display income report for a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))
    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    print_report(num_months, incomes)

main()
