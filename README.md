# SubbyBank
A small fullly functinoal  banking application which is authenticated with Jwt, Razorpay Integration,ml models for loan eligibility check  &amp; potential fraud detection ,Ai chatbot integration and much more 
# 💳  AI-Powered Banking System  

### 🚀 Made with Spring Boot + React + Python + MySQL  

SmartBank is a **full-stack AI-integrated digital banking system** that provides seamless banking operations for users and powerful administrative controls for the bank.  
It combines **Spring Boot**, **Python ML models**, **React**, and **MySQL** to deliver a secure, intelligent, and modern banking experience.  

---

## 🧠 Overview  

### 🔹 Technologies Used  
| Stack | Technology |
|--------|-------------|
| **Frontend** | React.js, Axios, Tailwind CSS |
| **Backend (Core)** | Spring Boot (Java) |
| **Backend (AI/ML)** | Python (Flask/FastAPI for model services) |
| **Database** | MySQL |
| **Payment Gateway** | Razorpay |
| **ML Libraries** | scikit-learn, XGBoost, imbalanced-learn, NumPy, Pandas |
| **Containerization** | Docker |

---

## 👤 User Features  

✅ **Authentication System**  
- Secure **User Signup / Login**  
- JWT-based authentication  
- Password encryption  

✅ **Banking Operations**  
- **Create a Bank Account** instantly after signup  
- **Add Money** to account using **Razorpay** payment gateway  
- **Check Transaction History** with filters and sorting  
- **Transfer Money**:
  - Within the same bank  
  - To external bank accounts  

✅ **Loan Services**  
- **Apply for a Loan**  
- **AI-based Loan Eligibility Check** using a trained **Python model**  
- **View Loan Status**  
- **Repay Loan** directly from account balance  

✅ **AI Chatbot Assistant** 🤖  
- Integrated **AI Chatbot** to help users with:  
  - Account-related queries  
  - Loan and repayment help  
  - Fraud warnings  
  - General assistance  

---

## 🧑‍💼 Admin Features  

✅ **Admin Dashboard**  
- View and manage **all users and transactions**  
- Edit / Delete **User Accounts**  
- Edit / Delete **Bank Accounts**  

✅ **Loan Management**  
- Approve or Reject Loan Applications  
- Monitor **Loan Repayments** by ID  

✅ **Transaction Management**  
- View all transactions  
- Filter or **search transactions by ID**  
- View repayment details by ID  

✅ **Fraud Detection System** ⚠️  
- Uses a **Python-based XGBoost ML model** to detect **potential fraudulent transactions** in real time  
- Flag suspicious users and accounts  

✅ **Security Actions**  
- **Block Bank Accounts** — once blocked, the user **cannot send or receive money**  
- **Delete / Update** accounts or loans as required  

---

## 🧠 Machine Learning Integration (Python)  

### 1️⃣ **Loan Eligibility Prediction Model**
- Trained on synthetic + real-like financial data  
- Predicts if a user qualifies for a loan based on salary, credit history, and existing debts  

### 2️⃣ **Fraud Detection Model**
- Built using **XGBoost** and **SMOTE** for handling class imbalance  
- Features used:  
  - Transaction amount  
  - Time of transaction (hour)  
  - Country risk factor  
  - Foreign transaction flag  
  - Historical spending pattern  
- Automatically flags suspicious activity to the admin dashboard  

---


