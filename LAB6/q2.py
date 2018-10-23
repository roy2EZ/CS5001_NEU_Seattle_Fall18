valid = []
outliers = []
flag = True

while flag == True:
    value = int(input("Please enter a number: "))
    if value == -99:
        flag = False
    elif (value>= -50 and value <= 100):
        valid.append(value)
    else:
        outliers.append(value)
    
total_list = valid + outliers
ave = sum(valid)/len(valid)

print(len(total_list),ave)