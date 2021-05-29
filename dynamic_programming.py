import sys
from itertools import combinations
import csv
import time
csv.field_size_limit(sys.maxsize)


class Dynamic_programming(object):
    def __init__(self, minimum_x, distance_f_path="distance.txt", profit_f_path="profit.txt"):
        self.minimum_x = minimum_x
        self.distance_values = []
        self.profit_values = []
        self.set_distance_value_file(distance_f_path)
        self.set_profit_value_file(profit_f_path)

    def find_best(self, liste):
        max_baz = [[], []]
        max_kar = 0
        for x in liste:
            toplam_kar = sum(x[0])
            if toplam_kar > max_kar:
                max_kar = toplam_kar
                max_baz = x
        return [max_baz]

    def dynamic_programming(self):
        releated_list = [[x, y] for x, y in zip(self.profit_values, self.distance_values)]# N defa
        releated_list = releated_list[:100]
        liste = [
            [[0], [-self.minimum_x]],# 1
        ]
        for x in range(len(releated_list)):# N defa
            for y in range(len(liste)):# N defa
                print(y)
                print(liste)
                if releated_list[x][1] - liste[y][1][-1] >= self.minimum_x:
                    liste[y][1].append(releated_list[x][1])
                    liste[y][0].append(releated_list[x][0])
                else:
                    new_list = [[], []]
                    for z in range(len(liste[y][0])-1):# N Defa
                        new_list[1].append(liste[y][1][z])
                        new_list[0].append(liste[y][0][z])
                    new_list[1].append(releated_list[x][1])
                    new_list[0].append(releated_list[x][0])
                    liste.append(new_list)
            liste = self.find_best(liste)
        return max(liste, key=lambda x: sum(x[0]))

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
    #print(sys.argv[1])
    print("X:", sys.argv[1], "N:", 100)
    dynamic_programming = Dynamic_programming(100, "Dist_on.csv", "Kar_on.csv")
    best_one = dynamic_programming.dynamic_programming()
    best_one[1].pop(0)
    best_one[0] = sum(best_one[0])
    print("length", len(best_one[1]))
    print("result:", best_one[0])
    b = time.time()
    print(b - a)
