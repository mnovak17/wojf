#fibonacci.py
#prints the fibonacci number at a given index
#Mitch Novak
#1/7/13

def main():
    print("My incredible Fibonacci number generator!")
    n = eval(input("Plaese enter an integer:"))
    f0 = 1
    f1 = 1
    for i in range(3, n+1):
        temp = f0 + f1
        f0 = f1
        f1 = temp
    print("The", n,"th number in the Fibonacci sequence is", f1)
main()