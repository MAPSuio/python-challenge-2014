# @EXPECTED_RESULTS@: CORRECT
from sys import stdin;

all_socks = [];
seen = {};
unpaired = [];

def already_seen(word):
	for s in seen:
		if(s == word):
			return True;
	return False;
	
def inc(name):
	if(name in seen):
		seen[name] +=1;
	else:
		seen[name] = 1;


line = stdin.readline();
N = int(line.strip());
for i in range(N):
	line = stdin.readline().strip();
	all_socks.append(line);
	inc(line);

for name in seen.keys():
	if(seen[name] == 1):
		unpaired.append(name);
unpaired.sort();
for name in unpaired:
	print(name);
if(len(unpaired) == 0):
	print('Sock-sess');
