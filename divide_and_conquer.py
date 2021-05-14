import sys
from itertools import combinations


class Divide_and_conquer(object):
    def __init__(self, minimum_x, distance_f_path, profit_f_path):
        self.minimum_x = minimum_x
        self.distance_values = []
        self.profit_values = []
        self.set_distance_value_file(distance_f_path)
        self.set_profit_value_file(profit_f_path)
        self.liste = list(zip(self.profit_values, self.distance_values))
        print(self.liste)
        self.mergeSort([0, 1, 2, 3, 4, 5, 6])

    def this_way(self, arr, start, end):
        if start+1 >= end:
            return [[arr[start]], self.liste[arr[start]][1]]
        else:
            index = start
            result_list = []
            while index+1 < end and self.liste[index][1] - self.liste[arr[start]][1] < self.minimum_x:
                result_list.append(self.this_way(arr, index+2, end))
                index += 1
            max_one = result_list[0]
            for x in result_list:
                if x[1] > max_one[1]:
                    max_one = x
            max_one[0].insert(0, arr[start])
            max_one[1] += self.liste[arr[start]][1]
            return max_one

    def fix_problems(self, arr, left, right):
        if right - left == 0:
            return [arr[left]]
        elif right - left == 1:
            return [max(arr[left], arr[right])]
        else:
            left_one = self.this_way(arr, left, right)
            right_one = self.this_way(arr, left+1, right)
            if left_one[1] > right_one[1]:
                return left_one[0]
            else:
                return right_one[0]

    def mergeSort(self, arr):
        index = 0
        result = []
        while len(arr) != index + 1:
            if self.liste[index+1][1] - self.liste[index][1] < self.minimum_x:
                cur_index = index
                while self.liste[cur_index+1][1] - self.liste[cur_index][1] < self.minimum_x and len(arr) != cur_index + 2:
                    cur_index += 1
                fixed_list = self.fix_problems(arr, index, cur_index+1 if len(arr) == cur_index + 2 else cur_index)
                index = cur_index + 1
                for x in range(len(fixed_list)):
                    result.append(fixed_list[x])
            else:
                result.append(arr[index])
                index += 1
        print("result:", result)

    def set_distance_value_file(self, path):
        dosya = open(path, "r")
        txt = dosya.read()
        self.distance_values = [int(x) for x in txt.split()]

    def set_profit_value_file(self, path):
        dosya = open(path, "r")
        txt = dosya.read()
        self.profit_values = [int(x) for x in txt.split()]


if __name__ == "__main__":
    divide_and_conquer = Divide_and_conquer(5, "distance.txt", "profit.txt")
