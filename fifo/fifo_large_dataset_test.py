
import time
import sys

# Untuk menghindari error pada rekursi, set batas rekursi lebih tinggi
sys.setrecursionlimit(5000)  # Anda bisa menyesuaikan jika dataset lebih besar

def fifo_iterative(stock):
    start_time = time.time()
    processed_items = []
    
    while stock:
        item = stock.pop(0)
        processed_items.append(item)
    
    end_time = time.time()
    execution_time = end_time - start_time
    return processed_items, execution_time

def fifo_recursive_list(stock, processed_items=None, start_time=None):
    if processed_items is None:
        processed_items = []
        start_time = time.time()

    if not stock:
        end_time = time.time()
        execution_time = end_time - start_time
        return processed_items, execution_time

    item = stock.pop(0)
    processed_items.append(item)
    return fifo_recursive_list(stock, processed_items, start_time)

if __name__ == "__main__":
    # Dataset besar untuk pengujian
    large_stock = list(range(1, 10001))  # 10,000 elemen

    print("=== Large Dataset Test (10,000 elements) ===")

    print("--- Iterative Method ---")
    processed_items, exec_time = fifo_iterative(large_stock.copy())
    print(f"Execution Time: {exec_time:.6f} seconds\n")

    print("--- Recursive Method ---")
    try:
        processed_items, exec_time = fifo_recursive_list(large_stock.copy())
        print(f"Execution Time: {exec_time:.6f} seconds")
    except RecursionError:
        print("Error: Maximum recursion depth exceeded in recursive method.")
