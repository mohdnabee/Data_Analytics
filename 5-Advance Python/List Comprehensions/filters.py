
scores = {"maths" : 80  ,  "Science" : 90  ,  "English" : 75}

passes = {k : v for k,  v in scores .items() if v>=  80}

print(passes)