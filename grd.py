#!/usr/bin/env python
# -- coding: utf-8 --
import sys

if sys.version[:3] != '2.7':
        raise SystemError


from grass.pygrass.modules import GridModule
from grass.pygrass.gis import Mapset

mapset = Mapset()

kwargs = {"group": "rgb",
          "rast": ['photo_r', 'photo_g', 'photo_b'],
          "hdf": "test.hdf",
          "seg_thresholds": [0.01,0.05],
          "seg_opts": "method=region_growing,similarity=euclidean,minsize=2",
          #"seg_name": "ortho_segs_l005",
          "data": "data",
          "datasum": "datasum",
          "training_hdf": "training.hdf",
          "training_kchk1": "Ktr",
          "training_kchk2": "Ktr2",
          "training_ychk": "ytr",
          "training_number" : 130,
          "training_conf": "mlconf.py",
          "training_mls": "BEST",
          "training_key": "tree",
          "transform": "standardize",
          "output": "tree_rm_small2",
          "area_size": 20,
          "visible": ['test', 'PERMANENT'],
          #"flags": 'r',
          "overwrite": True}

grid = {"width": 5000,
        "height": 5000,
        "overlap": 400,
        "debug": False}
grid.update(**kwargs)

md = GridModule('ml.nemesis', **grid)
md.run(clean=False)

