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
          "training_hdf": "training.hdf",
          "training_kchk1": "Ktr",
          "training_ychk": "ytr",
          "training_number" : 100,
          "training_conf": "mlconf.py",
          "training_mls": "BEST",
          "training_key": "tree",
          "output": "test_tree_800_0"}


grid = {"width": 800,
        "height": 800,
        "overlap": 30,
        "debug": False}
grid.update(**kwargs)


TEST = [(100, 100),
        (200, 100),
        (400, 100),
        (800, 100),
        ]

RES = 0.25

NAME = "test_tree_{grid}x{grid}m_with_{overlap}m"

EXPORT = """
paper a4
  end
scale {scale}
raster {name}
grid {grid}
  color black
  numbers 1 black
  width 2
  end
text 50% -7% grid: {width}x{height}m  overlap: {overlap}m
  fontsize 16
  end
"""

"""
ps.map input=- output=test.ps -r --o << EOF
paper a4
  end
scale 1:15
raster test_tree_100_0
grid 25
  color black
  numbers 1 black
  width 2
end
text 50% -7% grid:{width}x{height}m overlap={overlap}
  fontsize 16
  end
EOF
"""


#import ipdb; ipdb.set_trace()
psm = Module('ps.map', input='-', flags='r', overwrite=True, output='ps',
             run_=False)
for grd, ovl in TEST:
    grid['width'] = grd
    grid['height'] = grd
    grid['overlap'] = ovl
    grid['output'] = NAME.format(grid=int(grd * RES),
                                 overlap=int(ovl * RES))
    g = GridModule(**grid)
    g.run()
    psm(output=grid['output'] + '.ps',
        stdin_=EXPORT.format(scale='1:15',
                             name=grid['output'],
                             grid=grd,
                             width=int(grd * RES),
                             height=int(grd * RES),
                             overlap=int(ovl * RES)),
        run_=True)

#n = node.Nodes()


