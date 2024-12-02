def check_increasing(array):
    #return all(int(array[i]) > int(array[i-1]) for i in range(1, len(array)))
    for i in range(1, len(array)):
        if(array[i] <= array[i-1]):
            return False
        #elif(check_adjecent(array[i]), array[i-1]):
            return False
    return True

def check_decreasing(array):
    #return all(int(array[i]) < int(array[i-1]) for i in range(1, len(array)))
    for i in range(1, len(array)):
        if(array[i] >= array[i-1]):
            return False
    return True

def check_adjecent(first:int, adjecent:int):
    print ('{first} -- {adjecent}') 
    if((first - adjecent) > 3 and (first-adjecent) < 1):
        return False
    return True

total = 0
with open('input2', 'r') as file:
    for line in file:
        split = line.split(' ')
        print(split)
        if(check_decreasing(split) or check_increasing(split)):
            total += 1

print(f'total amount of reports: {total}')   
                