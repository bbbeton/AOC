with open("aoc3-4.txt") as file_input:
    file = file_input.read().splitlines()

def readFile(textFile):
    reports = []
    for line in textFile:
        reports.append(list(map(int, line.split())))
    return reports
    
def checkTrends(report):
    rising = True
    if report[0] > report[1]:
        rising = False 
    for i in range(1, len(report)):
        if rising and report[i-1] > report[i]:
            return False
        elif not rising and report[i-1] < report[i]:
            return False
    return True

def checkRange(report):
    for i in range(1, len(report)):
        difference = abs(report[i-1] - report[i])
        if difference > 3 or difference < 1:
            return False
    return True 

def countSafe(reports):
    safeReports = 0
    for element in reports:
        if checkRange(element) and checkTrends(element):
            safeReports += 1
    return safeReports

if __name__ == "__main__":
    print(countSafe(readFile(file)))
            
