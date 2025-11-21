import sys
import random

def generate_random_number(num):
    arr = []
    random.seed(3)
    while len(arr) < num:
        number = random.randint(1, 30)
        arr.append(number)
    arr.sort()
    return arr

def generate_output_file(num):
    try:
        filename = f"price{num}.txt"
        file_obj = open(filename, 'w')
        req_num_array = generate_random_number(num)
        file_obj.write(str(num) + "\n")
        file_obj.write(" ".join(map(str, req_num_array)) + "\n")
        file_obj.close()

    except Exception as e:
        print(f"Error writing file: {e}")
        sys.exit(1)

def main():
    rod_length = [5, 10, 20, 30]
    for n in rod_length:
        generate_output_file(n)

if __name__ == "__main__":
    main()