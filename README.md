# 🎵 Numeric Song Explicit Classifier

---

## 📌 Overview

This project is a **Machine Learning based web application** that predicts whether a song is **Explicit (🔞)** or **Non-Explicit (🎵)**.

It uses a **Random Forest Classifier** trained on Spotify track features and provides real-time predictions through an interactive web interface.

---

## 🚀 Features

* 🎵 Enter song features and get prediction  
* 🤖 Machine Learning model (Random Forest)  
* ⚡ Fast and efficient predictions  
* 🌐 Interactive UI using Gradio  
* 📊 Feature importance visualization  
* 📁 Works with numerical audio features  

---

## 🛠️ Tech Stack

* Python 🐍  
* Pandas  
* NumPy  
* Scikit-learn  
* Matplotlib  
* Seaborn  
* Gradio (Web Interface)  

---

## 📂 Project Structure


numeric-classifier/
│
├── dataset/
│ └── tracks_features.csv
│
├── model.pkl
├── scaler.pkl
├── app.py / main.py
├── requirements.txt
└── README.md


---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Numeric_Classifier_Dataset.git
cd Numeric_Classifier_Dataset
2️⃣ Install dependencies
pip install -r requirements.txt
▶️ Run the Project
python app.py

Or if using Gradio:

python main.py

Then open the generated link in your browser 🌐

## 📊 Model Details
Algorithm used: Random Forest Classifier
Number of estimators: 50
Max depth: 10
Train-test split: 80-20
## 📥 Input Features:
Danceability
Energy
Loudness
Speechiness
Acousticness
Instrumentalness
Liveness
Valence
Tempo
Duration (ms)
## 📤 Output:
🔞 Explicit Song
🎵 Non-Explicit Song
## 🧠 How It Works
Load dataset from CSV file
Clean data (remove duplicates and null values)
Select important numerical features
Scale data using StandardScaler
Train Random Forest model on training data
Validate model performance
Predict output for user input using Gradio
📈 Training Visualization
Feature Importance plotted using Matplotlib & Seaborn

## 🔥 Future Improvements
Deep Learning model (ANN)
Cloud deployment (Render / HuggingFace)
Auto feature extraction from song
Hyperparameter tuning

## 👨‍💻 Author
Shubham Maurya
