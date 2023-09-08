import typing

class Activation:
    """Class maintaining activation functions and retuning them as needed"""

    @staticmethod
    def relu(inp: float) -> float:
        """Rectified Linear Unit function: returns input if input >=0, else 0. Function cannot be negative."""
        return max(inp, 0)