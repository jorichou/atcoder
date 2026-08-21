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
def main():
    sinput = Input()
    N, M = sinput.int_map_input()
    X = N**0
    for i in range(1, M+1):
        X += N**i
    if X <= 1.0e9:
        print(X)
    else:
        print("inf")

#-------------------実行-------------------#
main()