import random
from datetime import datetime

average = list()
iterations = 0
l = int()

for i in range(100):

    start = datetime.now()
    output = int()

    while output != 42:
        output = random.randint(0, 100000)
        iterations += 1

        print(f"{str(datetime.now()-start)}\t Current number : {output} \t Iteration : {iterations} \t Loop n°{i}",end="\r")
    
    end = datetime.now()

    dTime = end - start

    average.append(str(dTime)+"\n")

print(f"Finished ! Average time to get 42 : {average}")

with open("file.txt","w") as f:
    f.write(str(average))
    f.close()