# The Interactive Food Drive Assistant app

The Interactive Food Drive Assistant app is a streamlit app that uses the Gradient AI platform to generate responses to questions about the Food Drive.

The app uses a base model from Gradient AI, which is a natural language generation model called Nous Hermes2. The app creates a model adapter from the base model and fine-tunes it on a custom dataset of Food Drive instructions and responses. The app then uses the model adapter to complete the user's query and generate a response.

The app requires a Gradient access token and a Gradient workspace ID to connect to the Gradient AI platform. These are secrets that should not be exposed in the app code or the hosted repo. To securely store and use these secrets, the app uses the streamlit secrets management feature.

To add the secrets to the app, follow these steps:

- Go to share.streamlit.io and log in with your GitHub account.
- Find your app in the list of deployed apps and click on the menu icon on the right.
- Select Manage app from the menu and go to the Advanced settings tab.
- In the Secrets field, enter your secrets in the TOML format. For example:

    # These will be available as environment variables
    GRADIENT_ACCESS_TOKEN = "YOUR_TOKEN"
  
    GRADIENT_WORKSPACE_ID = "YOUR_WORKSPACE_ID"

- Save the changes and redeploy your app. Your secrets will be securely stored and accessed by your app.

For more information on how to use secrets management in streamlit, you can refer to the [streamlit docs](https://blog.streamlit.io/content/images/2021/08/gif-1-4.gif#browser) or the [streamlit blog](https://blog.streamlit.io/secrets-in-sharing-apps/).


[Link to App](https://chatbot-c9tfhdbmxtzoyx4fu9ferg.streamlit.app/)
