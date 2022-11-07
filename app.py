# HuggingFace Spaces interface

import gradio as gr

from web_scrapers.web_scraper import minutes_scraper
from web_scrapers.web_scraper_summarizer import minutes_scraper_sum

with gr.Blocks() as app:
    gr.Markdown("Get the meeting minutes from a URL")
    with gr.Tab("Without Summary"):
        text_input = gr.Textbox()
        text_output = gr.JSON()
        text_button = gr.Button("Scrape")
    with gr.Tab("With Summary (Slower)"):
        text_input_sum = gr.Textbox()
        text_output_sum = gr.JSON()
        text_button_sum = gr.Button("Scrape & Summarize")

        with gr.Accordion("Note on Summary"):
            gr.Markdown("The summary is generated using AI. The summary is not perfect, but it is a good starting point for a quick overview of the meeting. Please bear in mind that this process may take longer depending on the amount of text to summarize.")


    text_button.click(minutes_scraper, inputs=text_input, outputs=text_output)
    text_button_sum.click(minutes_scraper_sum, inputs=text_input_sum, outputs=text_output_sum)

app.launch()