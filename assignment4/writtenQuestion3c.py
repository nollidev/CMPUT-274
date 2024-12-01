def quick_sort_extra_storage(S, a, b):
    if a >= b:
        return
    pivot = S[b] # choose the pivot
    # Create new arrays for the partitions
    left_partition = []
    right_partition = []
    for i in range (a, b): # iterate only until b (excluding pivot)
        if S[i] < pivot:
            left_partition.append(S[i])
        else:
            right_partition.append(S[i])

    print("Data to recurse:", [S, a, b, S[a], S[b], S[a:b+1], left_partition, pivot, right_partition])    
    # Sort left partition
    left_partition = quick_sort_extra_storage(left_partition, 0, len(left_partition) - 1)
    # Sort right partition
    right_partition = quick_sort_extra_storage(right_partition, 0 , len(right_partition) - 1)

    print("Updated partitions:", [left_partition, pivot, right_partition])

    # SOLUTION HERE:
    sorted_partition = left_partition + [pivot] + right_partition
    # print("Sort before insert:",sorted_partition)
    print("Attempt to combine: ", S[0:a], sorted_partition, S[b+1:len(S)])
    # print("Result:", S)
    
    return S[0:a] + sorted_partition + S[b+1:len(S)]

S = [22, 56, 62, 7, 6, 37, 256, 26, 72, 532]
quick_sort_extra_storage(S, 2, 8)
print(S)