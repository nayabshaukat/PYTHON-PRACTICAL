names = [" ali","babar "," ayesha","zainab ", "hamza "]
scores = [40,60,50,30,80]

status = "Pass","Fail"

for index, name in enumerate(names):
    name = name.strip().upper()
    if(scores[index] >= 50):
        status = "Pass"
    else:
        status = "Fail"
        
print(f"Rank {index+1}: {name} | Score: {scores[index]} | Status: {status}")
        

    
