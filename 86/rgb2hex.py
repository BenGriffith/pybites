def rgb_to_hex(rgb):
   """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
      boundaries (0, 255) and returns its converted hex, for example:
      Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
   red, green, blue = rgb
   values = range(0, 256)
   if red not in values or green not in values or blue not in values:
      raise ValueError
   return "#{:02X}{:02X}{:02X}".format(red, green, blue)