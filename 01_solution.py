from collections import Counter

def calculate_statistics(lst):
    if not lst:
        return None, None, None, None, None
    
    min_val = min(lst)
    max_val = max(lst)
    sum_val = sum(lst)
    avg_val = sum_val / len(lst)
    mode_val = Counter(lst).most_common(1)[0][0]
    
    return min_val, max_val, sum_val, avg_val, mode_val

def print_statistics(min_val, max_val, sum_val, avg_val, mode_val):
    print(f"min, max, sum, average and mode after addition of {mode_val} is {min_val}, {max_val}, {sum_val}, {avg_val}, {mode_val}.")

def process_stream(N, stream):
    lst = []
    for num in stream:
        lst.append(num)
        min_val, max_val, sum_val, avg_val, mode_val = calculate_statistics(lst)
        print_statistics(min_val, max_val, sum_val, avg_val, mode_val)

N = int(input())
stream = list(map(int, input().split()))

process_stream(N, stream)
