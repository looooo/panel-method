import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import parabem
from parabem.pan3d import doublet_3_0_n0
from parabem.utils import check_path

pnt1 = parabem.PanelVector3(-0.5, -0.5, 0)
pnt2 = parabem.PanelVector3(0.5, -0.5, 0)
pnt3 = parabem.PanelVector3(0.5, 0.5, 0)
pnt4 = parabem.PanelVector3(-0.5, 0.5, 0)

source = parabem.Panel3([pnt1, pnt2, pnt3, pnt4])

fig = plt.figure()

x = np.arange(-4, 4, 0.01)
y = []
for xi in x:
    target1 = parabem.PanelVector3(xi, 0, 0.0001)
    target2 = parabem.PanelVector3(xi, 0, 0.5)
    target3 = parabem.PanelVector3(xi, 0, 1.)
    val1 = doublet_3_0_n0(target1, source)
    val2 = doublet_3_0_n0(target2, source)
    val3 = doublet_3_0_n0(target3, source)
    y.append([val1, val2, val3])

ax1 = fig.add_subplot(131)
axes = fig.gca().set_ylim([-2, 5])
ax1.plot(x, y)

y = []
for xi in x:
    target1 = parabem.Vector3(0, xi, 0.0001)
    target2 = parabem.Vector3(0, xi, 0.5)
    target3 = parabem.Vector3(0, xi, 1)
    val1 = doublet_3_0_n0(target1, source)
    val2 = doublet_3_0_n0(target2, source)
    val3 = doublet_3_0_n0(target3, source)
    y.append([val1, val2, val3])

ax2 = fig.add_subplot(132)
axes = fig.gca().set_ylim([-2, 5])
ax2.plot(x, y)

y = []
for xi in x:
    target1 = parabem.Vector3(0, 0, xi)
    target2 = parabem.Vector3(0.5, 0, xi)
    target3 = parabem.Vector3(1, 0, xi)
    val1 = doublet_3_0_n0(target1, source)
    val2 = doublet_3_0_n0(target2, source)
    val3 = doublet_3_0_n0(target3, source)
    y.append([val1, val2, val3])


ax3 = fig.add_subplot(133)
axes = fig.gca().set_ylim([-2, 5])
ax3.plot(x, y)
plt.savefig(check_path("results/3d/doublet_far.png"))
