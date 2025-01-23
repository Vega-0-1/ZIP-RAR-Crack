
# ZIP & RAR Password Crack Tool

A Python-based tool for cracking passwords of ZIP and RAR files using brute force techniques. This tool allows users to efficiently attempt multiple password guesses using threading, enhancing the speed of cracking.

---

## 🚀 Features

- **Supports both ZIP and RAR files** for password cracking.
- **Multi-threading support** for faster operations.
- Provides **clear feedback** for every password attempt.
- Displays the cracked password upon success or informs if not found.

---

## 📋 Prerequisites

### Python Version
- Python 3.7 or higher.

### Required Libraries
Install the dependencies using:
```bash
pip install -r requirements.txt
```

Required libraries include:
- `rarfile`
- `zipfile`

---

## 🛠️ How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. Add a password list file (`PassWords.txt`) to the working directory.

3. Run the tool:
   ```bash
   python Password_Crack_tool.py
   ```

4. Follow the on-screen instructions:
   - Specify the **password list file** path.
   - Specify the **file type** (ZIP or RAR).
   - Enter the **path of the encrypted archive**.
   - Choose the number of threads to utilize.

5. The tool will attempt to crack the password and provide feedback.

---

## ⚠️ Disclaimer

This tool is for **educational purposes only**. Unauthorized use to access protected files is illegal. Use responsibly.

---

## 📞 Support

For issues, feel free to open a GitHub issue in the repository.

---

## 📜 License

This project is licensed under the MIT License.
