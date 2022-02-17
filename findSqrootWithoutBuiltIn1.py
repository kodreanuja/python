def findSqroot(num):
    sq = num ** (1/(2))
    return int(sq)



if __name__ == "__main__":
    num = 9
    print(findSqroot(num))