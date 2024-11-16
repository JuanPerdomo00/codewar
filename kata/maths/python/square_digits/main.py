def square_digits(num):
    # Your code here
    return int(''.join([str(int(i)**2) for i in str(num)]))


print(square_digits(9119))