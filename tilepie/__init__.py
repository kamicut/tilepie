from landez import TileManager

def tilereduce (options, map, callback, done):
  tm = TilesManager(mbtiles_file=options.source)
  tiles = tm.tileslist(bbox=options.bbox, zoomlevels=[zoom])

  for tile in tiles:
    tilecontent = tm.tile(tile)
