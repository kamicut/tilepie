import landez
import logging
import gzip
import StringIO
import multiprocessing as mp

def uncompress(compressed):
  fileobj = StringIO.StringIO(compressed)
  gz = gzip.GzipFile(fileobj=fileobj, mode='r')
  uncompressed = gz.read(fileobj)
  gz.close()

  return uncompressed

def tilereduce (options, mapper, callback, done):
  pool = mp.Pool()

  tm = landez.TilesManager(mbtiles_file=options.get('source'))
  zoom = options.get('zoom')
  tiles = tm.tileslist(bbox=options.get('bbox'), zoomlevels=[zoom])

  for tile in tiles:
    try: 
      tilecontent = uncompress(tm.tile(tile))
      pool.apply_async(mapper, args=(tile[1], tile[2], tile[0], tilecontent), callback = callback)
    except landez.ExtractionError:
      pass
  pool.close()
  pool.join()
  done()