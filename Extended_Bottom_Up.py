from math import inf
import sys

def Extended_bottup_up(p,n):
    p = [0] + p
    r = [0] * (n + 1)
    s = [0] * (n + 1)

    for j in range(1, n+1):
        q = -inf
        for i in range(1,j+1):
            # print(p[i])
            if q < p[i] + r[j-i]:
                q = p[i] + r[j-i]
                s[j] = i
        
        r[j] = q
    
    return r,s 

def main():

    if len(sys.argv) < 2:
        print("please provide a price.txt ")
        return
    rod_size = 0
    price_list = []
    data = []
    with open(sys.argv[1],'r') as file:
        for line in file:
            proccesed_line = line.strip().split()
            if proccesed_line:
                data.append(proccesed_line)

    rod_size = int(data[0][0])

    price_list = [int(i) for i in data[1]]

    print(rod_size)
    print(price_list)
    print('\n')

    revenue, cuts = Extended_bottup_up(price_list,rod_size)

    print(revenue)
    print(cuts)

if __name__ == "__main__":
    main()
        
