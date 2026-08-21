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
    import pprint
    N = int(input())
    grid = [["-" for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N+1-i):
            if i <= j:
                for tate in range(i, j):
                    for yoko in range(i, j):
                        if i % 2 == 0:
                            grid[tate][yoko] = "#"
                        else:
                            grid[tate][yoko] = "."
            else:
                pass
    for row in grid:
        print(*row, sep='')



#-------------------実行-------------------#
main()