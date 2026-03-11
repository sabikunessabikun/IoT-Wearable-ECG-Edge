import neurokit2 as nk
import pandas as pd
import matplotlib.pyplot as plt

print("🚀 R&D Phase 2: ECG Data Pipeline Initiating...")

# STEP 1: ECG Signal Simulation (Duration increased to 120 seconds!)
ecg_signal = nk.ecg_simulate(duration=120, heart_rate=70, noise=0.1)

# STEP 2: Signal Cleaning and R-Peak Detection
signals, info = nk.ecg_process(ecg_signal, sampling_rate=1000)

# STEP 3: Feature Extraction - ML STARTS HERE!
hrv_features = nk.hrv(info, sampling_rate=1000, show=False)

print("\n📊 Extracted Machine Learning (ML) Features:")
print(f"-> Time Domain - SDNN (Anomaly Indicator): {hrv_features['HRV_SDNN'].values[0]:.2f} ms")
print(f"-> Time Domain - RMSSD (Heart Rate Variability): {hrv_features['HRV_RMSSD'].values[0]:.2f} ms")
print(f"-> Frequency Domain - LF/HF Ratio (Autonomic Nervous System): {hrv_features['HRV_LFHF'].values[0]:.2f}")

# STEP 4: Visualization
nk.ecg_plot(ecg_signals=signals, info=info)

# CODE TO PREVENT TEXT OVERLAP AND SPACING ISSUES:
plt.tight_layout() 

plt.show()
