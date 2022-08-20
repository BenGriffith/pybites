def get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    calendar_split = calendar_output.strip().split(" ")
    calendar_rows = []
    calendar_row = []

    for calendar_element in calendar_split:
        
        if calendar_element == "":
            continue
        
        if calendar_element == calendar_split[-1]:
            calendar_rows.append(calendar_row)
    
        if calendar_element.find("\n") > 0: 
            previous_row, current_row = calendar_element.split("\n")

            calendar_row.append(previous_row)
            calendar_row = [element for element in calendar_row if element != ""]
            if len(calendar_row) != 7:
                for i in range((7 - len(calendar_row))):
                    calendar_row.insert(0, None)

            calendar_rows.append(calendar_row)
            
            calendar_row = []
            calendar_row.append(current_row)
        else:
            calendar_row.append(calendar_element)

    weekdays = {}
    calendar_rows_weekdays = calendar_rows[1]
    for i in range(len(calendar_rows)):
        if i in [0, 1]:
            continue

        for day, num in zip(calendar_rows_weekdays, calendar_rows[i]):

            if num == None:
                continue

            if num not in weekdays:
                weekdays[int(num)] = day

    return weekdays