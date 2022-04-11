citations = [0,0,0,0,0]
citations.sort(reverse=True)

answer = 0

for i in range(len(citations)): # eg. [9,7,6,2,1] > i = 0~4
    if citations[i] >= i+1:
        answer = i+1

    else:
        break

print(answer)


