import random


def binary_search(data, target, lowindex, highindex):
    if lowindex > highindex:
        return False

    mid = (lowindex + highindex) // 2

    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data, target, lowindex, mid - 1)
    else:
        return binary_search(data, target, mid + 1, highindex)

if __name__ == '__main__':
    data = [random.randint(0, 100) for i in range(10)]

    data.sort()

    print(data)

    target = int(input('What number would you like to find?'))
    found = binary_search(data, target, 0, len(data) - 1)

    print(found)
