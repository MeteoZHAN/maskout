# coding=utf-8
'''
本程序实现江西省范围内的格点选取
'''

import numpy as np
import shapefile
import shapely.geometry as geometry
from shapely.geometry import Polygon
from shapely.ops import cascaded_union
import matplotlib.pyplot as plt

shp = shapefile.Reader(r'DTool\dishi.shp')
rec = shp.shapeRecords()
polygon = []
for r in rec:
    polygon.append(Polygon(r.shape.points))  # 获取各个地市点边界
poly = cascaded_union(polygon)  # 并集
ext = list(poly.exterior.coords)  # 外部点，即最外面轮廓（省界）
x = [i[0] for i in ext]
y = [i[1] for i in ext]
plt.plot(x, y, 'r')

lon = np.linspace(113, 119, 50)
lat = np.linspace(24, 30.5, 50)
grid_lon, grid_lat = np.meshgrid(lon, lat)
flat_lon = grid_lon.flatten()  # 将坐标展成一维
flat_lat = grid_lat.flatten()  # 将坐标展成一维
plt.scatter(flat_lon, flat_lat)
flat_points = np.column_stack((flat_lon, flat_lat))  # 拼接成二维点
in_shape_points = []
for pt in flat_points:
    if geometry.Point(pt).within(geometry.shape(poly)):   # 判断点是否在多边形内
        in_shape_points.append(pt)
sel_lon = [elem[0] for elem in in_shape_points]
sel_lat = [elem[1] for elem in in_shape_points]

plt.scatter(np.array(sel_lon), np.array(sel_lat), c='g')
plt.show()
