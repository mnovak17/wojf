#sum.py
#sums the numbers up to n

# Mitch Novak

def main():
    sum = 0
    n = eval(input("Please give me a number: \n"))
    for i in range(1, n + 1):
        sum = sum + i
    print ("The sum of the first ", n, " positive integers is ", sum)
    
main()