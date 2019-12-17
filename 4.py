# 382345 => 388888 smallest possible number after lower bound with increasing digits
# 843167 => 799999 biggest possible number before upper bound with increasing digits

from itertools import groupby

def gen_candidates(low, up):
    for candidate in range(low, up+1):
        string_repr = str(candidate)
        if increasing_digits(candidate):
            groups_of_digits = [len(list(g)) for l, g in groupby(string_repr)]
            count_groups_of_digits = {n:len(list(g)) for n, g in groupby(groups_of_digits)}
            # if count_groups_of_digits.get(1, 0) < 6:  # part 1 
            if count_groups_of_digits.get(2, 0) > 0:  # part 2
                yield candidate

def increasing_digits(number):
    string_repr = str(number)
    for i in range(len(string_repr) - 1):
        if int(string_repr[i]) > int(string_repr[i+1]):
            return False
    return True

assert(increasing_digits(123456) == True)
assert(increasing_digits(111111) == True)
assert(increasing_digits(111011) == False)         

candidates = gen_candidates(388888, 799999)
print(len(list(candidates)))

