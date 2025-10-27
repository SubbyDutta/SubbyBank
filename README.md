# 💳 AI-Powered Banking System  

### 🚀 Made with Spring Boot + React + Python + PostgreSQL  

**SubbyBank** is a **full-stack AI-integrated digital banking system** that combines **Spring Boot**, **React**, **Python ML models**, and **PostgreSQL** to deliver a secure, intelligent, and scalable banking experience.  
Users can create accounts, perform transactions, apply for loans, and interact with an AI chatbot — while admins manage operations, detect fraud, and maintain complete control.  

---

## 🌐 Live Demo  
🔗 **Frontend:** (https://subbyfrontend.onrender.com)

---

## 🧠 Overview  

### 🔹 Technologies Used  

| Layer | Technology |
|--------|-------------|
| **Frontend** | React.js, Axios, **Bootstrap 5** |
| **Backend (Core)** | Spring Boot (Java, REST APIs, JWT Security) |
| **Backend (AI/ML)** | Python (Flask/FastAPI microservices) |
| **Database** | **PostgreSQL** (Production), MySQL (Local/Test) |
| **Payment Gateway** | Razorpay |
| **Machine Learning** | scikit-learn, XGBoost, imbalanced-learn, NumPy, Pandas |
| **Containerization** | Docker |
| **Deployment** | Render / Railway / Docker environments |

---

## 🔐 Security & Authentication  

✅ **JWT-Based Authentication**  
- Secure user login and signup using JSON Web Tokens  
- Tokens are validated in every API call for secure access  

✅ **Spring Security Configuration**  
- Prevents unauthorized domains or websites from accessing backend APIs  
- Cross-Origin Resource Sharing (CORS) configured only for verified frontend URLs  
- Passwords encrypted before storage  

✅ **Role-Based Authorization**  
- Separate access control for **Users** and **Admins**  
- Unauthorized users are blocked from accessing admin endpoints  

---

## 👤 User Features  

✅ **Account Management**  
- Create a bank account instantly after signup  
- Login securely using JWT  
- Add money to your account using **Razorpay Payment Gateway**  

✅ **Transactions**  
- Transfer money to internal or external accounts  
- View full transaction history with filters and sorting  

✅ **Loans**  
- Apply for loans anytime  
- **AI-based Loan Eligibility Check** powered by Python ML  
- Repay loans directly from account balance  

✅ **AI Chatbot Assistant** 🤖  
- Smart AI chatbot helps users with:  
  - Account balance queries  
  - Loan guidance and repayment info  
  - Fraud warnings  
  - General banking assistance  

---

## 🧑‍💼 Admin Features  

✅ **Admin Dashboard**  
- View and manage **all users, accounts, and transactions**  
- **Delete or update user accounts**  
- **Edit or delete bank accounts**  
- Monitor ongoing and repaid loans  

✅ **Fraud Detection System** ⚠️  
- Uses a **Python XGBoost model** to detect **potentially fraudulent transactions**  
- Fraud detection based on:  
  - Transaction amount  
  - Time of transaction  
  - Foreign or risky country flag  
  - Abnormal user spending patterns  
- Automatically flags suspicious activity in the dashboard  

✅ **Security Actions**  
- Block fraudulent or inactive user accounts  
- Delete, update, or modify user and loan records securely  
- Admin-only routes protected by JWT and role validation  

---

## 🧠 Machine Learning Integration  

### 1️⃣ Loan Eligibility Prediction Model  
- Trained on realistic banking and financial data  
- Predicts user’s eligibility based on income, debt ratio, and credit history  
- Returns **approval probability** with high accuracy  

### 2️⃣ Fraud Detection Model  
- Built using **XGBoost + SMOTE** for handling class imbalance  
- Detects anomalies and marks suspicious transactions in real-time  
- Features used include transaction value, time, location, and user pattern  

---

## 🧩 System Architecture  

**Frontend (React + Bootstrap)** →  
**Spring Boot Backend (JWT-secured APIs)** →  
**Python AI Microservices (Flask/FastAPI)** →  
**PostgreSQL Database**

All components communicate through secure REST endpoints, and unauthorized origins are automatically blocked via security configuration.

---

  


