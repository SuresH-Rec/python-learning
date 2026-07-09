questions = [
    {
        "question": "What does Boolean search use to combine keywords?",
        "options": ["Commas", "AND / OR / NOT", "Hashtags", "Semicolons"],
        "answer": "B",
        "explanation": "AND, OR, NOT are Boolean operators used to combine or exclude keywords."
    },
    {
        "question": "What does TAT stand for in recruitment?",
        "options": ["Turn Around Time", "Take At Time", "Turn And Take", "Time Analytics Turn"],
        "answer": "A",
        "explanation": "Turn Around Time is the agreed time to deliver hiring outcomes to stakeholders."
    },
    {
        "question": "What is the Boolean keyword used for excluding a skill?",
        "options": ["AND", "NOR", "NEITHER", "NOT"],
        "answer": "D",
        "explanation": "When NOT is used before a skill in the string it excludes that specific skill."
    },
    {
        "question": "What is the key metric to track an active requisition?",
        "options": ["Positions", "Role", "Ageing", "Skills"],
        "answer": "C",
        "explanation": "Requisition Ageing is a key metric to understand how long a position has been active."
    },
    {
        "question": "What does TTF stand for in recruitment?",
        "options": ["Time To Off", "Time To Fill", "Turn Time Fall", "Turn To Fill"],
        "answer": "B",
        "explanation": "Time To Fill measures how long it takes to close a requisition from opening to joining."
    },
    {
        "question": "Which sourcing platform is most used for tech hiring in India?",
        "options": ["Naukri", "Uphill", "NEET", "JEE"],
        "answer": "A",
        "explanation": "Naukri is one of the most popular and oldest sourcing platforms in India."
    },
    {
        "question": "What does ATS stand for?",
        "options": ["Application Transport System", "Applicant Tracking System",
                    "Application Training Science", "Artificial Tracking System"],
        "answer": "B",
        "explanation": "Applicant Tracking System is where recruiters maintain the entire recruitment pipeline."
    },
    {
        "question": "What is a Boolean string enclosed in quotes used for?",
        "options": ["Exact phrase search", "Either Any", "Split the phrase", "Ignore"],
        "answer": "A",
        "explanation": "Enclosing a phrase in quotes searches for that exact phrase in the results."
    },
    {
        "question": "What metric measures how many offered candidates actually join?",
        "options": ["Offer to Join Ratio", "Accepted Ratio", "No of Offers Made", "Offers in Pipeline"],
        "answer": "A",
        "explanation": "Offer to Join Ratio tracks actual joining against offers made — a key quality metric."
    },
    {
        "question": "What does SLA stand for in recruitment?",
        "options": ["Service Level Application", "Service Level Arrangement",
                    "Service Level Array", "Service Level Agreement"],
        "answer": "D",
        "explanation": "Service Level Agreement is the binding commitment between recruiter and client on timelines."
    }
]
 
 
# ── STAGE 2: ASK QUESTION FUNCTION ──────────────────────────
 
def ask_question(q_num, q):
    """Display one question, get and validate the answer, return True/False."""
    print(f"\nQ{q_num}. {q['question']}")
    print(f"   A) {q['options'][0]}")
    print(f"   B) {q['options'][1]}")
    print(f"   C) {q['options'][2]}")
    print(f"   D) {q['options'][3]}")
 
    while True:
        answer = input("   Your answer (A/B/C/D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            break
        print("   ⚠️  Invalid input. Please enter A, B, C or D.")
 
    if answer == q["answer"]:
        print("   ✅ Correct!")
        print(f"   💡 {q['explanation']}")
        return True
    else:
        print(f"   ❌ Wrong! Correct answer is {q['answer']}.")
        print(f"   💡 {q['explanation']}")
        return False
 
 
# ── STAGE 3: GRADE FUNCTION ─────────────────────────────────
 
def get_grade(score):
    """Return grade and feedback based on score."""
    if score == 10:
        return "Expert Recruiter", "Outstanding! You have excellent recruitment knowledge."
    elif score >= 8:
        return "Senior Recruiter Level", "Great job! You have strong recruitment skills."
    elif score >= 6:
        return "Mid-Level Recruiter", "Good effort! Keep improving your knowledge."
    else:
        return "Keep Practicing", "Don't worry — practice more and you will improve!"
 
 
# ── STAGE 4: MAIN QUIZ ──────────────────────────────────────
 
print("=" * 50)
print("   🎯  TECH RECRUITER QUIZ")
print("   Test your recruitment knowledge!")
print("=" * 50)
print("Answer each question by typing A, B, C, or D.")
print(f"Total Questions: {len(questions)}\n")
 
score = 0
 
for i, q in enumerate(questions, start=1):
    if ask_question(i, q):
        score += 1
 
# Results
grade, feedback = get_grade(score)
 
print("\n" + "=" * 50)
print("   📊  QUIZ RESULTS")
print("=" * 50)
print(f"   Your Score  : {score}/{len(questions)}")
print(f"   Grade       : {grade}")
print(f"   Feedback    : {feedback}")
print("=" * 50)
print("\nThank you for taking the Tech Recruiter Quiz!")
print("Keep learning and keep growing. 🚀")
