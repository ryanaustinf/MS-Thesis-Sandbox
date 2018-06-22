import numpy as np
from PIL import Image

def collatePhoto(site,id,heuristic,experts):
	img = np.zeros((768,1366))
	for x in experts:
		temp = np.array(Image.open("%s - %02d - H%d - %02d.png" % (site,id,heuristic,x)).convert("L"))
		img += temp

	img *= 1.0
	img /= len(experts)
	img = 255 - img
	img = np.rint(img)
	im = Image.fromarray(img)
	im = im.convert("RGB")
	im.save("%s - %02d - H%d.png" % (site,id,heuristic))

collatePhoto("Netflix",4,1,[1,2,3])