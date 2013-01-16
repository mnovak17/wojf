# factorial.py
# gives factorial of given number

#Mitch Novak

def main():
    n = eval(input("Please give me a number: \n"))
    product = 1
    for i in range (1, n +1):
        product = product * i
    print("The factorial of ", n , " is ", product)
main()
    