# by: jakepys
import time

def diamod(n):
    if n % 2 == 0 or n <= 0:
        return None

    d = ""
    
    # 1..n
    list_order_n = [i for i in range(1, n + 1, 2)]
    
    # n-2..1
    list_reverse_n = [i for i in range(n-2, 0, -2)]
    
    #parte superior del diamante
    for _, num in enumerate(list_order_n):
        d += (" " * ((n - num) // 2)) + ("*" * num) + "\n"

    #parte inferior del diamante
    for _, num in enumerate(list_reverse_n):
        d += (" " * ((n - num) // 2)) + ("*" * num) + "\n"

    if d.endswith("\n"):
        d = d[:-1]
    
    return f"{d}\n"

if __name__ == "__main__":
    for i in range(1, 100, 2):
        print(diamod(i))
        time.sleep(1)
        
    
    
    
