import sys
from itertools import combinations


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
        liste = list(zip(self.distance_values, self.profit_values))
        self.merkez_node = self.greedy(liste)
        print(self.find_best(self.merkez_node.next_list))

    def find_best(self, liste):
        if len(liste[0].next_list) > 0:
            result = [[], 0]
            listeler = []
            for x in liste:
                temp_list = self.find_best(x.next_list)
                temp_list[1] += x.profit
                temp_list[0].insert(0, x.distance)
                listeler.append(temp_list)
            for x in listeler:
                if x[1] > result[1]:
                    result[0] = x[0]
                    result[1] = x[1]
            return result
        else:
            result = [[], 0]
            for x in liste:
                if x.profit > result[1]:
                    result[1] = x.profit
                    result[0] = [x.distance]
            return result

    def greedy(self, liste):
        merkez_node = Node(-self.minimum_x, 0)
        cur_list = [merkez_node]
        liste.insert(0, [merkez_node.distance, merkez_node.profit])
        x = 1
        while x < len(liste):
            new_node = Node(liste[x][0], liste[x][1])
            new_cur_list = []
            for y in cur_list:
                new_cur_list.append(y)
            for y in cur_list:
                if new_node.distance - y.distance >= self.minimum_x:
                    y.next_list.append(new_node)
                    new_node.prev.append(y)
                if new_node not in new_cur_list:
                    new_cur_list.append(new_node)
                if x+2 < len(liste) and liste[x+2][0] - new_node.distance >= self.minimum_x:
                    for z in new_node.prev:
                        if z in new_cur_list:
                            new_cur_list.remove(z)
            cur_list = new_cur_list
            x += 1
        return merkez_node

    def set_distance_value_file(self, path):
        dosya = open(path, "r")
        txt = dosya.read()
        self.distance_values = [int(x) for x in txt.split()]

    def set_profit_value_file(self, path):
        dosya = open(path, "r")
        txt = dosya.read()
        self.profit_values = [int(x) for x in txt.split()]


if __name__ == "__main__":
    greedy = Greedy(5, "distance.txt", "profit.txt")
