import time
import multiprocessing

def basic_func(x):
    if x == 0:
        return 'zero'
    elif x % 2 == 0:
        return 'even'
    else:
        return 'odd'

def multiprocessing_func(x):
    y = x * x
    time.sleep(2)
    print('{} squared results in a/an {} number'.format(x, basic_func(y)))


if __name__ == '__main__':

    start_time = time.time()
    for i in range(0, 10):
        y = i * i
        time.sleep(2)
        print('{} squared results in a/an {} number'.format(i, basic_func(y)))

    print('Non parallel run took {} seconds'.format(time.time() - start_time))

    start_time = time.time()
    processes = []
    for i in range(0, 10):
        p = multiprocessing.Process(target=multiprocessing_func, args=(i,))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

    print('Parallel run using Process took {} seconds'.format(time.time() - start_time))

    start_time = time.time()
    pool = multiprocessing.Pool()
    pool.map(multiprocessing_func, range(0,10))
    pool.close()
    print('Parallel run using pool.map took {} seconds'.format(time.time() - start_time))