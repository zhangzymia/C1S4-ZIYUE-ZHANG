from datetime import datetime

def date_passed(todays_date, scheduled_date):
    # Function to convert the date format
    def convert_date(date_str):
        for suffix in ['th', 'rd', 'nd', 'st']:
            if suffix in date_str:
                date_str = date_str.replace(suffix, '')
                break
        return datetime.strptime(date_str, '%d %B')

    # Convert both dates
    todays_date = convert_date(todays_date)
    scheduled_date = convert_date(scheduled_date)

    # Compare and print the result
    if todays_date > scheduled_date:
        print("The scheduled date has passed.")
    elif todays_date < scheduled_date:
        print("The scheduled date is yet to pass.")
    else:
        print("The scheduled date is today.")

# Test cases
date_passed('26th March', '25th March') # should indicate that the scheduled date has passed.
date_passed('26th March', '26th March') # should indicate that the scheduled date is today.
date_passed('26th March', '27th March') # should indicate that the scheduled date is yet to pass.
