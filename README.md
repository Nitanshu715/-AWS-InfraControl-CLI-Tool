# ⚙️ AWS InfraControl CLI Tool

> **Final Year Cloud Computing Project**  
> Real-time EC2 monitoring, automation & notification system using AWS CLI, Lambda, SNS, EventBridge & S3

---

## 📌 Overview

This tool monitors EC2 instance state changes (start, stop, terminate), sends real-time email alerts via Amazon SNS, and logs all changes to an Amazon S3 bucket using AWS Lambda. Built with a serverless approach and automated via Python scripts using AWS CLI & Boto3.

---

## 🚀 Features

- ✅ Monitor EC2 state changes automatically
- ✅ Log all events to S3 in structured JSON
- ✅ Get email notifications instantly via SNS
- ✅ Fully serverless with Lambda and EventBridge
- ✅ Python scripts to manage EC2 from CLI

---

## 🧠 Tech Stack

- AWS EC2, Lambda, S3, SNS, EventBridge, IAM
- Python 3.12
- AWS CLI & Boto3

---

## 🧾 Files Included

- `lambda_function.py` — Lambda to log EC2 events
- `auto_terminate.py` — Countdown-based termination
- `terminate_instance.py` — Terminates specific instance
- `recent_instance.py` — Terminates most recently launched EC2
- `CloudProjectSynopsisPart1.docx` & `Part2.docx` — Academic documentation
- `ProjectReportAWSInfraControlCLITool.docx` — Detailed project report
- `LICENSE` — MIT license

---

## 🛠️ How to Use

1. Configure AWS CLI:
```bash
aws configure
```

2. Run Python scripts as needed:
```bash
python auto_terminate.py
python terminate_instance.py
python recent_instance.py
```

3. Lambda function is triggered by EC2 events via EventBridge and logs to S3.

---

## 🧑‍💻 Author

**Nitanshu Tak**  
Email: nitanshutak070105@gmail.com

---

## 📜 License

MIT License — see `LICENSE` file for details.
