import sys

def main():
    a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5 -22, 15, -4, 7]
    print(find_max_subarray(a, 0, len(a)-1))

def find_max_crossing_subarrary(A, l, m, r):
    l_sum = -sys.maxsize
    sum = 0
    max_left = None
    for i in range(m, l-1, -1):
        sum = sum + A[i]
        if sum > l_sum:
            l_sum = sum
            max_left = i
    
    r_sum = -sys.maxsize
    sum = 0
    max_right = None
    for i in range(m+1, r+1):
        sum = sum + A[i]
        if sum > r_sum:
            r_sum = sum
            max_right = i

    return (max_left, max_right, l_sum + r_sum)

def find_max_subarray(A, l, r):
    if l == r:
        return(l, r, A[l])
    else:
        m = (l + r) // 2
        l_low, l_high, l_sum = find_max_subarray(A, l, m)
        r_low, r_high, r_sum = find_max_subarray(A, m+1, r)
        c_low, c_high, c_sum = find_max_crossing_subarrary(A, l, m, r)

        if (l_sum >= r_sum) and (l_sum >= c_sum):
            return (l_low, l_high, l_sum)
        elif (r_sum >= l_sum) and (r_sum >= c_sum):
            return (r_low, r_high, r_sum)
        else:
            return (c_low, c_high, c_sum)


if __name__ == '__main__':
    main()
