# Financial Calculator

""" A financial calculator with dual menu options
for investments vs. bond loans"""

# Import library
import math


def menu():
    """
        A function to present and calculate investments vs. bonds
        """
    # Display menu options for user
    print("Financial calculator menu:")
    print("Investment- to calculate interest earned on investment")
    print("Bond      - to calculate payment on a home loan\n")

    # Retrieving initial user choice
    investment_cal = input(
        "Please enter 'investment' or 'bond' from the menu: "
        ).strip().lower()

    # ---- BOND CALCULATION ----
    if investment_cal == "bond":
        P = float(input("Please enter the present value of your home: "))
        i = (float(input("Please enter your interest rate: ")) / 100) / 12
        n = int(input("Please enter the number of months to repay bond: "))

        # Calculate monthly repayment
        repayment = (i * P) / (1 - (1 + i) ** (-n))
        repay_two = round(repayment, 2)
        print(f"You will repay ${repay_two:,.2f} each month. ")

    # ---- INVESTMENT CALCULATION ----
    elif investment_cal == "investment":
        P = float(input("Please enter the amount you will be depositing: "))
        r = float(input("Please enter your interest rate: ")) / 100
        t = float(input("Please enter the number of years investing: "))

        interest = input(
                "Please choose 'simple' or 'compound' interest: "
                ).strip().lower()

        if interest == "compound":
            A = P * math.pow((1 + r), t)
            new_compound = round(A, 2)
            print(f"Your compound value amount is ${new_compound:,.2f}.")

        elif interest == "simple":
            A = P * (1 + r * t)
            new_simple = round(A, 2)
            print(f"Your simple value amount is ${new_simple:,.2f}.")
        else:
            print("ERROR: invalid interest type selected")

    # ---- INVALID CHOICE ----
    else:
        print("ERROR: Please check your entry and try again.")


# Calling the function
menu()

# ------------ END OF CODE -------------
