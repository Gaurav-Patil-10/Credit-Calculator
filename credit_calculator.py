import argparse
import sys 
import math

def differentiated (principal , periods , interest): # function for calcultions of the differentiated payments per month
    sum1 = 0
    for x in range(1,periods+1):
        ans = (principal / periods)
        ans1 = ans + interest * (principal - (ans * (x -1)))
        sum1 += math.ceil(ans1)
        print(f"Month {x}: paid out {math.ceil(ans1)}")

    print(f"\nOverpayment = {math.ceil(sum1) - principal}")

def annuity (principal , interest_rate , count_months): # annuity payment
    ans1 = interest_rate * ((1 + interest_rate) ** count_months)
    ans2 = ((1 + interest_rate) ** count_months) - 1
    ans = principal * (ans1 / ans2)
    return ans

def principal (annuity , interest_rate , count_months): # principal 
    ans1 = interest_rate * ((1 + interest_rate) ** count_months)
    ans2 = ((1 + interest_rate) ** count_months) - 1
    ans = annuity / (ans1 / ans2)
    return ans

def num_payments (annuity , principal , interest_rate):   # number of the payments or the periods  
    ans1 = annuity / (annuity - (interest_rate * principal))
    ans = math.log(ans1 , (1 + interest_rate))
    return math.ceil(ans)

def interest_rate (credit_interest): # rate of interest
    ans = credit_interest / (12 * 100)
    return ans

def convert (num):  # conversion of the periods in years and months
    num1 = num // 12
    num2 = num % 12
    if num - 12 == 0:
        return f"You need 1 year to repay this credit!"
    elif num % 12 == 0:
        return f"You need {num//12} years to repay this credit!"
    elif num1 > 1:
        return f"You need {num1} years and {num2} months to repay this credit!"
    elif num2 >= 11 :
        num1 += 1
        return f"You need {num1} years to repay this credit!"





parser = argparse.ArgumentParser()   # arguments adding
parser.add_argument("--type") 
parser.add_argument("--principal",type = int)
parser.add_argument("--payment",type = int)
parser.add_argument("--periods",type = int)
parser.add_argument("--interest",type = float)
args = parser.parse_args()

if args.type not in ["diff" , 'annuity']:   # Arguments checking
    print("Incorrect parameters")
elif args.type == 'diff' and args.payment:
    print("Incorrect parameters")
elif args.type == 'diff' and args.payment:
    print("Incorrect parameters")
elif not args.interest:
    print("Incorrect parameters")
elif len(sys.argv) < 4:
    print("Incorrect parameters")
else:
        
    if args.type == 'diff':
        differentiated(args.principal , args.periods , interest_rate(args.interest))
        
    else:
        if not args.periods:
            ans = num_payments( args.payment , args.principal , interest_rate(args.interest))
            ans1 = convert(ans)
            print(ans1)
            print(f"Overpayment = {(ans * args.payment)-args.principal}")
        if not args.payment:
            ans = annuity(args.principal , interest_rate(args.interest) , args.periods)
            print(f"Your annuity payment = {math.ceil(ans)}!")
            print(f"Overpayment = {round((math.ceil(ans) * args.periods) - args.principal)}")
        if not args.principal: 
            total = args.periods * args.payment
            print(f"Your credit principal = {principal(args.payment,interest_rate(args.interest) , args.periods)}!")
            print(f'Overpayment = {total - principal(args.payment,interest_rate(args.interest) , args.periods)}')

# this result is given with the overpayment that is done 
# this program can be run on the Command line 
