# pk-potter-sme

# Social Media Engagement Analyzer


The Social Media Engagement Analyzer is a web application built using Streamlit. It allows users to analyze social media engagement data, generate reports, and interact with a chatbot powered by Langflow for insights and queries. The app leverages several data visualization libraries to present metrics such as engagement rate, audience distribution, and more.



## FeaturesData Analysis: 
Analyze social media data from platforms like Instagram, Facebook, LinkedIn, and Twitter.
AI Insights: Get AI-powered insights based on your platform's data.
Custom Reports: Generate custom reports based on your platform and post type.
Chatbot Integration: Ask questions about your social media data, and get AI-powered responses.
## Prerequisites
Before running the app, ensure you have the following installed:

Python 3.10


## Installation

- Clone this repository or download the project files.

- Navigate to the project folder in your terminal.

- Install the required packages by running:


```bash
  pip install -r requirements.txt
```
- Set up environment variables by creating a ```.env``` file in the root directory. The variables include:

```
LANGFLOW_AUTH_TOKEN

LANGFLOW_REPORT_URL

LANGFLOW_CHATBOT_URL

ASTRA_DB_TOKEN

ASTRA_DB_ENDPOINT

ASTRA_DB_COLLECTION_NAME
```
    

## Running the App

After installing the requirements and setting up your environment variables, you can run the app using Streamlit.

- Navigate to the project directory in your terminal.

- Run the Streamlit app using the following command:
```
streamlit run home.py
```

- The app should open in your default web browser. If it doesn't, you can manually visit
``` 
http://localhost:8501
```





## Python Packages Used

- Streamlit: For building the interactive frontend.
- Pandas: For handling and processing data.
- Plotly: For interactive data visualizations (used in plot_functions).
- requests: For making HTTP requests to Langflow API.
- json: For handling JSON files, especially for Lottie animations and API responses.
- dotenv: For loading environment variables from a .env file.
- streamlit_lottie: For embedding Lottie animations.
- astra: For connecting to the Astra DB service to fetch data.
## Notes

- The app uses Astra DB for data storage, which is queried via an API.
- The app includes AI-powered insights through Langflow's API, providing real-time analysis and chatbot interactions.
- Ensure that your .env file is properly set up to access the APIs, and that the Astra DB collection contains the necessary data for analysis.
## Authors

- [@Kirubhaharan B](https://github.com/Kirubhaharan-B)
- [@Prashanth Rao](https://github.com/Prash099)


