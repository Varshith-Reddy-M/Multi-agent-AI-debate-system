import gradio as gr
from debate_engine import run_debate


def start_debate(topic):

    result = run_debate(topic)

    transcript = result["history"]

    judges = result["judges"]

    winner = result["winner"]

    analyzer = result["analysis"]

    return transcript, judges, winner, analyzer


with gr.Blocks() as app:

    gr.Markdown("# AI Debate Arena")

    gr.Markdown(
        "Multi-Agent AI Debate System with Autonomous Judging"
    )
    gr.Markdown("""
⚠ **Important Notice**

This application currently runs on **free-tier LLM APIs via OpenRouter**.

Due to provider limitations, you may occasionally experience:

- Slow responses  
- API rate limit errors  
- Temporary model unavailability  

If a debate fails, please retry after some time.
""")


    topic = gr.Textbox(
        label="Enter Debate Topic",
        placeholder="Should AI replace software engineers?"
    )


    start_button = gr.Button("Start Debate")


    transcript_output = gr.Textbox(
        label="Debate Transcript",
        lines=18
    )


    judges_output = gr.Textbox(
        label="Judge Decisions",
        lines=8
    )


    winner_output = gr.Textbox(
        label="Final Winner"
    )


    analyzer_output = gr.Textbox(
        label="Debate Analyzer",
        lines=12
    )


    start_button.click(
        fn=start_debate,
        inputs=topic,
        outputs=[
            transcript_output,
            judges_output,
            winner_output,
            analyzer_output
        ]
    )


app.launch()