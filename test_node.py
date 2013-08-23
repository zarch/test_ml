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
          "data": "data", 
          "datasum": "datasum",
          "training_hdf": "training_hdf", 
          "training_kchk1": "Ktr",
          "training_ychk": "ytr",
          "training_number" : 100,
          "training_conf": "mlconf.py",
          "training_mls": "BEST",
          "training_key": "tree",
          "output": "test_tree_100"}


grid = {"width": 1000,
        "height": 1000,
        "overlap": 10,
        "debug": True}
grid.update(**kwargs)


#Module(**kwargs)
#import ipdb; ipdb.set_trace()
g = GridModule(**grid)
g.run()

#n = node.Nodes()


