inputs=input()
inputlist=inputs.split()
maximum=float(inputlist[0])
minimum=float(inputlist[0])
for i in inputlist:
    if float(i)>maximum:
        maximum=float(i)
    elif float(i)<minimum:
        minimum=float(i)
if maximum%1==0.0:
    maximum=int(maximum)
if minimum%1==0.0:
    minimum=int(minimum)
print('Minimum =',minimum)
print('maximum =',maximum)
