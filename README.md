tilepie 🍕
==========

Simple `.mbtiles` processor for python. Built with the [QA Tiles](https://osmlab.github.io/osm-qa-tiles/) in mind.

Based on the map/reduce/end structure in [@mapbox/tilereduce](https://github.com/mapbox/tile-reduce). Tiles are read from the `mbtiles` container and passed to a worker pool as asynchronous jobs that can run concurrently.

Docs
----
The main function is `tilereduce(options, map_function=map_function, callback=callback, error_callback=error_callback, done=done)`:

**options**

A dictionary with the following keys:
- source: a path to an mbtiles
- bbox: a bounding box limiting the tiles to read
- zoom: the zoom level to read from
- args: an optional dictionary which is passed to each worker

**map_function: (x, y, z, data) -> any**

A function that run on each tile asynchronously.
x, y and z specify the tile coordinates, and data is the tile contents.
The mapfunc takes the tile data and should return a value.

**callback: (any) -> void**

A function called with the return value of `map_function`.

**error_callback: (any) -> void**

A function called with an exception instance if one occurs in the worker.

**done: () -> void**

A function called at the end of all jobs.

Installing
----------
You can install `tilepie` from [PyPi](https://pypi.python.org/pypi/tilepie) ✨

```sh
pip install tilepie
```

Example
-------
```python
from tilepie import tilereduce
import mapbox_vector_tile

total_count = 0

## Define a mapper function that operates on each tile
def mapper(x, y, z, data):
  if data is None:
          return 0

  tile = mapbox_vector_tile.decode(data)

  count = 0
  if (tile['osm']['features']):
    count = len(tile['osm']['features'])

  return count

## Define a callback when each tile finishes
def on_tile_done(count):
  global total_count
  total_count += count

## Define a function that runs at the end of all jobs
def on_end():
  global total_count
  print total_count

## Log errors
def on_error(e):
  print(e)

# Call tilereduce
# This is using lebanon.mbtiles from the QA Tiles
tilereduce(
  {
    'zoom': 12,
    'source': '~/data/lebanon.mbtiles',
    'bbox': (35.1260526873, 33.0890400254, 36.6117501157, 34.6449140488)
  },
  map_function=mapper,
  callback=on_tile_done,
  error_callback=on_error,
  done=on_end
)
```

Acknowledgements & previous work
--------------------------------
- [mapbox/tilereduce](https://github.com/mapbox/tile-reduce)
- [jwass/tile-reduce-py](https://github.com/jwass/tile-reduce-py/)
- [makinacorpus/landez](https://github.com/makinacorpus/landez/)

License
----------
[MIT © Marc Farra](LICENSE.md) unless otherwise specified
