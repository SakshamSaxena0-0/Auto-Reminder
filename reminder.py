import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

# === CONFIG ===
URL = "your_product_link"
TARGET_PRICE = "your preferred price"
EMAIL_SENDER = "your email address"
EMAIL_PASSWORD = "your password"  # 16-character Gmail app password
EMAIL_RECEIVER = "your email address"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-IN,en;q=0.9"
}

def check_price():
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")

    try:
        title = soup.find(id="productTitle").get_text().strip()

        # Grab price components
        whole = soup.find("span", class_="a-price-whole").get_text().strip().replace(",", "").replace(".", "")
        fraction_tag = soup.find("span", class_="a-price-fraction")
        fraction = fraction_tag.get_text().strip() if fraction_tag else "00"

        # Construct valid float
        price_str = f"{whole}.{fraction}"
        price = float(price_str)

        print(f"[INFO] Current Price: ₹{price}")
        if price <= TARGET_PRICE:
            send_email(title, price)
        else:
            print("Price is still above target.")
    except Exception as e:
        print("❌ Error parsing price:", e)

def send_email(product, price):
    subject = f"🔥 Price Drop: {product} is now ₹{price}!"
    body = f"Hello Saksham,\n\nThe price of:\n\n{product}\nis now just ₹{price}.\n\nBuy now: {URL}"
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print("❌ Failed to send email:", e)

if __name__ == "__main__":
    check_price()
