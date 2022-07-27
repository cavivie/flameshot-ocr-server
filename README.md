# Flameshot OCR Server

It is a simple ocr server using pytesseract for [flameshot](https://github.com/flameshot-org/flameshot)'s new feature: OCR Recognizer.

## Requirements

- python3
- tesseract


## Installation

A simple for macOS 
```
brew install python3

brew install tesseract

pip3 install pytesseract

git clone https://github.com/cavivie/flameshot-ocr-server.git

cd flameshot-ocr-server

python3 main.py 
```

## Notice

Launch flameshot-ocr-server, and use flameshot to capture and click OCR button to recognize.

Also can config a different ocr server url in flameshot configuration pane.