import sys
from itertools import combinations
import time
import csv
csv.field_size_limit(sys.maxsize)
print("max", sys.maxsize)


class Node(object):
    def __init__(self, distance, profit):
        self.distance = distance
        self.profit = profit
        self.next_list = []
        self.prev = []

    def __str__(self):
        return f'distance:%d, profit:%d' % (self.distance, self.profit)


class Greedy(object):
    def __init__(self, minimum_x, distance_f_path="distance.txt", profit_f_path="profit.txt"):
        self.minimum_x = minimum_x
        self.distance_values = []
        self.profit_values = []
        self.set_distance_value_file(distance_f_path)
        self.set_profit_value_file(profit_f_path)
        self.liste = list(zip(self.distance_values, self.profit_values))

    def findMax(self):
        max1 = [0, 0]
        for i in self.liste:
            if i[1] > max1[1]:
                max1 = i
        return max1

    def removeMax(self, max1, x):
        i = 0
        while i != len(self.liste):
            if max1[0] - x < self.liste[i][0] < max1[0] + x:
                self.liste.remove(self.liste[i])
            else:
                i += 1

    def greedy(self):
        result = []
        while len(self.liste) != 0:
            result.append(self.findMax())
            self.removeMax(result[-1], self.minimum_x)
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
    a = time.time()
    greedy = Greedy(100, "Dist_yuzbin.csv", "Kar_yuzbin.csv")
    result = greedy.greedy()
    print("length:", len(result))
    print("result:", sum([x[1] for x in result]))
    b = time.time()
    print(b-a)
