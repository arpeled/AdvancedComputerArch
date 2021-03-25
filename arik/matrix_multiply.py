import time
import multiprocessing
from random import random, randrange
import multiprocessing as mp
import numpy as np
from datetime import datetime

import numpy as np
def sequence_dot_func(mat_a,mat_b):
    result_mat = np.zeros((mat_a.shape[0],mat_b.shape[1]))
    print(result_mat.shape)
    for i in range(mat_a.shape[0]):
        for j in range(mat_a.shape[1]):
            calculate_multiply_rows(mat_a,mat_b,i,j,result_mat)
            # print('i,j',i,j)

            # print ('len(mat_a[i,:])=',len(mat_a[i,:]))

    return result_mat

def calculate_multiply_rows(mat_a,mat_b,i,j,result_mat):
    res = 0
    for x in range(len(mat_a[i, :])):
        res += mat_a[i, :][x] * mat_b[:, j][x]
    result_mat[i, j] = res
def par_calculate_multiply_rows(mat_a,mat_b,i,j,result_mat):
    print('i,j,mat_a',i,j,mat_a)
    res = 0
    for x in range(len(mat_a[i, :])):
        res += mat_a[i, :][x] * mat_b[:, j][x]
    print('res=', res)
    result_mat[i, j] = res

def parallel_proccessing(mat_a,mat_b):
    # pool = mp.Pool(8)

    result_mat = np.zeros((mat_a.shape[0], mat_b.shape[1]))
    print(result_mat.shape)
    jobs = []

    for i in range(mat_a.shape[0]):
        for j in range(mat_a.shape[1]):
            # calculate_multiply_rows(mat_a, mat_b, i, j, result_mat)
            p = multiprocessing.Process(target=par_calculate_multiply_rows,
                                        args=(mat_a, mat_b, i, j, result_mat,))
            jobs.append(p)
            p.start()
            # results = pool.starmap_async(calculate_multiply_rows(), [(number,) for number in data]).get()
    for j in jobs:
        j.join()
        print ('%s.exitcode = %s' % (j.name, j.exitcode))
    return result_mat


if __name__ == '__main__':
    rows = 2
    cols = 2
    matrix_a = np.ones((rows, cols))
    matrix_b = np.ones((cols,rows))
    for i in range(rows):
        for j in range(cols):
            matrix_a[i, j] = randrange(0, 10)
            matrix_b[i, j] = randrange(0, 10)
    print(matrix_a)
    print(matrix_b)

    start_time = time.time()
    m = np.dot(matrix_a, matrix_b)
    print('--------------------np.dot -------------------------------')
    print(m)
    print('builtin dot matrix  run took {} seconds'.format(time.time() - start_time))
    print(matrix_a.shape[1])
    start_time = time.time()
    print('----------------- sequence_dot_func ----------------------')
    print(sequence_dot_func(matrix_a,matrix_b))
    print('sequence_dot_func dot matrix  run took {} seconds'.format(time.time() - start_time))

    start_time = time.time()
    print('----------------- parallel_proccessing-----------------')
    print(parallel_proccessing(matrix_a,matrix_b))
    print('parallel_proccessing dot matrix  run took {} seconds'.format(time.time() - start_time))


