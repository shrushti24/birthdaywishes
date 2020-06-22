import pandas as pd
import datetime
import smtplib
import getpass
#from PIL import Image

#GMAIL_ID = "useasspam1@gmail.com"
#GMAIL_PASSWORD = "priyanshu123"
GMAIL_ID = input("Enter your email id: ")
GMAIL_PASSWORD = getpass.getpass(prompt="Enter your password: ")


def send_email(to, sub, msg):
    # print(f"Email sent to {to} with title {sub} and message : {msg}")
    #img = Image.open("birthday-wishes-facebook-friend.jpg")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PASSWORD)
    s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")
    print(f"Email sent to {to} with title {sub} and message : {msg}")
    s.quit()


if __name__ == "__main__":
    df = pd.read_excel("data.xlsx")
    # print(df)
    today = datetime.datetime.now().strftime("%d-%m")
    # print(today)

    # img = Image.open("birthday-wishes-facebook-friend.jpg")
    # img.show()

    # iterating through the data sheet file row by row
    for index, item in df.iterrows():
        # print(item["Birthday"].strftime("%d-%m"))
        if item["Birthday"].strftime("%d-%m") == today:
            # print(item["Name"], "Yes")
            send_email(item["Email"], "Birthday Greetings", item["Message"])
