import sys#işletim sistem, kütüphanesi
import time# ne kadar sürede çalıştığını ölçmek için time kütüphanesi
import csv#csv dosyalarını okumak için
csv.field_size_limit(sys.maxsize)#csv nin okuma limitini arttır


class Greedy(object):
    def __init__(self, minimum_x, distance_f_path="distance.txt", profit_f_path="profit.txt"):#istenilen şekilde initialize et
        self.minimum_x = minimum_x
        self.distance_values = []#uzaklıklar
        self.profit_values = []#karlar
        self.set_distance_value_file(distance_f_path)#uzaklıkları dosyadan oku
        self.set_profit_value_file(profit_f_path)#karları dosyadan
        self.liste = list(zip(self.distance_values, self.profit_values))#baz istasyonlarını oluştur

    def findMax(self):#en karlı baz istasyonunu bul
        max1 = [0, 0]
        for i in self.liste:
            if i[1] > max1[1]:
                max1 = i
        return max1

    def removeMax(self, max1, x):#bulunan baz istasyonu ile çakışan baz istasyonlarını listeden sil
        i = 0
        for y in self.liste:
            if max1[0] - x < y[0] < max1[0] + x:
                self.liste.remove(y)

    def greedy(self):
        result = []
        while len(self.liste) != 0:#listenin eleman sayısı sıfır olmadığı sürece
            result.append(self.findMax())# en karlı baz istasyonunu sonuçlara ekle
            self.removeMax(result[-1], self.minimum_x)# en karlı baz istasyonu ile çakışan baz istasyonlarını sil
        return result

    def set_distance_value_file(self, path):#csv dosyasından oku
        liste = []
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                liste = row[0].split(',')
        last_count = 0
        for x in liste:
            last_count += int(x)
            self.distance_values.append(last_count)#uzaklık listesine ekle

    def set_profit_value_file(self, path):#csv dosyasından oku
        liste = []
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                liste = row[0].split(',')
        self.profit_values = [int(x) for x in liste]#kar listesine ekle


if __name__ == "__main__":
    greedy = Greedy(100, "Dist_yuzbin.csv", "Kar_yuzbin.csv")#algoritmayı hazırla
    a = time.time()  # başlangıç zamanı
    result = greedy.greedy()#algoritmayı çalıştır
    print("length:", len(result))#maximum karı veren baz istasyonlarının sayısı
    print("result:", sum([x[1] for x in result]))#maximum kar
    b = time.time()#bitiş zamanı
    print(b-a)#çalışma zamanı, saniye cinsinden
