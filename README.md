# Multi-LLM Tweet Generator

## Overview

This project is a Streamlit application that generates tweets on a user-specified topic using a variety of Large Language Models (LLMs). Users can select their preferred LLM from a dropdown menu and customize the number of tweets to generate.

## Features

-   **Tweet Generation**: Creates tweets based on a topic and desired quantity provided by the user.
-   **Multi-LLM Support**: Integrates with several leading LLMs, allowing users to choose the model that best suits their needs.
-   **Interactive User Interface**: Provides a simple Streamlit interface for inputting topics, selecting LLMs, and viewing generated tweets.

## Available LLMs

The application currently supports the following Large Language Models:

-   **Google Gemini**:
    -   `gemini-1.5-flash-latest`
-   **OpenAI**:
    -   `gpt-3.5-turbo`
    -   `gpt-4`
-   **Anthropic Claude**:
    -   `claude-3-sonnet-20240229`
    -   `claude-3-haiku-20240307`
-   **Cohere**:
    -   `command-r`

## Setup and Usage

Follow these steps to set up and run the Multi-LLM Tweet Generator:

1.  **Clone the Repository (Optional)**:
    If you haven't already, clone this repository to your local machine:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Install Dependencies**:
    Install the necessary Python packages using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

3.  **API Key Configuration**:
    To use the various LLMs, you need to provide API keys for the respective services. These keys should be stored in Streamlit's secrets management.

    Create a file named `secrets.toml` in a `.streamlit` directory within your project's root folder (i.e., `.streamlit/secrets.toml`).

    Add your API keys to this file with the following structure:

    ```toml
    # .streamlit/secrets.toml

    GOOGLE_API_KEY = "your_google_api_key_here"
    OPENAI_API_KEY = "your_openai_api_key_here"
    ANTHROPIC_API_KEY = "your_anthropic_api_key_here"
    COHERE_API_KEY = "your_cohere_api_key_here"
    ```
    Replace `"your_..._api_key_here"` with your actual API keys.

4.  **Run the Streamlit Application**:
    Launch the application using the following command in your terminal:
    ```bash
    streamlit run main.py
    ```

5.  **Using the Application**:
    -   Once the application is running, open it in your web browser.
    -   Enter the **Topic** for which you want to generate tweets.
    -   Select the desired **Number of tweets**.
    -   Choose an **LLM** from the dropdown menu.
    -   Click the **Generate** button.
    -   The generated tweets will appear below the button.

    If an API key for the selected LLM is missing or incorrect, the application will display an error message. Ensure your `.streamlit/secrets.toml` file is correctly configured.
