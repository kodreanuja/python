def plusOne(arr):
    result = int("".join([str(each) for each in arr])) + 1
    result = str(result)
    return list(result)
     
# if want = result[-1]  = digits[-1] + 1:
#     l = digits[-1]
#     digits.pop()
#     l = l +  1
#     digits.append(l)
# return digits     




if __name__ == "__main__":
    arr = [1, 2, 4, 5, 6]
    print(plusOne(arr))