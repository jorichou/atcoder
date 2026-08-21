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
    S = input()
    template = "abcdefghijklmnopqrstuvwxyz"

    s_set = set(S)
    for s in template:
        if s not in s_set:
            print(s)
            break


#-------------------実行-------------------#
main()