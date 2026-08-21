# from collections import Counter
import sys
# import bisect
# import fractions
# from itertools import permutations, combinations, combinations_with_replacement, product
# import numpy as np
import math
from collections import defaultdict

"""
AtCoderInputクラス
入力処理を簡単にするためのクラス

メソッド:
- single_input: 単一入力
- multiple_input: 複数入力
- list_input: リスト入力
- grid_input: グリッド入力

パラメータ:
- input_type: 入力の型（int, float, strなど）
- sep: 区切り文字（デフォルトはスペース）
- rows: グリッドの行数（grid_input用）

使用例:
aci = AtCoderInput()
n = aci.single_input(int)  # 単一整数入力
a, b = aci.multiple_input(int)  # 複数整数入力
lst = aci.list_input(int)  # 整数リスト入力
grid = aci.grid_input(3, int)  # 3行の整数グリッド入力
x, y = aci.multiple_input(float, sep=',')  # カンマ区切りの浮動小数点数入力
"""
class AtCoderInput: # 入力処理クラス
    def __init__(self):
        pass

    def single(self, input_type: type=int): # 単一入力
        return input_type(input())
    
    def multiple(self, input_type: type=int, sep=' '): # 複数入力
        return map(input_type, input().split(sep))
    
    def list(self, input_type: type=int, sep=' '): # リスト入力
        return list(map(input_type, input().split(sep)))
    
    def grid(self, rows:int, input_type: type=str, sep=' '): # グリッド入力
        grid = []
        for _ in range(rows):
            grid.append(list(map(input_type, input().split(sep))))
        return grid
    
"""
AtCoderOutputクラス
出力処理を簡単にするためのクラス

メソッド:
- single_output: 単一出力
- list_output: リスト出力
- grid_output: グリッド出力
- print_judge: 判定出力（Yes/No）

パラメータ:
- value: 出力する単一の値
- values: 出力するリスト
- grid: 出力するグリッド
- sep: 区切り文字（デフォルトはスペース）

使用例:
aco = AtCoderOutput()
aco.single_output(42)  # 単一出力
aco.list_output([1, 2, 3, 4])  # リスト出力
aco.grid_output([[1, 2], [3, 4]])  # グリッド出力
aco.print_judge(True)  # 判定出力
"""
class AtCoderOutput: # 出力処理クラス
    def __init__(self):
        pass

    def single(self, value): # 単一出力
        print(value)
    
    def list(self, values: list, sep=' '): # リスト出力
        print(sep.join(map(str, values)))

    def grid(self, grid: list, sep=''): # グリッド出力
        for row in grid:
            print(sep.join(map(str, row)))
    
    def judge(self, judge: bool): # 判定出力
        print("Yes" if judge else "No")

# def input_test(): # 入力処理テスト関数
#     aci = AtCoderInput()
#     n = aci.single_input(int)
#     a, b = aci.multiple_input(int)
#     lst = aci.list_input(int)
#     grid = aci.grid_input(3, int)
#     print(n, a, b, lst, grid)

# def output_test(): # 出力処理テスト関数
#     aco = AtCoderOutput()
#     aco.single_output(42)
#     aco.list_output([1, 2, 3, 4])
#     aco.grid_output([[1, 2], [3, 4]])
#     aco.print_judge(True)
#     aco.print_judge(0)

def dic_diff(d, target):
    for key in d.keys():
        if d[key] < target:
            d[key] = 0
        else:
            d[key] -= target
    return d

if __name__ == "__main__": # メイン処理
    # input_test()
    # output_test()
    acin = AtCoderInput()
    acout = AtCoderOutput()

    t = acin.single()

    for _ in range(t):
        n_a, n_b, n_c = acin.multiple()
        n_ch = {'A': n_a, 'B': n_b, 'C': n_c}
        contest_count = 0

        ch = min(n_ch, key=n_ch.get)
        if ch == 'A' or ch == 'C': # ok
            # print("a")
            print(n_ch[ch])
        else:        
            contest_count += n_ch['B']
            n_ch = dic_diff(n_ch, n_ch['B'])
            n_ch.pop('B')
            contest_count += min([n_ch['A'], n_ch['C'], (n_ch['A'] + n_ch['C']) // 3])
            # while (n_ch['A'] + n_ch['C'] >= 3) and (n_ch['A'] > 0 and n_ch['C'] > 0):
            # if n_ch['A'] < n_ch['C']: # Aのほうが少ないとき
            #     c_half = n_ch['C'] // 2
            #     # n_ch['C'] -= c_half
            #     if n_ch['A'] <= c_half: # AがCの半分以下のとき
            #         contest_count += n_ch['A']
            #         n_ch = dic_diff(n_ch, n_ch['A'])
            #         # print("b")
            #         # break
            #     else: # AがCの半分より多いとき
            #         # contest_count += c_half
            #         # n_ch = dic_diff(n_ch, c_half)
            #         contest_count += ((n_ch['A'] + n_ch['C']) // 3)
            #         # break
            #         # print("c")

            # else: # Cのほうが少ないとき 
            #     a_half = n_ch['A'] // 2
            #     # n_ch['A'] -= a_half
            #     if n_ch['C'] <= a_half: # CがAの半分以下のとき
            #         contest_count += n_ch['C']
            #         n_ch = dic_diff(n_ch, n_ch['C'])
            #         # print("d")
            #         # break

            #     else: # CがAの半分より多いとき
            #         # contest_count += a_half
            #         # n_ch = dic_diff(n_ch, a_half)
            #         contest_count += ((n_ch['A'] + n_ch['C']) // 3)
            #         # break

            #             # print("e")
 
            print(contest_count)

            