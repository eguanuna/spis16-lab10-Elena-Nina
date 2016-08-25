import cars

import matplotlib.pyplot as plt


cardata = cars.get_cars()

def horsepower(cardata):
    horsepower_list = []
    for h in (cardata):
        horsepower_list.append(h['Engine Information']['Engine Statistics']['Horsepower'])
    return horsepower_list
    

hp_list = horsepower(cardata)

from collections import defaultdict

def histogramify(data,bins):
	M = max(data)
	m = min(data)
	interval = (M-m)/bins
	hist = defaultdict(int)
	for d in data:
		for i in range(bins):
			if d>m+i*interval:
				f=m+i*interval
		hist[f]+=1
	return hist

hist_HP = histogramify(hp_list,25)

xs = range(min(hp_list),max(hp_list))

ys = [hist_HP[x] for x in xs]

plt.bar(xs,ys)

plt.clf()


plt.bar(xs,ys,20)
plt.title('Histogram of Horsepower Data')
plt.ylabel('Number of cars')
plt.xlabel('Horsepower')
plt.savefig('Histogram_HP')

def MPG(cardata):
    MPG_list = []
    for i in cardata:
        MPG_list.append(i['Fuel Information']['Highway mpg'])
    return MPG_list

MPG_list = MPG(cardata)

hist_MPG = histogramify(MPG_list, 25)

xs = range(min(MPG_list), max(MPG_list))

ys = [hist_MPG[x] for x in xs]

plt.bar(xs,ys)

plt.title('Histogram of MPG Data')
plt.ylabel('Number of cars')
plt.xlabel('MPG')
plt.savefig('Histogram_MPG')

plt.clf()


import numpy

X = [[1,h] for h in hp_list]
y = MPG_list
numpy.linalg.lstsq(X,y)

theta = numpy.linalg.lstsq(X,y)[0]

xs = range(min(hp_list),max(hp_list))
ys = [theta[1]*x + theta[0] for x in xs]
plt.plot(xs,ys)


plt.plot(xs,ys)
plt.scatter(hp_list,MPG_list)
plt.title('horsepower versus mpg')
plt.ylabel('Highway MPG')
plt.xlabel('Horsepower')


plt.savefig('HP_MPG_line')

plt.clf()

def cars_MPG_given_HP(horsepower):
	return theta[1]*horsepower+theta[0]

def torque(cardata):
    t_list = []
    for i in cardata:
        t_list.append(i['Engine Information']['Engine Statistics']['Torque'])
    return t_list

t_list = torque(cardata)


plt.scatter(hp_list, t_list)


X = [[1,h] for h in hp_list]
y = t_list
numpy.linalg.lstsq(X,y)

theta = numpy.linalg.lstsq(X,y)[0]

xs = range(min(hp_list),max(hp_list))
ys = [theta[1]*x + theta[0] for x in xs]
plt.plot(xs,ys)

plt.title('horsepower versus torque')
plt.ylabel('Torque')
plt.xlabel('Horsepower')
plt.savefig('Torque_HP_plot')
