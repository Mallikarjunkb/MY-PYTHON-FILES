# program using raspberry pi
import math
f = open('mydata.dat', 'w')
# loop
for degrees in range(720):
    #generate three data points
    si=math.sin(math.radians(degrees))
    co=0.5*math.cos(math.radians(degrees))
    if si>0:
        sq = 0.6
    else:
        sq = -0.6
    # write 3 data point to text file
    data = "{}{}{}{}\n".format(degrees,si,co,sq)
    f.write(data)

