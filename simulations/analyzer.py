"""
SIGINT Hub - FFT Analyzer
Developer: Yunus Çetin (IT Architect)
Location: Trabzon / Of
GitHub: https://github.com/bahattinyunus
"""
import numpy as np
from typing import Tuple

def perform_fft(signal: np.ndarray, sampling_rate: float) -> Tuple[np.ndarray, np.ndarray]:
    """
    Sinyal üzerinde Hızlı Fourier Dönüşümü (FFT) gerçekleştirir.
    
    Args:
        signal: Giriş sinyali (zaman alanı)
        sampling_rate: Örnekleme oranı (Hz)
    
    Returns:
        positive_freqs: Pozitif frekanslar (Hz)
        magnitude: Her frekansa karşılık gelen genlik
    """
    n = len(signal)
    fft_result = np.fft.fft(signal)
    freqs = np.fft.fftfreq(n, 1/sampling_rate)
    
    # Sadece pozitif frekansları al
    positive_freqs = freqs[:n//2]
    magnitude = np.abs(fft_result[:n//2]) * 2 / n
    
    return positive_freqs, magnitude

def calculate_snr(signal: np.ndarray, noise: np.ndarray) -> float:
    """
    Sinyal Gürültü Oranını (SNR) hesapla.
    
    Args:
        signal: Temiz sinyal
        noise: Gürültü sinyali
    
    Returns:
        SNR değeri (dB cinsinden)
    """
    signal_power = np.mean(signal ** 2)
    noise_power = np.mean(noise ** 2)
    
    if noise_power == 0:
        return float('inf')
    
    snr_linear = signal_power / noise_power
    snr_db = 10 * np.log10(snr_linear)
    return snr_db

if __name__ == "__main__":
    from generator import generate_signal
    
    FS = 1000.0
    t, signal = generate_signal(50.0, 1.0, FS) # 50 Hz sinyal
    
    freqs, mag = perform_fft(signal, FS)
    
    # En yüksek frekansı bul (Tepe Tespiti)
    peak_idx = np.argmax(mag)
    peak_freq = freqs[peak_idx]
    
    print(f"ANALİZ SONUCU:")
    print(f"----------------")
    print(f"Tespit Edilen Taşıyıcı Frekans: {peak_freq:.2f} Hz")
    print(f"Sinyal Genliği: {mag[peak_idx]:.2f}")
