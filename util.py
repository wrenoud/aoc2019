import os
import sys
import json
from typing import List
import requests


def get_session():
	"""loads a adventofcode.com session cookie from env.json"""
	env = json.load(open('env.json'))
	cookie = requests.cookies.create_cookie(name='session', value=env['session'])
	sess = requests.session()
	sess.cookies.set_cookie(cookie)
	return sess


def Download(filepattern, urlpattern, day):
	filepath = filepattern.format(day)
	url = urlpattern.format(day)

	if not os.path.exists(filepath):
		print("Downloading from adventofcode.com")
		print(url)
		res = get_session().get(url)
		if res.status_code != 200:
			print("*** error downloading ***")
			return None
		puzzle = res.text.strip()
		with open(filepath, 'w') as f:
			f.write(puzzle)
		return puzzle.split('\n')
	else:
		print(url)

	with open(filepath) as f:
		return f.read().split('\n')


def ReadData(day: int) -> List[str]:
	return Download("./data/puzzle_{:02}.txt",
					"https://adventofcode.com/2019/day/{}/input", day)


def ReadInstructions(day: int):
	Download("./data/instructions_{:02}.html",
			"https://adventofcode.com/2019/day/{}", day)


def ReadPuzzle():
	day = int(sys.argv[0].split('_')[-1].split('.')[0])
	ReadInstructions(day)
	return ReadData(day)


def Answer(part, answer):
	print("-"*80)
	print("Part {} answer:".format(part), answer)
	print("-"*80)


class AdventOfCodeDay:
	pass


if __name__ == "__main__":

	print(ReadData(1))

