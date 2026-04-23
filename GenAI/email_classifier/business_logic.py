import json
from dotenv import load_dotenv
from openai import OpenAI
import os
import time
load_dotenv()

client = OpenAI()

def load_prompt(filename):
    path = os.path.join('prompts',filename)
    with open(path,'r') as f:
        return f.read()
    
def call_llm(prompt):
    response = client.chat.completions.create(
                 model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
               
            )
    return response.choices[0].message.content.strip()

# inside function 
def classify_with_cot(email):
    template = load_prompt('classify_cot.md')
    prompt = template.format(subject= email['subject'],body = email['body'],sender=email['sender'])
    result = call_llm(prompt)

    # extraction logic
    category, urgency = None, None
    for line in result.split('\n'):
        if 'CATEGORY' in line:
            category = line.split(':')[1].strip()
        if 'URGENCY' in line:
            urgency = line.split(':')[1].strip()

    return {
        'category': category,
        'urgency' : urgency,
        'full_output': result
    }
    
from collections import Counter
def classify_with_self_consistency(email,n_runs=5):
    template = load_prompt('classify_cot.md')
    results = []
    traces = []
    for i in range(n_runs):
        prompt = template.format(
            subject=email["subject"],
            body   =email["body"],
            sender =email["sender"]
        )
        result = call_llm(prompt)
        traces.append(result)

        # extract the category ??
        for line in result.split("\n"):
            if "CATEGORY" in line:
                results.append(line.replace("CATEGORY",'').strip())

    votes = Counter(results)
    winner = votes.most_common(1)[0]
    confidance_score = winner[1]/n_runs *100
    urgency = None
    for line in traces[0].split("\n"):      
          if "URGENCY:" in line:
            urgency = line.replace("URGENCY:", "").strip()
    return {
        "category": winner[0],
        "urgency": urgency,
        "confidence": confidance_score,
    }



def draft_response_with_tot(email, classification):
    template = load_prompt("tree_of_thought.md")
    prompt   = template.format(
        subject =email["subject"],
        body    =email["body"],
        category=classification["category"]
    )
    return call_llm(prompt)