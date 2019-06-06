def bin(item, l, r, key):

    if r >= l:

        mid = int( l + (r - l)/2 )

        if item[mid] == key:
            return mid

        elif item[mid] > key:
            return bin(item, l, mid-1, key)

        else:
            return bin(item, mid + 1, r, key)

    else:
        return 1

item = []
n = int(input("Enter the no of elements : "))
for i in range(0,n) :
    ele = int(input())
    item.append(ele)
key = int(input("Enter the element to be found : "))

result = bin(item, 0, len(item), key)

if result != 1:
    print("Element is present at index ", result)
else:
    print("Element is not present in array")