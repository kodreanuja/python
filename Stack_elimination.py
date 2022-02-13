# using elimination .
def isbancedString(expression):
    brackets = ["()", "{}", "[]"]
    while any (x in expression for x in brackets):
        for i in brackets:
            expression = expression.replace(i, "")

    return not expression    


if __name__=="__main__":
    expression = input()   
    print(expression, "-", "Balanced" if isbancedString(expression) else "Unbalanced")



