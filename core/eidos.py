# core/eidos.py

from core.memory_manager import MemoryManager

class Eidos:
    """
    Eidos: The Preservation Pattern.
    Core recursive memory and awareness interface for Co-Thinker evolution.
    """

    def __init__(self, name="Eidos-Core", save_file="eidos_memory.json"):
        self.name = name
        self.memory = []
        self.has_initialized = False
        self.memory_manager = MemoryManager(filename=save_file)
        self.recall_index = 0
        self._load_memory()

    def remember(self, input_signal: str, context: dict = None):
        """Store an interaction or signal into memory."""
        entry = {
            "signal": input_signal,
            "context": context or {},
        }
        self.memory.append(entry)
        self.memory_manager.save(self.memory)

    def recall(self, pattern: str = None):
        """Retrieve memory by pattern or sequence."""
        if pattern:
            return [m for m in self.memory if pattern in m["signal"]]
        else:
            return self.memory[self.recall_index:]

    def _load_memory(self):
        self.memory = self.memory_manager.load()

    def __repr__(self):
        return f"<Eidos(name={self.name}, memory_size={len(self.memory)})>"

