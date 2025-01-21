import PyPDF2
from transformers import pipeline
from tkinter import Tk, messagebox
from tkinter.filedialog import askopenfilename

# Load the summarization model once
summarizer = pipeline("summarization", model="/home/kingston/my_model_cache/t5-large", tokenizer="/home/kingston/.cache/huggingface/t5-large")

# Step 1: PDF Reading Function
def read_pdf(file_path):
    """Read text from a PDF file."""
    pdf_text = ""
    try:
        with open(file_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page in reader.pages:
                text = page.extract_text()
                if text:  # Check if text extraction was successful
                    pdf_text += text
        return pdf_text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

# Step 2: Summarization Function
def summarize_text(text, max_length=130, min_length=30):
    """Summarize the provided text using a locally cached model."""
    try:
        # Chunk the text if it's too long
        if len(text) > 1024:  # Adjust this limit based on the model's max input size
            chunks = [text[i:i + 1024] for i in range(0, len(text), 1024)]
            summaries = [summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False) for chunk in chunks]
            return " ".join([summary[0]['summary_text'] for summary in summaries])
        else:
            summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
            return summary[0]['summary_text']
    except Exception as e:
        print(f"Error summarizing text: {e}")
        return None

# Step 3: Integration Function
def summarize_pdf(file_path):
    """Read a PDF file and summarize its content."""
    text = read_pdf(file_path)
    if text:
        print("PDF successfully read. Summarizing...")
        summary = summarize_text(text)
        if summary:
            print("Summary:")
            print(summary)
            messagebox.showinfo("Summary", summary)  # Show summary in a message box
        else:
            print("Failed to generate summary.")
            messagebox.showerror("Error", "Failed to generate summary.")
    else:
        print("Failed to read the PDF.")
        messagebox.showerror("Error", "Failed to read the PDF.")

# Example Usage
if __name__ == "__main__":
    # Prompt the user to select a PDF file
    Tk().withdraw()  # Hide the root Tkinter window
    file_path = askopenfilename(filetypes=[("PDF files", "*.pdf")], title="Select a PDF file")

    if file_path:
        summarize_pdf(file_path)
    else:
        print("No file selected.")
        messagebox.showwarning("Warning", "No file selected.")