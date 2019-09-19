def insertion_sort(A):
    x = 0
    j = 0

    for i in range(1,len(A)):
        x = A[i]
        j = i - 1

        while j >= 0 and x < A[j]:
            A[j + 1] = A[j]
            j -= 1

        A[j + 1] = x
