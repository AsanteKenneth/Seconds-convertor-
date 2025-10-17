total_seconds=int(input("enter the number of the seconds you want "))
days= total_seconds//86400
days_remainder=total_seconds%86400
hours=days_remainder//3600
hours_remainder=days_remainder%3600
minutes=hours_remainder//60
seconds=hours_remainder%60

if total_seconds >=86400:
    print(f"{total_seconds} is equal to {days} day(s), {hours} hours(s), {minutes} minute(s), {seconds} second(s)")
elif total_seconds >=3600:
    print(f"{total_seconds} is equal to {hours} hours(s), {minutes} minute(s), {seconds} second(s)")
elif total_seconds >=60:
    print(f"{total_seconds} is equal to {minutes} minute(s), {seconds} second(s)")
elif total_seconds <60:
    print(f"{total_seconds} is equal to {seconds} second(s)")     