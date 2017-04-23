import camera
from numpy import *
from PIL import Image
from pylab import *
from scipy import *

# load some images
im1 = array(Image.open('images/001.jpg'))
im2 = array(Image.open('images/002.jpg'))

# load 2D points for each view to a list
points2D = [loadtxt('2D/00'+str(i+1)+'.corners').T for i in range(3)]

# load 3D points
points3D = loadtxt('3D/p3d').T

# load correspondences
corr = genfromtxt('2D/nview-corners',dtype='int',missing_values='*')

# load cameras to a list of Camera objects (ma tran P cua tung Camera)
P = [camera.Camera(loadtxt('2D/00'+str(i+1)+'.P')) for i in range(3)]
