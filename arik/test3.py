import multiprocessing as mp
import numpy as np
from datetime import datetime
num_of_processes = mp.cpu_count();
# print("Number of processors: ", num_of_processes)
a=[]
for i in range(10000):
    a.append(i+1)
par=a
seq=a
def parrllel_sequre(array,index,number):
    array[index] =1/( number**11)

if __name__ == '__main__':
    start_time = datetime.now()
    pool = mp.Pool(num_of_processes)
    print(start_time)
    for i in range(len(a)):
        seq[i] =1/( a[i]**11)

    # print(seq)
    processing_time = datetime.now() - start_time
    print('sequence ' ,processing_time)

    start_time = datetime.now()
    for i in range(len(a)):
        pool.apply_async( parrllel_sequre(par,i,a[i]))
    processing_time = datetime.now() - start_time
    print(par[:10])
    print('parallel ' ,processing_time)


