from tilepie import tilereduce
import mapbox_vector_tile
import sys

## Example uses OSM QA tiles for lebanon
if __name__ == '__main__':
  total_count = 0

  def mapper(x, y, z, data, args):
    if data is None:
            return 0

    tile = mapbox_vector_tile.decode(data)

    count = 0
    if (tile['osm']['features']):
      count = len(tile['osm']['features'])
    return count

  def on_tile_done(count):
    global total_count
    total_count += count

  def on_error(e):
      print(e)

  def on_end():
    global total_count
    print(total_count)

  # Call tilereduce
  tilereduce(
    {
      'zoom': 12,
      'source': sys.argv[1],
      'bbox': (35.1260526873, 33.0890400254, 36.6117501157, 34.6449140488)
    },
    map_function=mapper,
    callback=on_tile_done,
    error_callback=on_error,
    done=on_end
  )
