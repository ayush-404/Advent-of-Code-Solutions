from functools import reduce

def answer_part1():
    mat = []
    with open('input_d8.txt') as f:
      for line in f:
          temp = []
          for c in line.strip():
            temp.append(int(c))
          mat.append(temp)

      def traverse(mat, i, j):
          val = mat[i][j]
          vis_count = 4
          for x in range(i - 1, -1, -1):
            if mat[x][j] >= val:
              vis_count -= 1
              break
          for x in range(i + 1, len(mat)):
            if mat[x][j] >= val:
              vis_count -= 1
              break
          for y in range(j - 1, -1, -1):
            if mat[i][y] >= val:
              vis_count -= 1
              break
          for y in range(j + 1, len(mat[0])):
            if mat[i][y] >= val:
              vis_count -= 1
              break

          return 1 if vis_count > 0 else 0

      ans = 0
      for i in range(0, len(mat)):
        for j in range(0, len(mat[0])):
          ans += traverse(mat, i, j)

    return ans


def answer_part2():
    mat = []
    with open('input_d8.txt') as f:
      for line in f:
          temp = []
          for c in line.strip():
            temp.append(int(c))
          mat.append(temp)

      def traverse(mat, i, j):
          val = mat[i][j]
          vis_counts = [0, 0, 0, 0]

          for x in range(i - 1, -1, -1):
              vis_counts[0] += 1
              if mat[x][j] >= val:
                 break
              
          for x in range(i + 1, len(mat)):
            vis_counts[1] += 1
            if mat[x][j] >= val:
              break

          for y in range(j - 1, -1, -1):
            vis_counts[2] += 1
            if mat[i][y] >= val:
              break

          for y in range(j + 1, len(mat[0])):
            vis_counts[3] += 1
            if mat[i][y] >= val:
              break

          return reduce(lambda x, y: x * y, vis_counts)

      ans = 0
      for i in range(0, len(mat)):
        for j in range(0, len(mat[0])):
          ans = max(ans, traverse(mat, i, j))

    return ans
   

if __name__ == '__main__':
    print(answer_part2())