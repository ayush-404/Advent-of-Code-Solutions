import re

'''In this part the order of the moving is reversed.'''
def input_reader():
    with open('input_d5.txt', 'r') as f:
        lines = f.readlines()
        stacks = [[] for i in range(0, 9)]
        for j in range(0, len(lines[0]), 4):
            for i in range(7, -1, -1):
                    if lines[i][j:j+4].strip() != '':
                        stacks[j//4].append(lines[i][j+1])
        
        print(stacks[1])
        return (lines [10:], stacks)

def answer_part1():
    ans = ''
    lines, stacks = input_reader()
    
    for line in lines:
        arr = [int(x) for x in re.findall(r'\d+', line)]
        for i in range(0, arr[0]):
            temp = stacks[arr[1] - 1].pop()
            stacks[arr[2] - 1].append(temp)
    
    for s in stacks:
        ans += s.pop()

    return ans

'''
In this part the order of the moving remains the same.
'''
def answer_part2():
    ans = ''

    lines, stacks = input_reader()

    for line in lines:
        arr = [int(x) for x in re.findall(r'\d+', line)]
        temp = []
        for i in range(0, arr[0]):
            x = stacks[arr[1] - 1].pop()
            temp.append(x)
        
        for i in range(len(temp)):
            x = temp.pop()
            stacks[arr[2] - 1].append(x)

    for s in stacks:
        ans += s.pop()

    return ans

if __name__ == '__main__':
    print(answer_part2())