import Image
import random
import collections
import io

NUM_CLUSTERS = [10,50,100,250,500]
ITERATIONS = 10
IMAGE_NAME = "starry"
PERCENT = 0.1

im = Image.open("starry.jpg")
rgb_im = im.convert('RGB')

pixels = list(im.getdata())
width, height = im.size #

pixel_data = []
for w in range(width):
	for h in range(height):
		r, g, b = rgb_im.getpixel((w,h))
		pixel_data.append([r,g,b,w,h])

def update_centers(centers, data, percent):
	center_to_data = collections.defaultdict(list)
	for d in data:
		if random.random() < percent:
			distances = [dist(d, center) for center in centers]
			center_index = distances.index(min(distances))
			center_to_data[center_index].append(d)
	for index, data_points in center_to_data.iteritems():
		centers[index] = average(data_points)

rint = random.randint
#intialize random centers
def getInitalCenters(n):
	centers = []
	for i in range(n):
		centers.append([rint(0,255),rint(0,255),rint(0,255),
			rint(0,width),rint(0,height)])
	return centers

def average(data):
	sum = [0,0,0,0,0]
	for d in data:
		for i in range(5):
			sum[i] += (1/(0.0+len(data))) * d[i]
	return sum

weights = [1,1,1,0,0]
# color distance, with local spatial weighting
def dist(a,b):
	sum  = 0
	for i in range(5):
		sum += weights[i]*(a[i]-b[i])*(a[i]-b[i])
	return (sum)**(0.5)

def save(n, centers):
	f = open(IMAGE_NAME+str(n)+".html", "w+")
	template = open("voroni.html").read()
	template = template.replace("REPLACE_WIDTH", str(width))
	template = template.replace("REPLACE_HEIGHT", str(height))
	s = """[\n"""
	centers = [list(x) for x in set(tuple(x) for x in centers)]
	for center in centers:
		s += """ {{"r":{},"g":{},"b":{}, "width":{},"height":{}}},\n """.format(center[0],center[1],center[2],center[3], center[4])
	s += """]"""
	f.write(template.replace("REPLACE_ME",s))
	f.close()

for num_cluster in NUM_CLUSTERS:
	print "starting "+str(num_cluster)
	centers = getInitalCenters(num_cluster)
	for i in range(ITERATIONS):
		if i%1 == 0:
			print "iteration "+str(i)
		update_centers(centers, pixel_data, PERCENT)
	save(num_cluster, centers)
