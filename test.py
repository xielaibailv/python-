def sumnew(x):
    r = 0
    for each in x:
        if (type(each) == int) or (type(each) == float):
            r = r + each
        else:
            continue

    return r



def minn(x):
    least = x[0]

    for each in x:
        if each < least:
            least = each
    return least


def sum(x):
    result = 0

    for each in x:
        if (type(each) == int) or (type(each) == float):
            result += each
        else:
            continue

    return result
