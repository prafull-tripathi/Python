'''

'''
file = open( 'mbox.txt' )
myList=[]

for line in file:
    print(line,end=" ")

    words=line.split(" ")
    for word in words:
        if word in myList:
            continue
        else:
            myList.append(word)

    print( myList )

print(sorted(myList))

