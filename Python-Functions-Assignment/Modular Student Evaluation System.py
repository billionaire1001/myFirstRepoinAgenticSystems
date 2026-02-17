def greet_student(name):
    return f"Hello, {name}"


def get_score_stats(scores):
    num_subjects = len(scores)
    average = sum(scores) / num_subjects if num_subjects > 0 else 0
    return num_subjects, average


def get_result(average_score):
    if average_score >= 50:
        return "Pass"
    return "Fail"


def main():
    student_name = "Alice"
    scores = [60, 70, 65]

    greeting = greet_student(student_name)
    num_subjects, average_score = get_score_stats(scores)
    result = get_result(average_score)

    print(greeting)
    print(f"Subjects: {num_subjects}")
    print(f"Average Score: {average_score}")
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
