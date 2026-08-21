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
    N = int(input())
    S = []
    results = []
    for _ in range(N):
        s = input()
        S.append(s)
    
    for i in range(N):
        for j in range(N):
            if i != j:
                result = S[i] + S[j]
                results.append(result)

    results = set(results)

    print(len(results))
        
        
    
    

#-------------------実行-------------------#
main()