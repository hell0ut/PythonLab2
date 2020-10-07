import time
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

    #arr=list(map(int,input().split()))
    arr=[
        16883, 30968, 93059, 19760, 85783, 5183, 16465, 32033, 22247, 1212, 73694, 15819, 68295, 15992, 53644, 85800,
        72202, 62182, 20892, 94154, 76632, 75528, 48367, 4239, 78286, 96692, 78870, 76377, 46249, 20975, 83657, 35661,
        17996, 63587, 77537, 47433, 57603, 27877, 77410, 24422, 43452, 28897, 5850, 67362, 59223, 18186, 92294, 64960,
        13104, 76510, 28937, 65186, 91914, 28262, 58729, 51992, 69415, 706, 76304, 15023, 64324, 30211, 73320, 55197,
        58763, 99510, 58444, 98363, 82718, 48408, 28603, 69661, 98973, 91709, 16743, 54097, 69473, 55515, 27458, 16579,
        95300, 40662, 73619, 18143, 84529, 96929, 21362, 51775, 40397, 20143, 91460, 44627, 72720, 14085, 37305, 5976,
        38480, 71855, 79117, 18019
        ]
    start_time = time.time()
    for i in range(10):
        sorted_arr=patience_sort(arr)
    print("--- %s seconds ---" % (time.time() - start_time))
    for a in sorted_arr:
        print(a,sorted_arr[a])