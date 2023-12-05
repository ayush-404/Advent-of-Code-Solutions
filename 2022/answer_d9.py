import re

'''In this part the order of the moving is reversed.'''
def input_reader():
    dirs = []
    steps = []
    with open('input_d5.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            dirs.append(line[0])
            steps.append(int(line[1:]))
    
    return dirs, steps

def answer_part1():
    ans = 0
    dirs, steps = input_reader()
    x_pos = set()
    y_pos = set()
    head_pos = [0, 0]
    tail_pos = [0, 0]

    for dir in dirs:
        if dir == 'U':
            head_pos[1] += 1
        elif dir == 'D':
            head_pos[1] -= 1
        elif dir == 'L':
            head_pos[0] -= 1
        elif dir == 'R':
            head_pos[0] += 1

        x_pos.add(head_pos[0])
        y_pos.add(head_pos[1])
        
        
    

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