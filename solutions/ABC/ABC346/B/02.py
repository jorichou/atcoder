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
    import sys
    import math
    sinput = Input()
    W, B = sinput.int_map_input()
    S = "wbwbwwbwbwbw"

    window_size = W + B
    listed_S = list(S * math.ceil(window_size / 10))

    def check_window(S, window_size):
        w_count = 0
        b_count = 0
        checked = S[0:window_size]
        for s in checked:
            if s == "w":
                w_count += 1
            else:
                b_count += 1
        return w_count, b_count
    
    w_count, b_count = check_window(listed_S, window_size)
    start = 0
    while start + window_size <= len(listed_S):
        # print(f"w_count: {w_count}, b_count: {b_count}, start: {start}")
        if w_count == W and b_count == B:
            print("Yes")
            sys.exit()
        out = listed_S[start] # ウィンドウの外に出る文字
        if out == "w":
            w_count -= 1
        else:
            b_count -= 1

        start += 1
        if start + window_size > len(listed_S):
            break
        if listed_S[start+window_size-1] == "w":
            w_count += 1
        else:
            b_count += 1

    print("No")
    # print(len(listed_S))

#-------------------実行-------------------#
main()