from collections import Counter
import sys

"""
AtCoderInputクラス
入力処理を簡単にするためのクラス

メソッド:
- single_input: 単一入力
- multiple_input: 複数入力
- list_input: リスト入力

パラメータ:
- input_type: 出力の型（int, float, strなど）
- sep: 区切り文字（デフォルトはスペース）

使用例:
aci = AtCoderInput()
n = aci.single_input(int)  # 単一整数入力
a, b = aci.multiple_input(int)  # 複数整数入力
lst = aci.list_input(int)  # 整数リスト入力
x, y = aci.multiple_input(float, sep=',')  # カンマ区切りの浮動小数点数入力
"""
class AtCoderInput: # 入力処理クラス
    def __init__(self):
        pass

    def single_input(self, input_type): # 単一入力
        return input_type(input())
    
    def multiple_input(self, input_type, sep=' '): # 複数入力
        return map(input_type, input().split(sep))
    
    def list_input(self, input_type, sep=' '): # リスト入力
        return list(map(input_type, input().split(sep)))
    

if __name__ == "__main__": # メイン処理
    aci = AtCoderInput()
    n = aci.single_input(int)
    print(f"n\t type: {type(n)}")


