
import time

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
    stock_list = [1, 2, 3, 4, 5]
    print("=== Iterative Method ===")
    processed_items, exec_time = fifo_iterative(stock_list.copy())
    print(f"Processed Items: {processed_items}")
    print(f"Execution Time: {exec_time:.6f} seconds\n")
    
    stock_list = [1, 2, 3, 4, 5]
    print("=== Recursive Method ===")
    processed_items, exec_time = fifo_recursive_list(stock_list.copy())
    print(f"Processed Items: {processed_items}")
    print(f"Execution Time: {exec_time:.6f} seconds")
