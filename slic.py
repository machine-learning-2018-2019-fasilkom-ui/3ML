from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from skimage import io
import matplotlib.pyplot as plt
 
# load image
print ("Load Image ...")
image = img_as_float(io.imread('/Users/rizki/Documents/ML/pleiades/PHR1A_PMS_201803310309070_ORT_8bit_ms_.tif'))
# print (image);
 
# loop over the number of segments
print ("Segmentation Process ...")
for numSegments in (250, 500, 1000):
	# apply SLIC and extract (approximately) the supplied number
	# of segments
	segments = slic(image, n_segments = numSegments, sigma = 5, slic_zero = True,
					convert2lab = None, multichannel = True)
 
	# show the output of SLIC
	fig = plt.figure("Superpixels -- %d segments" % (numSegments))
	ax = fig.add_subplot(1, 1, 1)
	ax.imshow(mark_boundaries(image, segments))
	plt.axis("off")
 
# show the plots
print ("Result ...")
plt.show()