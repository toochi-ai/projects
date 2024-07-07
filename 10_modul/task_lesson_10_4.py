filename = 'numbers.txt'
output = 'output.txt'

with open(filename) as f:
    min_ = max_ = float(f.readline())
    for line in f:
        num = float(line)
        if num > max_:
            max_ = num
        elif num < min_:
            min_ = num

    sum_ = min_ + max_
    print(sum_)

with open(output, 'w') as f:
    f.write(str(sum_))
print('---')

with open('estimates.txt', encoding='utf8') as file:
    for line in file:
        value = int(line.split()[-1])
        if value < 3:
            name = ' '.join(line.split()[:-1])
            print(name)
print('---')

with open('test.txt', 'r') as input_file:
    with open('output.txt', 'w') as output_file:
        for line in reversed(input_file.readline()):
            output_file.write(line)

with open('output.txt', 'r') as output_file:
    for line in output_file:
        print(line)
print('---')
