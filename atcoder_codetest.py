# from collections import Counter
# import sys
# import bisect
# import fractions
# from itertools import permutations, combinations, combinations_with_replacement, product
# import numpy as np

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

    def single_input(self, input_type:type): # 単一入力
        return input_type(input())
    
    def multiple_input(self, input_type:type, sep=' '): # 複数入力
        return map(input_type, input().split(sep))
    
    def list_input(self, input_type:type, sep=' '): # リスト入力
        return list(map(input_type, input().split(sep)))
    
    def grid_input(self, rows:int, input_type:type, sep=' '): # グリッド入力
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

    def single_output(self, value): # 単一出力
        print(value)
    
    def list_output(self, values:list, sep=' '): # リスト出力
        print(sep.join(map(str, values)))

    def grid_output(self, grid:list, sep=''): # グリッド出力
        for row in grid:
            print(sep.join(map(str, row)))
    
    def print_judge(self, judge:bool): # 判定出力
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

if __name__ == "__main__": # メイン処理
    # input_test()
    # output_test()
    aci = AtCoderInput()
    aco = AtCoderOutput()

    