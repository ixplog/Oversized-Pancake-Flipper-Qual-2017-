filename = "A-large-practice.in"

file = open(filename, "r")
T = int( file.readline() )

pancakes = []
for i in range(T):
    inputs = file.readline().split(" ")
    S = inputs[0]
    K = int( inputs[1] )
    pancakes.append( (S, K) )

file.close()

################################################

output = "output.txt"

file = open(output, "w")

for index in range(len(pancakes)):
    (S, K) = pancakes[index]
    S = list(S)
    
    counter = 0
    lunghezza_stringa = len(S)
    for i in range(lunghezza_stringa - K + 1):   
        if S[i] == "-":
            counter += 1
            # flip da qui in avanti di K posizioni
            for j in range(K):
                if S[i+j] == "+":
                    S[i+j] = "-"
                else:
                    S[i+j] = "+"
    
    effective = True
    for i in range(lunghezza_stringa - K + 1, lunghezza_stringa):
        if S[i] == "-":
            effective = False
            break
    if effective == True:
        file.write("Case #" + str(index+1) + ": " +  str(counter) + "\n")
    else:
        file.write("Case #" + str(index+1) + ": IMPOSSIBLE\n")
    