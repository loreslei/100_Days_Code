student_scores = [150, 140, 180, 95, 120, 175, 200, 65, 130, 85, 110, 190, 145, 155, 170, 60, 135, 125, 185, 100]

#total_exam_score = sum(student_scores)

#print(total_exam_score)

sum = 0
for score in student_scores:
    sum += score

print(sum)

#max_score = max(student_scores)

#print(max_score)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
        
print(max_score)