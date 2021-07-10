import math


# Mortgage Algorithm https://www.financeformulas.net/Loan_Payment_Formula.html
def get_mortgage_loan(principal, interest, years):
    f"""
    
    :param principal: {float} the present loan value
    :param interest: {float} the annual interest rate
    :param years: {int} the repayment period in years
    :return: {float} the total loan amount
    """
    # Monthly rate
    interest_rate = interest / (100 * 12)

    # number of payments
    payment_num = years * 12

    # monthly payment
    monthly_payment = (principal * interest_rate) / (1 - math.pow((1 + interest_rate), (-payment_num)))

    # total payment
    total_payment = monthly_payment * years * 12

    return total_payment


print(get_mortgage_loan(100000, 7.5, 30))
