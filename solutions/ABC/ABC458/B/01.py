# from collections import Counter
from socket import AddressInfo
import sys
import itertools
import heapq
# import bisect
# import fractions
# from itertools import permutations, combinations, combinations_with_replacement, product
# import numpy as np
import math
import pprint
from collections import defaultdict
from collections import deque

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
grid = aci.grid_input(3)  # 3行のグリッド入力
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
    
    def grid(self, rows:int): # グリッド入力
        grid = []
        for _ in range(rows):
            grid.append(list(input()))
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
    
    def list_obj(self, values: list, sep=' '): # リスト出力
        print(sep.join(map(str, values)))

    def grid(self, grid: list, sep=''): # グリッド出力
        for row in grid:
            print(sep.join(map(str, row)))
    
    def judge(self, judge: bool): # 判定出力
        print("Yes" if judge else "No")

def input_test(): # 入力処理テスト関数
    aci = AtCoderInput()
    n = aci.single(int)
    a, b = aci.multiple(int)
    lst = aci.list(int)
    grid = aci.grid(3)
    print(n, a, b, lst, grid)

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

def getRD(x, y):
    r = math.sqrt(x**2+y**2)
    rad = math.atan2(y, x)
    degree = math.degrees(rad)
    return r, degree

def delete_monster(start, goal, sum_monsters, monsters: dict):
    total = sum_monsters[start] - sum_monsters[goal] + monsters[goal]
    return total
    

# 迷路を幅優先探索する関数
# 幅優先探索に必要なもの：探索済み頂点の配列、探索予定頂点を管理するキュー    
"""
pram:
    G: 迷路本体
    sy: スタート位置のy座標
    sx: スタート位置のx座標
    gy: ゴールのy座標
    gx: ゴールのx座標
return: スタートからゴールまでの最短距離
"""
# def dfs_maze(C: G: list[list[str]], sy: int, sx: int, gy: int, gx: int):
#     sy -= 1
#     sx -= 1
#     gy -= 1
#     gx -= 1
    
#     # キューをQに入れ、スタート地点を追加
#     Q = deque()
#     Q.append([sy, sx])
    
#     # 未訪問と始点からの距離を管理するdistを定義。スタート地点に0を代入。
#     dist = [[-1]*C for _ in range(R)]
#     dist[sy][sx] = 0
    
#     # 今回は移動する４方向を事前に用意した。
#     dirc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
#     # キューの要素がなくなるまで処理を繰り返す。
#     while len(Q) > 0:
#       y, x = Q.popleft()
    
#     # 移動先で繰り返し処理
#       for dy, dx in dirc:
#         y2 = y + dy
#         x2 = x + dx
    
#     # 移動先が迷路の範囲内でなければ、continue
#         if not (0 <= y2 < R and 0 <= x2 < C):
#           continue
    
#     # 移動先が壁だったら、continue
#         if G[y2][x2] == "#":
#           continue
    
#     # 移動先が未訪問なら移動前の距離＋１をdistに入れて、キューに移動先の座標を追加
#         if dist[y2][x2] == -1:
#           dist[y2][x2] = dist[y][x] + 1
#           Q.append([y2, x2])
    
#     # ゴールの距離を出力
#     print(dist[gy][gx])
    


if __name__ == "__main__": # メイン処理
    # input_test()
    # output_test()
    acin = AtCoderInput()
    acout = AtCoderOutput()

    h, w = acin.multiple()
    if h == 1 and w == 1:
        print(0)
    elif h == 1:
        for j in range(w):
            if j == 0 or j == w - 1:
                print(1, end='')
            else:
                print(2, end='')
            if j < w - 1:
                print(' ', end='')
            else:
                print()
    elif w == 1:
        for i in range(h):
            if i == 0 or i == h - 1:
                print(1)
            else:
                print(2)
    else:
        for i in range(h):
            for j in range(w):
                if i == 0 or i == h - 1:
                    if j == 0 or j == w - 1:
                        print(2, end='')
                    else:
                        print(3, end='')
                else:
                    if j == 0 or j == w - 1:
                        print(3, end='')
                    else:
                        print(4, end='')
                if j < w - 1:
                    print(' ', end='')
            print()