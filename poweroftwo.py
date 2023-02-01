
def poweroftwo(base, exp):
    assert int(exp) == exp, 'The parameter must be Integer value'
    if exp == 0:
        return 1
    elif exp < 0:
        return 1/base * poweroftwo(base, exp+1)
    else:
        return base * poweroftwo(base, exp-1)

print(poweroftwo(2,-4))

# 2 * 2 * 2 * 2
#print(0.5 * 0.5 * 0.5 * 0.5)

