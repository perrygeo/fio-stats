# fio stats

Fiona plugin for summary statistics of GeoJSON feature properties

Install
```bash
$ pip install "git+https://github.com/perrygeo/fio-stats.git#egg=fio-stats"
```

Use with JSON output
```bash
$ fio dump ~/data/ballparks.geojson | fio stats
[
  ...
  {
    "attr": "Lat",
    "max": 53.61003,
    "n": 257,
    "min": -37.86,
    "mean": 34.694933016342425,
    "n_unique": 246
  },
  ...
  {
    "attr": "League",
    "max": null,
    "n": 257,
    "min": null,
    "mean": null,
    "n_unique": 23
  },
  ...
]
```

Or with tabular output
```
$ fio dump ~/data/ballparks.geojson | fio stats --table
attr           min      mean      max    n    n_unique
--------  --------  --------  -------  ---  ----------
Ballpark                               251         239
Class                                  257          12
Lat        -37.86    34.6949   53.61   257         246
League                                 257          23
Long      -122.498  -56.7517  153.033  257         245
Team                                   257         240
```

