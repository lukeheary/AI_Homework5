# Created by: Luke Heary and Dylan Jackson
# Date: 12/2/19

# cherry = 0
# lime = 1
def makeData(cherryCount, limeCount):
    dataSet = list()
    for x in range(0, cherryCount):
        dataSet.append(0)
    for x in range(0, limeCount):
        dataSet.append(1)
    return dataSet


def main():
    bag1 = .10
    bag2 = .20
    bag3 = .40
    bag4 = .20
    bag5 = .10

    h1 = makeData(100, 0)
    h2 = makeData(75, 25)
    h3 = makeData(50, 50)
    h4 = makeData(25, 75)
    h5 = makeData(0, 100)


main()
