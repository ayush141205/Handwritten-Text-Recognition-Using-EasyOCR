from tkinter import *
from tkinter import filedialog
from preprocess import preprocess_image
from recognizer import recognize_text
from efficiency import *

import cv2

def upload_image():

    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg")
        ]
    )

    if not file_path:
        return

 
    processed = preprocess_image(file_path)

    cv2.imwrite("processed.png", processed)

  
    text, processing_time = measure_processing_time(
        recognize_text,
        processed
    )

   
    actual_text = "AYUSH IS STUPID"


    char_accuracy = calculate_accuracy(
        actual_text,
        text
    )

    word_accuracy = calculate_word_accuracy(
        actual_text,
        text
    )

    error_rate = calculate_error_rate(
        actual_text,
        text
    )

   
    output.delete("1.0", END)

    output.insert(
        END,
        f"Predicted Text:\n{text}\n\n"
    )

    output.insert(
        END,
        f"Character Accuracy: {char_accuracy}%\n"
    )

    output.insert(
        END,
        f"Word Accuracy: {word_accuracy}%\n"
    )

    output.insert(
        END,
        f"Error Rate: {error_rate}%\n"
    )

    output.insert(
        END,
        f"Processing Time: {processing_time} seconds"
    )

root = Tk()

root.title("Handwriting Recognition System")
root.geometry("800x600")

title = Label(
    root,
    text="Handwriting Recognition",
    font=("Arial", 18, "bold")
)

title.pack(pady=20)

upload_btn = Button(
    root,
    text="Upload Handwritten Image",
    command=upload_image,
    font=("Arial", 12),
    padx=10,
    pady=5
)

upload_btn.pack(pady=10)

output = Text(
    root,
    height=20,
    width=90,
    font=("Arial", 14),
    bg="white",
    fg="black"
)

output.pack(pady=20)

root.mainloop()