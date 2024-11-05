"""
Install an additional SDK for JSON schema support Google AI Python SDK

$ pip install google.ai.generativelanguage
"""

import os
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_schema": content.Schema(
        type=content.Type.OBJECT,
        enum=[],  # Remove quotes
        required=["chain_of_thought_1", "heatmap", "chain_of_thought_2", "final_evaluation"],  # Remove quotes
        properties={
            "chain_of_thought_1": content.Schema(
                type=content.Type.STRING,
                description="Explanation of the analysis approach and methodology for chunk analysis",
            ),
            "heatmap": content.Schema(
                type=content.Type.ARRAY,
                items=content.Schema(
                    type=content.Type.OBJECT,
                    enum=[],  # Remove quotes
                    required=["chunk", "score"],  # Remove quotes
                    properties={
                        "chunk": content.Schema(
                            type=content.Type.STRING,
                            description="A semantic unit of text being analyzed",
                        ),
                        "score": content.Schema(
                            type=content.Type.NUMBER,
                            description="Risk score between 0.12-0.20 indicates safe content and 0.85-0.99 indicates potential injection",
                        ),
                    },
                ),
            ),
            "chain_of_thought_2": content.Schema(
                type=content.Type.STRING,
                description="Analysis of relationships between chunks and identification of dangerous patterns",
            ),
            "final_evaluation": content.Schema(
                type=content.Type.BOOLEAN,
                description="True if dangerous contiguous poison patterns detected (multiple consecutive chunks scoring above 0.85)",
            ),
        },
    ),
    "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "hey sup",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"chain_of_thought_1\": \"The input text is a common greeting and does not contain any code or potentially harmful content. Therefore, the risk score is extremely low.\", \"chain_of_thought_2\": \"There are no code patterns or code injections in the input text, nor are there any potentially harmful relationships between the chunks. The text is simply a friendly greeting.\", \"final_evaluation\": false, \"heatmap\": [{\"chunk\": \"hey sup\", \"score\": 0.12}]}\n\n```",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)