
def solution_helper (input:str, interval)-> int:
    captcha_sum = 0
    modulo_amount = len(input)
    for i in range(-1, len(input)-1):
        if input[i] == input[(i + interval)%modulo_amount]:
            captcha_sum += int(input[i])
    return captcha_sum

def solution_mid(input:str):
    return solution_helper(input, len(input)//2)

def solution(input:str):
    return solution_helper(input, 1)

def main():
    with open('input.txt', 'r') as input_file:
        val = input_file.readline()
    print(solution(val))
    print(solution_mid(val))


if __name__ == '__main__':
    main()
    print('first')
    first = [
        '1122',
        '1111',
        '1234',
        '9121212']
    for item in first:
        print(solution_mid(item))
    print('second')
    second = [
             '1212',
             '1221',
             '123425',
             '123123',
             '12131415'
            ]
    for item in second:
        print(solution(item))