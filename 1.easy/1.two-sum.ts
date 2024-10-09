/**
    Finds a pair in the list that sums to the target number and returns their indices.

    Args:
        nums: A list of numbers.
        target: The target number.

    Returns:
        A list of two indices whose elements sum to the target number, or None if no such pair exists.
 */

function twoSum(nums: number[], target: number) {

    if (!nums) {
        return null;
    }

    for (let i = 0; i < nums.length; i++) {

        const element = nums[i];

        const complement = target - element;
        
        if (element === complement) {
            const count = nums.filter(x => x===complement).length
            if (count < 2) {
                continue;
            }
        }

        if (nums.includes(complement)) {
            return [nums.indexOf(element), nums.indexOf(complement)];
        }

    }

     return null;   

}

console.log(twoSum([2, 7, 11, 15], 9)); // Expected output: [0, 1]
console.log(twoSum([3, 2, 4], 6));     // Expected output: [1, 2]
console.log(twoSum([1, 2, 3], 7));     // Expected output: null