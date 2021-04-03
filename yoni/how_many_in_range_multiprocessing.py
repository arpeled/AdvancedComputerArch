import multiprocessing as mp
import numpy as np
from datetime import datetime

print("Number of processors: ", mp.cpu_count())

# Prepare data
np.random.RandomState(100)
arr = np.random.randint(0, 10, size=[200000, 5])
data = arr.tolist()
data[:5]

results = []

def howmany_within_range(row, minimum=4, maximum=8):
    """Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count

def howmany_within_range_async(i, row, minimum, maximum):
    """Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return (i, count)

# collect result as a callback function for async processing
def collect_result(result):
    global results
    results.append(result)


def non_parallel_processing():
    # Non parallel processing
    results = []
    start_time = datetime.now()
    for row in data:
        results.append(howmany_within_range(row, minimum=4, maximum=8))
    processing_time = datetime.now() - start_time
    print(results[:10])
    print(f"Non parallel processing took {processing_time.total_seconds()}")

def parallel_processing_pool_apply(num_of_processes=mp.cpu_count()):
    # Synchronize parallel processing - using pool.apply
    # Step 1: Init multiprocessing.Pool()
    pool = mp.Pool(num_of_processes)
    results = []
    start_time = datetime.now()
    # Step 2: `pool.apply` the `howmany_within_range()`
    results = [pool.apply(howmany_within_range, args=(row, 4, 8)) for row in data]
    processing_time = datetime.now() - start_time
    # Step 3: Don't forget to close
    pool.close()
    print(results[:10])
    print(f"Synchronize parallel using pool.apply processing took {processing_time.total_seconds()} with {num_of_processes} number of processes")


def parallel_processing_pool_map(num_of_processes=mp.cpu_count()):
    # Synchronize parallel processing - using pool.map
    # Step 1: Init multiprocessing.Pool()
    pool = mp.Pool(num_of_processes)
    results = []
    start_time = datetime.now()
    # Step 2: `pool.map` the `howmany_within_range()`
    results = pool.map(howmany_within_range, [row for row in data])
    processing_time = datetime.now() - start_time
    # Step 3: Don't forget to close
    pool.close()
    print(results[:10])
    print(f"Synchronize parallel using pool.map processing took {processing_time.total_seconds()} with {num_of_processes} number of processes")


def parallel_processing_pool_starmap(num_of_processes=mp.cpu_count()):
    # Synchronize parallel processing - using pool.starmap
    # Step 1: Init multiprocessing.Pool()
    pool = mp.Pool(num_of_processes)
    results = []
    start_time = datetime.now()
    # Step 2: `pool.starmap` the `howmany_within_range()`
    results = pool.starmap(howmany_within_range, [(row, 4, 8) for row in data])
    processing_time = datetime.now() - start_time
    # Step 3: Don't forget to close
    pool.close()
    print(results[:10])
    print(f"Synchronize parallel using pool.starmap processing took {processing_time.total_seconds()} with {num_of_processes} number of processes")


def parallel_processing_pool_apply_async_callback(num_of_processes=mp.cpu_count()):
    # Asynchronized parallel processing - using pool.apply_async with callback
    # Step 1: Init multiprocessing.Pool()
    pool = mp.Pool(num_of_processes)
    results = []
    start_time = datetime.now()
    # Step 2: `pool.apply_async` use loop to parallelize`
    for i, row in enumerate(data):
        pool.apply_async(howmany_within_range_async, args=(i, row, 4, 8), callback=collect_result)

    processing_time = datetime.now() - start_time
    # Step 4: Close Pool and let all the processes complete
    pool.close()
    pool.join()  # postpones the execution of next line of code until all processes in the queue are done.

    print(results[:10])
    print(f"Asynchronous parallel using pool.apply_async with callback processing took {processing_time.total_seconds()} with {num_of_processes} number of processes")


