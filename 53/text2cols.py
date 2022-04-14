import re
import textwrap
from itertools import zip_longest

COL_WIDTH = 20


def text_to_columns(text):
   """Split text (input arg) to columns, the amount of double
      newlines (\n\n) in text determines the amount of columns.
      Return a string with the column output like:
      line1\nline2\nline3\n ... etc ...
      See also the tests for more info."""
   double_newlines_count = len(re.findall("\n\n", text))

   wrapper = textwrap.TextWrapper(width=COL_WIDTH)
   
   if double_newlines_count == 0:
      # one column
      text_list = wrapper.wrap(text=text)
      return "\n".join(text_list)

   else:
      # multiple columns
      text_lists = re.split("\n\n", text)
      print(text_lists)

      longest_index = 0
      for i in range(len(text_lists)):
         text_lists[i] = wrapper.wrap(text=text_lists[i].strip())

         if len(text_lists[i]) > longest_index:
            longest_index = len(text_lists[i])

      count = 0
      column_output = []
      while count < longest_index:

         line_across_columns = []
         for text_list in zip(text_lists):
            try:
               line = text_list[0][count]
               line_across_columns.append(line)
            except:
               pass
         
         column_output.append(" ".join(line_across_columns))
         count += 1
      return "\n".join(column_output)




# if __name__ == "__main__":
#    text4 = """My house is small but cosy."""
#    text1 = """My house is small but cosy.

#    It has a white kitchen and an empty fridge."""
#    text2 = """My house is small but cosy.

#    It has a white kitchen and an empty fridge.

#    I have a very comfortable couch, people love to sit on it."""
#    text_to_columns(text1)