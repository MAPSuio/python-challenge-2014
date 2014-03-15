# QeuroPark [easy]
After getting fired from several large parking operator companies you've decided enough is enough; you'll start your own parking operator company - QeuroPark.

![](../images/qeuropark.png)

Even though you didn't exactly excel at your previous jobs, you know what it takes to be an efficient parking operator. There are three main factors affecting the success of such a company: A skilled and daring business crew, a motivated corps of inspectors and a super efficient call center, handling appeals and complaints.

Seeing as you are both daring and motivated, the only thing missing is an efficient call center. This is where your programming skills come into play. Emails received at the call center typically belong to one of two categories: _complaint_ and _other_. If an email is categorized as _other_, then there's no way around taking a look at it yourself to decide if it's important. If the mail is categorized as a _complaint_ on the other hand, it's easy; complaints are rejected.

Write a program that based on the subject line of an email, decides what action should be taken. You can assume that all complaint emails have `Complaint` as subject line.

## Input
The first line of input contains a single integer _n_, the number of emails your program should process.

Then follows _n_ lines, each representing the subject line of an email. The subject line is either `Complaint`, or some non-empty string.

## Output
For each email output whether you should `Reject` it or `Investigate` it.

## Constraints
1 &le; _n_ &le; 10<sup>4</sup>

## Sample input
```
10
Complaint
Welcome to IAESTE's Career Fair
Ways to make your love more passionate
Complaint
Complaint
Contact Western union
You have received a postcard!
Complaint
Has Anyone Really Been Far Even
Complaint
```

## Sample output
```
Reject
Investigate
Investigate
Reject
Reject
Investigate
Investigate
Reject
Investigate
Reject
```