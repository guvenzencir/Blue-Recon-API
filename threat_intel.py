import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
VT_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
ABUSE_API_KEY = os.getenv("ABUSEIPDB_API_KEY")

def check_virustotal(ip):
    """VirusTotal üzerinden IP itibarını sorgular."""
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"x-apikey": VT_API_KEY}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            stats = data["data"]["attributes"]["last_analysis_stats"]
            return {"malicious": stats["malicious"], "suspicious": stats["suspicious"]}
        return {"error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

def check_abuseipdb(ip):
    """AbuseIPDB üzerinden raporlanma geçmişini sorgular."""
    url = "https://api.abuseipdb.com/api/v2/check"
    # Sadece son 90 gündeki raporları getirmesi için parametre ekliyoruz
    querystring = {"ipAddress": ip, "maxAgeInDays": "90"}
    headers = {
        "Accept": "application/json",
        "Key": ABUSE_API_KEY
    }
    
    try:
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            data = response.json()
            return {
                "abuse_confidence_score": data["data"]["abuseConfidenceScore"],
                "total_reports": data["data"]["totalReports"],
                "country": data["data"]["countryCode"]
            }
        return {"error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

def main():
    hedef_ip = input("Sorgulanacak IP Adresini Girin: ")
    print(f"\n[*] {hedef_ip} için istihbarat toplanıyor, lütfen bekleyin...")

    rapor = {
        "hedef_ip": hedef_ip,
        "virustotal_analizi": check_virustotal(hedef_ip),
        "abuseipdb_analizi": check_abuseipdb(hedef_ip)
    }

    # Sonuçları JSON formatında dışa aktar
    dosya_adi = f"rapor_{hedef_ip.replace('.', '_')}.json"
    with open(dosya_adi, "w", encoding="utf-8") as f:
        json.dump(rapor, f, indent=4, ensure_ascii=False)

    print(f"[+] Analiz tamamlandı! Tüm bulgular '{dosya_adi}' dosyasına kaydedildi.")

if __name__ == "__main__":
    if not VT_API_KEY or not ABUSE_API_KEY:
        print("[!] Hata: .env dosyasında API anahtarları eksik!")
    else:
        main()