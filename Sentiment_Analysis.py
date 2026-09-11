import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download lexicon data
nltk.download('vader_lexicon', quiet=True)

class SentimentDetector:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze(self, text: str) -> dict:
        scores = self.analyzer.polarity_scores(text)
        compound = scores['compound']
        
        if compound >= 0.05:
            sentiment = "Positive "
        elif compound <= -0.05:
            sentiment = "Negative "
        else:
            sentiment = "Neutral "
            
        return {"sentiment": sentiment, "score": compound, "details": scores}

# Demo execution
detector = SentimentDetector()
sample_texts = [
    "I absolutely love the new AI features, outstanding work!",
    "The pipeline execution was slow and kept crashing.",
    "The meeting is scheduled for 3 PM tomorrow.",
    "The project was so so their was nothing special in that project ",
    "The project was good but the present was bad",
    "you hit the nail on the head"
]

print(" AI Sentiment Analysis Results:\n" + "-"*40)
for text in sample_texts:
    result = detector.analyze(text)
    print(f"Text: \"{text}\"")
    print(f"Detected: {result['sentiment']} (Compound Score: {result['score']})\n")
