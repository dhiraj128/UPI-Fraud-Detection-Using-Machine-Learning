# UPI Fraud Detection Using Machine Learning

This project focuses on detecting fraudulent transactions in the Unified Payments Interface (UPI) system using machine learning techniques. The goal is to build a robust fraud detection system that can identify suspicious activities in real-time and enhance the security of digital payment systems.

---

## Dataset Description

The UPI Fraud Detection dataset consists of **647 transactions** with **20 attributes**, aiming to identify fraudulent activities in online transactions. The dataset contains various features that describe transaction details, user behavior, and network information. Key attributes include:

- **Transaction Metadata**:
  - `Transaction_ID`: Unique identifier for each transaction.
  - `Merchant_ID`: Identifier for the merchant involved in the transaction.
  - `Customer_ID`: Identifier for the customer involved in the transaction.
  - `Device_ID`: Identifier for the device used in the transaction.
  - `Date` and `Time`: Timestamp of the transaction.

- **Transaction Details**:
  - `Transaction_Type`: Type of transaction (e.g., Refund, Bank Transfer, Subscription, Investment).
  - `Payment_Gateway`: Payment gateway used for the transaction.
  - `Transaction_City` and `Transaction_State`: Geographical location of the transaction.
  - `Transaction_Amount`: Amount involved in the transaction.

- **Network and Device Information**:
  - `IP_Address`: IP address used for the transaction.
  - `Device_OS`: Operating system of the device used.
  - `Transaction_Status`: Status of the transaction (e.g., Success, Failed).

- **Behavioral Features**:
  - `Transaction_Frequency`: Frequency of transactions by the customer.
  - `Merchant_Category`: Category of the merchant.
  - `Transaction_Channel`: Channel used for the transaction (e.g., Mobile App, Web).
  - `Transaction_Amount_Deviation`: Deviation from the average transaction amount.
  - `Days_Since_Last_Transaction`: Days since the customer's last transaction.

- **Target Variable**:
  - `is_fraud`: Fraud label (`0` = Not Fraud, `1` = Fraud).

---

## Methodology

The project follows the following steps:

1. **Data Preprocessing**:
   - Handle missing values and outliers.
   - Encode categorical variables (e.g., `Transaction_Type`, `Payment_Gateway`).
   - Normalize numerical features (e.g., `Transaction_Amount`).

2. **Feature Engineering**:
   - Create new features such as transaction frequency and time-based patterns.
   - Analyze geographical inconsistencies and device usage patterns.

3. **Model Training**:
   - Train machine learning models such as Logistic Regression, Random Forest, and Gradient Boosting (XGBoost).
   - Evaluate models using metrics like accuracy, precision, recall, F1-score, and ROC-AUC.

4. **Real-Time Fraud Detection**:
   - Develop a web-based interface using Flask for real-time transaction analysis.
   - Allow users to upload transaction data and view fraud detection results.

5. **Model Evaluation**:
   - Compare the performance of different models.
   - Identify the best-performing model for deployment.

---

## Results

The Random Forest algorithm achieved the best performance with the following metrics:
- **Accuracy**: 98.5%
- **Precision**: 97.8%
- **Recall**: 96.2%
- **F1-Score**: 97.0%
- **ROC-AUC**: 99.1%

The web-based interface provides a user-friendly platform for uploading transaction data and viewing fraud detection results. Users can analyze transactions in real-time and download the results for further review.

---

## How to Run the Code

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/upi-fraud-detection.git
   cd upi-fraud-detection
