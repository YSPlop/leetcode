def convert(s: str, numRows: int) -> str:

    gap = 2 * (numRows - 1)
    result = ""
    max_shift = False # max_shift is true when we are reading from almost full columns and false otherwise

    if numRows == 1:
        return s

    while (len(result) < len(s)):
        for i in range(numRows):
            max_shift = False
            current_counter = i
            if (i == 0 or i == (numRows - 1)):
                while (current_counter < len(s)):
                    result += s[current_counter]
                    current_counter += gap
            else:
                while (current_counter < len(s)):
                    if (max_shift == False):
                        result += s[current_counter]
                        current_counter += gap - (2 * i)
                        max_shift = True
                    else:
                        result += s[current_counter]
                        current_counter += (2 * i)
                        max_shift = False
    print(result)
    return result
        
print("PINALSIGYAHRPI" == convert("PAYPALISHIRING", 4))