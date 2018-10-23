def  weighted_avg(list,weight):
    sum = 0
    for i in range(len(list)):
        sum += list[i]* weight[i]
    return sum
    
print(weighted_avg([2, 5, 18, 1], [0.5, 0.2, 0.2, 0.1]))

