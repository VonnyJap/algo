def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == "__main__":
    # get the gcd of two values
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    d = 3
    n = len(arr)
    c = gcd(d,n)
    for i in range (c):
        temp = arr[i]
        print("temp: "+str(temp))
        k = i
        while (True):
            k = k + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[k-d] = arr[k]
        arr[k-d] = temp
    print(arr)