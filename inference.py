from env import CoupleConflictEnv
from tasks import TASKS
from grader import grade
import numpy as np

env = CoupleConflictEnv()

# 🔥 LOAD TRAINED MODEL
q_table = np.load("q_table.npy")

def run():
    results = []
    details = []

    for task in TASKS:
        state = env.set_state(task["state"])

        action = int(np.argmax(q_table[state[0], state[1], state[2]]))

        score = grade(task, action)

        # store details (instead of only printing)
        details.append({
            "task": task["name"],
            "state": state,
            "action": action,
            "score": score
        })

        results.append(score)

    final_score = sum(results) / len(results)

    return final_score, details


# Optional CLI run (still works locally)
if _name_ == "_main_":
    score, details = run()
    print("Final Score:", score)
    for d in details:
        print(d)