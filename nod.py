#!/usr/bin/env python
# -- coding: utf-8 --
import sys

if sys.version[:3] != '2.7':
        raise SystemError

PBS = """#!/bin/csh
#-------------------------------
#PBS -l nodes=1:ppn=8
#PBS -o work.log
#PBS -m abe
#PBS -M pizamb48@ceh.ac.uk
#PBS -q small
#-------------------------------

#
# SET GRASS ENVIRONMENT VARIABLES
#
source ~/.csh_profile
echo "print GISRC:"
echo $GISRC

set RUNDIR = "/home/pizamb48/work/grass/20130913"
cd $RUNDIR


echo "current working directory: " `pwd`
echo "-------------------------------------------------------------------"
echo "Job started on" `date`
echo "-------------------------------------------------------------------"
python {script}
echo "-------------------------------------------------------------------"
echo "Job ended on" `date`
echo "-------------------------------------------------------------------"

"""


from grass.pygrass.modules.grid import GridModule
from grass.pygrass.modules.grid import Nodes
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

slp = {'elevation': 'elevation',
       'slope': 'slope',
       'aspect': 'aspect',
       'overwrite': True}

grid = {"width": 1000,
        "height": 1000,
        "overlap": 100,
        "debug": True,
        "move": "/tmp/pizamb48",
        "log": True}

grid.update(**kwargs)
#grid.update(**slp)

node = {"nwidth": 1000,
        "nheight": 1000,
        "pbs_template": PBS}

node.update(**grid)

#md = GridModule('ml.nemesis', **grid)
#md = GridModule('r.slope.aspect', **grid)
#md.run(clean=False)

nd = Nodes("ml.nemesis", **node)
import ipdb; ipdb.set_trace()
nd.populate()
que = nd.queue[0]
que.create()
que.run()

