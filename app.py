import gradio as gr
import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np
from transformers import pipeline

# Load data
emotion_df = pd.read_csv("emotion_map_full.csv")
emotion_map = emotion_df.set_index("emotion").to_dict(orient="index")

# Load ML models
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
generator = pipeline("text-generation", model="gpt2")

# Custom styling
css = """
.gradio-container {
    max-width: 800px;
    margin: 0 auto;
    font-family: 'Poppins', sans-serif;
}
.header {
    text-align: center;
    margin-bottom: 2em;
}
.header h1 {
    background: linear-gradient(90deg, #8e44ad, #3498db);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}
.input-container {
    background: white;
    padding: 1.5em;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
"""

def process_input(user_input):
    # Classify emotion
    result = classifier(user_input, candidate_labels=list(emotion_map.keys()))
    emotion = result['labels'][0]
    response = emotion_map.get(emotion, {
        "metaphor": "Your feeling is important",
        "quote": "All emotions are valid",
        "suggestion": "Try journaling about how you feel"
    })
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.text(0.5, 0.5, emotion.upper(), 
            fontsize=24, ha='center', va='center',
            color="#8e44ad")
    ax.axis('off')
    
    return response["metaphor"], response["quote"], response["suggestion"], fig

with gr.Blocks(css=css) as app:
    with gr.Column():
        with gr.Column(elem_classes="header"):
            gr.Markdown("# 🌈 Mood Metaphor Companion")
            gr.Markdown("Transform your emotions into beautiful insights")
        
        with gr.Column(elem_classes="input-container"):
            input_box = gr.Textbox(label="How are you feeling?")
            submit_btn = gr.Button("Get Insights", variant="primary")
        
        with gr.Row():
            metaphor = gr.Textbox(label="Metaphor")
            quote = gr.Textbox(label="Wisdom")
            suggestion = gr.Textbox(label="Suggestion")
        
        visualization = gr.Plot()

    submit_btn.click(
        fn=process_input,
        inputs=input_box,
        outputs=[metaphor, quote, suggestion, visualization]
    )

app.launch()
