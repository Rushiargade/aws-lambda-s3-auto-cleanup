# Automated S3 Bucket Cleanup Using AWS Lambda and Boto3

## 📌 Objective
The objective of this project is to automate the cleanup of an Amazon S3 bucket by deleting objects that are older than a specified time threshold using AWS Lambda and Boto3.

For testing purposes, the cleanup threshold has been set to **2 minutes** instead of 30 days.

---

## 🛠 AWS Services Used
- Amazon S3
- AWS Lambda
- AWS IAM
- Amazon CloudWatch Logs
- Boto3 (AWS SDK for Python)

---

## 📂 S3 Bucket Details
- **Bucket Name:** `s3-auto-cleanup-demo-r`
- The bucket contains multiple objects uploaded for testing the cleanup process.

---

## 🏷 Cleanup Logic
- Objects older than **2 minutes** are automatically deleted.
- The object age is determined using the `LastModified` timestamp from S3.

---

## 🧾 IAM Role & Permissions
The Lambda function uses an IAM role with the following policies:
- `AmazonS3FullAccess`
- `AWSLambdaBasicExecutionRole`

> Note: In real-world scenarios, permissions should be restricted following the principle of least privilege.

---

## 🧠 Lambda Function Workflow
1. Initialize the S3 client using Boto3
2. List all objects in the specified S3 bucket
3. Compare object `LastModified` time with the cutoff time
4. Delete objects older than the defined threshold
5. Log deleted object names in CloudWatch

---

## 🧪 Testing Procedure
1. Upload files to the S3 bucket
2. Wait for more than **2 minutes**
3. Manually invoke the Lambda function
4. Verify:
   - Old files are deleted from the bucket
   - Logs appear in CloudWatch showing deleted objects

---

## 📜 Lambda Code
The main Lambda function code is available in: lambda_function.py
