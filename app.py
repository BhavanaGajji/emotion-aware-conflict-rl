import gradio as gr
import numpy as np
from env import CoupleConflictEnv
from tasks import TASKS
from grader import grade

env = CoupleConflictEnv()
q_table = np.load("q_table.npy")

def run_model():
    results = []

    output_text = ""

    for task in TASKS:
        state = env.set_state(task["state"])

        action = np.argmax(q_table[state[0], state[1], state[2]])
        score = grade(task, action)

        output_text += f"Task: {task['name']}\n"
        output_text += f"State: {state}\n"
        output_text += f"Action: {action}\n"
        output_text += f"Score: {score}\n"
        output_text += "------\n\n"

        results.append(score)

    final_score = sum(results) / len(results)

    output_text += f"Final Score: {final_score}"

    return output_text

demo = gr.Interface(
    fn=run_model,
    inputs=[],
    outputs="text",
    title="BhavanaBeginsML RL Demo"
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)