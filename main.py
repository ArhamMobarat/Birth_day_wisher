
import pandas
import datetime as dt
import os
import random
import smtplib
MY_EMAIL = os.environ["EMAIL"]
MY_PASSWORD = os.environ["PASSWORD"]

birth_day_data = pandas.read_csv("birthdays.csv")
birthday_list_dict =  birth_day_data.to_dict(orient="records")

now = dt.datetime.now()
month = now.month
day = now.day

for person in birthday_list_dict:
    if person["month"] == month and person["day"] == day:
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
            letter_template = letter.read()
            final_letter = letter_template.replace("[NAME]", person["name"])
            if final_letter is not None:
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=person["email"],
                        msg=f"Subject: HAPPY BIRTHDAY\n\n {final_letter}"
                    )