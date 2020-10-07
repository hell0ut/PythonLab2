import time
import os
def patience_sort(arr):
    compares, copies = 0, 0
    size = len(arr)
    piles = [[]*size for i in range(size)]
    j_size, cur_j = 0, 0
    for el in arr:
        for j in range(size):
            size_t=len(piles[j])
            compares += 1
            if size_t == 0 or (size_t > 0 and piles[j][-1] >= el):

                piles[j].append(el)
                copies += 1
                if size_t == 0:
                    j_size += 1
                break

    lenghts=[len(el) for el in piles]
    cur_j = 0
    for i in range(size):
        for j in range(lenghts[cur_j]):
            compares += 1
            if len(piles[j])>0 and piles[j][-1]<piles[cur_j][-1]:
                cur_j=j
        arr[i]=piles[cur_j].pop()
        copies += 1
        for j in range(j_size):
            if len(piles[j])>0:
                cur_j=j
                break
    return {'arr':arr, 'compares':compares, 'copies':copies}




if __name__=='__main__':
    tree=os.walk('IncomingDataLab2')
    m=next(tree)
    for el in m[-1]:
        with open('IncomingDataLab2/'+el,'r',encoding='utf-8') as arr_file:
            arr=list(map(int,arr_file.read().split(',')))
            start_time = time.time()
            sorted_arr=patience_sort(arr)#тут бля название вашей функции сортировки
            print("--- %s seconds ---" % (time.time() - start_time))
            print(el)
            for a in sorted_arr:
                print(a,sorted_arr[a])