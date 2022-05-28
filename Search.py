import re


def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    left_index = -1 #探索範囲の左端のindex
    right_index = len(sorted_array) #探索範囲の右端のindex

    while (right_index - left_index) > 1:
        mid_index = round(left_index + (right_index - left_index) / 2) #探索範囲の中央のindex

        if sorted_array[mid_index] == target_number:
            return mid_index
        elif sorted_array[mid_index] >= target_number:
            right_index = mid_index
        else:
            left_index = mid_index
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()