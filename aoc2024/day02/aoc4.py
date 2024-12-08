from aoc3 import readFile, checkRange, checkTrends

with open("aoc3-4.txt") as file_input:
    file = file_input.read().splitlines()

def isSafe(report):
    if checkRange(report) and checkTrends(report):
        return True

def isSafeRemoved(report):
    for i in range(len(report)):
        modified_list = report[:i] + report[i+1:]
        if checkRange(modified_list) and checkTrends(modified_list):
            return True
    return False

def countSafe(reports):
    safeReports = 0
    for element in reports:
        if isSafe(element) or isSafeRemoved(element):
            safeReports += 1
    return safeReports

if __name__ == "__main__":
    print(countSafe(readFile(file)))
