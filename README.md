Welcome to the Python Utility Scripts Collection!
Hello there! 👋

This repository is packed with some handy Python scripts that cover a range of cool functionalities—from encrypting messages and securing images to checking password strength and logging activities. Whether you're learning Python or just looking for some ready-made utilities, there’s something here for you.

What's Inside?
CipherBox: Text Encryption and Decryption
ImageGuard: Secure Your Images
ImageDecryptor: Decrypt Your Images
PassSafe: Password Strength Checker
LogMaster: Comprehensive Logging System
Let’s dive in!

1. CipherBox: Text Encryption and Decryption
What’s this?

CipherBox is a simple tool to encrypt or decrypt text messages using a basic substitution cipher. Perfect if you want to play around with basic cryptography or keep a secret note!

Key Features:


Encrypts any message you enter.
Decrypts messages back to their original form.
Saves your plaintext messages in a CSV file called Blackbox.csv.
How to Use It:


Run the script and choose whether to encrypt or decrypt a message.
Enter your text, and the script will handle the rest.
You can keep going or exit whenever you’re done.
2. ImageGuard: Secure Your Images
What’s this?


ImageGuard is a quick and easy way to encrypt your image files using a key-based XOR operation. Think of it as putting a digital lock on your pictures!


Key Features:


Encrypts any image file with a key you provide.
Be aware that it modifies the original image file, so keep a backup just in case!
How to Use It:


Run the script and provide the path to the image you want to encrypt.
Enter a numeric key (your secret password for the image).
Voilà! Your image is now encrypted.
3. ImageDecryptor: Decrypt Your Images
What’s this?


ImageDecryptor is the companion tool for ImageGuard. If you’ve encrypted an image, this script will help you decrypt it using the same key.

Key Features:

Decrypts images encrypted with ImageGuard.
Needs the exact key used during encryption to unlock the image.
How to Use It:


Run the script and provide the path to the encrypted image.
Enter the decryption key (the same one you used for encryption).
Your image will be restored to its original form!
4. PassSafe: Password Strength Checker
What’s this?


PassSafe is a straightforward tool that helps you check whether your password is strong enough to keep your accounts secure.


Key Features:


Ensures your password is at least 8 characters long.
Checks for at least one uppercase letter, one lowercase letter, one digit, and one special character.
Gives you feedback on what’s missing if the password doesn’t meet the criteria.
How to Use It:


Run the script and enter the password you want to check.
The script will tell you if your password is strong or what you need to change.
5. LogMaster: Comprehensive Logging System
What’s this?

LogMaster is all about keeping track of what’s happening in your application. It logs messages of different severity levels (like debug, info, warning, error, and critical) to both your console and a log file.

Key Features:


Logs everything from debug info to critical errors.
Provides examples of how to log messages in functions to catch and report errors.
Saves logs to app.log and displays them in the console, so you never miss a thing!
How to Use It:


Run the script to see example log messages.
Use the provided divide function to test how logging works with different inputs (including errors like dividing by zero).
Getting Started
To start using these scripts, you'll need Python 3.x installed on your system. Some of the scripts require additional modules, like pandas for CipherBox.


Installation:


Clone this repository:

bash
Copy code
git clone https://github.com/yourusername/your-repo.git
cd your-repo
Install the necessary Python modules:

bash
Copy code
pip install pandas
