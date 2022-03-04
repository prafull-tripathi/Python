'''
Write a program which repeatedly reads numbers until the user enters “done”.
Once “done” is entered, print out the total, count, and average of the numbers.
If the user enters anything other than a number, detect their mistake using try and except and print an error
message and skip to the next number.

'''

lt = []
cnt = 0
total = 0

while True:
    try:
        line = input( "" )
        if line == 'done':
            break
        else:
            x = int( line )
            cnt += 1
            total += x
            lt.append( x )
    except:
        print( "Enter number" )

print( f'Total is: {total}' )
print( f'Count is {cnt}' )
print( f'Average is {total // cnt}' )
print(f'Minimum number from list is: {min(lt)}')
print(f'Maximum number from list is: {max(lt)}')
