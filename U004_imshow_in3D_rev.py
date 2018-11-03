import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm

# # create a 21 x 21 vertex mesh
# xx, yy = np.meshgrid(np.linspace(0,1,21), np.linspace(0,1,21))
#
# # create vertices for a rotated mesh (3D rotation matrix)
#
# X = xx
# Y = yy
# Z = 10*np.ones(X.shape)
# # create some dummy data (20 x 20) for the image
# data = np.cos(xx) * np.cos(xx) + np.sin(yy) * np.sin(yy)

nx = 30
ny = 20
nz = 50

vx = np.linspace(1500, 3000, nx)
vy = np.linspace(1500, 4000, ny)
vz = np.linspace(1500, 8000, nz)

vxy = np.sqrt(np.transpose(np.mat(vy)) * np.mat(vx))
vxyz = []
for i in range(len(vz)):
    vxyz.append(np.sqrt(vxy * vz[i]))
vxyz = np.array(vxyz).transpose()
data = vxyz[:,:,0]
x = np.linspace(0, 50, nx)
y = np.linspace(0, 40, ny)
z = np.linspace(0, 100, nz)

Y, X = np.meshgrid(y, x)
print(min(X.shape),Y.shape,data.shape)




# print(np.min(X))
# create the figure
fig = plt.figure()

# show the reference image
ax1 = fig.add_subplot(121)
ax1.imshow(data, cmap=plt.cm.jet, interpolation='nearest', origin='lower', extent=[(np.min(X)),(np.max(X)),(np.min(Y)),(np.max(Y))])

# show the 3D rotated projection
ax2 = fig.add_subplot(122, projection='3d')
cset = ax2.contourf(X, Y, data, 10, zdir='z', offset=80, cmap=cm.BrBG)

ax2.set_zlim((np.max(z), np.min(z)))

# plt.colorbar(cset)
plt.show()