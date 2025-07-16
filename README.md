# Price Drop Notifier

A simple Python script that monitors the price of a product on Amazon and sends you an email notification when the price falls below a target threshold.

- Built with `requests`, `BeautifulSoup`, and Python’s built-in `smtplib`.
- Configurable for any Amazon product URL and any desired target price.
- Sends notification via Gmail SMTP (using an app-specific password).

## Features

- Fetches current price and product title from Amazon.
- Compares against your target price.
- Sends an email alert when the price drops in your favor.
- Runs as a standalone script—great for scheduling via Task Scheduler or cron.

## Prerequisites

- Python 3.7+  
- A Gmail account with an [App Password](https://support.google.com/accounts/answer/185833).  
- The following Python packages:
  
```bash
pip install -r requirements.txt


## How to setup
 - Enter the name of the task (application) according to your wish.

 - Open Task Scheduler and go to the Triggers tab.

 - Click New, set it to Daily, choose your desired Start time, then click OK.

 - Switch to the Actions tab and click New.

 - In Program/script, enter the path to your Python executable.

 - In Add arguments, enter the full path to reminder.py, then click OK.

 - In the Conditions tab, uncheck “Start the task only if the computer is on AC power”, then click OK.

 - Finally, click OK in the main Task Scheduler window to save your scheduled task.