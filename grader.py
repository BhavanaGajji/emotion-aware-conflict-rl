def grade(task, action):
    return 1.0 if action == task["expected_action"] else 0.0