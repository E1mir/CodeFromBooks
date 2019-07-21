class BinarySearch(object):

    def __init__(self, array):
        self.list = array
        self.length = len(array)
        self.count = 0

    def search(self, target):
        low = 0
        high = self.length - 1
        self.count = 0
        while low <= high:
            mid_idx = (low + high) / 2
            middle_item = self.list[mid_idx]
            if middle_item == target:
                return mid_idx

            if middle_item > target:
                high = mid_idx - 1
            else:
                low = mid_idx + 1
            self.count += 1

        return None


if __name__ == '__main__':
    my_list = [5, 7, 13, 33, 45, 76, 81, 89, 90, 102, 106, 203]
    bin_s = BinarySearch(my_list)
    a = bin_s.search(203)
    print(a)
