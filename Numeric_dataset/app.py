import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import gradio as gr

# Load dataset
df = pd.read_csv("tracks_features.csv")

df = df.sample(50000, random_state=42)
df = df.drop_duplicates().dropna()

features = [
    'danceability', 'energy', 'loudness', 'speechiness',
    'acousticness', 'instrumentalness', 'liveness',
    'valence', 'tempo', 'duration_ms'
]

X = df[features]
y = df['explicit'].astype(int)

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Model
rf = RandomForestClassifier(
    n_estimators=50,
    max_depth=10,
    n_jobs=-1
)

rf.fit(X_scaled, y)

# Prediction function
def predict_explicit(danceability, energy, loudness, speechiness,
                     acousticness, instrumentalness, liveness,
                     valence, tempo, duration_ms):

    input_data = np.array([[danceability, energy, loudness, speechiness,
                            acousticness, instrumentalness, liveness,
                            valence, tempo, duration_ms]])

    input_scaled = scaler.transform(input_data)
    prediction = rf.predict(input_scaled)[0]

    return "🔞 Explicit Song" if prediction == 1 else "🎵 Non-Explicit Song"


# Gradio UI
interface = gr.Interface(
    fn=predict_explicit,
    inputs=[
        gr.Slider(0, 1, label="Danceability"),
        gr.Slider(0, 1, label="Energy"),
        gr.Slider(-60, 0, label="Loudness"),
        gr.Slider(0, 1, label="Speechiness"),
        gr.Slider(0, 1, label="Acousticness"),
        gr.Slider(0, 1, label="Instrumentalness"),
        gr.Slider(0, 1, label="Liveness"),
        gr.Slider(0, 1, label="Valence"),
        gr.Slider(50, 250, label="Tempo"),
        gr.Slider(50000, 300000, label="Duration (ms)")
    ],
    outputs="text",
    title="🎵 Song Explicit Prediction App",
    description="Predict whether a song is explicit or not"
)

interface.launch()