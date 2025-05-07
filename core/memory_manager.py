# core/memory_manager.py

import json
import os

class MemoryManager:
    def __init__(self, filename="eidos_memory.json"):
        self.filename = filename
        self.path = os.path.join(os.getcwd(), self.filename)

    def save(self, memory_list):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(memory_list, f, indent=2)

    def load(self):
        if not os.path.exists(self.path):
            return []
        with open(self.path, 'r', encoding='utf-8') as f:
            return json.load(f)
