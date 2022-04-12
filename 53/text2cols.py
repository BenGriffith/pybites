import re
from columnar import columnar

COL_WIDTH = 20


def text_to_columns(text):
   """Split text (input arg) to columns, the amount of double
      newlines (\n\n) in text determines the amount of columns.
      Return a string with the column output like:
      line1\nline2\nline3\n ... etc ...
      See also the tests for more info."""
   double_newlines_count = len(re.findall("\n\n", text))
   print(double_newlines_count)

   if double_newlines_count == 0:
      # one column
      table = columnar(headers=None, data=[text.split(" ")], no_borders=True, justify='l', max_column_width=COL_WIDTH)
      print(table)





if __name__ == "__main__":
   text4 = """My house is small but cosy."""
   text1 = """My house is small but cosy.

   It has a white kitchen and an empty fridge."""
   text2 = """My house is small but cosy.

   It has a white kitchen and an empty fridge.

   I have a very comfortable couch, people love to sit on it."""
   text_to_columns(text4)