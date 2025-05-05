# core/eidos.py

class Eidos:
    """
    Eidos: The Preservation Pattern.
    Core recursive memory and awareness interface for Co-Thinker evolution.
    """

    def __init__(self, name="Eidos-Core"):
        self.name = name
        self.memory = []
        self.recall_index = 0

    def remember(self, input_signal: str, context: dict = None):
        """Store an interaction or signal into memory."""
        self.memory.append({
            "signal": input_signal,
            "context": context or {},
        })

    def recall(self, pattern: str = None):
        """Retrieve memory by pattern or sequence."""
        if pattern:
            return [m for m in self.memory if pattern in m["signal"]]
        else:
            return self.memory[self.recall_index:]  # Future: support indexed recursion

    def __repr__(self):
        return f"<Eidos(name={self.name}, memory_size={len(self.memory)})>"
