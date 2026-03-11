# 🫀 IoT Wearable ECG Monitor: Edge Computing & Hardware Architecture

![Project Status](https://img.shields.io/badge/Status-Hardware_Validated-success)
![Focus](https://img.shields.io/badge/Focus-MedTech%20%7C%20Signal%20Processing-blue)
![Phase](https://img.shields.io/badge/Phase-Moving_to_ML_Pipeline-orange)

## 📌 Project Overview
This repository contains the end-to-end engineering architecture for an IoT-enabled Wearable ECG Monitor. Moving beyond breadboard prototyping, this project focuses on industrial hardware design, real-time signal processing at the edge, and risk management aligned with **ISO 14971** principles. The ultimate goal is to develop a highly scalable, reliable, and manufacturable MedTech device.

[PCB Görselini Veya Pitch Deck Kapağını Buraya Ekleyeceksin]

## ⚙️ Hardware Design (DFM Validated)
The hardware architecture is built to ensure pristine signal integrity for microvolt-level cardiac activity.
* **Analog Front-End:** AD8232 biopotential signal extraction chip.
* **Microcontroller:** ESP8266 for edge computing and Wi-Fi telemetry.
* **EMI Shielding:** Engineered a continuous **GND Copper Pour** (Faraday Cage) on the bottom layer to mitigate high-frequency Wi-Fi noise and ambient electromagnetic interference.
* **Status:** Gerber and Drill files exported; ready for PCB fabrication and SMD assembly.

## 🧠 Edge Computing & Firmware (C++)
To prevent false alarms and handle varying patient conditions autonomously:
* **Active Leads-Off Detection:** Firmware actively monitors the AD8232 LO+/LO- pins. In case of electrode detachment, the system suppresses noise and outputs a "0 BPM" safe state.
* **Adaptive Thresholding:** Implemented a dynamic R-peak detection algorithm. It utilizes a 3-second moving average to adjust the threshold to 60% of the maximum peak, effectively managing signal attenuation caused by high skin impedance (dry skin).

## 🛡️ Risk Management (Mini-FMEA)
Designed with MedTech compliance in mind (GDPMD / ISO 14971 considerations):
| Subsystem | Failure Mode | Clinical Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| **Hardware** | Severe motion artifact / Electrode drop | False tachycardia alarms | Active Leads-Off detection (HW/SW integration). |
| **Algorithm** | Signal attenuation due to impedance | False bradycardia (Missed R-peaks) | Real-time Adaptive Thresholding deployed. |
| **Telemetry** | Wi-Fi / Cloud connection loss | Interrupted real-time data | Autonomous auto-reconnect routines. |

## 🚀 Phase 2: AI & Machine Learning Pipeline (In Progress)
The next evolution of this project involves shifting from simple heuristic algorithms to robust AI-driven arrhythmia classification, targeting true "Edge AI" deployment.
* **Data Foundation:** Utilizing the **MIT-BIH Arrhythmia Database** (PhysioNet) for model training.
* **Feature Engineering:** Developing a Python pipeline using `scipy` and `neurokit2` to extract Time-Domain (SDNN, RMSSD) and Frequency-Domain (LF, HF) features from the ECG signals.
* **Target Architecture:** Researching the implementation of a **1D-CNN + LSTM** network to classify arrhythmias, with the ultimate goal of deploying the quantized model directly onto the MCU via **TinyML**, ensuring offline, life-saving autonomous decisions.

---
*Designed and engineered by Volkan.*
