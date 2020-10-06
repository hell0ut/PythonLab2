import time
def patience_sort(arr):
    size = len(arr)
    piles = [[]*size for i in range(size)]
    j_size, cur_j = 0, 0
    for el in arr:
        for j in range(size):
            size_t=len(piles[j])
            if size_t == 0 or (size_t > 0 and piles[j][-1] >= el):
                piles[j].append(el)
                if size_t == 0:
                    j_size += 1
                break
    for i in range(size):
        for j in range(j_size):
            if len(piles[j])>0 and piles[j][-1]<piles[cur_j][-1]:
                cur_j=j
        arr[i]=piles[cur_j].pop()
        for j in range(j_size):
            if len(piles[j])>0:
                cur_j=j
                break
    return arr




if __name__=='__main__':

    #arr=list(map(int,input().split()))
    arr=[

        ]
    start_time = time.time()
    for i in range(1):
        sorted_arr=patience_sort(arr)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(sorted_arr)