# Emotion-to-Metaphor Mood Uplifter

This project is an interactive NLP-powered app that helps users reflect on their emotions using creative metaphors, motivational quotes, and mood-lifting suggestions. Whether you're feeling joyful, anxious, or uncertain, the app offers compassionate, AI-driven support to lift your spirits.

---

## Features

-  **Emotion Detection**: Users enter how they're feeling in plain text.
-  **Metaphor Generation**: The app responds with a metaphor capturing that emotion.
-  **Motivational Quote**: A carefully selected quote offers encouragement.
- **Mood-Lifting Suggestion**: Practical advice to help users move forward.

---

## How It Works

1. **User Input**: Type how you’re feeling (e.g., “sadness”, “anxious”, or “I feel overwhelmed”).
2. **Emotion Matching**: The app maps your mood to a known emotional state.
3. **Uplifting Response**: It returns a metaphor, quote, and a helpful suggestion — all drawn from a custom dataset.

---

## Technologies Used

- **Python 3.9+**
- **Gradio** for the interactive UI
- **Pandas** for loading and managing the dataset
- **Transformers** (optional) for zero-shot emotion classification and GPT-based metaphor generation

---

## Files

- `Emotion_to_Metaphor_Mood_Uplifter.ipynb`: Jupyter Notebook version of the project
- `emotion_map_full.csv`: Dataset mapping emotions to metaphors, quotes, and suggestions
- `app.py`: Optional standalone Python script with Gradio interface
- `README.md`: This file

---

## Installation & Running

### Step 1: Clone the Repository

```bash
git clone https://github.com/sparkysparo/NLP-mood-metaphors.git
cd emotion-to-metaphor
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the App

```bash
python app.py
```

> Or run the notebook:
```bash
jupyter notebook Emotion_to_Metaphor_Mood_Uplifter.ipynb
```

---

## Dataset Example

```csv
emotion,metaphor,quote,suggestion
sadness,"A cloud that won’t stop raining.","Every storm runs out of rain.","Take a short walk or listen to your favorite music."
joy,"A balloon floating into a clear sky.","Joy is not in things; it is in us.","Celebrate with someone — joy grows when shared."
...
```

---

## Future Enhancements

-  Optional facial expression detection
- AI-generated metaphors using GPT-2 or T5
-  Mobile/web deployment via Hugging Face Spaces or Streamlit Cloud
- Reverse: Metaphor → Emotion prediction

---

## Inspiration

This project blends affective computing, creative writing, and mental wellness. Inspired by therapeutic practices and expressive NLP, it aims to offer a gentle nudge toward positivity.

---

## 📄 License

MIT License
