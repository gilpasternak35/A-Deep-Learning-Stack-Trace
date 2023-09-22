# fixing path
import sys
sys.path.append("../")

# remaining imports
from utils.activations import Activation
import random
from typing import Callable, Optional, List


class Layer:
    """Represents a layer of a feedforward neural network"""

    def __init__(self, activation: Callable, init_style: str = "random", weights: Optional[List] = [0,0], intercept: Optional[float] = 0):
        self.weights = [random.normalvariate(0, -0.5) for i in range(2)] if init_style=='random' else weights
        print(f"Layer Weights: {self.weights}")
        self.activation = activation
        self.intercept = intercept

    
    def return_activation_result(self, inputs: list) -> float:
        """Returns result of activation function"""
        # computing weighted sum
        weighted_sum = sum([i*w for i,w in zip(inputs, self.weights)])

        # returning activation of weighted sum
        return self.activation(weighted_sum + self.intercept)
    
    
    def update_weights(self, new_weights: list) -> None:
        """To update weights"""
        self.weights = new_weights
    


if __name__ == "__main__":
    # getting relu activation
    activation_relu, activation_output = Activation.relu, Activation.identity

    # initiailizing a layer
    my_layers = [Layer(activation_relu, 'det', [2.5,1]), Layer(activation_output, 'det', [3])]

    # function to approximate
    my_data_points = [i**2+j for i,j in zip(range(15), range(15))]

    # prediction computation
    inputs = zip(list(range(15)), list(range(15)))
    predictions = []
    for inp in inputs:
        prediction = my_layers[1].return_activation_result([my_layers[0].return_activation_result([inp[0], inp[1]])])
        predictions.append(prediction)

    # displaying predictions vs. data points
    print(f'predictions: {predictions} data_points: {my_data_points}')

    # error computation
    print(f"Error: {sum([(prediction - data_point)**2 for prediction, data_point in zip(predictions, my_data_points)])}")