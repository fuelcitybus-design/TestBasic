import gradio as gr

# Define a simple function
def greet(name):
    return f"Hello, {name}! Welcome to Azure + Gradio."

# Build Gradio interface
demo = gr.Interface(fn=greet, inputs="text", outputs="text")

# Expose Gradio app as WSGI callable for Gunicorn
app = demo.app

if __name__ == "__main__":
    # Local testing
    demo.launch(server_name="0.0.0.0", server_port=8000
