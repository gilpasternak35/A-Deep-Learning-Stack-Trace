import random
import logging

# A McCullough-Pitts model
class MPClassifier:
	def __init__(self, weighting_fn: list, decision_boundary: float):
		"""Constructor initializing weights"""
		self.weights = weighting_fn
		self.db = decision_boundary
	
	def predict(self, inputs: list) -> int:
		"""McCullough Pitts prediction function, weighting input list and checking if it is larger than some decision criterion"""
		return int(sum([weight * inp for weight, inp in zip(self.weights, inputs)]) > self.db)

def test_mp_classifier():
	weighting_fn = [0.2, 0.2, 0.3, 0.3]
	decision_boundary = 0.5
	mp = MPClassifier(weighting_fn, decision_boundary)
	assert mp.predict([0.1, 0.2, 0.3, 0.4]) == 0, "Test Failed: MPClassifier failed to classify negative example"
	assert mp.predict([1,2,0,0]) == 1, "Test Failed: MPClassifier failed to classify positive example"

if __name__ == "__main__":
	# Test the MPClassifier
	test_mp_classifier()
	logging.basicConfig(level=logging.INFO, filename = "mp.log", filemode = "a", format="%(asctime)s %(levelname)s: %(message)s")
	logger = logging.getLogger()
	logger.info("Test passed: MPClassifier")

