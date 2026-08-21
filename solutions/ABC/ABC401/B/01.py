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
    N = int(input())
    S = []
    for _ in range(N):
        s_tmp = input()
        S.append(s_tmp)

    login_flag = False
    error_counter = 0

    for s in S:
        if s == "login":
            login_flag = True
        elif s == "logout":
            login_flag = False
        
        if login_flag == False and s == "private":
            error_counter += 1

    print(error_counter)


#-------------------実行-------------------#
main()