def gcd_2(a,b):
    min_num = min(a,b)
    max_num = max(a,b)
    if max_num % min_num == 0:
        return min_num
    else:
        return  gcd_2(min_num,max_num % min_num)

def gcd_n(lst):
    if len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        return gcd_2(lst[0],lst[1])
    else:
        return gcd_2(lst[0],gcd_n(lst[1:]))



def test_gcd():
    assert(gcd_2(8,12)==4)
    assert(gcd_2(30,15)==15)
    assert(gcd_2(10,3)==1)
    assert(gcd_n([12,24,8,32])==4)
    assert(gcd_n([78,45,105,26])==1)
    assert(gcd_n([256,1024,64])==64)