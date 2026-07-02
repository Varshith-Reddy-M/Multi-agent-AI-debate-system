# agents.py

import os
import time
from openai import OpenAI
from dotenv import load_dotenv


# Load env
load_dotenv()


# OpenRouter client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


# Model
MODEL = "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"


# --------------------------------------------------
# UNIVERSAL STREAMING (terminal + future web UI)
# --------------------------------------------------
def run_agent_stream(prompt, stream_output=True):

    for i in range(3):

        full_response = ""

        try:

            stream = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                stream=True,
                temperature=0.3
            )

            for chunk in stream:

                # Skip malformed chunks
                if not chunk.choices:
                    continue

                delta = chunk.choices[0].delta

                # Some providers return empty delta
                if delta and delta.content:

                    token = delta.content

                    # Terminal mode → print live
                    if stream_output:
                        print(token, end="", flush=True)
                        time.sleep(0.03)

                    # Always save response
                    full_response += token


            # Only terminal mode needs newline
            if stream_output:
                print("\n")


            # Success
            if full_response:
                return full_response


            # Empty response
            if stream_output:
                print(f"Streaming attempt {i+1}: Empty response")


        except Exception as e:

            # Only print errors in terminal mode
            if stream_output:
                print(f"\nStreaming attempt {i+1} failed:", e)


        # Wait before retry
        time.sleep(3)


    return "[Streaming failed after 3 retries]"