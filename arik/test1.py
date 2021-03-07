from multiprocessing import Process
import time
import howmanyinrange_multiprocessing_example

start = time.perf_counter()


def do_something(time_for_sleep):
    print(f'Sleeping {time_for_sleep} second...')
    time.sleep(time_for_sleep)
    print('Done Sleeping...')


p1 = Process(target=do_something, args=[1])
p2 = Process(target=do_something, args=[2])


if __name__ == '__main__':
    # howmanyinrange_multiprocessing_example.parallel_processing_pool_apply()
    # howmanyinrange_multiprocessing_example.parallel_processing_pool_apply(2)
    # howmanyinrange_multiprocessing_example.parallel_processing_pool_apply(8)
    howmanyinrange_multiprocessing_example.parallel_processing_pool_map()
    howmanyinrange_multiprocessing_example.parallel_processing_pool_map(2)
    howmanyinrange_multiprocessing_example.parallel_processing_pool_map(4)
    howmanyinrange_multiprocessing_example.parallel_processing_pool_starmap()
    howmanyinrange_multiprocessing_example.parallel_processing_pool_starmap(2)
    howmanyinrange_multiprocessing_example.parallel_processing_pool_starmap(4)
    # parallel_processing_pool_apply_async_callback()
    # parallel_processing_pool_apply_async_callback_sorting()
    howmanyinrange_multiprocessing_example.parallel_processing_pool_apply_async_no_callback()
    howmanyinrange_multiprocessing_example.parallel_processing_pool_apply_async_no_callback(2)
    howmanyinrange_multiprocessing_example.parallel_processing_pool_apply_async_no_callback(4)
    howmanyinrange_multiprocessing_example.parallel_processing_pool_map_async()
    howmanyinrange_multiprocessing_example.parallel_processing_pool_map_async(2)
    howmanyinrange_multiprocessing_example.parallel_processing_pool_map_async(4)
    howmanyinrange_multiprocessing_example.parallel_processing_pool_starmap_async()
    howmanyinrange_multiprocessing_example.parallel_processing_pool_starmap_async(2)
    howmanyinrange_multiprocessing_example.parallel_processing_pool_starmap_async(4)
    howmanyinrange_multiprocessing_example.parallel_processing_pool_starmap_async_sorting()
    howmanyinrange_multiprocessing_example.parallel_processing_pool_starmap_async_sorting(2)
    howmanyinrange_multiprocessing_example.parallel_processing_pool_starmap_async_sorting(4)
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start,2 )} second(s)')