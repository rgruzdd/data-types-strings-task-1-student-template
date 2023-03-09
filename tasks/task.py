def get_fractions(a_b: str, c_b: str) -> str:
    """
    Add your code here
    """
    a = a_b.split('/')[0]
    c = c_b.split('/')[0]
    sum = int(a) + int(c)
    result = a_b + ' + ' + c_b + ' = ' + str(sum) + '/' + a_b.split('/')[1]
    return result

a_b = '1/3'
c_b = '5/3'

print(get_fractions(a_b, c_b))


