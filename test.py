from datetime import datetime
specific_date = datetime.now()
today_date = specific_date.strftime("%m/%d/%Y").lstrip('0').replace('/0', '/')

print(today_date)
