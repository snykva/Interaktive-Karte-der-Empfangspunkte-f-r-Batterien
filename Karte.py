import folium as fo
import numpy as np
from folium.plugins import MarkerCluster


xs =[] #массив с координатами x
ys = [] #массив с координатами y
zs = [] #массив с адресами
ws = [] #массив с названиями
qs = [] #массив с временем работы
adresses=[] # массив с адресами для инф табло
names =[] # массив с названиями для инф табло
timing=[] # массив с временем для инф табло

file = open("Points.txt", encoding='utf-8')

for line in file:  #из файла с данными добавляем их в массивы
    els = line.split(";")
    num = float(els[0])
    num1 = float(els[1])
    num2 = els[2]
    num3 =els[3]
    num4 = els[4]
    xs = np.append(xs, num)
    ys = np.append(ys, num1)
    zs = np.append(zs, num2)
    ws = np.append(ws, num3)
    qs = np.append(qs, num4)

map = fo.Map(location=[55.75, 37.6], zoom_start=10) #создаем карту(координаты Москвы)

marker_cluster = MarkerCluster().add_to(map) #кластеризация маркеров

for j in range(len(zs)-1): #цикл для записи адресов в правильном формате для инф табло и добавления их в массив adresses
    adress = "<i>" + str(zs[j]) + "</i>"
    adresses= np.append(adresses, adress)

for a in range(len(ws)-1): #цикл для записи названия в правильном формате и добавления их в массив names
    name = "<i>" + str(ws[a]) + "</i>"
    names= np.append(names, name)

for b in range(len(qs)-1): #цикл для записи графика работы пунктов в правильном формате для инф табло и добавления их в массив timing
    time = "<i>" + str(qs[b]) + "</i>"
    timing= np.append(timing, time)

def marker(x,y, z,q, w): #функция для добавления маркеров с названиями пунктов и инф табло
    popup1 = (
        " {addr}"
        " {timer}<br> "
        "{b}    {b1}"
    ).format(addr=z,timer = q, b = '<button>Пункт заполнен</button>',b1 = '<button>Пункт пустой</button>' )
    iframe = fo.IFrame(popup1)
    popup2 = fo.Popup(iframe,
                         min_width=230,
                         max_width=230)
    return fo.Marker(location=[x,y], popup=popup2, tooltip=w, icon = fo.Icon(icon = "fa-recycle", prefix='fa', color = "green")).add_to(marker_cluster)

for i in range(len(xs)-1): #выполнение функции при заданных нами значениях
    marker(xs[i],ys[i], adresses[i],timing[i],names[i])



map.save("mape.html") #сохраняем карту

file.close()