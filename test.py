import datetime
import calendar

# Get today's date
today = datetime.date.today()

# 1. Days in the running month
_, days_in_month = calendar.monthrange(today.year, today.month)
print(f"Days in the running month: {days_in_month}")

# 2. Days in the running week
# Get the start of the week (Monday) and the end of the week (Sunday)
start_of_week = today - datetime.timedelta(days=today.weekday())  # Monday
end_of_week = start_of_week + datetime.timedelta(days=6)  # Sunday

print(f"Start of the week: {start_of_week}")
print(f"End of the week: {end_of_week}")
print(f"Days in the running week: {7}")  # Always 7 days in a week

# Additional Info (Optional): Calculate days elapsed and remaining
days_elapsed_in_month = today.day
days_remaining_in_month = days_in_month - today.day
print(f"Days elapsed in the running month: {days_elapsed_in_month}")
print(f"Days remaining in the running month: {days_remaining_in_month}")

days_elapsed_in_week = (today - start_of_week).days + 1
days_remaining_in_week = 7 - days_elapsed_in_week
print(f"Days elapsed in the running week: {days_elapsed_in_week}")
print(f"Days remaining in the running week: {days_remaining_in_week}")
