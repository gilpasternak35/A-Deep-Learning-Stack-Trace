from utils.activations import Activation
import random
from typing import Callable, Optional, List

# fixing path
import sys
sys.path.append("../")


class Layer:
    """Represents a layer of a feedforward neural network"""

    def __init__(self, activation: Callable, init_style: str = "random", weights: Optional[List] = [0,0]):
        self.weights = [random.normalvariate(0, -0.5) for i in range(2)] if init_style=='random' else weights
        print(f"Layer Weights: {self.weights}")
        self.activation = activation

    
    def return_activation_result(self, inputs: list) -> float:
        """Returns result of activation function"""
        # computing weighted sum
        weighted_sum = sum([i*w for i,w in zip(inputs, self.weights)])

        # returning activation of weighted sum
        return self.activation(weighted_sum)
    
    
    def update_weights(self, new_weights: list) -> None:
        """To update weights"""
        self.weights = new_weights

    


if __name__ == "__main__":
    # getting relu activation
    activation = Activation.relu

    # initiailizing a layer
    my_layer = Layer(activation, 'random')
    print(my_layer.return_activation_result([1,2]))