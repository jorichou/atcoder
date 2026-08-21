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
    N, M = sinput.int_map_input()
    A = sinput.int_list_input()
    total = sum(A)
    if total <= M:
        print("Yes")
    else:
        print("No")
        
        
    
    

#-------------------実行-------------------#
main()