#sequence.py
#prints all squares down to 1 from a givenn number
# Mitch Novak
#1/7/09

def main():
    start = eval(input("Enter a number:"))
    print ("Squares from", start, "down to 1:")
    for i in range(start, 1, -1):
        print(i*i, ",", end = " ")
    print ("1")
main()