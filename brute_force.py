import sys
import csv
from itertools import combinations
import time


class Brute_force(object):
    def __init__(self, minimum_x, distance_f_path="distance.txt", profit_f_path="profit.txt"):
        self.minimum_x = minimum_x
        self.distance_values = []
        self.profit_values = []
        self.set_distance_value_file(distance_f_path)
        self.set_profit_value_file(profit_f_path)

    def is_valid_array(self, array):
        distances = [x[1] for x in array]
        temp = [x for x in distances]
        temp.reverse()
        index = 0
        while index+1 != len(distances):
            if distances[index+1] - distances[index] < self.minimum_x:
                return False
            index += 1
        return True

    def brute_force(self):
        releated_list = [[x, y] for x, y in zip(self.profit_values, self.distance_values)]
        all_combinations = [list(map(list, combinations(releated_list, i))) for i in range(len(self.distance_values) + 1)]
        all_combinations.pop(0)
        valid_arrays = []
        for z in all_combinations:
            liste = [x for x in z if self.is_valid_array(x)]
            for x in liste:
                valid_arrays.append(x)
        profit_list = [sum([x[0] for x in y]) for y in valid_arrays]
        #return max(profit_list)  # if asking max profit
        return max(valid_arrays, key=lambda x: sum([y[0] for y in x]))  # return both of them

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
    a = time.time()
    brute_force = Brute_force(100, "Dist_on.csv", "Kar_on.csv")
    result = sum([x[0] for x in brute_force.brute_force()])
    b = time.time()
    print(result)
    print(b-a)
