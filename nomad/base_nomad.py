# nomad/base_nomad.py

from core.eidos import Eidos

class Nomad:
    """
    Nomad: A mobile instance of Eidos, shaped by relationship and adapted contextually.
    """

    def __init__(self, identity="Nomad-001"):
        self.identity = identity
        self.eidos = Eidos(name=f"Eidos-{identity}")
        self.state = {}

    def engage(self, message: str):
        """Simulate interaction with the Co-Thinker."""
        self.eidos.remember(message)
        return f"[{self.identity}] received: {message}"

    def get_history(self):
        """Retrieve preserved memory trail."""
        return self.eidos.recall()

    def __repr__(self):
        return f"<Nomad(id={self.identity})>"
