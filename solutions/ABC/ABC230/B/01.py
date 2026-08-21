#------------------モジュール------------------#
class Input:
    def spase_split_input(self):
        return input().split(' ')
    
    def int_map_input(self):
        return map(int, self.spase_split_input())
    
    def int_list_input(self):
        return list(self.int_map_input())
    
    def grid_input(self, height):
        return [list(input()) for _ in range(height)]
    
class Output:
    def print_judge(self, judge):
        print("Yes" if judge else "No")

#------------------メイン処理------------------#
import sys

def main():
    S = input()
    o = 0
    x = 0

    if len(S) == 1:
        print("Yes")
        sys.exit()
    elif len(S) == 2:
        if S == "oo":
            print("No")
            sys.exit()
        else:
            print("Yes")
            sys.exit()
    
    for i in range(len(S)):
        s = S[i]
        if s == "o":
            o += 1
            if x < 2 and i > 1:
                print("No")
                sys.exit()
            else:
                x = 0
        else:
            x += 1
            o = 0

        if o > 1:
            print("No")
            sys.exit()
        elif x > 2:
            print("No")
            sys.exit()
    print("Yes")


#-------------------実行-------------------#
main()