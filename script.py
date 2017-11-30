import json as jss
from pprint import pprint
from shapely.geometry import Polygon
from collections import namedtuple

data2 = jss.load(open(r"/home/gcinizwe/Desktop/CarDetectionScript/stream2.json"))
data = jss.load(open(r"/home/gcinizwe/Desktop/CarDetectionScript/stream1.json"))

def area(a, b):  # returns None if rectangles don't intersect
    dx = min(a.xmax, b.xmax) - max(a.xmin, b.xmin)
    dy = min(a.ymax, b.ymax) - max(a.ymin, b.ymin)
    if (dx>=0) and (dy>=0):
        return dx*dy

for i in range(len(data["LABELS"])):
	h1 = data["LABELS"][i]["box2d_front"]["0"]["h"]
	w1 = data["LABELS"][i]["box2d_front"]["0"]["w"]
	area1 = w1 * h1

	for j in range (len(data2["LABELS"])):

		x_1 =  data["LABELS"][i]["box2d_front"]["0"]["x"]
		y_1 = data["LABELS"][i]["box2d_front"]["0"]["y"]
		width_1 = w1
		height_1 = h1

		x_2 = data2["LABELS"][j]["box2d_front"]["0"]["x"]
		y_2 = data2["LABELS"][j]["box2d_front"]["0"]["y"]
		width_2 = data2["LABELS"][j]["box2d_front"]["0"]["w"]
		height_2 = data["LABELS"][j]["box2d_front"]["0"]["h"]

		area2 = width_2 * height_2
		Rectangle = namedtuple('Rectangle', 'xmin ymin xmax ymax')

		ra = Rectangle(x_1, (y_1 - height_1), (x_1 + width_1), y_1)
		rb = Rectangle(x_2, (y_2 - height_1), (x_2 + width_2), y_2)

		total = area(ra, rb)
		
		if isinstance(total, int) and total > 0:
			print (total*2.0)
			print(area1+area2)
			percent = (2*total/(area1+area2))
			print (percent)

			#print (area1 / total )
		#pprint (total)

# intersection here is (3, 3, 4, 3.5), or an area of 1*.5=.5





