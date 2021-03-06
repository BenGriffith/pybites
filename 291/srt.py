from datetime import datetime, timedelta
from typing import List


def get_srt_section_ids(text: str) -> List[int]:
   """Parse a caption (srt) text passed in and return a
      list of section numbers ordered descending by
      highest speech speed
      (= ratio of "time past:characters spoken")

      e.g. this section:

      1
      00:00:00,000 --> 00:00:01,000
      let's code

      (10 chars in 1 second)

      has a higher ratio then:

      2
      00:00:00,000 --> 00:00:03,000
      code

      (4 chars in 3 seconds)

      You can ignore milliseconds for this exercise.
   """
   sections_raw = [word.strip() for word in text.strip().split("\n") if word != ""]
   sections_clean = [sections_raw[i-3:i] for i in range(3, len(sections_raw) +1, 3)]
   sections_ranking = {}

   for section in sections_clean:
      start, stop = section[1].split(" --> ")
      total_chars = len(section[2])
      start_h, start_m, start_s = start.split(":")
      stop_h, stop_m, stop_s = stop.split(":")
      start = timedelta(hours=int(start_h), minutes=int(start_m), seconds=int(start_s[:2]))
      stop = timedelta(hours=int(stop_h), minutes=int(stop_m), seconds=int(stop_s[:2]))
      time_delta = stop - start
      sections_ranking[int(section[0])] = total_chars / time_delta.seconds

   return sorted(sections_ranking, key=sections_ranking.get, reverse=True)


if __name__ == "__main__":
   text1 = """
   1
   00:00:00,498 --> 00:00:02,827
   Beautiful is better than ugly.

   2
   00:00:02,827 --> 00:00:06,383
   Explicit is better than implicit.

   3
   00:00:06,383 --> 00:00:09,427
   Simple is better than complex.
   """

   text2 = """
   18
   00:01:12,100 --> 00:01:17,230
   If you want a bit more minimalistic view, you can actually hide the sidebar.

   19
   00:01:18,200 --> 00:01:19,500
   If you go to Settings

   20
   00:01:23,000 --> 00:01:26,150
   scroll down to 'Focus Mode'.

   21
   00:01:28,200 --> 00:01:35,180
   You can actually hide the sidebar and have only the description and the code editor.
   """

   print(get_srt_section_ids(text1))