1. 📦 Matrix Transposition with AWS Lambda
This project demonstrates how to build a reusable AWS Lambda Layer containing a Python function to transpose a 2D matrix. The function is defined in matrix_transformation_layer.py, placed under a python/ directory, and packaged as a Lambda Layer. A separate AWS Lambda function then imports this layer to perform the matrix transposition.

2. 📦 S3 File Size Alert with AWS Lambda
This project sets up an AWS Lambda function that is triggered by file upload events to an Amazon S3 bucket. The Lambda function, defined in `check-file-size-alert.py`, inspects the size of each uploaded file. If a file exceeds 100MB, it logs an alert. This project demonstrates event-driven processing using AWS Lambda and S3, along with basic file metadata handling and logging practices.
