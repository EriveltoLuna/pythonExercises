import calendar
from pathlib import Path

month_names = list(calendar.month_name[1:])
days = list(range(1,32))

for i, month in enumerate(month_names, start=1):
    if i == 1 or i ==3 or i ==5 or i ==7 or i ==8 or i ==10 or i ==12:
        for day in days:
            Path(f'2024/{i}.{month}/{day}').mkdir(parents=True, exist_ok=True)
    elif i == 2:
        for counter, day in enumerate(days, start=1):
            if counter <= 28:
                Path(f'2024/{i}.{month}/{day}').mkdir(parents=True, exist_ok=True)
    else:
        for counter, day in enumerate(days, start=1):
            if counter <=30:
                Path(f'2024/{i}.{month}/{day}').mkdir(parents=True, exist_ok=True)