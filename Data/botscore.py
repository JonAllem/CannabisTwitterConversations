"""
Script to score users as bot or not using botometer.
"""
import datetime
import os
import threading
import pickle

import botometer
import pandas as pd

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_botscores(start, end):
	"""
	Apply botometer on file Tweeets/sampled.pickle.
	Args:
		start (int): The line number of the first user to read from.
		end (int): The line number of the last to read.
	Returns the botometer result per user.
	"""
	users_file = os.path.join(CURRENT_DIR, 'Tweets\\sampled.pickle')
	with open(users_file, 'rb') as file_handle:
		sample = pickle.load(file_handle)
		users = sample.UserId.unique()[start:end].tolist()

	bom = botometer.Botometer(
		mashape_key='',
		consumer_key='',
		consumer_secret='',
		botometer_api_url='https://botometer-pro.p.rapidapi.com',
		wait_on_ratelimit=True
	)

	results = {}
	for i, user in enumerate(users):
		try:
			score_dict = bom.check_account(user)
			results[user] = {
				'cap': score_dict['cap'],
				'scores': {
					'english': score_dict['display_scores']['english'],
					'universal': score_dict['display_scores']['universal']
				}
			}
			if i % 50 == 0:
				print(f'Processsed {start}-{end}:{i} users.')
		except Exception as e:
			print(f'Exception on user {user}')
	print(f'Finished {start}-{end}')
	return results

class ThreadWithReturnValue(threading.Thread):
	def __init__(self, group=None, target=None, name=None,
				 args=(), kwargs={}, Verbose=None):
		threading.Thread.__init__(self, group, target, name, args, kwargs)
		self._return = None

	def run(self):
		if self._target is not None:
			self._return = self._target(*self._args,
												**self._kwargs)

	def join(self, *args):
		threading.Thread.join(self, *args)
		return self._return

def main():
	thread1 = ThreadWithReturnValue(target=get_botscores, args=(36000, 47000))
	thread2 = ThreadWithReturnValue(target=get_botscores, args=(47000, 58000))
	thread3 = ThreadWithReturnValue(target=get_botscores, args=(58000, 69000))

	thread1.start()
	thread2.start()
	thread3.start()

	final_result = {**thread1.join(), **thread2.join(), **thread3.join()}
	pickle_file = os.path.join(CURRENT_DIR, 'Users\\botscores.pickle')

	if os.path.exists(pickle_file):
		with open(pickle_file, 'rb') as file_handle:
			stored_result = pickle.load(file_handle)
			final_result = {**final_result, **stored_result}
	with open(pickle_file, 'wb') as file_handle:
		pickle.dump(final_result, file_handle)

if __name__ == '__main__':
	main()
	print(datetime.datetime.now())
