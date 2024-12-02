left = []
right = []

with open('input', 'r') as file:
    for line in file:
        result = line.split('   ')
        left.append(int(result[0]))
        right.append(int(result[1]))
        
left.sort(reverse=False)
right.sort(reverse=False)

total = 0
for i in range(len(left)):
    value = (max(left[i], right[i]) - min(left[i],right[i]))
    print(f'distance between {left[i]} and {right[i]} equals {value}')
    total += value

print(f'total value = {total}')