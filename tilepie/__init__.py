import logging
import gzip
from io import BytesIO
import multiprocessing as mp

from tilepie.reader import MBTilesReader, ExtractionError

def uncompress(compressed):
  fileobj = BytesIO(compressed)
  gz = gzip.GzipFile(fileobj=fileobj, mode='r')
  uncompressed = gz.read()
  gz.close()

  return uncompressed

def tilereduce (options, map_function, callback, done, **kwargs):
  pool = mp.Pool()

  tm = MBTilesReader(options.get('source'))
  zoom = options.get('zoom')
  tiles = tm.tileslist(bbox=options.get('bbox'), zoomlevels=[zoom])
  args = options.get('args')

  for tile in tiles:
    try:
      tilecontent = uncompress(tm.tile(tile[0], tile[1], tile[2]))
      pool.apply_async(
          map_function, args=(tile[1], tile[2], tile[0], tilecontent, args),
          callback=callback,
          **kwargs
          )
    except ExtractionError:
      pass
  pool.close()
  pool.join()
  done()
