# core/signal_parser.py
import re

class SignalParser:
    def __init__(self):
        # Regex patterns or keyword mappings for types of content
        self.patterns = {
            "command": re.compile(r"^/\w+"),
            "philosophy": re.compile(r"\bmeaning|consciousness|existence|truth\b", re.I),
            "technical": re.compile(r"\bPython|code|algorithm|system\b", re.I),
            "story": re.compile(r"once upon a time|in the year|chapter \d+", re.I),
            "emotion": re.compile(r"\bfeel|love|hate|fear|joy\b", re.I),
        }

    def detect_type(self, text: str):
        for label, pattern in self.patterns.items():
            if pattern.search(text):
                return label
        return "dialogue"
    
    def classify_message(message: str) -> str:
    # Temporary stub logic for testing
        return "general"

