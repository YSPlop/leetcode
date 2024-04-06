def reverse(x:int) -> int:
    result = 0
    if x < 0:
        result =  -1 * int(str((-1 * x))[::-1])
    else:
        result = int(str(x)[::-1])

    if ((-2) ** 31)<= result <= (((2) ** 31) - 1):
        return result
    else:
        return 0