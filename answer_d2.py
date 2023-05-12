def answer():
    ans = 0
    with open('input_d2.txt', 'r') as f:
        for line in f:
            players = line.split(' ')
            opp = players[0].strip()
            our = players[1].strip()

            print(opp, our)
            if opp == 'A':
                if our == 'X':
                    print("hello")
                    ans += 3 + 1
                elif our == 'Y':
                    ans += 6 + 2
                elif our == 'Z':
                    ans += 3
            elif opp == 'B':
                if our == 'X':
                    ans += 1
                elif our == 'Y':
                    ans += 2 + 3
                elif our == 'Z':
                    ans += 6 + 3
            elif opp == 'C':
                if our == 'X':
                    ans += 6 + 1
                elif our == 'Y':
                    ans += 2
                elif our == 'Z':
                    ans += 3 + 3

    return ans

def answer_part2():
    ans = 0
    with open('input_d2.txt', 'r') as f:
        for line in f:
            players = line.split(' ')
            opp = players[0].strip()
            play = players[1].strip()

            if play == 'Z':
                if opp == 'A':
                    ans += 2 + 6
                elif opp == 'B':
                    ans += 3 + 6
                elif opp == 'C':
                    ans += 1 + 6
            elif play == 'Y':
                ans += 3
                if opp == 'A':
                    ans += 1
                elif opp == 'B':
                    ans += 2
                elif opp == 'C':
                    ans += 3
            elif play == 'X':
                if opp == 'A':
                    ans += 3
                elif opp == 'B':
                    ans += 1
                elif opp == 'C':
                    ans += 2

    return ans

if __name__ == '__main__':
    print(answer_part2())