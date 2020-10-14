# birthdaywishes

This is a ```PYTHON``` program which can be used to send birthday wishes to your friends and families without actually opening Gmail and typing the wishes.

### Installation and Prerequisites
The user can send mails only if their Gmail account provides access to third party apps. 

**Caution:** The user is risking the security of their Gmail account. It is advised to use a temporary acocunt for the purpose.

To activate Less Security Mode go to [Google Account settings](https://myaccount.google.com/lesssecureapps) >> Login with you id and password >> Under the ```Security Tab``` go to Less secure app access >> Turn it **ON**

**Install the supporting modules:**

```sh
pip install pandas
pip install xlrd
```

**Privacy while entering the Gmail password**

The program contains ```getpass``` library which hides the characters while you enter your password. This utility works well if the ```main.py``` script is executed in the terminal. However ```Pycharm```'s default settings does not hide the characters as expected. An error shown below will be popped up
```sh
Warning: Password input may be echoed.
```

To use this utility in ```PyCharm``` >> Click on **Edit Configurations** on the left of the **RUN** button and check **Emulate Terminal in Output Console**.

### How to use the program
* An ```Excel Spreadsheet``` has been provided along where you can get the basic template
* Open the ```Excel Spreadsheet``` and make necessary changes according to you convinience
* Run the ```main.py``` script using any python editor or terminal.

### Todos

 - Make the program fully automatic
 - Add images to the mail being sent
 - Make the excell sheet self updating to avoid multiple wishes to the same person in the same year
 
 
