# @EXPECTED_RESULTS@: WRONG-ANSWER
from sys import stdin;
import random;

def arg(word):
	graph = ['Rock', 'Scissors', 'Paper']  
	for i in range(len(graph)):
		if(word == graph[i]):
			return i;
	
	return None;

def relation(you, friend):
	graph = ['Rock', 'Scissors', 'Paper']   
	y = arg(you);
	f = arg(friend);
	c = (f-y)%3;
	r = random.random();
	cut = 0.25;
	if((c == 0 and r >= cut ) or (c==1 and r < cut)):
		return graph[(y+2)%3];
	else:
		return graph[(y+1)%3];

line = stdin.readline();
T = int(line.strip());
for t in range(T):
	for i in range(10000):
		line = stdin.readline();
		play = line.split();
		ans = relation(play[0], play[1]);
		print(ans);

