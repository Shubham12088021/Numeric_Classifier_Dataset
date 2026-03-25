🎵 Numeric Song Explicit Classifier (ML Project)
📌 Overview

This project is a Machine Learning based web application that predicts whether a song is Explicit (🔞) or Non-Explicit (🎵) using its audio features.

It uses a Random Forest Classifier trained on Spotify track features and provides real-time predictions via Gradio UI.

🚀 Features

🎵 Predict if a song is explicit or not
🤖 Machine Learning model (Random Forest)
⚡ Fast predictions with optimized dataset sampling
📊 Feature importance visualization
🌐 Interactive UI using Gradio
📉 Data preprocessing (cleaning, scaling)

🛠️ Tech Stack
Python 🐍
Pandas & NumPy
Scikit-learn
Matplotlib & Seaborn
Gradio (Web Interface)
📂 Project Structure
numeric-song-classifier/
│
├── dataset/
│   └── tracks_features.csv
│
├── model.pkl
├── scaler.pkl
├── app.py / main.py
├── requirements.txt
└── README.md
⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/YOUR_USERNAME/Numeric_Classifier_Dataset.git
cd Numeric_Classifier_Dataset
2️⃣ Install dependencies
pip install -r requirements.txt
▶️ Run the Project
python app.py

Or if using Gradio:

python main.py

Then open the generated link in your browser 🌐

📊 Model Details
Algorithm: Random Forest Classifier
Number of estimators: 50
Max depth: 10
Train-test split: 80-20
📥 Input Features:
Danceability
Energy
Loudness
Speechiness
Acousticness
Instrumentalness
Liveness
Valence
Tempo
Duration
📤 Output:
🔞 Explicit Song
🎵 Non-Explicit Song
🧠 How It Works
Load dataset (tracks_features.csv)
Clean data (remove duplicates & null values)
Select relevant features
Scale data using StandardScaler
Train Random Forest model
Evaluate model performance
Predict using Gradio interface
📈 Visualization
Feature Importance plotted using Seaborn
Helps understand which features impact prediction most
💾 Model Saving
model.pkl → trained Random Forest model
scaler.pkl → fitted scaler
⚠️ Challenges
Dataset imbalance (explicit vs non-explicit)
Feature correlation issues
Real-world prediction accuracy may vary
🔥 Future Improvements
Use Deep Learning (ANN)
Deploy on cloud (Render / HuggingFace)
Add song name → auto feature extraction
Improve accuracy with hyperparameter tuning
👨‍💻 Author

Shubham Maurya
