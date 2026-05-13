import osgeo
import numpy as np
import rasterio
from rasterio.mask import mask
import geopandas as gpd
from shapely.geometry import mapping
import os

# your shapefile filename here

os.chdir('16_2a')

shapefile = gpd.read_file('16_2a_train_poly.shp')

# dummy CRS
shapefile.set_crs(epsg=4326)

# extract the geometry in GeoJSON format

shapefiles = [0]*8

# 'Class' is the vector attribute that contains the integer mineral class
for i in range(1,9):
    shapefiles[i-1] = shapefile[shapefile["Class"] == i]

# This extracts values from the .tif file based on the training polygon geometries -- clunky: one loop for each
# elemental intensity raster

values_Ca = [0]*8
for i in range(len(shapefiles)):
    geoms = shapefiles[i].geometry.values # list of shapely geometries
# transform to GeJSON format
    for j in range(len(geoms)):
        geoms1 = [mapping(geoms[j])]
# extract the raster values values within the polygon -- assign same dummy CRS
        with rasterio.open('Ca_7.tif', crs='EPSG:4326') as src:
            out_images, out_transform = mask(src, geoms1, crop=True)
        no_data=src.nodata
        data = out_images
        values1 = np.extract(data != no_data, data)
        values_Ca[i] = np.append(values_Ca[i], values1)

test2 = [0]*8
for i in range(len(values_Ca)):
    test2[i] = values_Ca[i][1:]
test3 = np.hstack(test2)
Ca_vals = test3

values_Na = [0]*8
for i in range(len(shapefiles)):
    geoms = shapefiles[i].geometry.values # list of shapely geometries
# transform to GeJSON format
    for j in range(len(geoms)):
        geoms1 = [mapping(geoms[j])]
# extract the raster values values within the polygon -- assign same dummy CRS
        with rasterio.open('Na_7.tif', crs='EPSG:4326') as src:
            out_images, out_transform = mask(src, geoms1, crop=True)
        no_data=src.nodata
        data = out_images
        values1 = np.extract(data != no_data, data)
        values_Na[i] = np.append(values_Na[i], values1)

test2 = [0]*8
for i in range(len(values_Na)):
    test2[i] = values_Na[i][1:]
test3 = np.hstack(test2)
Na_vals = test3

values_Mg = [0]*8
for i in range(len(shapefiles)):
    geoms = shapefiles[i].geometry.values # list of shapely geometries
# transform to GeJSON format
    for j in range(len(geoms)):
        geoms1 = [mapping(geoms[j])]
# extract the raster values values within the polygon -- assign same dummy CRS
        with rasterio.open('Mg_7.tif', crs='EPSG:4326') as src:
            out_images, out_transform = mask(src, geoms1, crop=True)
        no_data=src.nodata
        data = out_images
        values1 = np.extract(data != no_data, data)
        values_Mg[i] = np.append(values_Mg[i], values1)

test2 = [0]*8
for i in range(len(values_Mg)):
    test2[i] = values_Mg[i][1:]
test3 = np.hstack(test2)
Mg_vals = test3

values_K = [0]*8
for i in range(len(shapefiles)):
    geoms = shapefiles[i].geometry.values # list of shapely geometries
# transform to GeJSON format
    for j in range(len(geoms)):
        geoms1 = [mapping(geoms[j])]
# extract the raster values values within the polygon -- assign same dummy CRS
        with rasterio.open('K_7.tif', crs='EPSG:4326') as src:
            out_images, out_transform = mask(src, geoms1, crop=True)
        no_data=src.nodata
        data = out_images
        values1 = np.extract(data != no_data, data)
        values_K[i] = np.append(values_K[i], values1)

test2 = [0]*8
for i in range(len(values_K)):
    test2[i] = values_K[i][1:]
test3 = np.hstack(test2)
K_vals = test3

values_Fe = [0]*8
for i in range(len(shapefiles)):
    geoms = shapefiles[i].geometry.values # list of shapely geometries
# transform to GeJSON format
    for j in range(len(geoms)):
        geoms1 = [mapping(geoms[j])]
# extract the raster values values within the polygon -- assign same dummy CRS
        with rasterio.open('Fe_7.tif', crs='EPSG:4326') as src:
            out_images, out_transform = mask(src, geoms1, crop=True)
        no_data=src.nodata
        data = out_images
        values1 = np.extract(data != no_data, data)
        values_Fe[i] = np.append(values_Fe[i], values1)

test2 = [0]*8
for i in range(len(values_Fe)):
    test2[i] = values_Fe[i][1:]
