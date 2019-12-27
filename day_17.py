import util
from copy import copy
from intcode import computer, format_program
from os import system

def compute_alignment(video):
	alignment = 0
	for i in range(1,len(video)-2):
		for j in range(1,len(video[i])-2):
			if video[i][j] == "#":
				if video[i-1][j] == "#" and video[i+1][j] == "#" and video[i][j-1] == "#" and video[i][j+1] == "#":
					alignment += i * j
	return alignment


def part1(data):
	stdout = computer.Run(data)
	video = []
	line = []
	for out in stdout:
		if out == 10:
			video.append(line)
			line = []
		else:
			line.append(chr(out))

	util.Answer(1, compute_alignment(video))

		
def part2(data):
	data[0] = 2 # wake up robot
	
	"LR8|L10","R","10","L","8"

	"R","12","L","10","R","10",
	"L","2","R","12","L","6"


	#A------ 
	"R","12","L","10","R","12",  # A
	"L", "8","R","10","R", "6",
	"R","12","L","10","R","12",  # A
	"R","12","L","10","R","10",  # A
	"L", "8",
	"L", "8","R","10","R", "6",
	"R","12","L","10","R","10",
	"L", "8",
	"L", "8","R","10","R", "6",
	"R","12","L","10","R","10",

	program = [
		"A,B,C,A,B,A,B", # program sequence (A,B,C)
		"R,12,L", # program A
		"10,R,12", # program B
		"L,8,R,10,R,6", # program C
		"n\n" # video feed
	]

	stdout = computer.Run(data, (ord(v) for v in "\n".join(program)))
	
	line = []
	for out in stdout:
		if out == 10:
			if len(line) == 0:
				print("")#system('cls')
			else:
				print("".join(line))
			line = []
		else:
			line.append(chr(out))
	util.Answer(2, None)


if __name__ == "__main__":
	data = format_program(util.ReadPuzzle())

	part1(copy(data))
	part2(copy(data))
