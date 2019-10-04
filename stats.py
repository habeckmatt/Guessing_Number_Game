from math import sqrt

DATA = 'sample_dataset'


def total():
    """
    represents the total number n
    of observations in the sample.
    """
    i = 0
    with open(DATA) as file:
        for line in file:
            i += 1
        return i



def summation():
    i = 0
    with open(DATA) as file:
        for num in file:
            i += int(num)
        return i

def mean():
    sum = 0
    n = total()
    with open(DATA) as file:
        for x in file:
            sum += int(x)
        return sum / n

def variance():
    n = total()

    with open(DATA) as file:
        for x in file:
            sum = (int(x) - n)**2
        return sum / (n - 1)

def standard_dev():
    v = variance()

    return sqrt(v)

def median():
    """
    calculates the median for a dataset.
    """
    items = []
    with open(DATA) as file:
        for x in file:
            items.append(int(x))
        ordered = sorted(items)
        size = total()
        if size % 2 == 0:
            middle = int(size / 2)
            return ordered[middle]
        else:
            middle = size // 2
            return ordered[middle]
def min():
    """
    one way to compute the minimum
    number in the dataset.
    """
    items = []
    with open(DATA) as file:
        for x in file:
            items.append(int(x))
    i = 0
    min = items[0]
    while i < len(items):
        if items[i] < min:
            min = items[i]
        i += 1
    return min


def max():
    """
    one way to compute the max
    number in the dataset.
    """
    items = []
    with open(DATA) as file:
        for x in file:
            items.append(int(x))
    max = items[0]
    i = 0
    while i < len(items):
        if items[i] > max:
            max = items[i]
        i += 1
    return max



            


print(total())
print(summation())
print(mean())
print(variance())
print(standard_dev())
print(median())
print(min())
print(max())



