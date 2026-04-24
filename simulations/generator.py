"""
SIGINT Hub - Signal Generator
Developer: Yunus Çetin (IT Architect)
Location: Trabzon / Of
GitHub: https://github.com/bahattinyunus
"""
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

def generate_signal(frequency: float, duration: float, sampling_rate: float, noise_level: float = 0.1) -> Tuple[np.ndarray, np.ndarray]:
    """
    Simüle edilmiş bir sinyal oluşturur (Sinüs dalgası + Gürültü).
    
    Args:
        frequency: Taşıyıcı frekans (Hz)
        duration: Sinyal süresi (saniye)
        sampling_rate: Örnekleme hızı (Hz)
        noise_level: Gürültü seviyesi (0.0 - 1.0)
    
    Returns:
        t: Zaman vektörü
        signal: İşlenmiş sinyal (sinüs + gürültü)
    """
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    signal = np.sin(2 * np.pi * frequency * t)
    noise = np.random.normal(0, noise_level, signal.shape)
    return t, signal + noise

if __name__ == "__main__":
    # Parametreler
    FREQ = 10.0  # 10 Hz
    DURATION = 1.0  # 1 saniye
    SAMPLING_RATE = 1000.0  # 1 kHz
    
    t, signal = generate_signal(FREQ, DURATION, SAMPLING_RATE)
    print(f"Sinyal Oluşturuldu: {FREQ} Hz, {SAMPLING_RATE} Hz örnekleme hızı.")
    
    # Basit bir çıktı (CSV olarak kaydedilebilir)
    with open("assets/signal_sample.txt", "w") as f:
        f.write("Time,Amplitude\n")
        for i in range(100): # İlk 100 örnek
            f.write(f"{t[i]:.4f},{signal[i]:.4f}\n")
    print("Sinyal verisi 'assets/signal_sample.txt' dosyasına kaydedildi.")
