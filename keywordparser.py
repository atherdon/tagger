import csv

with open("blockchain keywords.csv") as b_word:
    blockchain = []
    for b in b_word:
        blockchain+=b.split(",")

with open ("programming keywords.csv") as p_word:
    programming = []
    for p in p_word:
        programming+=p.split(",")

with open ("startups keywords.csv") as s_word:
    startups = []
    for s in s_word:
        startups+= s.split(",")