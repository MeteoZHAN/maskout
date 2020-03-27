# coding = utf-8

import shapefile
import numpy as np
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from shapely.ops import cascaded_union


shp = shapefile.Reader('dishi')
rec = shp.shapeRecords()

polygon = list()

for r in rec:
    polygon.append(Polygon(r.shape.points))
poly = cascaded_union(polygon)   #并集
ext = list(poly.exterior.coords)  #外部点

codes = [Path.MOVETO] + [Path.LINETO] * (len(ext) - 1)
codes += [Path.CLOSEPOLY]
ext.append(ext[0])
path = Path(np.array(ext), codes)
patch = PathPatch(path,facecolor = 'None')
fig,ax = plt.subplots()
ax.add_patch(patch)

sample_data = np.random.rand(100, 100)
x = np.linspace(110, 120, 100)
y = np.linspace(20, 30, 100)
qs = plt.contourf(x, y, sample_data)
for col in qs.collections:
    col.set_clip_path(patch)

plt.show()
