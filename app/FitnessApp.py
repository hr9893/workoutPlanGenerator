import streamlit as st
from app.GroqService import GroqService


class FitnessApp:

    def __init__(self):
        self.groq_service = GroqService()

    def run(self):

        st.title("🏋️ Fitness Plan Generator")

        fitness_goal = st.selectbox(
            "Fitness Goal:",
            [
                "Build muscle",
                "Lose fat",
                "General fitness",
                "Improve endurance"
            ]
        )

        experience_level = st.selectbox(
            "Experience Level:",
            [
                "Beginner",
                "Intermediate",
                "Advanced"
            ]
        )

        available_days = st.slider(
            "Choose days:",
            min_value=1,
            max_value=7
        )

        available_equipment = st.selectbox(
            "Select Available Equipment:",
            [
                "No equipment",
                "Home dumbbells",
                "Full gym"
            ]
        )

        injuries = st.text_input(
            "Enter if any injuries:"
        )
        if st.button("Generate Plan", type="primary"):

            fitness_data = {
                "fitness_goal": fitness_goal,
                "experience_level": experience_level,
                "available_days": available_days,
                "available_equipment": available_equipment,
                "injuries": injuries
            }

            try:

                with st.spinner("Generating Fitness Plan..."):

                    response = self.groq_service.generate_response(
                        fitness_data
                    )

                # Store data in session
                st.session_state["fitness_plan"] = response
                st.session_state["fitness_data"] = fitness_data

            except Exception as e:

                st.error(
                    f"Exception occurred while getting the response "
                    f"from LLM: {e}"
                )

        if "fitness_plan" in st.session_state:

            st.subheader("Generated Fitness Plan")

            st.markdown(
                st.session_state["fitness_plan"]
            )

            st.download_button(
                label="📥 Download Plan",
                data=st.session_state["fitness_plan"],
                file_name="fitness_plan.txt",
                mime="text/plain"
            )

            if st.button("🔄 Regenerate Plan"):

                try:

                    with st.spinner("Regenerating your plan..."):

                        response = self.groq_service.generate_response(
                            st.session_state["fitness_data"]
                        )

                    st.session_state["fitness_plan"] = response

                    st.rerun()

                except Exception as e:

                    st.error(
                        f"Exception occurred while regenerating "
                        f"the plan: {e}"
                    )