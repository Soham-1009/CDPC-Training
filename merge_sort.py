# merge sort with sorted array
# class Mergesort:
#     def mergesort(self,arr1,arr2):
#         arr3=[]
#         i=0
#         j=0
#         k=0
#         while i<len(arr1) and j<len(arr2):
#             if arr1[i]<arr2[j]:
#                 arr3.append(arr1[i])
#                 i+=1
#                 k+=1
#             else:
#                 arr3.append(arr2[j])
#                 j+=1
#                 k+=1

#         return arr3

# if __name__ == '__main__':
#     obj=Mergesort()
#     arr1=[1,3,5]
#     arr2=[2,4,6]
#     ans=obj.mergesort(arr1,arr2)
#     print(ans)

###################################################################################

# merge sort with multiple elements isn 1 array

# class MergeSorts:
#     def mergeSort(self, arr1, arr2):
#         arr3 = []
#         i = 0
#         j = 0
#         k = 0
#         while i < len(arr1) and j < len(arr2):
#             if arr1[i] < arr2[j]:
#                 arr3.append(arr1[i])
#                 i += 1
#                 k += 1
#             else:
#                 arr3.append(arr2[j])
#                 j += 1
#                 k += 1
#         while len(arr1) > i:
#             arr3.append(arr1[i])
#             i += 1
#             k += 1
#         while len(arr2) > j:
#             arr3.append(arr2[j])
#             j += 1
#             k += 1
#         return arr3


# if __name__ == "__main__":
#     obj = MergeSorts()
#     arr1 = [1, 3, 5, 7, 8, 9]
#     arr2 = [2, 4, 6]
#     ans = obj.mergeSort(arr1, arr2)
#     print(ans)


#######################################################################
# merge sort with single unsorted array
#
#
#
# class MergeSorts:
#     def mergeSort(self, arr):
#         if len(arr) > 1:
#             mid = len(arr) // 2
#             arr1 = arr[:mid]
#             arr2 = arr[mid:]
#             self.mergeSort(arr1)
#             self.mergeSort(arr2)
#             i = 0
#             j = 0
#             k = 0
#             while i < len(arr1) and j < len(arr2):
#                 if arr1[i] < arr2[j]:
#                     arr[k] = arr1[i]
#                     i += 1
#                     k += 1
#                 else:
#                     arr[k] = arr2[j]
#                     j += 1
#                     k += 1
#             while len(arr1) > i:
#                 arr[k] = arr1[i]
#                 i += 1
#                 k += 1
#             while len(arr2) > j:
#                 arr[k] = arr2[j]
#                 j += 1
#                 k += 1
#             return arr


# if __name__ == "__main__":
#     obj = MergeSorts()
#     arr = [5, 7, 9, 6, 8, 3, 67]
#     ans = obj.mergeSort(arr)
#     print(ans)


############################################################################

class MergeSorts:
    def mergeSort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            arr1 = arr[:mid]
            arr2 = arr[mid:]
            self.mergeSort(arr1)
            self.mergeSort(arr2)
            i = 0
            j = 0
            k = 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] > arr2[j]:
                    arr[k] = arr1[i]
                    i += 1
                    k += 1
                else:
                    arr[k] = arr2[j]
                    j += 1
                    k += 1
            while len(arr1) > i:
                arr[k] = arr1[i]
                i += 1
                k += 1
            while len(arr2) > j:
                arr[k] = arr2[j]
                j += 1
                k += 1
            return arr


if __name__ == "__main__":
    obj = MergeSorts()
    arr = [5, 7, 9, 6, 8, 3, 67]
    ans = obj.mergeSort(arr)
    print(ans)