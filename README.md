# Handwriting Recognition System

A simple desktop application for handwritten text recognition built with Python, Tkinter, OpenCV, and EasyOCR. The app lets you upload an image, preprocesses it, runs OCR, and displays the predicted text along with basic timing and accuracy metrics.

## Features

- Upload handwritten images from a desktop GUI.
- Preprocess images with OpenCV before OCR.
- Recognize text using EasyOCR.
- Display predicted text, character accuracy, word accuracy, error rate, and processing time.

## Requirements

- Python 3.9 or newer
- Windows, macOS, or Linux with a working desktop environment
- Dependencies listed in `requirements.txt`

## Installation

1. Create and activate a virtual environment.
2. Install the dependencies:

```bash
pip install -r requirements.txt
```

If EasyOCR or OpenCV needs additional system packages on your platform, install those first using the instructions for your operating system.

## Running the App

Launch the GUI from the project root:

```bash
python main.py
```

In the app, click **Upload Handwritten Image**, choose a `.png`, `.jpg`, or `.jpeg` file, and wait for the OCR result.

## How It Works

- `main.py` starts the application.
- `gui.py` defines the Tkinter interface and the upload flow.
- `preprocess.py` resizes, converts to grayscale, and blurs the image.
- `recognizer.py` uses EasyOCR to extract text.
- `efficiency.py` calculates accuracy and timing metrics.

## Notes

- The app currently compares OCR output against a sample ground-truth string defined in `gui.py` when calculating accuracy metrics. If you want real evaluation, replace that string with the correct expected text for each image.
- The application saves the processed image as `processed.png` in the project root.

## Project Structure

```text
main.py
gui.py
preprocess.py
recognizer.py
efficiency.py
requirements.txt
```

## Troubleshooting

- If the app fails to open, confirm that your virtual environment is activated and all dependencies are installed.
- If EasyOCR cannot load, make sure PyTorch and the supporting packages from `requirements.txt` installed correctly.
- If image selection does nothing, check that the file is a supported image format and that the GUI window has focus.
