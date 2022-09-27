# Salary calculator for single people year 2022
# Takes income, Federal and, State tax for the current year only 
# (State input should be 2 letter format) 
# Shows how much you make a month, biweekly, daily 
# To run program `python3 "Salary calculator.py"
def get_federal_tax(income):
    tax_brack_percent = { 
                            (0,10_275): 0.10,
                            (10_275,41_775): 0.12,
                            (41_776,89_075): 0.22,
                            (89_076,170_050): 0.24,
                            (170_051,215_950): 0.32,
                            (215_951,539_901): 0.35,                       
    }
    
    result = 0
    taxed_value = 0
    
    for income_level, percentage in tax_brack_percent.items(): 
        if income_level[0] < income < income_level[1]:
            result += (income - taxed_value) * percentage
            return result
        else:
            result += (income_level[1] - 1 - taxed_value) * percentage
            taxed_value = income_level[1] - 1
            
    result +=  (income - taxed_value) * .37 # For incomes in the top tax bracket
    
    return result
 
def get_ladder_percent(income,brackets,level):
    pass
 
def get_state_tax(income):
    CA = 0  
    if income < 9326: 
        CA = .01
    elif income < 22108: 
        CA = .02 
    elif income < 34893: 
        CA = .04 
    elif income < 48436: 
        CA = .06 
    elif income < 61215: 
        CA = .08 
    elif income < 312687: 
        CA = .093 
    elif income < 375222: 
        CA = .103 
    elif income < 625370: 
        CA = .113 
    else: 
        CA = .123
    return CA 
    
def calc_state_tax(income):

    calc = 0
    if income < 9326: 
        calc = income * .01 
    elif 9326 <= income <= 22108: 
        calc = ((income - 9325) * .02) + (9325 * .01)
    elif 22107 <= income <= 34893: 
        calc = ((income - 22106) * .04) + (22107 * .02) + (9325 * .01) 
    elif 34892 <= income <= 48435: 
        calc = ((income - 3489) * .06) + (34892 * .04) + (22107 * .02) + (9325 * .01) 
    elif 48435 <= income <= 61215: 
        calc = ((income - 48434) * .08) + (48434 * .06) + (34893 * .04) + (22107 * .02) + (9325 * .01) 
    elif 61214 <= income <= 312687: 
        calc = ((income - 61214) * .093) + (61214 * .08) + (48435 * .06) + (34893 * .04) + (22107 * .02) + (9325 * .01) 
    elif 312687 <= income <= 375222: 
        calc = ((income - 312686) * .103) + (312686 * .093) + (61214 * .08) + (48435 * .06) + (34893 * .04) + (22107 * .02) + (9325 * .01) 
    elif 375222 <= income <= 625369: 
        calc = ((income - 375221) * .113) + (375221 * .103) + (312686 * .093) + (61214 * .08) + (48435 * .06) + (34893 * .04) + (22107 * .02) + (9325 * .01)  
    else: 
        calc = ((income - 625370) * .123) + (625369 + .113) + (375221 * .103) + (312686 * .093) + (61214 * .08) + (48435 * .06) + (34893 * .04) + (22107 * .02) + (9325 * .01)  
    return calc 
    
income = float(input("Enter your yearly salary: ")) 

federal_tax = get_federal_tax(income) 
state_tax = get_state_tax(income) 
calc_state = calc_state_tax(income)

print(f"Your state tax rate is: {(state_tax)* 100:.2f}%") 
print(f"Your federal actual tax rate is {(federal_tax/income) * 100:.2f}%")
print(f"Uncle Sam stole ${federal_tax} from you") 
print(f"California stole ${calc_state} from you")
