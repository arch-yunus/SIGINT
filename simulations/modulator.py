"""
SIGINT Hub - Advanced Modulation Engine
Developer: Yunus Çetin (IT Architect)
Location: Trabzon / Of
GitHub: https://github.com/bahattinyunus
"""
import numpy as np
from typing import Tuple

def generate_baseband(duration: float, sampling_rate: float, freq: float = 5.0) -> Tuple[np.ndarray, np.ndarray]:
    """Temel bant sinyali oluştur."""
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    return t, np.sin(2 * np.pi * freq * t)

def am_modulate(t: np.ndarray, message: np.ndarray, fc: float = 100.0, ka: float = 0.5) -> np.ndarray:
    """
    Genlik Modülasyonu (AM)
    
    Args:
        t: Zaman vektörü
        message: Mesaj sinyali
        fc: Taşıyıcı frekans (Hz)
        ka: Modülasyon indeksi
    
    Returns:
        AM modüle edilmiş sinyal
    """
    carrier = np.sin(2 * np.pi * fc * t)
    return (1 + ka * message) * carrier

def fm_modulate(t: np.ndarray, message: np.ndarray, fc: float = 100.0, kf: float = 50.0) -> np.ndarray:
    """
    Frekans Modülasyonu (FM)
    
    Args:
        t: Zaman vektörü
        message: Mesaj sinyali
        fc: Taşıyıcı frekans (Hz)
        kf: Frekans modülasyon indeksi
    
    Returns:
        FM modüle edilmiş sinyal
    """
    # Mesaj sinyalinin integralini al
    integral_message = np.cumsum(message) / len(t)
    return np.sin(2 * np.pi * fc * t + 2 * np.pi * kf * integral_message)

def bpsk_modulate(t: np.ndarray, bits: np.ndarray, fc: float = 100.0) -> np.ndarray:
    """
    BPSK Modülasyonu
    
    Args:
        t: Zaman vektörü
        bits: İkili veriler
        fc: Taşıyıcı frekans (Hz)
    
    Returns:
        BPSK modüle edilmiş sinyal
    """
    samples_per_bit = len(t) // len(bits)
    message = np.repeat(bits, samples_per_bit)
    if len(message) < len(t):
        message = np.append(message, [message[-1]] * (len(t) - len(message)))
    carrier = np.sin(2 * np.pi * fc * t)
    return (2 * message - 1) * carrier

if __name__ == "__main__":
    FS = 2000.0
    DURATION = 1.0
    t, message = generate_baseband(DURATION, FS)
    
    # AM
    am_signal = am_modulate(t, message)
    print("AM Sinyali Oluşturuldu.")
    
    # FM
    fm_signal = fm_modulate(t, message)
    print("FM Sinyali Oluşturuldu.")
    
    # BPSK
    bits = np.random.randint(0, 2, 10)
    bpsk_signal = bpsk_modulate(t, bits)
    print(f"BPSK Sinyali Oluşturuldu (Bits: {bits}).")
    
    # Kaydet
    np.savez("assets/modulated_signals.npz", t=t, am=am_signal, fm=fm_signal, bpsk=bpsk_signal)
    print("Modüle edilmiş sinyaller 'assets/modulated_signals.npz' olarak kaydedildi.")
