from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Hedef kelime
target_word = "word"

# Başlangıç URL'si
start_url = "https://ornek.com"

# Tarayıcıyı başlat
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(start_url)
time.sleep(3)  

# Sayfadaki tüm <a> taglerinden linkleri al
link_elements = driver.find_elements(By.TAG_NAME, "a")
links = set()

for link in link_elements:
    href = link.get_attribute("href")
    if href and href.startswith("http"):
        links.add(href)

print(f"{len(links)} link bulundu. Kontrol ediliyor...\n")

# Hedef kelimeyi içeren sayfaların listesi
matching_pages = []

for url in links:
    try:
        driver.get(url)
        time.sleep(1)
        page_source = driver.page_source

        if target_word.lower() in page_source.lower():
            print(f"✅ Kelime bulundu: {url}")
            matching_pages.append(url)
        else:
            print(f"❌ Bulunamadı: {url}")

    except Exception as e:
        print(f"⚠️ Hata oluştu: {url} — {str(e)}")


print("\n🔍 Kelimeyi içeren sayfalar:")
for page in matching_pages:
    print(page)


driver.quit()
