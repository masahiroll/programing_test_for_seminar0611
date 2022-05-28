def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    j = 0
    k = 1
    flg = False

    for i in range(len(array)):
        for j in range(j,len(array)): #前方から基準値以上のindexを探索
            if array[j] >= pivot:
                break

        for k in range(k,len(array)): #後方から基準値未満のindexを探索
            if j <= (len(array) - k): #先頭と末端の探索がぶつかったかの判定
                if array[-k] < pivot:

                    tmp_num = array[j] #値を交換するためにtmp_numに一時的に格納
                    array[j] = array[-k]
                    array[-k] = tmp_num

                    break
            else:
                array_front = list(array[:(len(array) - k)]) #分割後の基準値未満のグループ
                array_rear = list(array[(len(array) - k):]) #分割後の基準値以上のグループ

                flg = True #分割に成功したのでforループを抜けるためのフラグを立てる
                break
        if flg:
            break

        j += 1
        k += 1

    return array
    # ここまで記述

if __name__ == '__main__':
    main()