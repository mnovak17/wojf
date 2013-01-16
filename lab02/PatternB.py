#patternB.py
#prints out a pattern of numbers
#Mitch Novak
#1/11/13

def main():
    n = eval(input("Enter a number:"))
    for i in range(1, n+1):
        for j in range(1 , n+1):
            print(i, end = " ")
        print()
main()