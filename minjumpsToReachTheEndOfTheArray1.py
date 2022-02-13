def minJumps(arr, n):
    jumps = [0 for i in range(n)]

    if (n == 0) or (arr[0] == 0):
        return float('inf')

    jumps[0] = 0

    for i in range(1, n):

        jumps[i] = float('inf')

        for j in range(i):

            if (i <= j + arr[j]) and (jumps[j] != float('inf')):

                jumps[i] = min(jumps[i], jumps[j] + 1)

                break
    print("Minimum jumps to reach the end of the array : ", end = " ")
    return  jumps[n-1]

if __name__ == "__main__":
    arr = [1, 3, 6, 1, 0, 9]
    n = len(arr)
    print(minJumps(arr, n))