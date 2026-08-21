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
    sinput = Input()
    H, W = sinput.int_map_input()
    C = sinput.grid_input(H)
    x_list = [0 for _ in range(W)]

    for j in range(W):
        for i in range(H):
            if C[i][j] == "#":
                x_list[j] += 1

    print(*x_list)

#-------------------実行-------------------#
main()