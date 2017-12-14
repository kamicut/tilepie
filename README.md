# tilepie 🍕

Simple `.mbtiles` processor for python. Built with the [QA Tiles](https://osmlab.github.io/osm-qa-tiles/) in mind.

Based on the map/reduce/end structure in [@mapbox/tilereduce](https://github.com/mapbox/tile-reduce)

## Example
```python
import tilereduce
import mapbox_vector_tile

total_count = 0

def mapper(x, y, z, data):
  if data is None:
          return 0

  tile = mapbox_vector_tile.decode(data)

  count = 0
  if (tile['osm']['features']):
    count = len(tile['osm']['features'])

  return count

def callback(count):
  global total_count
  total_count += count
  
def done():
  global total_count
  print total_count
  
# Call tilereduce
# This is using lebanon.mbtiles from the QA Tiles
tilereduce(
  {
    'zoom': 12,
    'source': sys.argv[1],
    'bbox': (35.1260526873, 33.0890400254, 36.6117501157, 34.6449140488)
  },
  mapper,
  callback,
  done
)
```

## Previous work (as far as I know)
- [mapbox/tilereduce](https://github.com/mapbox/tile-reduce)
- [jwass/tile-reduce-py](https://github.com/jwass/tile-reduce-py/)

## License
[MIT © Marc Farra](LICENSE.md)