# def binary_search(n, arr, target):
#     flag = False
#     low = 0
#     high = n - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if target == arr[mid]:
#             flag = True
#             loc = mid
#             break
#         elif target < arr[mid]:
#             high = mid - 1
#         else:
#             low = mid + 1
#     if flag:
#         print("Search is successful and present at index:", loc)
#     else:
#         print("Search is unsuccessful.")

# if __name__ == "__main__":
#     n = int(input("Enter the size of array: "))
#     arr = []
#     for i in range(n):
#         arr.append(int(input("Enter the Elements: ")))
#     target = int(input("Enter no which is to be searched: "))
#     binary_search(n, arr, target)


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return -1

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    result = sol.search(nums, target)
    if result != -1:
        print(f"Target {target} found at index: {result}")
    else:
        print(f"Target {target} not found")

