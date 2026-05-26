import gradio as gr

def greet(name):
    return f"Hello, {name}! Welcome to Azure + Gradio."

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

# Expose Gradio app for Gunicorn
app = demo.app