test3 = np.hstack(test2)
Fe_vals = test3

values_Ti = [0]*8
for i in range(len(shapefiles)):
    geoms = shapefiles[i].geometry.values # list of shapely geometries
# transform to GeJSON format
    for j in range(len(geoms)):
        geoms1 = [mapping(geoms[j])]
# extract the raster values values within the polygon -- assign same dummy CRS
        with rasterio.open('Ti_7.tif', crs='EPSG:4326') as src:
            out_images, out_transform = mask(src, geoms1, crop=True)
        no_data=src.nodata
        data = out_images
        values1 = np.extract(data != no_data, data)
        values_Ti[i] = np.append(values_Ti[i], values1)


test2 = [0]*8
for i in range(len(values_Ti)):
    test2[i] = values_Ti[i][1:]
test3 = np.hstack(test2)
Ti_vals = test3


# only needs run once -- Can use any set of values; using Ti here
test2 = [0]*8
for i in range(len(values_Ti)):
    test = values_Ti[i][1:]
    test1 = np.zeros_like(test)+i+1
    test2 = np.append(test2,test1)

test3 = test2[test2 > 0]
Ti_mins = test3


X_rf1 = np.vstack((Ca_vals, Na_vals, Mg_vals, Fe_vals, K_vals, Ti_vals))

X_rf1 = X_rf1.T
y_rf1 = Ti_mins


np.savetxt('x_rf_16_2a.csv', X_rf1, delimiter=',')
np.savetxt('y_rf_16_2a.csv', y_rf1, delimiter=',')

os.chdir('..')

# 1-13a

os.chdir('1_13a')
# shapefile filename here
shapefile = gpd.read_file('1_13a_train_poly.shp')

# dummy CRS
shapefile.set_crs(epsg=4326)

# extract the geometry in GeoJSON format

shapefiles = [0]*8

# 'Class' is the vector attribute that contains the integer mineral class
for i in range(1,9):
    shapefiles[i-1] = shapefile[shapefile["Class"] == i]

# This extracts values from the .tif file based on the training polygon geometries -- clunky: one loop for each
# elemental intensity raster

values_Ca = [0]*8
for i in range(len(shapefiles)):
    geoms = shapefiles[i].geometry.values # list of shapely geometries
# transform to GeJSON format
    for j in range(len(geoms)):
        geoms1 = [mapping(geoms[j])]
# extract the raster values values within the polygon -- assign same dummy CRS
        with rasterio.open('Ca_7.tif', crs='EPSG:4326') as src:
            out_images, out_transform = mask(src, geoms1, crop=True)
        no_data=src.nodata
        data = out_images
        values1 = np.extract(data != no_data, data)
        values_Ca[i] = np.append(values_Ca[i], values1)

test2 = [0]*8
for i in range(len(values_Ca)):
    test2[i] = values_Ca[i][1:]
test3 = np.hstack(test2)
Ca_vals = test3

values_Na = [0]*8
for i in range(len(shapefiles)):
    geoms = shapefiles[i].geometry.values # list of shapely geometries
# transform to GeJSON format
    for j in range(len(geoms)):
        geoms1 = [mapping(geoms[j])]
# extract the raster values values within the polygon -- assign same dummy CRS
        with rasterio.open('Na_7.tif', crs='EPSG:4326') as src:
            out_images, out_transform = mask(src, geoms1, crop=True)
        no_data=src.nodata
        data = out_images
        values1 = np.extract(data != no_data, data)
        values_Na[i] = np.append(values_Na[i], values1)

test2 = [0]*8
for i in range(len(values_Na)):
    test2[i] = values_Na[i][1:]
test3 = np.hstack(test2)
Na_vals = test3

values_Mg = [0]*8
for i in range(len(shapefiles)):
    geoms = shapefiles[i].geometry.values # list of shapely geometries
# transform to GeJSON format
    for j in range(len(geoms)):
        geoms1 = [mapping(geoms[j])]
# extract the raster values values within the polygon -- assign same dummy CRS
        with rasterio.open('Mg_7.tif', crs='EPSG:4326') as src:
            out_images, out_transform = mask(src, geoms1, crop=True)
        no_data=src.nodata
        data = out_images
        values1 = np.extract(data != no_data, data)
        values_Mg[i] = np.append(values_Mg[i], values1)

test2 = [0]*8
for i in range(len(values_Mg)):
    test2[i] = values_Mg[i][1:]
test3 = np.hstack(test2)
Mg_vals = test3

