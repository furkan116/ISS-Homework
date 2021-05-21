import sys
from itertools import combinations


class Dynamic_programming(object):
    def __init__(self, minimum_x, distance_f_path="distance.txt", profit_f_path="profit.txt"):
        self.minimum_x = minimum_x
        self.distance_values = []
        self.profit_values = []
        self.set_distance_value_file(distance_f_path)
        self.set_profit_value_file(profit_f_path)

    def dynamic_programming(self):
        releated_list = [[x, y] for x, y in zip(self.profit_values, self.distance_values)]
        print(releated_list)
        liste = [
            [[0], [-self.minimum_x]],
        ]
        for x in range(len(releated_list)):
            for y in range(len(liste)):
                if releated_list[x][1] - liste[y][1][-1] >= self.minimum_x:
                    liste[y][1].append(releated_list[x][1])
                    liste[y][0].append(releated_list[x][0])
                else:
                    new_list = [[], []]
                    for z in range(len(liste[y][0])-1):
                        new_list[1].append(liste[y][1][z])
                        new_list[0].append(liste[y][0][z])
                    new_list[1].append(releated_list[x][1])
                    new_list[0].append(releated_list[x][0])
                    liste.append(new_list)
        print(liste)
        return max(liste, key=lambda x: sum(x[0]))

    def set_distance_value_file(self, path):
        dosya = open(path, "r")
        txt = dosya.read()
        self.distance_values = [int(x) for x in txt.split()]

    def set_profit_value_file(self, path):
        dosya = open(path, "r")
        txt = dosya.read()
        self.profit_values = [int(x) for x in txt.split()]


if __name__ == "__main__":
    dynamic_programming = Dynamic_programming(5, "distance.txt", "profit.txt")
    best_one = dynamic_programming.dynamic_programming()
    best_one[1].pop(0)
    best_one[0] = sum(best_one[0])
    print(best_one)
