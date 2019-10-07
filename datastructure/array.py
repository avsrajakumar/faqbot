arrayVar = [1, 2, 3, 4, 5]

def printarrvals(e):
    print("print Array values")
    for entry in e:
        print(entry)


def isempty(e):
    if not e:
        print("print Array is empty")
    else:
        print("print Array is not empty")


def replace(arr, index, value):
    arrtemp = []
    print("Array before replace", arr)
    i = 0
    while i < arr.__len__():
        if (i is index):
            arrtemp.append(value)
        else:
            arrtemp.append(arr[i])
        i += 1
    print("Array before replace", arrtemp)
    return arrtemp


def insert(arr, value):
    print("Array before adding value", arr)
    arr.append(value)
    print("Array after adding value", arr)
    return arr

def delete(arr, value):
    arrtemp = []
    print("Array before delete", arr)
    for i in range(arr.__len__()):
        if (arr[i] is not value):
            arrtemp.append(arr[i])
    print("Array after delete", arrtemp)
    return arrtemp


printarrvals(arrayVar)
isempty(arrayVar)
insert(arrayVar, 7)
replace(arrayVar, 1, 8)
delete(arrayVar,3)