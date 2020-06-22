import pandas as pd
import datetime
import smtplib
import getpass

GMAIL_ID = input("Enter your Gmail id: ")
GMAIL_PASSWORD = getpass.getpass(prompt="Enter your password: ")


def send_email(to, sub, msg):
    # use of smtp to send emails through port 587. For more information visit [Gmail SMTP Docs](https://support.google.com/a/answer/176600?hl=en)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PASSWORD)
    s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")
    print(f"Email sent to {to} with title {sub} and message : {msg}")
    s.quit()


if __name__ == "__main__":
    df = pd.read_excel("data.xlsx")
    today = datetime.datetime.now().strftime("%d-%m")


    # iterating through the data sheet file row by row
    for index, item in df.iterrows():
        if item["Birthday"].strftime("%d-%m") == today
            send_email(item["Email"], "Birthday Greetings", item["Message"])
