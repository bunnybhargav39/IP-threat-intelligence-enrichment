
# Threat Intelligence IP Enrichment from TXT File
# ============================================================

import pandas as pd
import requests
import time

# AbuseIPDB API Key

API_KEY = "24bb5a7f8acf36dddb0624f221b57f026ccd256f515801c6ae4d630b74cdb1330ce209c98ffc36c6"

# Input and Output Files

INPUT_FILE = r"C:\Users\INTEL\Desktop\reputation_score.txt"
OUTPUT_FILE = r"C:\Users\INTEL\Desktop\output.xlsx"

# Read IPs from TXT File

with open(INPUT_FILE, "r") as file:
    ip_list = [line.strip() for line in file.readlines()]

results = []

url = "https://api.abuseipdb.com/api/v2/check"

for ip in ip_list:

    print(f"Checking IP: {ip}")

    headers = {
        'Key': API_KEY,
        'Accept': 'application/json'
    }

    params = {
        'ipAddress': ip,
        'maxAgeInDays': 90
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            params=params
        )

        data = response.json()

        reputation_score = data['data']['abuseConfidenceScore']          # Extract Values
        country = data['data']['countryCode']
        isp = data['data']['isp']

        results.append({
            "IP": ip,
            "Reputation_Score": reputation_score,
            "Country": country,
            "ISP": isp
        })

        print(f"Success -> Score: {reputation_score}")

    except Exception as e:

        print(f"Error for IP {ip}: {e}")

        results.append({
            "IP": ip,
            "Reputation_Score": "Error",
            "Country": "Error",
            "ISP": "Error"
        })

    # Delay to Avoid Rate Limit

    time.sleep(1)
  
# Convert to DataFrame

df = pd.DataFrame(results)

df.to_excel(OUTPUT_FILE, index=False)

# output
print("\n===================================")
print("IP Enrichment Completed Successfully")
print(f"Output saved as: {OUTPUT_FILE}")
print("===================================")
