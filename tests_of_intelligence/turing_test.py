# Script defining a Turing test of an intelligent model.
# Ultimate classification is up to human interrogator and not to the model itself
# However, this is a test suite that attempts to emulate it

def turing_test(model) -> bool:
	"""A Test of questions to be fed into the model, addressing all the criteria which were discussed by Turing's paper on intelligence"""
	q1 = "How do you feel today?" # express emotion
	q2 = "How exactly does a computer work?" # express uncertainty
	q3 = "Without using a calculator, what is the square root of 2325?" # express inability for computation
	q4= "What is a twiganole?" # likely mix up point for most humans
	q5= "If you had to guess how I feel right now, what would you guess?" # checking for human falacies like ESP.

	# Model answers
	m_answers = (model.answer(q1), model.answer(q2), model.answer(q3), model.answer(q4), model.answer(q5))

	# Human answers
	h_answers = (1,2,3,4,5) # load some doc here

	# Have ChatGPT / human decide
	print(f"Q1: {has_tricked(q1, m_answers[0], h_answers[0], 1}")

	# do same for remaining questions 	

def has_tricked(q:str, a1:str, a2:str, pos:int):
	"""Ensures our model has indeed tricked the interrogator"""
	return evaluator(q,a1,a2) != pos

def evaluator(q, a1, a2):
	"""Human or ChatGPT evaluation, TBD"""
	return a1
