# Leaf nodes and files and internal nodes are directories
class TreeNode:
    def __init__(self, val=0, name='', parent = None, type=""):
        self.size = val
        self.name = name
        self.children = []
        self.parent = parent
        self.type = type
    
    def __str__(self):
        return self.name + ' ' + str(self.size)

def read_input_get_tree():
    root = TreeNode(0)
    with open('input_d7.txt', 'r') as f:
        for line in f:
            split_line = line.strip().split(' ')
            if split_line[0] == '$':
                if split_line[1] == 'cd':
                    if split_line[2] == '..':
                        root = root.parent
                    elif split_line[2] == '/':
                        root = root
                    else:
                        for child in root.children:
                            if child.name == split_line[2]:
                                root = child
                                break
            else:
                if split_line[0] == 'dir':
                    root.children.append(TreeNode(0, split_line[1], root, "dir"))
                else:
                    root.children.append(TreeNode(int(split_line[0]), split_line[1], root, "file"))
                    root.size += int(split_line[0])
        
    stack = [root]
    ans = 0
    while len(stack) > 0:
        curr = stack.pop()
        print(curr.name, curr.type, curr.size)
        for child in curr.children:
            if (child.type == "dir"):
                ans += child.size

    return root
                


# Get the sum of the leaf nodes
def answer_part1(root):
    stack = [root]
    ans = 0
    while len(stack) > 0:
        curr = stack.pop()
        if curr.type=="dir" and curr.size > 100000:
            print("yeee")
            ans += 1
        
        for child in curr.children:
            stack.append(child)

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
    root = read_input_get_tree()
    print(answer_part1(root))