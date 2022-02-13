def dulplicates(arr):
    s = set()
    for i in arr:
        if i not in s:
            s.add(i)
        else:
            return i    


if __name__ == "__main__":
    arr = [3, 2, 1, 3, 4]
    print(dulplicates(arr))