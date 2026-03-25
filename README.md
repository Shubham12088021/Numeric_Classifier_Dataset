🎵 Numeric Song Explicit Classifier
📌 Overview

This project is a Machine Learning based web application that predicts whether a song is Explicit (🔞) or Non-Explicit (🎵).

It uses a Random Forest Classifier trained on Spotify track features and provides real-time predictions through an interactive web interface.

🚀 Features
🎵 Enter song features and get prediction
🤖 Machine Learning model (Random Forest)
⚡ Fast and efficient predictions
🌐 Interactive UI using Gradio
📊 Feature importance visualization
📁 Works with numerical audio features
🛠️ Tech Stack
Python 🐍
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
Gradio (Web Interface)
📂 Project Structure
numeric-classifier/
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
Features used for prediction:
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
Model used:
Random Forest Classifier
50 estimators
Max depth = 10
🧠 How It Works
Load dataset from CSV file
Remove duplicates and missing values
Select important numerical features
Scale data using StandardScaler
Train Random Forest model
Evaluate performance
Predict output using Gradio interface
📈 Training Visualization
Feature Importance plotted using Matplotlib & Seaborn
👨‍💻 Author

Shubham Maurya
