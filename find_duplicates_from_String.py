from collections import Counter
  
def find_dup_char(input):
    WC = Counter(input)
    j = -1

    for i in WC.values():
        j = j + 1
        if( i > 1 ):
            print Wc.keys()[j],
if __name__ == "__main__":
    input = 'geeksforgeeks'
    find_dup_char(input)


