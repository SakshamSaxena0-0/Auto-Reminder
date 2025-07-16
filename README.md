# Auto-Reminder
# 🔔 Price Drop Email Reminder

A simple Python script that checks the price of a product (e.g., on Amazon) and sends you an email notification when it drops below your target price.

## 📌 Features
- Scrapes product title and price using `requests` + `BeautifulSoup`
- Sends alert email via Gmail SMTP when price falls below target
- Easy to customize and schedule

---

## 🧰 Requirements

- Python 3.7+
- Gmail account with an [App Password](https://support.google.com/accounts/answer/185833)
- The following Python packages (install using pip):

```bash
pip install -r requirements.txt

 ## How to setup