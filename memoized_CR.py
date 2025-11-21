from math import inf 
import sys

def memoized_cut_rod(p,n):
    r = []

    for i in range(0,n+1):
        r.append(-inf)

    return memoized_cut_rod_aux(p,n,r)

def memoized_cut_rod_aux(p,n,r):
    if r[n] >= 0:
        return r[n]
    
    if n == 0:
        q = 0
    else:
        q = -inf
        
        for i in range(1, n+1):
            q = max(q,p[i-1] + memoized_cut_rod_aux(p,n-i,r))

    r[n] = q

    return q

def main():
    
    if len(sys.argv) < 2:
        print("please provide a rod file after")
    
    rodsize = 0
    price_list = []
    data = []

    with open(sys.argv[1],'r') as file:
        for line in file:
            processed_line = line.strip().split()
            
            if processed_line:
               data.append(processed_line)

    rodsize = int(data[0][0])
    price_list = [int(x) for x in data[1]]

    print(rodsize)

    print(price_list)

    best_revenue = memoized_cut_rod(price_list, rodsize)

    print(best_revenue)


        





if __name__ == "__main__":
    main()
    



    
