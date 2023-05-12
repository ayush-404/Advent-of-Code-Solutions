def answer_part1():
    ans = 0
    with open('input_d3.txt', 'r') as f:
        for line in f:
            n = len(line.strip())
            s1 = set()
            s2 = set()
            for i in range(0, n // 2):
                s1.add(line[i])
            for i in range(n // 2, n):
                s2.add(line[i])
            word = s1.intersection(s2).pop()

            if word.isupper():
                ans += ord(word) - 64 + 26
            else:
                ans += ord(word) - 96

    return ans

def answer_part2():
     ans = 0

     with open('input_d3.txt', 'r') as f:
         lines = f.readlines()

         for i in range(0, len(lines), 3):
                sets = [set(), set(), set()]
                for j in range(3):
                    for c in lines[i + j].strip():
                        sets[j].add(c)

                word = sets[0].intersection(sets[1]).intersection(sets[2]).pop()

                if word.isupper():
                    ans += ord(word) - 64 + 26
                else:
                    ans += ord(word) - 96
     return ans

if __name__ == '__main__':
    print(answer_part2())