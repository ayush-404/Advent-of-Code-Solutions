def answer_part1():
    ans = 0
    with open('input_d6.txt', 'r') as f:
        ans = 0
        line = f.readline().strip()

        frame = [line[i] for i in range(0, 4)]
        s1 = set(frame)
        for j in range(4, len(line)):
            if len(s1) == len(frame):
                return ans
            else:
                frame.pop(0)
                frame.append(line[j])
                s1 = set(frame)
                ans += 1

        return ans
            

def answer_part2():
    ans = 0
    with open('input_d6.txt', 'r') as f:
        ans = 0
        line = f.readline().strip()

        frame = [line[i] for i in range(0, 14)]
        s1 = set(frame)
        for j in range(14, len(line)):
            if len(s1) == len(frame):
                return ans
            else:
                frame.pop(0)
                frame.append(line[j])
                s1 = set(frame)
                ans += 1

        return ans

if __name__ == '__main__':
    print(answer_part2() + 14)