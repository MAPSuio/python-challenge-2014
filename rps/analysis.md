Let it be the case that   
a beats b  
b beats c    
c beats a  

CASE 1:
=======
(1 a a) (both players pick the same hand)  

In this case there is no doubt. By playing b every time, the worst possible case is draw, which gives you 0.5 points.  



CASE 2:
=======
(1 a b) (first player beats second player)  

Let p be the probability that the first player selects b in second round.  

prob p     (2 b _)  
    (2 b a) -> (3 c c) -> 0.5  
    (2 b c) -> (3 c a) -> 1  
prob 1-p   (2 c _)  
    (2 c a) -> (3 b c) -> 1  
    (2 c c) -> (3 b a) -> 0  


CASE 3: 
=======
(1 b a) (second player beats first player)  

Let q be the probability that the first player selects a in second round.  

prob q     (2 a _)  
    (2 a b) -> (3 c c) -> 0.5  
    (2 a c) -> (3 c b) -> 0  

prob 1-q   (2 c _)  
    (2 c b) -> (3 a c) -> 0  
    (2 c c) -> (3 a b) -> 1  


CASE 2 and CASE 3 together: 
===========================
So only considering CASE 2 and CASE 3, we have 4 different opponent strategies: 
Opp(x,y) plays x in CASE 2 and y in CASE 3.

Calculating expected number of points against  each opponent when playing one CASE 2 round and one CASE 3 round:
Opp(a,b) -> p*0.5 + (1-p)*1 + q*0.5 + (1-q)*0 = 1 - 0.5*p + 0.5*q
Opp(a,c) -> p*0.5 + (1-p)*1 + q*0 + (1-q)*1   = 2 - 0.5*p - q
Opp(c,b) -> p*1 + (1-p)*0 + q*0.5 + (1-q)*0   = p + 0.5*q
Opp(c,c) -> p*1 + (1-p)*0 + q*0 + (1-q)*1     = 1 + p - q

Then, for each choice of p and q, we assume that we meet the most clever opponent. So we want to calculate the min of these opponents, and maximize that result. Find such p and q.

Wolfram alpha:
max(min(1 - 0.5*p + 0.5*q, 2 - 0.5*p - q, p + 0.5*q, 1 + p - q)) = 1 when p = 2/3 and q = 2/3

So when p = 2/3 and q = 2/3, we will gain 1 point per pair of (CASE 2, CASE 3), so expected number of points for each of CASE 2 and CASE 3 is 0.5. In other words, we have managed to gain at least 0.5 points for each of the three cases.
expected number of points = 10000 * 0.5 = 5000, and in almost all cases, one gets more than 4750 points.


Conclusion:
===========
Without adding the probability in this problem, one cannot do as good as needed. Most people would do (2 b _) in CASE 2, and (2 c _) in CASE 3. 
But if you do this and meet an opponent which always plays (2 a _) in CASE 2 and (2 b _) in CASE 3, then you will loose more than you win.

