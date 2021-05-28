import sys
from itertools import combinations
import csv
import time
csv.field_size_limit(sys.maxsize)
print("max", sys.maxsize)


class Divide_and_conquer(object):
    def __init__(self, minimum_x, distance_f_path, profit_f_path):
        self.minimum_x = minimum_x
        self.distance_values = []
        self.profit_values = []
        self.set_distance_value_file(distance_f_path)
        self.set_profit_value_file(profit_f_path)
        self.liste = list(zip(self.profit_values, self.distance_values))

    def mergesort_algorithm(self):
        result = self.mergeSort(range(len(self.liste)))
        return [self.liste[x] for x in result]

    def fix_problems(self, arr, left, right):
        liste = []
        for x in range(arr[left], arr[right]+1):# N - 1
            liste.append([self.liste[x][1], self.liste[x][0], x])
        return [x[2] for x in self.greedy(liste)]

    def findMax(self, liste):
        max1 = [0, 0]
        for i in liste:
            if i[1] > max1[1]:
                max1 = i
        return max1

    def removeMax(self, max1, x, liste):
        i = 0
        while i != len(liste):
            if max1[0] - x < liste[i][0] < max1[0] + x:
                liste.remove(liste[i])
            else:
                i += 1

    def greedy(self, liste):
        result = []
        while len(liste) != 0:
            result.append(self.findMax(liste))
            self.removeMax(result[-1], self.minimum_x, liste)
        return result

    def mergeSort(self, arr):
        index = 0 # 1
        result = [] # 1
        while len(arr) != index + 1: # N+1
            if self.liste[index+1][1] - self.liste[index][1] < self.minimum_x:
                cur_index = index # 1
                while self.liste[cur_index+1][1] - self.liste[cur_index][1] < self.minimum_x and len(arr) != cur_index + 2:# N - 1
                    cur_index += 1
                fixed_list = self.fix_problems(arr, index, cur_index+1 if len(arr) == cur_index + 2 else cur_index)
                index = cur_index + 1
                for x in range(len(fixed_list)):
                    result.append(fixed_list[x])
            else:
                result.append(arr[index])
                index += 1
            if len(arr) == index + 1 and self.liste[index][1] - self.liste[result[-1]][1] >= self.minimum_x:
                    result.append(arr[index])
        return result

    def set_distance_value_file(self, path):
        liste = []
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                liste = row[0].split(',')
        last_count = 0
        for x in liste:
            last_count += int(x)
            self.distance_values.append(last_count)

    def set_profit_value_file(self, path):
        liste = []
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                liste = row[0].split(',')
        self.profit_values = [int(x) for x in liste]


if __name__ == "__main__":
    divide_and_conquer = Divide_and_conquer(1000, "Dist_birmilyon.csv", "Kar_birmilyon.csv")
    a = time.time()
    result = divide_and_conquer.mergesort_algorithm()
    print("result:", result)
    print("length:", len(result))
    print("sum", sum([x[0] for x in result]))
    b = time.time()
    print(b - a)