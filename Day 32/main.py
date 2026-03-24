from datetime import datetime
import random
import smtplib
import pandas

MY_EMAIL = "your_email@email.com"
MY_PASS = "your_pass"
YOUR_NAME = "your_name"


today = datetime.now()

today_tuple = (today.month, today.day)

# Rename to birthdays.csv
data = pandas.read_csv("birthdays_filled.csv")

birthdays_dict = {(data_row['month'], data_row['day']) : data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        replacements = {
            "[NAME]": birthday_person["name"],
            "[YOUR_NAME]" : YOUR_NAME
        }
        for old_str, new_str in replacements.items():
            contents = contents.replace(old_str, new_str)
      
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(
            from_add=MY_EMAIL,
            to_addrs=birthday_person['email'],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )

        
