def myAtoi(s: str) -> int:
    
    UPPER_BOUND = (2 ** 31) - 1
    LOWER_BOUND = -(2 ** 31)

    current_index = 0
    number_encountered = False
    number_is_positive = True

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    result_number = ""

    while (current_index < len(s)):

        if (s[current_index] == '-') and (number_encountered == False):
            number_is_positive = False
        elif (s[current_index] in numbers):
            result_number += s[current_index]
            number_encountered = True
        elif (number_encountered == True) and (s[current_index] not in numbers):
            break
        elif (number_encountered == False) and not ( (s[current_index] == " ") or (s[current_index] == "+") ):
            return 0
        
        current_index += 1
        

    result_number = int(result_number)
    if (number_is_positive == True):
        
        if result_number <= UPPER_BOUND:
            return result_number
        else:
            return UPPER_BOUND
    else:

        result_number = -1 * result_number
        if result_number >= LOWER_BOUND:
            return result_number
        else:
            return LOWER_BOUND

print ("42", myAtoi("words with 4193 with words"))