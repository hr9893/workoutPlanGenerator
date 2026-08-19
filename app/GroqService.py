from groq import Groq
import streamlit as st

class GroqService:

    def generate_response(self, fitness_data: str):

        client = Groq(api_key=st.secrets["GROQ_API_KEY"]) 

        prompt = f"""
You are a professional fitness planning assistant.

Create a personalized workout plan using the following user information :

Fitness Goal:{fitness_data['fitness_goal']}

Experience Level: {fitness_data['experience_level']}

Available Days: {fitness_data['available_days']}

Available Equipment:{fitness_data['available_equipment']}

injuries: {fitness_data['injuries']}

Create a workout plan based on this information.

Include:
- Workout for each day
- Exercises
- Sets
- Repetitions
- Rest periods
- General recommendations
"""

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{
                "role": "system",
                "content": "You are a professional fitness assistant."
            }, {
                "role": "user",
                "content": prompt
            }])

        return response.choices[0].message.content

