import time
import matplotlib.pyplot as plt

def recursive_top_down(n, p):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1, n+1):
        q = max(q, p[i-1] + recursive_top_down(n-i, p))
    return q

def bottom_up(n, p):
    r = [0] * (n+1)
    s = [0] * (n+1)
    for j in range(1, n+1):
        q = float('-inf')
        for i in range(1, j+1):
            if q < p[i-1] + r[j-i]:
                q = p[i-1] + r[j-i]
                s[j] = i
        r[j] = q
    cuts = []
    rem = n
    while rem > 0:
        cuts.append(s[rem])
        rem = rem - s[rem] 
    return r[n], cuts

def memoized_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n==0:
        q = 0
    else:
        q = float('-inf')
        for i in range(1, n+1):
            q = max(q, p[i-1] + memoized_aux(p, n-i, r))
    r[n] = q
    return q

def memoized(n, p):
    r = [float('-inf')] * (n+1)
    return memoized_aux(p, n, r)

def plot_line_graph(td, bu, ma):
    n = [5, 10, 20, 30]

    plt.figure(figsize=(12, 6))

    plt.semilogy(n, td, 'ro-', label="Recursive Top-Down", markersize=4)
    plt.semilogy(n, bu, 'go-', label="Bottom-up", markersize=4)
    plt.semilogy(n, ma, 'bo-', label="Memoized Approach", markersize=4)

    plt.xlabel('Rod Length', fontsize=8)
    plt.ylabel('Execution Time (seconds)', fontsize=8)
    plt.title('Rod Cutting Algorithm Performance Comparison', fontsize=12, fontweight='bold')
    plt.legend(fontsize=8)
    plt.grid(True, alpha=0.3)
    plt.xticks(n)

    plt.show()


def main():
    files = ["price5.txt", "price10.txt", "price20.txt", "price30.txt"]
    time_taken_td = []
    time_taken_bu = []
    time_taken_ma = []

    for i, f in enumerate(files):
        with open(f, 'r') as f:
            n = int(f.readline().strip())
            prices = list(map(int, f.readline().strip().split()))

        print('\n')
        print('*' * 80)
        print(f"Prices: {n} \n")
        
        start = time.perf_counter()
        max_profit = recursive_top_down(n, prices)
        end = time.perf_counter()
        time_taken = end - start
        print(f"Recursive Top-Down Algorithm: \nMax profit for {n} prices: {max_profit}")
        print(f"Time taken: {time_taken:.6f} seconds\n")
        time_taken_td.append(time_taken)
        # print(time_taken_td)

        op_cuts = []
        start = time.perf_counter()
        max_profit, op_cuts = bottom_up(n, prices)
        end = time.perf_counter()
        time_taken = end - start
        print(f"Extended-Bottom-Up approach: \nMax profit for {n} prices: {max_profit}")
        print(f"Optimal cuts: {op_cuts}")
        print(f"Time taken: {time_taken:.6f} seconds\n")
        time_taken_bu.append(time_taken)
        # print(time_taken_bu)

        start = time.perf_counter()
        max_profit = memoized(n, prices)
        end = time.perf_counter()
        time_taken = end - start
        print(f"Memoized Approach: \nMax profit for {n} prices: {max_profit}")
        print(f"Time taken: {time_taken:.6f} seconds\n")
        time_taken_ma.append(time_taken)
        # print(time_taken_ma)

    plot_line_graph(time_taken_td, time_taken_bu, time_taken_ma)

if __name__ == "__main__":
    main()