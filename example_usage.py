"""
SIGINT Hub - Komple Örnek Kullanım
Developer: Yunus Çetin (IT Architect)
Location: Trabzon / Of
GitHub: https://github.com/bahattinyunus

Bu script, SIGINT Hub'ın tüm özelliklerini gösteren kapsamlı bir örnektir.
"""

import numpy as np
import sys
import os
import logging
from typing import Optional

# Logging konfigürasyonu
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

# Simülasyon modüllerini içe aktar
sys.path.append(os.path.join(os.path.dirname(__file__), 'simulations'))

try:
    from generator import generate_signal
    from analyzer import perform_fft, calculate_snr
    from modulator import am_modulate, fm_modulate, bpsk_modulate, generate_baseband
    logger.info("Tüm modüller başarıyla yüklendi")
except ImportError as e:
    logger.error(f"Modül import hatası: {e}")
    sys.exit(1)

def main() -> None:
    """SIGINT Hub kapsamlı demonstrasyon."""
    try:
        print("="*80)
        print(" " * 25 + "SIGINT HUB - KOMPLE DEMO")
        print("="*80)
        
        # 1. Sinyal Üretimi
        logger.info("[1/5] Sinyal Üretimi başlanıyor...")
        FS = 2000.0
        DURATION = 1.0
        t, clean_signal = generate_signal(100.0, DURATION, FS, noise_level=0.05)
        logger.info(f"✓ {len(t)} örnekli sinyal oluşturuldu (Sampling Rate: {FS} Hz)")
        
        # 2. FFT Analizi
        logger.info("[2/5] FFT Analizi başlanıyor...")
        freqs, mag = perform_fft(clean_signal, FS)
        peak_idx = np.argmax(mag)
        peak_freq = freqs[peak_idx]
        logger.info(f"✓ Tespit Edilen Frekans: {peak_freq:.2f} Hz")
        logger.info(f"✓ Sinyal Gücü: {mag[peak_idx]:.2f}")
        
        # 3. SNR Hesaplama
        logger.info("[3/5] SNR Hesaplama başlanıyor...")
        # Gürültü sinyali oluştturulur
        noise = np.random.normal(0, 0.05, len(clean_signal))
        snr_value = calculate_snr(clean_signal, noise)
        logger.info(f"✓ SNR Değeri: {snr_value:.2f} dB")
        
        # 4. Modülasyon Demosu
        logger.info("[4/5] Modülasyon Simülasyonları başlanıyor...")
        t_mod, message = generate_baseband(DURATION, FS, freq=5.0)
        
        am_sig = am_modulate(t_mod, message, fc=200.0)
        logger.info("✓ AM Modülasyonu tamamlandı")
        
        fm_sig = fm_modulate(t_mod, message, fc=200.0, kf=50.0)
        logger.info("✓ FM Modülasyonu tamamlandı")
        
        bits = np.array([1, 0, 1, 1, 0, 0, 1, 0])
        bpsk_sig = bpsk_modulate(t_mod, bits, fc=200.0)
        logger.info(f"✓ BPSK Modülasyonu tamamlandı (Bits: {bits})")
        
        # 5. Sonuç Raporu
        logger.info("[5/5] Operasyon Raporu")
        print("-"*80)
        print(f"Toplam İşlenen Sinyal Sayısı: 4")
        print(f"Tespit Edilen Taşıyıcı Frekans: {peak_freq:.2f} Hz")
        print(f"SNR Değeri: {snr_value:.2f} dB")
        print(f"Modülasyon Teknikleri: AM, FM, BPSK")
        print("="*80)
        logger.info("Demonstrasyon başarıyla tamamlandı")
        print(f"Operasyon Durumu: BAŞARILI ✓")
        print("="*80)
        print("\nTaktik dashboard için: python dashboard.py")
        
    except Exception as e:
        logger.error(f"Hata oluştu: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
