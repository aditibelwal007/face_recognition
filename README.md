# face_recognition
Face recognition is a computer vision technique used to identify or verify individuals by analyzing and comparing facial features from images or video frames. With Python, it becomes accessible and efficient using libraries like OpenCV, face_recognition, and dlib.

# 👁️‍🗨️ Face Recognition Using Python

This project demonstrates a real-time face recognition system built using **Python**, **OpenCV**, and the **face_recognition** library. It captures video through a webcam, detects faces, and recognizes individuals based on pre-trained images.

---

## 📚 Table of Contents

- [Features](#features)  
- [Demo](#demo)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Contributing](#contributing)  
- [Contact](#contact)

---

## ✅ Features

- 🎯 Real-time face detection and recognition via webcam  
- 🔍 Automatic face encoding and comparison with known faces  
- 🧠 Labels recognized faces with names  
- 🚫 Identifies unknown faces  
- 🖼️ Uses `dlib` via `face_recognition` for precise accuracy  
- 💡 Easy to extend with more known faces

---

## 💻 Installation

To run this project locally, follow these steps:

1. **Clone the repository**
```bash
git clone https://github.com/your-username/face-recognition-python.git
cd face-recognition-python

Install required dependencies

bash

pip install face_recognition opencv-python numpy

```
⚙️ Usage
Place your known face images in the project folder (e.g., person.jpg).

Update the image filename in the script.

Run the script:

bash
Copy
Edit
python face_recognition_live.py
Press Q to quit the webcam window.

🧠 How It Works
Loads a known image and encodes it.

Opens a webcam stream.

Detects faces and encodes them in real-time.

Compares detected faces with known encodings.

Displays the name if matched, otherwise "Unknown".

🤝 Contributing
Contributions are welcome and appreciated! Here's how you can contribute:

Fork this repository

Create a new branch (git checkout -b feature/YourFeature)

Commit your changes (git commit -m 'Add your feature')

Push to the branch (git push origin feature/YourFeature)

Open a Pull Request

📬 Contact
Feel free to reach out with suggestions or questions:

🌐 Website: www.aditibelwal.dev

💼 GitHub: @aditibelwal007

🔗 LinkedIn: Aditi Belwal
