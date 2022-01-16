def next_smaller(number):
    new_number = number
    number = list(str(number))
    num_len = len(number)-1

    if len(number) == 1 or sorted(number) == number:
        return -1

    for i in range(num_len-1, -1, -1):
        for j in range(num_len, i-1, -1):
            if number[j] < number[i]:
                number[j], number[i] = number[i], number[j]
                first = number[0:i+1]
                second = number[-1:i:-1]
                number = first + second
                new_number = int(''.join(number))
                if number[0] == '0':
                    return -1
                else:
                    return new_number
    return new_number
