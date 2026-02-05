# Convert seconds in range from 1-86400 seconds to days, hours,minutes, and seconds

num_seconds = int(input('How many seconds?: '))
total_days = num_seconds // (24 * 3600)
num_seconds = num_seconds % (24 * 3600)
total_hours = num_seconds // 3600
num_seconds %= 3600

total_minutes = num_seconds // 60
num_seconds %= 60
total_seconds = num_seconds
print('There are', int(total_days),'days,', int(total_hours),'hours,',int(total_minutes),'minutes, and',int(total_seconds),'seconds.' )
