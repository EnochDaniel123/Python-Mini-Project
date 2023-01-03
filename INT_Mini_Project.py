#Leap Year Program

#Taking input from user for starting year
year = int(input("Enter the Starting Year: "))
# taking input from user for ending year
year2 = int(input("Enter the Ending Year: "))

# creating empty list
s = []
# creating empty list
b = []

for i in range(year,(year2)+1):                    # Loop for starting year to ending year
    if i % 4 == 0:                                 # Conditions for checking leap year or not
        if i % 100 != 0:
            s.append(i)                            # Using append function to store value in the Lists
                                                   
        elif i % 100 == 0:
            if i % 400 == 0:
                s.append(i)

            else:
                b.append(i)
    else:
        b.append(i)

# printing leap year

print("Leap Years: ",end="")        
for x in range(len(s)):                   #Converting List of Leap-Years into form of output by traversing it
    print(s[x],end=", ")

print("\n")

# printing non leap year

print(" Non Leap Years: ",end="")        
for x in range(len(b)):                   #Converting List of Non-Leap-Years into form of output by traversing it
    print(b[x],end=", ")
