# A McCullough-Pitts model
class MPClassifier:
	def __init__(self, weighting_fn: lst, decision_boundary: float):
		"""Constructor initializing weights"""
		self.weights = weighting_fn
	
	def predict(inputs: list) -> int:
		"""McCullough Pitts prediction function, weighting input list and checking if it is larger than some decision criterion"""
		return int(sum([weight * inp for weight, inp in zip(self.weights, inputs)]) > decision_boundary)
