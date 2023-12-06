# Import necessary libraries
import streamlit as st
from gradientai import Gradient
import os
os.environ['GRADIENT_ACCESS_TOKEN'] = "dnDfqMBrmGSG5ZQ7Yze64mcfx4RVGGHy"
os.environ['GRADIENT_WORKSPACE_ID'] = "4aff21f7-6c85-463c-a3eb-4edd81ffe0ff_workspace"

def main():
    # Streamlit title and description
    st.title("Interactive Food Drive Assistant")
    st.write("Ask a question about the Food Drive!")

    with Gradient() as gradient:
        base_model = gradient.get_base_model(base_model_slug="nous-hermes2")
        new_model_adapter = base_model.create_model_adapter(name="interactive_food_drive_model")

        user_input = st.text_input("Ask your question:")
        if user_input and user_input.lower() not in ['quit', 'exit']:
            sample_query = f"### Instruction: {user_input} \n\n### Response:"
            st.markdown(f"Asking: {sample_query}")

            # before fine-tuning
            completion = new_model_adapter.complete(query=sample_query, max_generated_token_count=100).generated_output
            st.markdown(f"Generated: {completion}")

        # Delete the model adapter after generating the response
        new_model_adapter.delete()

if __name__ == "__main__":
    main()
