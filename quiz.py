def run_quiz():
    questions = [
        {"q": "What is the capital of France?", "a": "paris"},
        {"q": "What is 5 + 5?", "a": "10"}
    ]
    score = 0
    
    for item in questions:
        ans = input(item["q"] + " ").strip().lower()
        if ans == item["a"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            
    print(f"Your final score: {score}/{len(questions)}")

# run_quiz()