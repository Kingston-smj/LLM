import PyPDF2
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Step 1: PDF Reading Function
def read_pdf(file_path):
    """Read text from a PDF file."""
    pdf_text = ""
    try:
        with open(file_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page in reader.pages:
                pdf_text += page.extract_text()
        return pdf_text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

# Step 2: Model Initialization
def initialize_model():
    """Download and initialize the model for summarization."""
    try:
        model_name = "sshleifer/distilbart-cnn-12-6"
        print("Downloading model and tokenizer...")
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
        print("Model and tokenizer successfully downloaded.")
        return summarizer
    except Exception as e:
        print(f"Error initializing model: {e}")
        return None

# Step 3: Summarization Function
def summarize_text(text, summarizer, max_length=130, min_length=30):
    """Summarize the provided text using a pre-trained model."""
    try:
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print(f"Error summarizing text: {e}")
        return None

# Step 4: Integration Function
def summarize_pdf(file_path, summarizer):
    """Read a PDF file and summarize its content."""
    text = read_pdf(file_path)
    if text:
        print("PDF successfully read. Summarizing...")
        summary = summarize_text(text, summarizer)
        if summary:
            print("Summary:")
            print(summary)
        else:
            print("Failed to generate summary.")
    else:
        print("Failed to read the PDF.")

# Example Usage
if __name__ == "__main__":
    # Initialize the model
    summarizer = initialize_model()
    if summarizer:
        # Prompt the user to select a PDF file
        Tk().withdraw()  # Hide the root Tkinter window
        file_path = askopenfilename(filetypes=[("PDF files", "*.pdf")], title="Select a PDF file")

        if file_path:
            summarize_pdf(file_path, summarizer)
        else:
            print("No file selected.")
    else:
        print("Failed to initialize the model.")