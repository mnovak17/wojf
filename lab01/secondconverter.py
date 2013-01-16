#secondconverter.py
#Translates seconds into hours, minutes, and seconds

#Mitch Novak

def main():
    print("Welcome to my Second Converter! \n")
    print("This program will properly calculate the number of \n minutes and seconds under 60 from a given number of seconds")
    n = eval(input("How many seconds have you got?"))
    total = n
    h = n//3600
    n = n%3600
    m = n//60
    s = n%60
    print (total, " seconds is equal to ", h ," hours, ", m ," minutes, and ", s ,"seconds.")
main()
