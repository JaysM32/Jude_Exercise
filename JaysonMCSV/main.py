import statistics as stat
import datetime as dt


def makedict(chosenfile):
    data = chosenfile.split("\n")
    res = {}

    for line in range(0,len(data)):
        temp = data[line].split(",")
        if line == 0:
            for header in data[line].split(","):
                res[header.strip('"')] = []
        else:
            if len(temp) == 1: break
            res["steps"].append(temp[0].strip())
            res["date"].append(temp[1].split('"')[1])
            res["interval"].append(temp[2].strip())

    return res


def part1(chosenfile):
    data = chosenfile.split("\n")
    missing = 0
    perdayDict = {}
    perdaysteps = []

    for line in range(len(data)):
        test = data[line].split(",")
        if test[0] == 'NA':
            missing += 1
            perdayDict.setdefault(test[1], 0)
            perdayDict[test[1]] = "NA"
        elif line > 0:
            if len(test) == 1: break
            perdayDict.setdefault(test[1], 0)
            perdayDict[test[1]] = perdayDict[test[1]] + int(test[0])
    for steps in perdayDict.values():
        if steps != "NA":
            perdaysteps.append(steps)
    mean = stat.mean(perdaysteps)
    median = stat.median(perdaysteps)

    return perdayDict,mean,median,missing


def part2(chosenfile):
    newfile = open("activityfilled.csv","w")
    data = chosenfile.split("\n")
    count = 0
    text = ""

    for line in range(len(data)):
        newdata = data[line].replace('"', "").replace('NA', '0').split(",")
        if line > 0:
            if len(newdata) == 1: break
            if newdata[1][8] == '0':
                if dt.datetime(int(newdata[1][:4]), int(newdata[1][5:7]), int(newdata[1][9])).weekday() < 5:
                    newdata.append('weekday')
                else:
                    newdata.append('weekend')
            elif newdata[1][8] != '0':
                if dt.datetime(int(newdata[1][:4]), int(newdata[1][5:7]), int(newdata[1][8:])).weekday() < 5:
                    newdata.append('weekday')
                else:
                    newdata.append('weekend')
        else: newdata.append("daytype")


        for items in newdata:
            count +=1
            if count <= 3: text = text + items + ","
            else:
                text = text + items + "\n"
                count = 0

    newfile.write(text)
    newfile.close()



if __name__ == '__main__':
    file = None
    with open("activity.csv", "r") as d:
        file = d.read()

    fileDict = makedict(file)
    # total = 570608
    ttlperday, mean, median, missingVal = part1(file)
    print("total steps = ", ttlperday)
    print("mean steps = ", mean)
    print("median steps = ", median)
    print("total missing = ", missingVal)
    part2(file)