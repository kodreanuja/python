def pythoagorialTripletSum(sum1):
    if sum == 0:
        return 0

    for i in range(1, int(sum1/3)+1):
        for j in range(i +1, int(sum1/2) + 1):
            k = sum1 - i - j
            if (i * i + j *j == k * k):
                print(i, j, k, end = " ")
                return 
    print("No Triplets")         

    return 0




if __name__ == "__main__":
    sum1 = int(input())
    print(pythoagorialTripletSum(sum1))