#patternE.py
#prints out an E
#Mitch Novak
#1/11/13

def main():
    n = eval(input("Enter a number:"))
    for i in range(0, n+2):
        print("*" , end = " ")
    print()
    for i in range(0, n):
        print("*")
    for i in range(0, n+1):
        print("*" , end = " ")
    print()
    for i in range(0, n):
        print("*")
    for i in range(0, n+2):
        print("*" , end = " ") 
        
    
main()