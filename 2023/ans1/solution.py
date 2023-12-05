def part1():
  with open("input.txt") as f:
    lines = f.readlines()

    count = 0
    ans = [0,0]
    a = 0
    for line in lines:
      for c in line:
        if c.isnumeric():
          ans[count] = c
          count = -1
          ans[count] = c
      print(ans)
      a += int(ans[0] + ans[1])
      ans = [0,0]
      count = 0
    
    print(a)
  return a


def get_formatted_line(line):
  nums = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
  ]
  
  ans = ""

  for i in range(len(line)):
    if line[i] in [num[0] for num in nums]:
      new_line = line[i: i+5 if i+5 < len(line) else len(line)]
      if new_line[0:3] in nums:
        ans += str(nums.index(new_line[0:3]) + 1)
        i += 3
      elif new_line[0:4] in nums:
        ans += str(nums.index(new_line[:4]) + 1)
        i += 4
      elif new_line[0:5] in nums:
        ans += str(nums.index(new_line[:5]) + 1)
        i += 5
    else:
      ans += line[i]
    
  return ans


def part2():
  nums = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
  ]

  with open("input.txt") as f:
    lines = f.readlines()
    count = 0
    ans = [0,0]
    a = 0
    for line in lines:
      line = get_formatted_line(line)

      for c in line:
        if c.isnumeric():
          ans[count] = c
          count = -1
          ans[count] = c
      print(line, ans)
      a += int(ans[0] + ans[1])
      ans = [0,0]
      count = 0
  return a

print(part1(), part2())