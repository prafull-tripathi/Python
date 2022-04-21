# Python3 Program for recursive binary search.

def binarySearch(arr, left, right, target):
    # Check base case
    if right >= left:

        mid = left + (right - left) // 2

        # If element is present at the middle itself
        if arr[mid] == target:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left sub-array
        elif arr[mid] > target:
            return binarySearch( arr, left, mid - 1, target )

        # Else the element can only be present
        # in right sub-array
        else:
            return binarySearch( arr, mid + 1, right, target )

    else:
        # Element is not present in the array
        return -1


if __name__ == '__main__':

    arr = [2, 3, 4, 10, 40]
    target = 10

    # Function call
    result = binarySearch( arr, 0, len( arr ) - 1, target )

    if result != -1:
        print( f'Element is present at position:  {result+1}' )
    else:
        print( "Element is not present in array" )
