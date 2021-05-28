from csv import reader
import time


# istasyonlari okuyor
def getStations():
    with open("Dist_on.csv", "r") as readObj:
        for i in reader(readObj):
            dist = list(i)

    with open("Kar_on.csv", "r") as readObj:
        for i in reader(readObj):
            value = list(i)

    dist = list(map(int, dist))
    value = list(map(int, value))

    n = len(dist)
    num = 0
    for i in range(n):
        num += dist[i]
        dist[i] = num

    return [dist, value]


# value degeri en buyuk olan elemani buluyor
def findMax(stations):
    max = [0, 0]

    for i in stations:
        if i[1] > max[1]:
            max = i

    return max


# verilen max degeri ve onun X cevresindekileri siliyor
def removeMax(stations, max, X):
    i = 0
    while i != len(stations):
        if max[0] - X < stations[i][0] and stations[i][0] < max[0] + X:
            stations.remove(stations[i])
        else:
            i += 1


""" stations[i][0] = distance
    stations[i][1] = value """

if __name__ == "__main__":
    X = int(input("X gir: "))
    result = []

    start = time.time()

    # istasyonlari aliyor
    tempStations = getStations()
    stations = list(map(list, zip(tempStations[0], tempStations[1])))
    print(stations, "stations")

    # stations bosalana kadar en verimli elemani bulup result'a ekliyor
    while (len(stations) != 0):
        result.append(findMax(stations))
        removeMax(stations, result[-1], X)

    # toplami yazdiriyor
    print("Sum:", sum([i[1] for i in result]))
    print("Size:", len(result))
    # sonuc listeyi yazdiriyor
    print(*result)

    end = time.time()
    print("calc time:", end - start)