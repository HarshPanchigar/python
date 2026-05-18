def sumData(data):
    return sum(data)

disc_p = 10
def disc(sub):
    return sub - (sub * (disc_p/100))

data = [1,2,3,4,5]
print(sumData(data))
sub = sumData(data)
print(disc(sub))