def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    
    total_length = len(nums1) + len(nums2)

    # this means you need to add and take the average of the middle value
    if total_length % 2 == 0:

        middle_index = total_length / 2

        # These will be the indexes of the two arrays 
        current_index_1 = 0
        current_index_2 = 0

        while (current_index_1 + current_index_2) < middle_index:

            if nums1[current_index_1] < nums2[current_index_2]:
                current_index_1 += 1
            else:
                current_index_2 += 1
        

        
        median = num1[current_index_1] + nums2[current_index_2]


        

    # if not there is a middle value answer
    else: 
        