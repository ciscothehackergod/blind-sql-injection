# blind-sql-injection
A blind SQL injection script that extracts data character-by-character using ASCII comparison. It targets vulnerable parameters to retrieve hidden values like admin passwords without direct output, ideal for boolean-based blind SQLi testing in ethical hacking and security research.

Sure! Here's a project description you can use for a portfolio, GitHub repo, or blog post:

---

### 🔍 **Blind SQL Injection Character Extraction Script**

This project demonstrates a practical implementation of **blind SQL injection** using ASCII-based character extraction. The script is designed to retrieve sensitive data (such as an admin password) from a vulnerable web application by leveraging **boolean-based SQL injection** techniques.

The core logic revolves around incrementally guessing each character of the target string using SQL functions like `SUBSTRING()` and `ASCII()`, and interpreting server responses to determine whether a guessed character is correct. For example:

```sql
ASCII(SUBSTRING((SELECT password FROM users WHERE username='admin'), 1, 1)) = 65
```

This checks if the first character of the admin’s password is `'A'` (ASCII 65). The script automates this process for all characters in the string, allowing full recovery of the password even when the application does not display direct SQL query results.

---

### ⚙️ **Features**

* Supports extraction of any column value character-by-character
* Uses ASCII code comparison for stealthy exfiltration
* Designed for boolean-based blind SQLi scenarios
* Fully customizable for table, column, and condition targeting

---

### 🚨 **Note**

This project is intended **strictly for educational and ethical purposes**. It highlights the importance of secure coding practices and demonstrates the critical need for input validation and parameterized queries in web applications.

---

Let me know if you'd like a readme, code snippet for the script, or to extend this for **time-based injection**, **error-based injection**, or even automate it with Python or Burp extensions.

