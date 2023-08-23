import gradio as gr
from transformers import pipeline

GenAI = pipeline('text-generation', model='gpt2')

def generate(text):
    result = GenAI(text, max_length=30, num_return_sequences=1)
    return result[0]['generated_text']

examples= [
    ["how many planets are there"],
    ["what does earth consists of"]
]

mkk = gr.Interface(fn =generate,
                   inputs=gr.inputs.Textbox(lines=5,label="Input text..."),
                   outputs=gr.outputs.Textbox(label="Generated text"),
                   examples=examples
                   )
mkk.launch()
