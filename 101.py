

from clearml import Task
import random
import os
from dotenv import load_dotenv

load_dotenv()

def prompt_response (prompt):
    return "dummy response  for prompt: " + prompt

#create a clearml task
task = Task.init(project_name="LLM", task_name="LLM Chat")

prompts = [
    "Tell me a fun fact about space.",
    "Who is Apple CEO.",
    "What is the capital of France?",
]

for prompt in prompts:
    response = prompt_response(prompt)
    # print(f"Prompt: {prompt}")
    # print(f"Response: {response}")
    # Log data to ClearML
    task.get_logger().report_text(f"Prompt: {prompt}")
    task.get_logger().report_text(f"Response: {response}")

# Finalize the experiment
task.close()
print("Experiment logged in ClearML.")
