# 🚀 AWS Lambda Mini Projects

This repository contains two small projects demonstrating AWS Lambda use cases:  
1. A **Matrix Transposition Layer**
2. An **S3 File Size Alert Function**

Each project highlights key AWS concepts like Lambda Layers, S3 event triggers, and serverless best practices.

---

## 📦 Project 1: Matrix Transposition with AWS Lambda

### 🧩 Overview
This project demonstrates how to build a reusable AWS Lambda Layer that contains a Python function to transpose a 2D matrix.

### 📁 Structure
- The core function is defined in **`matrix_transformation_layer.py`**.
- The function is placed inside a `python/` directory (as required by Lambda Layer packaging conventions).
- The layer is zipped and deployed as a **Lambda Layer**.
- A separate Lambda function then imports this layer and uses the transposition logic.

### 🔧 Concepts Covered
- Lambda Layers
- Code modularization and reuse
- Python-based matrix operations

---

## 📂 Project 2: S3 File Size Alert with AWS Lambda

### 🧩 Overview
This project sets up an AWS Lambda function that is triggered by file upload events to an S3 bucket. The function checks the size of each uploaded file and logs an alert if the size exceeds **100MB**.

### 📁 Structure
- Lambda function logic is written in **`check-file-size-alert.py`**.
- Triggered automatically by **S3 event notifications** (specifically `s3:ObjectCreated:*`).
- Uses `head_object` to fetch metadata and log alerts for oversized files.

### 🔧 Concepts Covered
- AWS Lambda + S3 integration
- Event-driven architecture
- File metadata handling
- Logging and alerting