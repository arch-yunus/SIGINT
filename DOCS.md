# SIGINT Hub - Teknik Dokümantasyon

## İçindekiler
1. [Sistem Mimarisi](#sistem-mimarisi)
2. [Modül Detayları](#modül-detayları)
3. [Kurulum ve Kullanım](#kurulum-ve-kullanım)
4. [Gelişmiş Özellikler](#gelişmiş-özellikler)

---

## Sistem Mimarisi

SIGINT Hub, üç ana katmandan oluşur:

### 1. Sinyal Toplama Katmanı
- **SDR Entegrasyonu:** Yazılım Tanımlı Radyo (SDR) donanımları ile uyumlu
- **Frekans Aralığı:** HF/VHF/UHF bantları (3 MHz - 3 GHz)
- **Örnekleme Hızı:** Ayarlanabilir (varsayılan: 2 MHz)

### 2. Dijital Sinyal İşleme (DSP) Katmanı
- **FFT Motoru:** Hızlı Fourier Dönüşümü ile spektral analiz
- **Modülasyon/Demodülasyon:** AM, FM, BPSK desteklenir
- **Filtreleme:** Gürültü azaltma ve bant geçiren filtreler

### 3. İstihbarat Analiz Katmanı
- **ELINT:** Elektronik sinyal parametreleri (frekans, PRI, PW)
- **COMINT:** İletişim protokolü tanımlama
- **Otomatik Sınıflandırma:** Makine öğrenmesi tabanlı sinyal tanıma (gelecek sürüm)

---

## Modül Detayları

### generator.py
**Amaç:** Ham sinyal verisi üretimi

**Parametreler:**
- `frequency`: Taşıyıcı frekans (Hz)
- `duration`: Sinyal süresi (saniye)
- `sampling_rate`: Örnekleme hızı (Hz)
- `noise_level`: Gürültü seviyesi (0.0 - 1.0)

**Çıktı:** Zaman serisi verisi (CSV formatında)

### analyzer.py
**Amaç:** Spektral analiz ve frekans tespiti

**Algoritma:**
1. FFT uygulama
2. Pozitif frekansları filtreleme
3. Tepe noktası tespiti (peak detection)
4. SNR hesaplama

**Çıktı:** Tespit edilen frekans ve genlik bilgisi

### modulator.py
**Amaç:** Gelişmiş modülasyon teknikleri

**Desteklenen Modülasyonlar:**
- **AM (Amplitude Modulation):** Genlik modülasyonu
- **FM (Frequency Modulation):** Frekans modülasyonu
- **BPSK (Binary Phase Shift Keying):** İkili faz kaydırmalı anahtarlama

### spectrogram.py
**Amaç:** Zaman-frekans analizi

**Teknik:**
- STFT (Short-Time Fourier Transform)
- Pencere boyutu: 256 örnek
- Örtüşme: 128 örnek

**Çıktı:** ASCII tabanlı spektrogram önizlemesi

### dashboard.py
**Amaç:** Gerçek zamanlı taktik izleme

**Özellikler:**
- Canlı spektrum görselleştirmesi
- Sistem log akışı
- Operatör bilgileri
- ANSI renk kodlaması

---

## Kurulum ve Kullanım

### Kurulum
```bash
# Repository'yi klonlayın
git clone https://github.com/bahattinyunus/SIGINT.git
cd SIGINT

# Bağımlılıkları yükleyin
pip install -r requirements.txt
```

### Temel Kullanım
```bash
# 1. Sinyal üretin
python simulations/generator.py

# 2. Analiz edin
python simulations/analyzer.py

# 3. Modülasyon simülasyonu
python simulations/modulator.py

# 4. Spektrogram analizi
python simulations/spectrogram.py

# 5. Taktik dashboard'u başlatın
python dashboard.py
```

---

## Gelişmiş Özellikler

### Özel Sinyal Üretimi
```python
from simulations.generator import generate_signal

t, signal = generate_signal(
    frequency=144.5e6,  # 144.5 MHz
    duration=2.0,
    sampling_rate=10e6,  # 10 MHz
    noise_level=0.05
)
```

### Özel Modülasyon
```python
from simulations.modulator import am_modulate, generate_baseband

t, message = generate_baseband(1.0, 1000.0, freq=10.0)
modulated = am_modulate(t, message, fc=200.0, ka=0.8)
```

### CI/CD Entegrasyonu
Repository, GitHub Actions ile otomatik test süreçlerine sahiptir. Her commit'te:
- Tüm simülasyonlar çalıştırılır
- Hata kontrolü yapılır
- Test sonuçları raporlanır

---

## Katkıda Bulunma

Detaylı katkı rehberi için [CONTRIBUTING.md](file:///c:/github%20repolar%C4%B1m/SIGINT/CONTRIBUTING.md) dosyasına bakınız.

---

**Geliştirici:** Yunus Çetin (IT Architect)  
**GitHub:** [@bahattinyunus](https://github.com/bahattinyunus)  
**LinkedIn:** [linkedin.com/in/bahattinyunus](https://www.linkedin.com/in/bahattinyunus/)
