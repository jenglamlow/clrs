def insertion_sort(A):
    for j in range(1, len(A)): # Start from second element
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key: # Swap the key if larger
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key

def main():
    a = [9, 2, 1, 5, 6 , 10, 4]
    insertion_sort(a)
    print(a)

if __name__ == '__main__':
    main()
