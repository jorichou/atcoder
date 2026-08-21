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
    import sys
    sinput = Input()
    S = input()
    t_indexes = []
    max_rate = 0
    for i in range(len(S)):
        if S[i] == 't':
            t_indexes.append(i)

    for i in range(len(t_indexes)-1):
        for j in range(i, len(t_indexes)):
            if t_indexes[j] + 1 - t_indexes[i] >= 3:
                rate = (j + 1 - i - 2) / (t_indexes[j] + 1 - t_indexes[i] - 2)
            else:
                rate = 0

            if rate > max_rate:
                max_rate = rate
            else:
                pass
    
    print(max_rate)

#-------------------実行-------------------#
main()