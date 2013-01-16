#interest.py
#get a deposit, interest rate, monthly deposit, and number of months
#then print out total money after n months
#Mitch Novak
#1/7/13

def main():
    print ("Welcom to the Interest Calculator!")
    print()
    base = eval(input("Enter your initial savings:"))
    rate = eval(input("Enter the monthly interest rate:"))
    month = eval(input("Enter your monthly contribution:"))
    nMonth = eval(input("How many months would you like computed:"))
    print ()
    print("Initially you put in $", base)
    for i in range(1, nMonth + 1):
        base = base + (base * rate)
        base = base * 100
        base = int(base)
        base = base/100
        base = base + month
        print("After month", i, "you would have", base)
main()