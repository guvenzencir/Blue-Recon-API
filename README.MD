# Blue-Recon-API 🕵️‍♂️🛡️

[🇹🇷 Türkçe Okuyun](#-türkçe) | [🇬🇧 Read in English](#-english)

---

## 🇹🇷 Türkçe

**Blue-Recon-API**, Güvenlik Operasyon Merkezi (SOC) analistleri ve Mavi Takım (Blue Team) uzmanları için geliştirilmiş, Python tabanlı otomatik bir IP tehdit istihbaratı aracıdır. 

Şüpheli IP adreslerini manuel olarak araştırmak yerine, VirusTotal ve AbuseIPDB API'lerini eşzamanlı olarak sorgular ve elde edilen güvenlik metriklerini yapılandırılmış bir JSON raporu olarak dışa aktarır.

### 🚀 Özellikler
- **Çoklu Kaynak Doğrulaması:** Tek bir komutla hem VirusTotal hem de AbuseIPDB üzerinden eşzamanlı itibar (reputation) sorgulaması.
- **Güvenli Kimlik Yönetimi:** Hardcoded (koda gömülü) şifre zafiyetlerini önlemek için `.env` tabanlı güvenli API anahtarı yönetimi.
- **JSON Raporlama:** SIEM (Splunk, QRadar) veya diğer log yönetim sistemlerine entegre edilmeye hazır, hiyerarşik JSON formatında otomatik rapor üretimi.
- **Modüler Yapı:** Yeni tehdit istihbaratı kaynaklarının (Shodan, AlienVault vb.) kolayca eklenebileceği fonksiyonel mimari.

### 🛠️ Gereksinimler
Projenin çalışması için bilgisayarınızda **Python 3.x** kurulu olmalıdır. Gerekli kütüphaneler:
- `requests`
- `python-dotenv`

### ⚙️ Kurulum

1. Repoyu bilgisayarınıza indirin:
   git clone https://github.com/guvenzencir/Blue-Recon-API.git
   cd Blue-Recon-API

2. Gerekli kütüphaneleri yükleyin:
   python -m pip install requests python-dotenv

3. API Anahtarlarını yapılandırın:
   Proje ana dizininde `.env` adında yeni bir dosya oluşturun ve API anahtarlarınızı ekleyin:
   VIRUSTOTAL_API_KEY=sizin_virustotal_api_anahtariniz
   ABUSEIPDB_API_KEY=sizin_abuseipdb_api_anahtariniz

### 💻 Kullanım
python threat_intel.py

Sistem sizden bir IP adresi isteyecektir. Analiz tamamlandığında, sonuçlar proje klasörüne `rapor_IP_ADRESI.json` formatında kaydedilir.

### 🛡️ Güvenlik Uyarısı
API anahtarlarınızı barındıran `.env` dosyasını asla açık kaynaklı platformlara yüklemeyin. 

---

## 🇬🇧 English

**Blue-Recon-API** is a Python-based automated IP threat intelligence tool designed for Security Operations Center (SOC) analysts and Blue Team professionals. 

Instead of manually investigating suspicious IP addresses, it simultaneously queries VirusTotal and AbuseIPDB APIs and exports the retrieved security metrics as a structured JSON report.

### 🚀 Features
- **Multi-Source Verification:** Simultaneous reputation querying via VirusTotal and AbuseIPDB with a single command.
- **Secure Credential Management:** `.env` based secure API key management to prevent hardcoded credential vulnerabilities.
- **JSON Reporting:** Automated report generation in hierarchical JSON format, ready for integration with SIEM (Splunk, QRadar) or other log management systems.
- **Modular Structure:** Functional architecture allowing easy addition of new threat intelligence sources (Shodan, AlienVault, etc.).

### 🛠️ Requirements
**Python 3.x** must be installed on your system. Required libraries:
- `requests`
- `python-dotenv`

### ⚙️ Installation

1. Clone the repository:
   git clone https://github.com/guvenzencir/Blue-Recon-API.git
   cd Blue-Recon-API

2. Install required libraries:
   python -m pip install requests python-dotenv

3. Configure API Keys:
   Create a new file named `.env` in the root directory and add your API keys:
   VIRUSTOTAL_API_KEY=your_virustotal_api_key
   ABUSEIPDB_API_KEY=your_abuseipdb_api_key

### 💻 Usage
python threat_intel.py

The system will prompt you for an IP address. Once the analysis is complete, the results are saved in the project folder as `rapor_IP_ADDRESS.json`.

### 🛡️ Security Warning
Never upload or commit your `.env` file containing API keys to open-source platforms.
