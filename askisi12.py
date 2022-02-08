from urllib.request import Request, urlopen

# Οι γύροι είναι από 1627331 έως 1627430

text= ""

round = "1627431"
for  i in range (100):
    req = Request('https://drand.cloudflare.com/public/' + round, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    round = int(round) - 1
    round = str (round)
    data = urlopen(req).read()
    text = text + str(data[31:95],"utf-8")

temp = int(text,16)

temp2= bin(temp)

final = temp2[2:]

# Μέγιστες ακολουθίες
max0 = -1
max1 = -1

# Πλήθος συνεχόμενων ψηφίων
pl0 = 0
pl1 = 0

for i in range (len(final)-1):

    if final[i] == "0" and  final[i+1] == "0":
        pl0 = pl0 +1
        if pl0 > max0:
            max0 = pl0
    else:
        pl0 = 0

    if final[i] == "1" and final[i+1] == "1":
        pl1 +=1
        if pl1 > max1:
            max1 = pl1
    else:
        pl1 = 0
    
print ("H megaluterh akolou8ia apo mhdenika einai ish me:", max0)
print ("H megaluterh akolou8ia apo assous einai ish me:", max1)