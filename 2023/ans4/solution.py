def part1():
  with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    ans = 0
    for line in lines:
      cards = line.split('|')
      winning = cards[0].split(":")[1].strip().split(" ")
      winning = [int(x) for x in winning if x != '']
      print(winning)
      ours = cards[1].strip().split(" ")
      ours = [int(x) for x in ours if x != '']

      curr = 0
      for x in ours:
        if x in winning:
          winning.remove(x)
          curr = 1 if curr == 0 else curr*2
      ans += curr
  return ans

print(part1())