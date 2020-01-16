#!/usr/local/bin/python3

from pyorbital.tlefile import Tle
from datetime import datetime
import os, sys
import argparse
import json
import shutil

SATELLITES = ["NOAA19", "METOP-A", "METOP-B", "METOP-C" ]

TLE_TRANSLATION = {
    "NOAA15":"NOAA 15",
    "NOAA18":"NOAA 18",
    "NOAA19":"NOAA 19",
    "NOAA20":"NOAA 20",
    "METOP-A":"METOP-A",
    "METOP-B":"METOP-B",
    "METOP-C":"METOP-C",
    "FENGYUN-2C":"FENGYUN 2C",
    "FENGYUN-2D":"FENGYUN 2D",
    "FENGYUN-3A":"FENGYUN 3A",
    "FENGYUN-3B":"FENGYUN 3B",
    "FENGYUN-3C":"FENGYUN 3C",
    "FENGYUN-3D":"FENGYUN 3D",
    "SUOMI-NPP": "SUOMI NPP",
    "NPP":"NPP",
    "JPSS-1":"JPSS-1"
    }

outdir = "/opt/aapp8/AAPP/orbelems/tle_db"


# Get time stamps for archive directory
time = datetime.utcnow().strftime("%Y%m%d")
month = datetime.utcnow().strftime("%Y_%m")

# Dir names
archive_dir = os.path.join(outdir, month)

# Create outdirs if they do not exist
os.makedirs(archive_dir, mode=0o775, exist_ok=True)

filename ="tle_{}.txt".format(time)

# Write to tmp dir first and then move the file
tmpfile = os.path.join("/tmp", filename)

# Write tle file for platforms of interest
with open(tmpfile, "w") as tle_file:
    for platform in SATELLITES:
        platform = TLE_TRANSLATION[platform]
        try:
            tle = Tle(platform)
            tle_file.write("\n".join([platform, tle.line1, tle.line2]) + "\n")
        except KeyError:
            print(platform)

shutil.copy(tmpfile, archive_dir)

