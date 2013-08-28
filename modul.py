#!/usr/bin/env python
# -- coding: utf-8 --
import sys

if sys.version[:3] != '2.7':
        raise SystemError


from grass.pygrass.modules import Module, GridModule


kwargs = {"cmd": "ml.nemesis",
          "group": "rgb",
          "rast": ['photo_r', 'photo_g', 'photo_b'],
          "hdf": "test.hdf",
          "seg_thresholds": [0.01,0.05],
          "seg_opts": "method=region_growing,similarity=euclidean,minsize=2",
          "seg_name": "ortho_segs_l005",
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
          "output": "tree_rm_small",
          "area_size": 20,
          "flags": 'r',
          "overwrite": True}

#md = Module('ml.nemesis')
Module(**kwargs)

