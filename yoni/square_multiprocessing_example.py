import multiprocessing as mp
import numpy as np
from datetime import datetime

print("Number of processors: ", mp.cpu_count())

# Prepare data
data = [0,1,2,3,4,5,6,7,8,9,10]

def square(number):
    return number * number

def square_async(i, number):
    return (i, number * number)

def non_parallel_processing():
    results = []
    start_time = datetime.now()
    for number in data:
        results.append(square(number))
    processing_time = datetime.now() - start_time
    print(results)
    print(f"Non parallel processing took {processing_time.total_seconds()}")


def parallel_processing_pool_apply(num_of_processes=mp.cpu_count()):
    pool = mp.Pool(num_of_processes)
    start_time = datetime.now()
    results = [pool.apply(square, args=(number, )) for number in data]
    processing_time = datetime.now() - start_time
    pool.close()
    print(results)
    print(f"Synchronize parallel using pool.apply processing took {processing_time.total_seconds()} with {num_of_processes} number of processes")


def parallel_processing_pool_map(num_of_processes=mp.cpu_count()):
    pool = mp.Pool(num_of_processes)
    start_time = datetime.now()
    results = pool.map(square, data)
    processing_time = datetime.now() - start_time
    pool.close()
    print(results)
    print(f"Synchronize parallel using pool.map processing took {processing_time.total_seconds()} with {num_of_processes} number of processes")


def parallel_processing_pool_starmap(num_of_processes=mp.cpu_count()):
    pool = mp.Pool(num_of_processes)
    start_time = datetime.now()
    results = pool.starmap(square, [(number, ) for number in data])
    processing_time = datetime.now() - start_time
    pool.close()
    print(results[:10])
    print(f"Synchronize parallel using pool.starmap processing took {processing_time.total_seconds()} with {num_of_processes} number of processes")

def parallel_processing_pool_apply_async_no_callback(num_of_processes=mp.cpu_count()):
    pool = mp.Pool(num_of_processes)
    start_time = datetime.now()
    result_objects = [pool.apply_async(square, args=(number, )) for number in data]
    results = [r.get() for r in result_objects]

    processing_time = datetime.now() - start_time
    pool.close()
    pool.join()
    print(results[:10])
    print(f"Asynchronous parallel using pool.apply_async without callback processing took {processing_time.total_seconds()} with {num_of_processes} number of processes")


def parallel_processing_pool_map_async(num_of_processes=mp.cpu_count()):
    pool = mp.Pool(num_of_processes)
    start_time = datetime.now()
    results = pool.map_async(square, data).get()
    processing_time = datetime.now() - start_time
    pool.close()
    pool.join()

    print(results[:10])
    print(f"Asynchronous parallel using pool.map_async without callback processing took {processing_time.total_seconds()} with {num_of_processes} number of processes")


def parallel_processing_pool_starmap_async(num_of_processes=mp.cpu_count()):
    pool = mp.Pool(num_of_processes)
    start_time = datetime.now()
    results = pool.starmap_async(square, [(number, ) for number in data]).get()
    processing_time = datetime.now() - start_time
    pool.close()
    pool.join()
    print(results[:10])
    print(f"Asynchronous parallel using pool.starmap_async without callback without sorting processing took {processing_time.total_seconds()} with {num_of_processes} number of processes")

#running different methods
non_parallel_processing()
parallel_processing_pool_apply()
parallel_processing_pool_apply(2)
parallel_processing_pool_apply(1)
parallel_processing_pool_map()
parallel_processing_pool_map(2)
parallel_processing_pool_map(1)
parallel_processing_pool_starmap()
parallel_processing_pool_starmap(2)
parallel_processing_pool_starmap(1)
parallel_processing_pool_apply_async_no_callback()
parallel_processing_pool_apply_async_no_callback(2)
parallel_processing_pool_apply_async_no_callback(1)
parallel_processing_pool_map_async()
parallel_processing_pool_map_async(2)
parallel_processing_pool_map_async(1)
parallel_processing_pool_starmap_async()
parallel_processing_pool_starmap_async(2)
parallel_processing_pool_starmap_async(1)