import sys#işletim sistem, kütüphanesi
import time# ne kadar sürede çalıştığını ölçmek için time kütüphanesi
import csv#csv dosyalarını okumak için
csv.field_size_limit(sys.maxsize)#csv nin okuma limitini arttır
from itertools import combinations#python standart kütüphanesinin tüm olası kombinasyonları bulan fonksiyonu


class Brute_force(object):
    def __init__(self, minimum_x, distance_f_path="distance.txt", profit_f_path="profit.txt"):#algoritma için gerekli verileri hazırla
        self.minimum_x = minimum_x
        self.distance_values = []#uzaklık listesi
        self.profit_values = []#kar listesi
        self.set_distance_value_file(distance_f_path)#dosyadan uzaklıkları oku
        self.set_profit_value_file(profit_f_path)#dosyadan karları oku

    def is_valid_array(self, array):# bu dizilim kurallara uyuyormu
        distances = [x[1] for x in array]#uzaklıkları al
        index = 0
        while index + 1 != len(distances):#tüm listeyi dolaş
            if distances[index + 1] - distances[index] < self.minimum_x:#uymuyora false döndür
                return False
            index += 1
        return True#uyuyorsa true döndür

    def brute_force(self):
        releated_list = [[x, y] for x, y in zip(self.profit_values, self.distance_values)]#baz istasyonlarını oluştur
        all_combinations = [list(map(list, combinations(releated_list, i))) for i in range(len(self.distance_values) + 1)]#tüm olası kombinasyonları hesapla
        all_combinations.pop(0)#boş listeyi çıkar
        valid_arrays = []#kurallara uyan dizilimler
        for z in all_combinations:
            liste = [x for x in z if self.is_valid_array(x)]# kurallara uyan dizilimleri oluştur
            for x in liste:#listeye ekle
                valid_arrays.append(x)
        return max(valid_arrays, key=lambda x: sum([y[0] for y in x]))  # en karlısını döndür

    def set_distance_value_file(self, path):#csv dosyasından uzaklıkları oku
        liste = []
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                liste = row[0].split(',')
        last_count = 0
        for x in liste:
            last_count += int(x)
            self.distance_values.append(last_count)

    def set_profit_value_file(self, path):#csv dosyasından karları oku
        liste = []
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                liste = row[0].split(',')
        self.profit_values = [int(x) for x in liste]


if __name__ == "__main__":
    brute_force = Brute_force(100, "Dist_yuz.csv", "Kar_yuz.csv")#algoritmayı hazırla
    a = time.time()#başlangıç zamanı
    result_list = brute_force.brute_force()#algoritmayı çalıştır
    print("length:", len(result_list))#maximum karı veren baz istasyonlarının sayısı
    result = sum([x[0] for x in result_list])#maximum kar
    b = time.time()#bitiş zamanı
    print(b-a)#çalışma süresi
