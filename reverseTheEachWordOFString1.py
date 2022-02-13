def reverse(String):
    stack = []
    temp = ""
    for i in range(len(String)):
        if String[i] == " ":
            stack.append(temp)
            temp = ""

        else:
            temp = temp + String[i]  
    stack.append(temp)  

    while len(stack) != 0:
        temp = stack[len(stack) -1]
        print(temp, end = " ")
        stack.pop()   

    print()     



if __name__ == "__main__":
    String = "Anuja is a Clever girl"
    print(reverse(String))
