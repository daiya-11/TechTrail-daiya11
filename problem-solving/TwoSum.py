# The Two Sum problem involves finding two numbers in a given array that add up to a specific target sum
# and returning their indices


def two_sum(nums, target):
    # Loop through each element in the list
    for i in range(len(nums) - 1):
        # Loop through the elements following the current element
        for j in range(i + 1, len(nums)):
            # Check if the current pair of elements sum up to the target
            if nums[i] + nums[j] == target:
                # If they do, return their indices as a list
                return [i, j]
    # Return an empty list if no pair sums up to the target
    return []


# Example usage of the function
nums = [2, 5, 5, 11]
target = 10
print(two_sum(nums, target))
