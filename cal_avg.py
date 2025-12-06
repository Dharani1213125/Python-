def cal_avg():
    list= [10, 20, 30, 40, 50]
    sum = 0
    for i in range(len(list)): 
        sum += list[i]         

    return sum / len(list)

print(cal_avg())
