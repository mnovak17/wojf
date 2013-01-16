#patternN.py
#prints out an E
#Mitch Novak
#1/11/13

def main():
    n = eval(input("Enter a number:"))
    print("*", end = '')
    for i in range(1, n+1):
        print(" ", end='')
    print("*")
    for i in range(1,n + 1):
        print("*", end='')
        for j in range(1,i):
            print(" ", end = '')
        print("*", end='')
        for j in range(i, n):
            print(" ", end = '')
        print("*")
    print("*", end = '')
    for i in range(1, n+1):
        print(" ", end='')
    print("*")
    
main()