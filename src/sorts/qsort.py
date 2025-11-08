def qsort(arr):
    if len(arr) <= 1:
        return arr

    prev = arr[0]
    right = [x for x in arr[1:] if x > prev]
    left = [x for x in arr[1:] if x <= prev]

    return qsort(left) + [prev] + qsort(right)
