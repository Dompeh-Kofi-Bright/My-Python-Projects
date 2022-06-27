number = input("Enter Your number to generate it's factors.\n> ")

print("The Factors Of",number,"Are:")

for num in range(1,1000,1):
    if(int(number) % num == 0):
        print(num)
    else:
        continue    
    