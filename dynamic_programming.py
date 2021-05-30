import sys#işletim sistem, kütüphanesi
import time# ne kadar sürede çalıştığını ölçmek için time kütüphanesi
import csv#csv dosyalarını okumak için
csv.field_size_limit(sys.maxsize)#csv nin okuma limitini arttır


class Dynamic_programming(object):
    def __init__(self, minimum_x, distance_f_path="distance.txt", profit_f_path="profit.txt"):#istenilen şekilde initialize et
        self.minimum_x = minimum_x
        self.distance_values = []#uzaklıklar
        self.profit_values = []#karlar
        self.set_distance_value_file(distance_f_path)#dosyadan uzaklıkları oku
        self.set_profit_value_file(profit_f_path)#dosyadan karları oku

    def find_best(self, liste):#en karlı olan baz istasyonu dizilimini bul
        max_baz = [[], []]
        max_kar = 0
        for x in liste:
            toplam_kar = sum(x[0])
            if toplam_kar > max_kar:
                max_kar = toplam_kar
                max_baz = x
        return [max_baz]

    def dynamic_programming(self):
        releated_list = [[x, y] for x, y in zip(self.profit_values, self.distance_values)]# tüm baz istasyonları
        #releated_list = releated_list[:10000]#veri sayısı sınırlayıcı
        liste = [#mevcut en iyi baz istasyonu dizilimleri
            [[0], [-self.minimum_x]],# 1
        ]
        for x in range(len(releated_list)):# tüm baz istasyonlarını kontrol et
            for y in range(len(liste)):# tüm olası en iyi baz istasyon dizilimleri için
                if releated_list[x][1] - liste[y][1][-1] >= self.minimum_x:#eğer çakışma yoksa mevcut dizilime ekle
                    liste[y][1].append(releated_list[x][1])
                    liste[y][0].append(releated_list[x][0])
                else:#çakışma varsa
                    new_list = [[], []]#yeni dizilim oluştur
                    for z in range(len(liste[y][0])-1):# eski dizilimi çakışan baz istasyonu hariç tamamen kopyala
                        new_list[1].append(liste[y][1][z])
                        new_list[0].append(liste[y][0][z])
                    new_list[1].append(releated_list[x][1])#çakışan baz istasyonunu ekle
                    new_list[0].append(releated_list[x][0])
                    liste.append(new_list)#mevcut dizilimi olası en iyi dizilimlere ekle
            liste = self.find_best(liste)#en iyi dizilimi bul ve eklemeye buradan devam et
        return max(liste, key=lambda x: sum(x[0]))# en karlı dizilimi döndür

    def set_distance_value_file(self, path):#csv dosyasından uzaklıkları oku
        liste = []
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                liste = row[0].split(',')
        last_count = 0
        for x in liste:
            last_count += int(x)
            self.distance_values.append(last_count)#uzaklıklar listesine ekle

    def set_profit_value_file(self, path):#csv dosyasından karları oku
        liste = []
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                liste = row[0].split(',')
        self.profit_values = [int(x) for x in liste]#karlar listesine ekle


if __name__ == "__main__":
    dynamic_programming = Dynamic_programming(1000, "Dist_yuzbin.csv", "Kar_yuzbin.csv")#algoritmayı hazırla
    a = time.time()  # başlangıç zamanı
    best_one = dynamic_programming.dynamic_programming()#algoritmayı çalıştır
    best_one[1].pop(0)#boş listeyi at
    best_one[0] = sum(best_one[0])#karların toplamını al
    print("length", len(best_one[1]))# maximum karı veren baz istasyonlarının sayısı
    print("result:", best_one[0])#maximum kar
    b = time.time()#bitiş zamanı
    print(b - a)#çalışma zamanı, saniye cinsinden
