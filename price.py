import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.in/dp/B0CHX2F5QT/"  # Replace with your product
TARGET_PRICE = 65000  # Change this to your budget

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

title_tag = soup.find(id="productTitle")
price_tag = soup.find("span", {"class": "a-price-whole"})
coupon_tag = soup.find("span", class_="savingsPercentage")  # Sometimes used for coupons
coupon_text = soup.find("span", class_="couponBadgeMessage")

if title_tag and price_tag:
    title = title_tag.get_text().strip()
    price = float(price_tag.get_text().strip().replace(",", ""))

    print(f"\n📦 Product: {title}")
    print(f"💰 Current Price: ₹{price}")

    # Check for coupons
    if coupon_text:
        coupon_msg = coupon_text.get_text().strip()
        print(f"🎁 Coupon Available: {coupon_msg}")
    elif coupon_tag:
        coupon_msg = coupon_tag.get_text().strip()
        print(f"🎁 Coupon Offer: {coupon_msg}")
    else:
        print("❌ No coupon available.")

    # Price check
    if price < TARGET_PRICE:
        print("🎉 Price dropped below target! Good time to buy!")
    else:
        print("⏳ Still above your target price. Keep waiting.")
else:
    print("⚠️ Could not find product title or price. Amazon may be blocking the request.")
