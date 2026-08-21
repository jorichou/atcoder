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
    Q = int(input())
    A = []
    head = 0
    for _ in range(Q):
        query = sinput.int_list_input()
        if query[0] == 1:
            c = query[1]
            x = query[2]
            a = [x, c]
            A.append(a)
        elif query[0] == 2:
            head_x = A[head][0]
            head_v = A[head][1]
            k = query[1]
            if head_v > k:
                A[head][1] -= k
                print(head_x * k)
            elif head_v == k:
                head += 1
                print(head_x * k)
            else:
                total = 0
                while A[head][1] < k:
                    total += A[head][0] * A[head][1]
                    k -= A[head][1]
                    head += 1
                A[head][1] -= k
                total += A[head][0] * k
                print(total)


#-------------------実行-------------------#
main()