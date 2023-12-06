import streamlit as st
from gradientai import Gradient

# Fetch API keys from Streamlit Secrets
gradient_access_token = st.secrets["gradient"]["access_token"]
gradient_workspace_id = st.secrets["gradient"]["workspace_id"]

if gradient_access_token is None or gradient_workspace_id is None:
    st.error("API key or workspace ID not found. Please set the secrets in the Streamlit Sharing dashboard.")
    st.stop()

def main():
    # Streamlit title and description
    st.title("Interactive Food Drive Assistant")
    st.write("Ask a question about the Food Drive!")

    with Gradient(api_key=gradient_access_token, workspace_id=gradient_workspace_id) as gradient:
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
