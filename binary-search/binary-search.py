class BinarySearch:
    @staticmethod
    def get_first_and_last_indices(items, target_item):
        left = 0
        right = len(items) - 1
        first_index_of_target_item = -1
        last_index_of_target_item = -1
        for i in range(len(items)):
            mid = (left + right) // 2

            if items[mid] == target_item:
                first_index_of_target_item = mid
                last_index_of_target_item = mid
                j = mid + 1
                k = mid - 1

                while True:
                    if items[j] == target_item:
                        last_index_of_target_item = j
                    else:
                        break
                    j += 1

                while True:
                    if items[k] == target_item:
                        first_index_of_target_item = k
                    else:
                        break
                    k -= 1

                break
            elif items[mid] > target_item:
                right = mid - 1
            else:
                left = mid + 1

        return [first_index_of_target_item, last_index_of_target_item]

    @staticmethod
    def get_first_index(items, target_item):
        index = -1

        left = 0
        right = len(items) - 1

        while left <= right:
            mid = (left + right) // 2

            if items[mid] == target_item:
                index = mid
                right = mid - 1
            elif items[mid] < target_item:
                left = mid + 1
            else:
                right = mid - 1

        return index

    @staticmethod
    def get_last_index(items, target_item):
        index = -1
        left = 0
        right = len(items) - 1

        while left <= right:
            mid = (left + right) // 2

            if items[mid] == target_item:
                index = mid
                left = mid + 1
            elif items[mid] > target_item:
                right = mid - 1
            else:
                left = mid + 1

        return index

    @staticmethod
    def get_first_and_last_occurrences(items, target_item):
        first_occurrence = BinarySearch.get_first_index(items, target_item)
        last_occurrence = BinarySearch.get_last_index(items, target_item)
        return [first_occurrence, last_occurrence]


number_list_1 = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
target = 9
first_and_last_indices = BinarySearch.get_first_and_last_indices(number_list_1, target)
print(first_and_last_indices)
first_and_last_occurrences = BinarySearch.get_first_and_last_occurrences(number_list_1, target)
print(first_and_last_occurrences)

number_list_2 = [1, 2, 3, 4, 5, 6, 10]
target = 9
first_and_last_indices = BinarySearch.get_first_and_last_indices(number_list_2, target)
print(first_and_last_indices)
first_and_last_occurrences = BinarySearch.get_first_and_last_occurrences(number_list_2, target)
print(first_and_last_occurrences)


number_list_3 = [100, 150, 150, 153]
target = 150
first_and_last_indices = BinarySearch.get_first_and_last_indices(number_list_3, target)
print(first_and_last_indices)
first_and_last_occurrences = BinarySearch.get_first_and_last_occurrences(number_list_3, target)
print(first_and_last_occurrences)


number_list_4 = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
target = 2
first_and_last_indices = BinarySearch.get_first_and_last_indices(number_list_4, target)
print(first_and_last_indices)
first_and_last_occurrences = BinarySearch.get_first_and_last_occurrences(number_list_4, target)
print(first_and_last_occurrences)


