from transformers import pipeline

class summarizer:

    def __init__(self, max_length=30, min_length=5):
        self.max_length = max_length
        self.min_length = min_length

    def summarize(self, text):
        classifier = pipeline(task="summarization", model="facebook/bart-large-cnn", max_length=self.max_length, min_length=self.min_length, num_beams=4)
        summary = classifier(text)

        return summary