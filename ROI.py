
# Calculate ROI on a rental property taking into account Income, Expenses, Cash Flow, Cash on Cash ROI
# Income: Rental Income, Laundry, Storage, Misc.
# Expenses: Tax, Insurance, Utilities, HOA, lawn/snow care, Vacancy,
#        Repairs, CopEx (replace), Property Management, Mortgage
# Cash Flow: (Income - Expenses)
# CoC ROI: Down payment, Closing Costs, Renovations, Misc.
# (Cash Flow x 12 months) / Total CoC ROI


class ROI():
    
    print("\n")
    print("Let's calculate your ROI on a rental property. If the answer to any question is None, enter 0\n")

    def income(self):
        rent_income = input("How much does this property rent for? $")
        laundry_income = input("How much is laundry? $")
        storage_income = input("How much is storage? $")
        misc_income = input("Is there any miscellaneous income? $")
        month_income = float(rent_income) + float(misc_income) + float(laundry_income) + float(storage_income)
        self.monthly_income = "{:.2f}".format(month_income)
        print(f"\nThe total monthly income is ${self.monthly_income}.\n")


    def expenses(self):
        tax = input("How much is the monthly tax? $")
        insurance = input("How much is the monthly cost of insurance? $")
        utilities = ""
        utilities_question = input("Is the occupant responsible for paying the utilities? (Y/N) ")
        if utilities_question.lower() == "y":
            utilities = 0
        else:
            electric = input("How much is the electric bill? $")
            water = input("How much is the water bill? $")
            sewer = input("How much is the sewer bill? $")
            garbage = input("How much is the garbage bill? $")
            gas = input("How much is the gas bill? $")
            utilities = float(electric) + float(water) + float(sewer) + float(garbage) + float(gas)
        hoa = input("How much are the monthly HOA fees? $")
        lawn_snow = input("How much is the lawn/snow maintenance? $")
        vacancy = input("How much will you save monthly for vacancy reasons? $")
        repairs = input("How much will you save for repairs? $")
        capex = input("How much will you save for capital expenditures? $")
        prop_man = input("How much is property management? $")
        mortgage = input("How much is the monthly mortgage payment? $")
        month_expenses = float(tax) + float(insurance) + float(utilities) + float(hoa) + float(lawn_snow) + float(vacancy) + float(repairs) + float(capex) + float(prop_man) + float(mortgage)
        self.monthly_expenses = "{:.2f}".format(month_expenses)
        print(f"\nThe total monthly expenses are ${self.monthly_expenses}.\n")

    
    def cashflow(self):
        month_cashflow = float(self.monthly_income) - float(self.monthly_expenses)
        self.monthly_cashflow = "{:.2f}".format(month_cashflow)
        print(f"\nThe monthly cash flow is ${self.monthly_cashflow}.\n")

    def CoC_ROI(self):
        down_payment = input("How much is your total down payment? $")
        closing_costs = input("How much are your closing costs? $")
        renovations = input("How much will you spend to renovate? ")
        miscellaneous = input("Are there any other fees or expenses? ")
        total_investment = float(down_payment) + float(closing_costs) + float(renovations) + float(miscellaneous)
        yearly_cashflow = float(self.monthly_cashflow) * 12
        roi = yearly_cashflow / total_investment * 100
        self.roi_percent = round(roi, 2)

        print(f"\nMonthly Income: ${self.monthly_income}")
        print(f"Monthly Expenses: ${self.monthly_expenses}")
        print(f"Monthly Cash Flow: ${self.monthly_cashflow}")
        print(f"Annual ROI: {self.roi_percent}%")


property_roi = ROI()


def calcROI():
    while True:
        property_roi.income()
        property_roi.expenses()
        property_roi.cashflow()
        property_roi.CoC_ROI()
        break
calcROI()