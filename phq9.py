# from flask import render_template

# # Define the PHQ-9 questions and scoring options
# questions = [
#     "Little interest or pleasure in doing things?",
#     "Feeling down, depressed, or hopeless?",
#     "Trouble falling or staying asleep, or sleeping too much?",
#     "Feeling tired or having little energy?",
#     "Poor appetite or overeating?",
#     "Feeling bad about yourself — or that you are a failure or have let yourself or your family down?",
#     "Trouble concentrating on things, such as reading the newspaper or watching television?",
#     "Moving or speaking so slowly that other people could have noticed? Or the opposite — being so fidgety or restless that you have been moving around a lot more than usual?",
#     "Thoughts that you would be better off dead or of hurting yourself in some way?"
# ]

# scoring_options = [
#     "Not at all",
#     "Several days",
#     "More than half the days",
#     "Nearly every day"
# ]

# # Define the PHQ-9 scoring algorithm
# def detect_depression(scores):
#     total_score = sum(scores)
#     if total_score >= 20:
#         return "Severe"
#     elif total_score >= 15:
#         return "Moderate"
#     elif total_score >= 10:
#         return "Mild"
#     else:
#         return "None"

# # Define the function for getting PHQ-9 scores from the form data
# def get_phq_scores(form):
#     scores = []
#     for i in range(1, 10):
#         question = 'question_' + str(i)
#         answer = int(form[question])
#         scores.append(answer)
#     return scores

# # Define the route for the PHQ-9 questions
# def phq9_questions():
#     return render_template('phq9_questions.html', questions=questions, options=scoring_options)
# #
# # Define the route for the PHQ-9 result
# def phq9_result(form):
#     scores = get_phq_scores(form)
#     severity = detect_depression(scores)
#     return render_template('phq9_result.html', scores=sum(scores), severity=severity)
