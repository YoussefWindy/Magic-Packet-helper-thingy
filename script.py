import requests
import smtplib
from email.message import EmailMessage

def get_public_ip():
    services = [
        ("https://api.ipify.org?format=json", lambda r: r.json().get("ip")),
        ("https://ipinfo.io/json", lambda r: r.json().get("ip")),
        ("https://ifconfig.me/all.json", lambda r: r.json().get("ip_addr")),
        ("https://checkip.amazonaws.com", lambda r: r.text.strip()),
    ]

    for url, extractor in services:
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            ip = extractor(response)
            if ip:
                return ip
        except Exception as e:
            print(f"Service failed: {url} → {e}")
    
    print("All services failed to retrieve your public IP.")
    return None

def change_detected(ip):
    with open("addresses.txt") as f:
        change = f.readlines()[-1].strip() != ip
    if change:
        with open("addresses.txt", 'a') as f:
            f.write('\n' + ip)
    return change

def send_email(ip):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    with open("password.txt") as f:
        password = f.read().strip()
    s.login("noreply.auto.gen152577523@gmail.com", password)
    msg = EmailMessage()
    msg['Subject'] = "IP Address Change Detected"
    msg['From'] = "noreply.auto.gen152577523@gmail.com"
    msg['To'] = "guindi.y@gmail.com"
    if ip == None:
        msg.set_content("Failed to retrieve IP")
    else:
        msg.set_content(f"New IP address: {ip}")
    s.send_message(msg)
    s.quit()

if __name__ == "__main__":
    ip, i = None, 0
    while ip == None and i < 10:
        ip = get_public_ip()
    if change_detected(ip):
        send_email(ip)
    