for i in range(1,5):
    score = int(input("Enter your score: "))
    documents_complete = bool(input("Enter whether documents are complete: "))
    attendance = int(input("Enter your attendance percentage: "))
    interview = float(input("Enter your interview score: "))
    def rule_based(score, documents_complete, attendance, interview):
        return "Review" if documents_complete and score >= 70 and attendance >= 75 and interview >= 60 else "Hold"
    probability = score/100  
    def probability_based(probability):
        return "Review" if probability >= 0.70 else "Hold"
    print(f"\ncase#0{i}")
    print("Score: ", score)
    print("Documents Complete: ", documents_complete)
    print("Attendance: ",attendance)
    print("Interview Score: ", interview)
    print("Output: ",rule_based(score, documents_complete, attendance, interview))
    print("\n")