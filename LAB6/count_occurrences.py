#### Signature
# count_occurrences :: (List, Integer) => Integer
#### Template
# def count_occurrences(given...):
#    return returns...
def count_occurrences(list,value):
    flag = 0
    i = 0
    for i in range(len(list)):
        if list[i] == value:
            flag += 1
            i += 1 
    return flag

def test_count_occurrences():
    assert(count_occurrences([3, 3, 4, 5, 1, 2], 2) == 1)
    assert(count_occurrences([3, 3, 4, 5, 1, 2], 3) == 2)
    assert(count_occurrences([5, 5, 5, 5, 1], 2) == 0)

