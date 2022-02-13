def create_cycle():
    x = []
    x.append(x)
    x.append(1)
    x.append(2)
    print(x)
    del x
create_cycle()    
