d = {'math': {'john': 90, 'jane': 80},
     'science': {'john': 85, 'jane': 95}}

inverted = {}

for subject,student_scores in d.items():
    for student,score in student_scores.items():
        if student not in inverted:
            inverted[student]={}
        inverted[student][subject]=score

print(inverted)