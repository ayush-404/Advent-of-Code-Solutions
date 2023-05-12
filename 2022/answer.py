def answer():
    
    ans = [0, 0, 0]
    curr = 0
    with open('input.txt', 'r') as f:
        for line in f:
            if line in ["\n", "\r\n"]:
                ans.sort()
                for i in range(3):
                    if curr > ans[i]:
                        ans[i] = curr 
                        break
                curr = 0
            else:
                curr += int(line)

    return sum(ans)



if __name__ == '__main__':
    print(answer())