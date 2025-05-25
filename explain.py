import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def explain_test_result(test_name, value, normal_range, status):
    prompt = (
        f"Explain this medical test result in simple terms:\n"
        f"Test: {test_name}\n"
        f"Value: {value}\n"
        f"Normal Range: {normal_range}\n"
        f"Status: {status}\n\n"
        f"What does this mean for the patient? Suggest any necessary follow-up actions."
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful medical assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7,
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Error generating explanation: {str(e)}"