values_K = [0]*8
for i in range(len(shapefiles)):
    geoms = shapefiles[i].geometry.values # list of shapely geometries
# transform to GeJSON format
    for j in range(len(geoms)):
        geoms1 = [mapping(geoms[j])]
# extract the raster values values within the polygon -- assign same dummy CRS
        with rasterio.open('K_7.tif', crs='EPSG:4326') as src:
            out_images, out_transform = mask(src, geoms1, crop=True)
        no_data=src.nodata
        data = out_images
        values1 = np.extract(data != no_data, data)
        values_K[i] = np.append(values_K[i], values1)

test2 = [0]*8
for i in range(len(values_K)):
    test2[i] = values_K[i][1:]
test3 = np.hstack(test2)
K_vals = test3

values_Fe = [0]*8
for i in range(len(shapefiles)):
    geoms = shapefiles[i].geometry.values # list of shapely geometries
# transform to GeJSON format
    for j in range(len(geoms)):
        geoms1 = [mapping(geoms[j])]
# extract the raster values values within the polygon -- assign same dummy CRS
        with rasterio.open('Fe_7.tif', crs='EPSG:4326') as src:
            out_images, out_transform = mask(src, geoms1, crop=True)
        no_data=src.nodata
        data = out_images
        values1 = np.extract(data != no_data, data)
        values_Fe[i] = np.append(values_Fe[i], values1)

test2 = [0]*8
for i in range(len(values_Fe)):
    test2[i] = values_Fe[i][1:]
test3 = np.hstack(test2)
Fe_vals = test3

values_Ti = [0]*8
for i in range(len(shapefiles)):
    geoms = shapefiles[i].geometry.values # list of shapely geometries
# transform to GeJSON format
    for j in range(len(geoms)):
        geoms1 = [mapping(geoms[j])]
# extract the raster values values within the polygon -- assign same dummy CRS
        with rasterio.open('Ti_7.tif', crs='EPSG:4326') as src:
            out_images, out_transform = mask(src, geoms1, crop=True)
        no_data=src.nodata
        data = out_images
        values1 = np.extract(data != no_data, data)
        values_Ti[i] = np.append(values_Ti[i], values1)


test2 = [0]*8
for i in range(len(values_Ti)):
    test2[i] = values_Ti[i][1:]
test3 = np.hstack(test2)
Ti_vals = test3


# only needs run once -- Can use any set of values; using Ti here
test2 = [0]*8
for i in range(len(values_Ti)):
    test = values_Ti[i][1:]
    test1 = np.zeros_like(test)+i+1
    test2 = np.append(test2,test1)

test3 = test2[test2 > 0]
Ti_mins = test3


X_rf1 = np.vstack((Ca_vals, Na_vals, Mg_vals, Fe_vals, K_vals, Ti_vals))

X_rf1 = X_rf1.T
y_rf1 = Ti_mins


np.savetxt('x_rf_1_13a.csv', X_rf1, delimiter=',')
np.savetxt('y_rf_1_13a.csv', y_rf1, delimiter=',')

os.chdir('..')

# 6-3a

os.chdir('6_3a')

shapefile = gpd.read_file('6_3a_train_poly.shp')

# dummy CRS
shapefile.set_crs(epsg=4326)

# extract the geometry in GeoJSON format

shapefiles = [0]*8

# 'Class' is the vector attribute that contains the integer mineral class
for i in range(1,9):
    shapefiles[i-1] = shapefile[shapefile["classvalue"] == i]

# This extracts values from the .tif file based on the training polygon geometries -- clunky: one loop for each
# elemental intensity raster

values_Ca = [0]*8
for i in range(len(shapefiles)):
    geoms = shapefiles[i].geometry.values # list of shapely geometries
# transform to GeJSON format
    for j in range(len(geoms)):
        geoms1 = [mapping(geoms[j])]
# extract the raster values values within the polygon -- assign same dummy CRS
        with rasterio.open('Ca_7.tif', crs='EPSG:4326') as src:
            out_images, out_transform = mask(src, geoms1, crop=True)
        no_data=src.nodata
        data = out_images
        values1 = np.extract(data != no_data, data)
        values_Ca[i] = np.append(values_Ca[i], values1)

test2 = [0]*8
for i in range(len(values_Ca)):
    test2[i] = values_Ca[i][1:]
test3 = np.hstack(test2)
Ca_vals = test3

values_Na = [0]*8
for i in range(len(shapefiles)):
    geoms = shapefiles[i].geometry.values # list of shapely geometries
