from collections import namedtuple
from datetime import date

import pandas as pd

DATA_FILE = "https://bites-data.s3.us-east-2.amazonaws.com/weather-ann-arbor.csv"
STATION = namedtuple("Station", "ID Date Value")


def high_low_record_breakers_for_2015():
   """Extract the high and low record breaking temperatures for 2015

   The expected value will be a tuple with the highest and lowest record
   breaking temperatures for 2015 as compared to the temperature data
   provided.

   NOTE:
   The date values should not have any timestamps, should be a
   datetime.date() object. The temperatures in the dataset are in tenths
   of degrees Celsius, so you must divide them by 10

   Possible way to tackle this challenge:

   1. Create a DataFrame from the DATA_FILE dataset.

   2. Manipulate the data to extract the following:
      * Extract highest temperatures for each day / station pair between 2005-2015
      * Extract lowest temperatures for each day / station  between 2005-2015
      * Remove February 29th from the dataset to work with only 365 days

   3. Separate data into two separate DataFrames:
      * high/low temperatures between 2005-2014
      * high/low temperatures for 2015

   4. Iterate over the 2005-2014 data and compare to the 2015 data:
      * For any temperature that is higher/lower in 2015 extract ID,
        Date, Value
         
   5. From the record breakers in 2015, extract the high/low of all the
      temperatures
      * Return those as STATION namedtuples, (high_2015, low_2015)
   """
   ann_arbor = pd.read_csv(DATA_FILE)

   ann_arbor["Date"] = pd.to_datetime(ann_arbor["Date"])
   ann_arbor["Data_Value"] = ann_arbor["Data_Value"] / 10
   ann_arbor = ann_arbor.drop(ann_arbor[ann_arbor["Date"].dt.strftime("%m%d") == "0229"].index)


   ann_arbor_2014 = ann_arbor[ann_arbor["Date"].dt.year < 2015]
   ann_arbor_2014_max = ann_arbor_2014[ann_arbor_2014.Element == "TMAX"]
   ann_arbor_2014_min = ann_arbor_2014[ann_arbor_2014.Element == "TMIN"]

   ann_arbor_2015 = ann_arbor[ann_arbor["Date"].dt.year == 2015]
   ann_arbor_2015_max = {f"{value.get('ID')}_{value.get('Date').strftime('%m%d')}": value.get("Data_Value") for value in ann_arbor_2015[ann_arbor_2015.Element == "TMAX"].to_dict("index").values()}
   ann_arbor_2015_min = {f"{value.get('ID')}_{value.get('Date').strftime('%m%d')}": value.get("Data_Value") for value in ann_arbor_2015[ann_arbor_2015.Element == "TMIN"].to_dict("index").values()}

   max_temps = {}
   min_temps = {}

   for row in ann_arbor_2014_max.itertuples():
   
      key = f"{row.ID}_{row.Date.strftime('%m%d')}"

      try:
         max_2015_temp = ann_arbor_2015_max[key]
      except KeyError:
         pass
      else:
         if max_2015_temp > row.Data_Value:
            if key not in max_temps:
               max_temps[key] = max_2015_temp
      
   high_temp = sorted(max_temps.items(), key=lambda item: item[1], reverse=True)[0]
   station, high_temp_date = high_temp[0].split("_")
   high_station = STATION(station, date(2015, int(high_temp_date[:2]), int(high_temp_date[2:])), high_temp[1])

   for row in ann_arbor_2014_min.itertuples():
   
      key = f"{row.ID}_{row.Date.strftime('%m%d')}"

      try:
         min_2015_temp = ann_arbor_2015_min[key]
      except KeyError:
         pass
      else:
         if min_2015_temp < row.Data_Value:
            if key not in min_temps:
               min_temps[key] = min_2015_temp
      
   low_temp = sorted(min_temps.items(), key=lambda item: item[1])[0]
   station, low_temp_date = low_temp[0].split("_")
   low_station = STATION(station, date(2015, int(low_temp_date[:2]), int(low_temp_date[2:])), low_temp[1])
   
   
   return (high_station, low_station)


if __name__ == "__main__":
   print(high_low_record_breakers_for_2015())