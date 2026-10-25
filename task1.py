# Task 1: Sales Tax and Employee Sales Calculation
# Total Employees: 5

def main():
    num_employees = 5
    total_sales = 0.0

    print("=" * 45)
    print("      Mobile Phone Shop - Daily Sales Record")
    print("=" * 45)

    for i in range(1, num_employees + 1):
        print(f"\n--- Employee {i} ---")
        try:
            sales = float(input(f"Enter daily sales amount for Employee {i} (Rs.): "))
        except ValueError:
            print("Invalid input! Setting sales to 0.")
            sales = 0.0

        # Tax calculation based on rules:
        # Less than 50,000 -> 5%
        # Between 50,000 and 100,000 -> 10%
        # Greater than 100,000 -> 15%
        if sales < 50000:
            tax_rate = 0.05
        elif sales <= 100000:
            tax_rate = 0.10
        else:
            tax_rate = 0.15

        tax_amount = sales * tax_rate
        total_sales += sales

        # Display for each employee
        print(f"Sales Amount : Rs. {sales:,.2f}")
        print(f"Tax Rate     : {int(tax_rate * 100)}%")
        print(f"Tax Amount   : Rs. {tax_amount:,.2f}")

    # Calculate average sales
    average_sales = total_sales / num_employees

    # Summary after all employees are entered
    print("\n" + "=" * 45)
    print("                  SUMMARY")
    print("=" * 45)
    print(f"Total Sales   : Rs. {total_sales:,.2f}")
    print(f"Average Sales : Rs. {average_sales:,.2f}")
    print("=" * 45)


if __name__ == "__main__":
    main()
