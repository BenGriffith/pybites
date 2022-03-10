from contextlib import redirect_stdout
from io import StringIO
from multiprocessing.sharedctypes import Value
from types import BuiltinFunctionType


def get_len_help_text(builtin: BuiltinFunctionType) -> int:
   """Receives a builtin, and returns the length of its help text.
      You need to redirect stdout from the help builtin.
      If the the object passed in is not a builtin, raise a ValueError.
   """
   if not isinstance(builtin, BuiltinFunctionType):
      raise ValueError

   with StringIO() as help_text_length, redirect_stdout(help_text_length):
      help(builtin)
      output = help_text_length.getvalue()
   return len(output)

if __name__ == "__main__":
   get_len_help_text(len)