def calculate_user_averages(users):
    averages = []
    for user in users:
        scores = user["scores"]
        average = sum(scores) / len(scores) if scores else 0
        averages.append((user["name"], average))
    return averages


def has_admin_access(roles):
    return "admin" in roles


def main():
    users = [
        {
            "name": "Alice",
            "scores": [80, 85, 82, 83],
            "roles": {"admin", "editor"},
        },
        {
            "name": "Hammer",
            "scores": [70, 75, 72],
            "roles": {"viewer"},
        },
        {
            "name": "Tony Stark",
            "scores": [90, 88, 92],
            "roles": {"editor", "viewer"},
        },
    ]

    averages = calculate_user_averages(users)
    average_by_name = {name: avg for name, avg in averages}

    for user in users:
        name = user["name"]
        avg_score = average_by_name[name]
        admin_access = has_admin_access(user["roles"])

        print(f"Name: {name}")
        print(f"Average Score: {avg_score}")
        print(f"Admin Access: {admin_access}")
        print("-" * 20)


if __name__ == "__main__":
    main()