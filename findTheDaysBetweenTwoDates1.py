from datetime import date 
def days():

    d1 = date(2019, 6, 6)
    d2 = date(2019, 4, 4)
    delta = d1 - d2 
    print(delta.days)

if __name__ == "__main__":
    print(days())