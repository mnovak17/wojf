#patternD.py
#prints out a pattern of numbers
#Mitch Novak
#1/11/13

def main():
    n = eval(input("Enter a number:"))
    for i in range(1, n+1):
        for j in range(0 , i +1):
            for z in range(1, j+1):
                print(j, end=" ")
        print()
main()