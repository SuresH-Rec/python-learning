def employee_rating(score):
    if score >= 90:
        return "outstanding"
    elif score >= 75:
        return "excellent"
    elif score >= 60:
        return "good"
    else:
        return "needs_improvement"


employees = [
    {"name": "Suresh.K", "score": 95},
    {"name": "Tushar.C", "score": 92},
    {"name": "Samyaka.L", "score": 88},
    {"name": "Parjwal.K", "score": 59},
    {"name": "Lavanya.C", "score": 65},
    {"name": "Praveen.D", "score": 75},
    {"name": "Keerthana.K", "score": 86},
    {"name": "Shivani.N", "score": 55}
]

outstanding = 0
excellent = 0
good = 0
needs_improvement = 0

for employee in employees:
    result = employee_rating(employee["score"])

    print(employee["name"], "-", result)

    if result == "outstanding":
        outstanding += 1
    elif result == "excellent":
        excellent += 1
    elif result == "good":
        good += 1
    else:
        needs_improvement += 1

print()
print("Summary Report")
print("----------------")
print("Total Outstanding      :", outstanding)
print("Total Excellent        :", excellent)
print("Total Good             :", good)
print("Needs Improvement      :", needs_improvement)
