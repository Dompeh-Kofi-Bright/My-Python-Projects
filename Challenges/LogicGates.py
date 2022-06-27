
import sys
def wrong():
    print("Values are invalid.")

def AndLogic (x, y):
    if (x == '0' and y == '1'):
        print ('The logic answer is',x)
    elif(x == '1' and y == '0'):
        print ('The logic answer is',y)
    elif(x == '0' and y == '0' ):
        print('The logic answer is',x)
    elif(x == '1' and y == '1' ):
        print('The logic answer is',x)
    else:
        wrong()
    
def OrLogic (x, y):
    if(x == '0' and y == '1'):
        print('The logic answer is',y)
    elif(x == '1' and y == '0'):
        print('The logic answer is',x)
    elif(x == '1' and y =='1'):
        print('The logic answer is',x)
    elif(x == '0' and y == '0'):
        print('The logic answer is',x)
    else:
        wrong()

def XorLogic (x, y):
    if(x == '0' and y == '1'):
        print('The logic answer is', y)
    elif(x =='1' and y == '0'):
        print('The logic answer is', x)
    elif(x == '1' and y == '1'):
        print('The logic answer is', x)
    elif(x == '0' and y == '0'):
        print('The logic answer is', x)
    else:
        wrong()

def process(a, b, c):
    a = input("Input your first value\n> ")
    b = input("Input your second value\n> ")
    c = input("The logic type\n> ")

    while(c == "or" or c == "OR" or c == "Or"):
        OrLogic(a, b)
        ask = input("\nWould you like to run again?\n> ")
        if(ask == "No" or ask == "no" or ask == "NO"):
            quit()
        else:
            print("\nLoading.....\n")
            process("a", "b", "c")

    while(c == "and" or c == "AND" or c == "And"):
        AndLogic(a, b)
        ask = input("\nWould you like to run again?\n> ")
        if(ask== "No" or ask == "no" or ask == "NO"):
            quit()
        else:
            print("\nLoading.....\n")
            process("a", "b", "c")

    while(c == "xor" or c == "XOR" or c =="Xor"):
        XorLogic(a, b)
        ask = input("\nWould you like to run again?\n> ")
        if(ask == "No" or ask == "no" or ask == "NO"):
            quit()
        else:
            print("\nLoading.....\n")
            process(a, b, c)

process("a", "b", "c")

