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


