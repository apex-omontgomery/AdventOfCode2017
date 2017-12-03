import itertools

def max_min(input: list) -> int:
    return max(input) - min(input)

def even_divisor(input: list )-> int:
    for first, second in itertools.combinations(input, 2):
        if check_div(first, second):
            return max(first, second) // min(first, second)

def check_div(first, second):
    return first % second == 0 or second % first == 0

def single_row(input: str, callback) -> int:
    split_list = [int(item) for item in input.strip('\n').split()]
    return callback(split_list)

def main_solution(input: list , callback)-> int:
    return sum([single_row(value, callback) for value in input])

def main():
    with open('input.txt', 'r') as input_file:
        val = input_file.readlines()
        print(main_solution(val, max_min))
        print(main_solution(val, even_divisor))


if __name__ == '__main__':
    main()