# transform to GeJSON format
    for j in range(len(geoms)):
        geoms1 = [mapping(geoms[j])]
# extract the raster values values within the polygon -- assign same dummy CRS
        with rasterio.open('Na_7.tif', crs='EPSG:4326') as src:
            out_images, out_transform = mask(src, geoms1, crop=True)
        no_data=src.nodata
        data = out_images
        values1 = np.extract(data != no_data, data)
        values_Na[i] = np.append(values_Na[i], values1)

test2 = [0]*8
for i in range(len(values_Na)):
    test2[i] = values_Na[i][1:]
test3 = np.hstack(test2)
Na_vals = test3

values_Mg = [0]*8
for i in range(len(shapefiles)):
    geoms = shapefiles[i].geometry.values # list of shapely geometries
# transform to GeJSON format
    for j in range(len(geoms)):
        geoms1 = [mapping(geoms[j])]
# extract the raster values values within the polygon -- assign same dummy CRS
        with rasterio.open('Mg_7.tif', crs='EPSG:4326') as src:
            out_images, out_transform = mask(src, geoms1, crop=True)
        no_data=src.nodata
        data = out_images
        values1 = np.extract(data != no_data, data)
        values_Mg[i] = np.append(values_Mg[i], values1)

test2 = [0]*8
for i in range(len(values_Mg)):
    test2[i] = values_Mg[i][1:]
test3 = np.hstack(test2)
Mg_vals = test3

values_K = [0]*8
for i in range(len(shapefiles)):
    geoms = shapefiles[i].geometry.values # list of shapely geometries
# transform to GeJSON format
    for j in range(len(geoms)):
        geoms1 = [mapping(geoms[j])]
# extract the raster values values within the polygon -- assign same dummy CRS
        with rasterio.open('K_7.tif', crs='EPSG:4326') as src:
            out_images, out_transform = mask(src, geoms1, crop=True)
        no_data=src.nodata
        data = out_images
        values1 = np.extract(data != no_data, data)
        values_K[i] = np.append(values_K[i], values1)

test2 = [0]*8
for i in range(len(values_K)):
    test2[i] = values_K[i][1:]
test3 = np.hstack(test2)
K_vals = test3

values_Fe = [0]*8
for i in range(len(shapefiles)):
    geoms = shapefiles[i].geometry.values # list of shapely geometries
# transform to GeJSON format
    for j in range(len(geoms)):
        geoms1 = [mapping(geoms[j])]
# extract the raster values values within the polygon -- assign same dummy CRS
        with rasterio.open('Fe_7.tif', crs='EPSG:4326') as src:
            out_images, out_transform = mask(src, geoms1, crop=True)
        no_data=src.nodata
        data = out_images
        values1 = np.extract(data != no_data, data)
        values_Fe[i] = np.append(values_Fe[i], values1)

test2 = [0]*8
for i in range(len(values_Fe)):
    test2[i] = values_Fe[i][1:]
test3 = np.hstack(test2)
Fe_vals = test3

values_Ti = [0]*8
for i in range(len(shapefiles)):
    geoms = shapefiles[i].geometry.values # list of shapely geometries
# transform to GeJSON format
    for j in range(len(geoms)):
        geoms1 = [mapping(geoms[j])]
# extract the raster values values within the polygon -- assign same dummy CRS
        with rasterio.open('Ti_7.tif', crs='EPSG:4326') as src:
            out_images, out_transform = mask(src, geoms1, crop=True)
        no_data=src.nodata
        data = out_images
        values1 = np.extract(data != no_data, data)
        values_Ti[i] = np.append(values_Ti[i], values1)


test2 = [0]*8
for i in range(len(values_Ti)):
    test2[i] = values_Ti[i][1:]
test3 = np.hstack(test2)
Ti_vals = test3


# only needs run once -- Can use any set of values; using Ti here
test2 = [0]*8
for i in range(len(values_Ti)):
    test = values_Ti[i][1:]
    test1 = np.zeros_like(test)+i+1
    test2 = np.append(test2,test1)

test3 = test2[test2 > 0]
Ti_mins = test3


X_rf1 = np.vstack((Ca_vals, Na_vals, Mg_vals, Fe_vals, K_vals, Ti_vals))

X_rf1 = X_rf1.T
y_rf1 = Ti_mins


np.savetxt('x_rf_6_3a.csv', X_rf1, delimiter=',')
np.savetxt('y_rf_6_3a.csv', y_rf1, delimiter=',')

os.chdir('..')















