import sys#işletim sistem, kütüphanesi
import time# ne kadar sürede çalıştığını ölçmek için time kütüphanesi
import csv#csv dosyalarını okumak için
csv.field_size_limit(sys.maxsize)#csv nin okuma limitini arttır


class Divide_and_conquer(object):
    def __init__(self, minimum_x, distance_f_path, profit_f_path):#algoritma için gerekli verileri hazırla
        self.minimum_x = minimum_x
        self.distance_values = []#uzaklıkların listesi
        self.profit_values = []#karların listesi
        self.set_distance_value_file(distance_f_path)#uzaklıkları dosyadan oku
        self.set_profit_value_file(profit_f_path)#karları dosyadan oku
        self.liste = list(zip(self.profit_values, self.distance_values))#baz istasyonlarını oluştur

    def divide_and_conquer_algorithm(self):#algoritmayı başlatan fonksiyon
        result = self.divide_and_conquer(range(len(self.liste)))#range list oluştur ve gönder
        return [self.liste[x] for x in result]#cevabı return et

    def fix_problems(self, arr, left, right):#birbirleriyle çakışan baz istasyonlarının içinden en karlı dizilimi bul
        liste = []
        for x in range(arr[left], arr[right]+1):# N - 1
            liste.append([self.liste[x][1], self.liste[x][0], x])
        return [x[2] for x in self.greedy(liste)]

    def findMax(self, liste):#en karlı baz istasyonunu bul
        max1 = [0, 0]
        for i in liste:
            if i[1] > max1[1]:
                max1 = i
        return max1

    def removeMax(self, max1, x, liste):#en karlı baz istasyonu ile çakışan baz istasyonlarını sil
        i = 0
        while i != len(liste):
            if max1[0] - x < liste[i][0] < max1[0] + x:
                liste.remove(liste[i])
            else:
                i += 1

    def greedy(self, liste):#divide and conquer dan üretilen küçük problemler greedy ile çözülür. çünkü çakışma çok fazladır.
        result = []
        while len(liste) != 0:#küçük problem tamamen çözülene kadar
            result.append(self.findMax(liste))# en büyüğü bul
            self.removeMax(result[-1], self.minimum_x, liste)# en büyüğü ile çakışanları sil
        return result#çözümü döndür

    def divide_and_conquer(self, arr):#arr verilerin kendilerini değil indexlerini tutar
        index = 0
        result = []
        while len(arr) != index + 1:# listenin sonuna kadar
            if self.liste[index+1][1] - self.liste[index][1] < self.minimum_x:# mevcut baz istasyonu kendinden sonraki ile çakışıyorsa
                cur_index = index # 1
                #peşi sıra çakışan baz istasyonlarının listedeki başlangıç ve bitiş indexlerini bul
                while self.liste[cur_index+1][1] - self.liste[cur_index][1] < self.minimum_x and len(arr) != cur_index + 2:# bir sonraki bir önceki ile çakışmayana kadar
                    cur_index += 1#küçük problemin indexini arttır
                fixed_list = self.fix_problems(arr, index, cur_index+1 if len(arr) == cur_index + 2 else cur_index)#küçük problemin çözülmesi için gönder
                index = cur_index + 1#küçük problem çözüldüğüne göre bu elemanları atla
                for x in range(len(fixed_list)):#çözümü sonuca ekle
                    result.append(fixed_list[x])
            else:#çakışma yok ise direk listeye eklenebilir
                result.append(arr[index])
                index += 1
            if len(arr) == index + 1 and self.liste[index][1] - self.liste[result[-1]][1] >= self.minimum_x:#listenin son elemanı ise ve çakışmıyorsa
                    result.append(arr[index])#sonuca eklenir
        return result

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
    divide_and_conquer = Divide_and_conquer(1000, "Dist_birmilyon.csv", "Kar_birmilyon.csv")#algoritmayı hazırla
    a = time.time()#başlangıç zamanı
    result = divide_and_conquer.mergesort_algorithm()#algoritmayı çalıştır
    print("length:", len(result))#maximum karı veren baz istasyonlarının sayısı
    print("sum", sum([x[0] for x in result]))#maximum kar
    b = time.time()#bitiş zamanı
    print(b - a)#çalışma zamanı, saniye cinsinden
