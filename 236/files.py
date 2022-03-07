from pathlib import PosixPath, Path
import difflib as dl


def get_matching_files(directory: PosixPath, filter_str: str) -> list:
   """Get all file names in "directory" and (case insensitive) match the ones
      that exactly match "filter_str"

      In case there is no exact match, return closely matching files.
      If there are no closely matching files either, return an empty list.
      (Return file names, not full paths).

      For example:

      d = Path('.')
      files in dir: bite1 test output

      get_matching_files(d, 'bite1') => ['bite1']
      get_matching_files(d, 'Bite') => ['bite1']
      get_matching_files(d, 'pybites') => ['bite1']
      get_matching_files(d, 'test') => ['test']
      get_matching_files(d, 'test2') => ['test']
      get_matching_files(d, 'output') => ['output']
      get_matching_files(d, 'o$tput') => ['output']
      get_matching_files(d, 'nonsense') => []
   """
   match = []
   for file in directory.iterdir():
      name = file.name
      if name == filter_str:
         match.append(name)
      elif dl.get_close_matches(name, [filter_str], n=1):
         match.append(name)

   return match


# if __name__ == "__main__":
#    print(get_matching_files(Path('/com.docker.devenvironments.code/236/files'), 'bite1'))