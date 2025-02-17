import requests
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
NUMVERIFY_API_KEY = os.getenv("NUMVERIFY_API_KEY")
IPINFO_API_KEY = os.getenv("IPINFO_API_KEY")

def get_phone_details(phone_number):
    """Fetches phone number details from NumVerify API"""
    url = f"http://apilayer.net/api/validate?access_key={NUMVERIFY_API_KEY}&number={phone_number}"
    response = requests.get(url)
    data = response.json()

    if not data.get("valid"):
        print("❌ Invalid phone number. Check API key or number format.")
        return None

    return {
        "valid": data.get("valid"),
        "country": data.get("country_name"),
        "location": data.get("location"),
        "carrier": data.get("carrier"),
        "calling_code": data.get("country_code"),
    }

def get_ip_from_phone(phone_number):
    """Finds an IP address associated with a phone number using IPinfo"""
    url = f"https://ipinfo.io/{phone_number}?token={IPINFO_API_KEY}"
    response = requests.get(url)
    data = response.json()

    return data.get("ip")

def get_location_from_ip(ip_address):
    """Fetches geolocation details using IP-API"""
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()

    return {
        "city": data.get("city"),
        "region": data.get("regionName"),
        "country": data.get("country"),
        "lat": data.get("lat"),
        "lon": data.get("lon"),
        "google_maps": f"https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}"
    }

# Main function
def track_phone(phone_number):
    phone_details = get_phone_details(phone_number)
    if not phone_details:
        return

    print("\n📞 Phone Number Details:")
    for key, value in phone_details.items():
        print(f"✅ {key.capitalize()}: {value}")

    ip_address = get_ip_from_phone(phone_number)
    if not ip_address:
        print("\n❌ Could not find an associated IP address.")
        return

    print(f"\n🌍 Found IP Address: {ip_address}")

    location = get_location_from_ip(ip_address)
    if location:
        print("\n📍 Exact Location:")
        for key, value in location.items():
            print(f"✅ {key.capitalize()}: {value}")

# Run script
phone_number = input("📲 Enter phone number in international format (+123xxxxxxxxx): ")
track_phone(phone_number)
