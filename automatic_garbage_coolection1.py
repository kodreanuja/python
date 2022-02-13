import gc
print("Garbage collection thresholds:",gc.get_threshold())
collected = gc.collect()
print("Garbage collector: collected","%d objects." % collected)

# manual garbage collection ...
i = 0
def create_cycle():
    x = {}
    x[i+1]=x
    print(x)
collected= gc.collect()
print("Garbage collector: collected %d objects." % (collected))
print ("Creating cycles...")
for i in range(10):
    create_cycle()
    collected = gc.collect()
print ("Garbage collector: collected %d objects." % (collected))