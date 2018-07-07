def merge(A, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0 , n1):
        L[i] = A[l + i]
 
    for j in range(0 , n2):
        R[j] = A[m + 1 + j]
 
    # Merge the temp arrays back into A[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

def merge_sort(A, l, r):
    if l < r:
        m = int((l + r) / 2)
        merge_sort(A, l, m)
        merge_sort(A, m+1, r)
        merge(A, l, m, r)


def main():
    a = [9, 2, 8, 1, 5, 6, 10, 4, 3, 7]
    merge_sort(a, 0, len(a)-1)
    print(a)

if __name__ == '__main__':
    main()
