from datetime import datetime
from dateutil.relativedelta import relativedelta

MAC1 = """
reboot    ~                         Wed Apr 10 22:39
reboot    ~                         Wed Mar 27 16:24
reboot    ~                         Wed Mar 27 15:01
reboot    ~                         Sun Mar  3 14:51
reboot    ~                         Sun Feb 17 11:36
reboot    ~                         Thu Jan 17 21:54
reboot    ~                         Mon Jan 14 09:25
"""


def calc_max_uptime(reboots):
   """Parse the passed in reboots output,
      extracting the datetimes.

      Calculate the highest uptime between reboots =
      highest diff between extracted reboot datetimes.
      Return a tuple of this max uptime in days (int) and the
      date (str) this record was hit.

      For the output above it would be (30, '2019-02-17'),
      but we use different outputs in the tests as well ...
   """
   reboots_parsed = [reboot.strip().lstrip("~").lstrip() for reboot in reboots.split("reboot") if reboot.strip() != ""]
   reboots_dates = [datetime.strptime(f"2022 {reboot}", "%Y %a %b %d %H:%M") for reboot in reboots_parsed]

   max_uptime = 0
   max_uptime_date = datetime(1900, 1, 1)
   for i in range(1, len(reboots_dates)):
      current_reboot = reboots_dates[i - 1]
      previous_reboot = reboots_dates[i]
      
      delta = relativedelta(current_reboot, previous_reboot)

      if delta.days > max_uptime:
         max_uptime = delta.days
         max_uptime_date = current_reboot.strftime("%Y-%m-%d")

   return (max_uptime, max_uptime_date)


if __name__ == "__main__":
   calc_max_uptime(MAC1)