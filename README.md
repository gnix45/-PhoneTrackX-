<div align="center">
  <img src="https://media.giphy.com/media/j6ZK7Dan4P2fK/giphy.gif" width="150px">
  <h1>📍 Phone Number Tracker</h1>
  <p>Track phone numbers with precise location using NumVerify, Google Maps API & IP Geolocation</p>

  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge">
</div>

---

## ✨ **Features**
✅ **Phone Number Lookup** (Carrier, Country, City, Timezone)  
✅ **Exact GPS Location** (Google Geolocation API)  
✅ **IP-Based Location Fallback** (IP Geolocation API)  
✅ **Google Maps Link for Easy Tracking**  
✅ **Secured API Keys via `.env` file**  
✅ **Lightweight & Fast (Uses `requests` and `dotenv`)**  

---

## 🚀 **Installation & Setup**
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/yourusername/phone-tracker.git
cd phone-tracker
```
### **Install Depencies**
```bash
pip install -r requirements.txt  
```
### **Add API's to .env**
```bash
NUMVERIFY_API_KEY=your_key_here  
IPINFO_API_KEY=your_key_here  
Google_Map_Api=API
```
### **Run the scripts**
```bash
python main.py  
```
### **📍 Example Output:**
```bash
📞 Phone Number Details:  
✅ Valid: True  
✅ Country: USA  
✅ Carrier: AT&T  
✅ Calling Code: +1  

🌍 Found IP Address: 192.168.1.1  
📍 Exact Location:  
✅ City: New York  
✅ Region: NY  
✅ GPS: 40.7128, -74.0060  
🔗 Google Maps: https://www.google.com/maps?q=40.7128,-74.0060  
```
### **Disclaimer**
**⚡ Use this tool responsibly! This is for educational purposes only.**

## Credits to **TECH-TRIBE**