def parallel_processing_pool_apply_async_callback_sorting(num_of_processes=mp.cpu_count()):
    # Asynchronized parallel processing - using pool.apply_async with callback and soritng
    # Step 1: Init multiprocessing.Pool()
    pool = mp.Pool(num_of_processes)
    results = []
    start_time = datetime.now()
    # Step 2: `pool.apply_async` use loop to parallelize`
    for i, row in enumerate(data):
        pool.apply_async(howmany_within_range_async, args=(i, row, 4, 8), callback=collect_result)

    # Step 3: Close Pool and let all the processes complete
    pool.close()
    pool.join()  # postpones the execution of next line of code until all processes in the queue are done.

    # Step 4: Sort results [OPTIONAL]
    results.sort(key=lambda x: x[0])
    results_final = [r for i, r in results]
    processing_time = datetime.now() - start_time

    print(results_final[:10])
    print(f"Asynchronous parallel using pool.apply_async with callback and sorting processing took {processing_time.total_seconds()} with {num_of_processes} number of processes")


def parallel_processing_pool_apply_async_no_callback(num_of_processes=mp.cpu_count()):
    # Asynchronized parallel processing - using pool.apply_async without callback
    # Step 1: Init multiprocessing.Pool()
    pool = mp.Pool(num_of_processes)
    results = []
    start_time = datetime.now()
    # Step 2: `pool.apply_async` without callback`
    result_objects = [pool.apply_async(howmany_within_range_async, args=(i, row, 4, 8)) for i, row in enumerate(data)]
    # Step 3: result_objects is a list of pool.ApplyResult objects
    results = [r.get()[1] for r in result_objects]

    processing_time = datetime.now() - start_time
    # Step 4: Close Pool and let all the processes complete
    pool.close()
    pool.join()  # postpones the execution of next line of code until all processes in the queue are done.

    print(results[:10])
    print(f"Asynchronous parallel using pool.apply_async without callback processing took {processing_time.total_seconds()} with {num_of_processes} number of processes")


def parallel_processing_pool_map_async(num_of_processes=mp.cpu_count()):
    # Asynchronized parallel processing - using pool.map_async
    # Step 1: Init multiprocessing.Pool()
    pool = mp.Pool(num_of_processes)
    results = []
    start_time = datetime.now()
    # Step 2: `pool.map_async`
    results = pool.map_async(howmany_within_range, [row for row in data]).get()
    processing_time = datetime.now() - start_time
    # Step 3: Close Pool and let all the processes complete
    pool.close()
    pool.join()  # postpones the execution of next line of code until all processes in the queue are done.

    print(results[:10])
    print(f"Asynchronous parallel using pool.map_async without callback processing took {processing_time.total_seconds()} with {num_of_processes} number of processes")


def parallel_processing_pool_starmap_async(num_of_processes=mp.cpu_count()):
    # Asynchronized parallel processing - using pool.starmap_async
    # Step 1: Init multiprocessing.Pool()
    pool = mp.Pool(num_of_processes)
    results = []
    start_time = datetime.now()
    # Step 2: `pool.starmap_async`
    results = pool.starmap_async(howmany_within_range_async, [(i, row, 4, 8) for i, row in enumerate(data)]).get()
    processing_time = datetime.now() - start_time
    # Step 3: Close Pool and let all the processes complete
    pool.close()
    pool.join()  # postpones the execution of next line of code until all processes in the queue are done.
    results.sort(key=lambda x: x[0])
    results_final = [r for i, r in results]
    print(results[:10])
    print(results_final[:10])
    print(f"Asynchronous parallel using pool.starmap_async without callback without sorting processing took {processing_time.total_seconds()} with {num_of_processes} number of processes")


def parallel_processing_pool_starmap_async_sorting(num_of_processes=mp.cpu_count()):
    # Asynchronized parallel processing - using pool.starmap_async
    # Step 1: Init multiprocessing.Pool()
    pool = mp.Pool(num_of_processes)
    results = []
    start_time = datetime.now()
    # Step 2: `pool.starmap_async`
    results = pool.starmap_async(howmany_within_range_async, [(i, row, 4, 8) for i, row in enumerate(data)]).get()
    results.sort(key=lambda x: x[0])
    results_final = [r for i, r in results]
    processing_time = datetime.now() - start_time
    # Step 3: Close Pool and let all the processes complete
    pool.close()
    pool.join()  # postpones the execution of next line of code until all processes in the queue are done.
    print(results[:10])
    print(results_final[:10])
    print(f"Asynchronous parallel using pool.starmap_async without callback with sorting processing took {processing_time.total_seconds()} with {num_of_processes} number of processes")

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
parallel_processing_pool_starmap_async_sorting()
parallel_processing_pool_starmap_async_sorting(2)
parallel_processing_pool_starmap_async_sorting(1)