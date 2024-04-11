def sortScore(N):
    studentsScore = []
    for _ in range(N):
        name, kor, eng, math = input().split()
        kor, eng, math = int(kor), int(eng), int(math)
        studentsScore.append((name, kor, eng, math))
    studentsScore = sorted(studentsScore, key= lambda x: (-x[1], x[2], -x[3], x[0]))

    return studentsScore

N = int(input())

sortedScores = sortScore(N)

for studentScore in sortedScores:
    print(studentScore[0])