#fizzbuzz
for number in range(1,101):
# if number is a multiple of 3, print 'fizz'
# if number is a multiple of 5, print 'buzz'
# if number is a multiple of 3 and 5, print 'fizzbuzz'
    if number % 3 == 0 or number % 5 == 0:
        if number % 3 == 0:
            print ('Fizz', end='')
        if number % 5 == 0:
            print ('Buzz', end='')
        print()
    else:
        print (number)
