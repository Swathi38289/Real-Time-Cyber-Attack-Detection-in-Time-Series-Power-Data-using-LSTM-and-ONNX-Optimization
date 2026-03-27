# ⚡ Real-Time Cyber Attack Detection in Time-Series Power Data using LSTM and ONNX Optimization

## 🚀 Overview
This project presents an **AI-driven cybersecurity system** designed to detect cyber attacks in **simulated power system (synchrophasor) data**.  
It uses **machine learning and deep learning models** to identify anomalies in real-time and simulates **hardware-efficient deployment using ONNX**.

---

## 🎯 Key Features
- 🔌 Simulated power system data (voltage, current, frequency, phase angle)
- 🚨 Cyber attack simulation (False Data Injection)
- 🤖 AI-based anomaly detection:
  - Random Forest (baseline)
  - LSTM (time-series detection)
- ⚡ ONNX-based model optimization (FPGA-style inference simulation)
- 🌐 FastAPI backend for real-time predictions
- 📊 Streamlit dashboard with live visualization

---

## 🧠 Technologies Used

| Category        | Technology |
|----------------|-----------|
| Programming    | Python |
| ML Models      | Scikit-learn (Random Forest) |
| Deep Learning  | TensorFlow / Keras (LSTM) |
| Optimization   | ONNX, ONNX Runtime |
| Backend API    | FastAPI |
| Visualization  | Streamlit |
| Data Handling  | Pandas, NumPy |

---

## 🏗️ System Architecture

Simulated Power Data
↓
Attack Injection (FDIA)
↓
AI Models (RF + LSTM)
↓
ONNX Optimization
↓
FastAPI Backend
↓
Streamlit Dashboard (Real-Time Visualization)


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
### 2️⃣ Create Virtual Environment
python -m venv myenv
myenv\Scripts\activate   # Windows
 ### 3️⃣ Install Dependencies
pip install -r requirements.txt
### ▶️ Running the Project
Step 1: Generate Data
python src/simulation/pmu_simulator.py
Step 2: Inject Attacks
python src/attacks/attack_simulator.py
Step 3: Train Model
python src/models/train_model.py
Step 4: Convert to ONNX
python src/optimization/onnx_converter.py
Step 5: Train LSTM Model
python src/models/lstm_model.py
Step 6: Start API
uvicorn src.api.app:app --reload
Step 7: Run Dashboard
streamlit run dashboard.py
