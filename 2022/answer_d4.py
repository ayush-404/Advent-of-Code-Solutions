def answer_part1():
    ans = 0
    with open('input_d4.txt', 'r') as f:
        for line in f:
          ranges = line.split(',')
          n1 = ranges[0].split('-')[0]
          n2 = ranges[0].split('-')[1]
          n3 = ranges[1].split('-')[0]
          n4 = ranges[1].split('-')[1]

          if int(n1) <= int(n3) <= int(n2) and int(n1) <= int(n4) <= int(n2):
              ans += 1
          elif int(n3) <= int(n1) <= int(n4) and int(n3) <= int(n2) <= int(n4):
              ans += 1
    
    return ans
        

def answer_part2():
    ans = 0
    with open('input_d4.txt', 'r') as f:
        for line in f:
          ranges = line.split(',')
          n1 = ranges[0].split('-')[0]
          n2 = ranges[0].split('-')[1]
          n3 = ranges[1].split('-')[0]
          n4 = ranges[1].split('-')[1]

          if int(n1) <= int(n3) <= int(n2) or int(n1) <= int(n4) <= int(n2):
              ans += 1
          elif int(n3) <= int(n1) <= int(n4) or int(n3) <= int(n2) <= int(n4):
              ans += 1
    
    return ans

if __name__ == '__main__':
    print(answer_part1())