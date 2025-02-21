# 🚀 Daily Report Mailer

A simple automation script to send daily reports via email.

## 📌 Steps to Set Up and Run

### **Step 1: Start the API Server**
1. Open the `apiserver` folder.
2. Run the following commands:
   ```sh
   npm install
   nodemon server.js
   ```

### **Step 2: Configure Email Settings**
- Modify `config.py` to:
  - Set the **sender email**.
  - Set the **receiver email**.
  - Configure the **API endpoint** for email dispatch.

### **Step 3: Run the Report Mailer**
1. Open the `report-mailer` folder.
2. Install dependencies and start the script:
   ```sh
   pip install -r requirements.txt
   python main.py
   ```

---

