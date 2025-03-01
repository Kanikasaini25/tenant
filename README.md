# tenant
# 🏢 Multi-Tenant SaaS Application using Django

## 🚀 Overview
A **multi-tenant SaaS application** built with Django & Django REST Framework (DRF).  
Supports **multiple organizations (tenants)**, **JWT authentication**, **user management**, and **AWS S3 media storage**.

---

## 🛠 Features
✅ Multi-Tenant Architecture (Isolated data per tenant)  
✅ JWT Authentication (Secure login & session management)  
✅ User & Admin Management  
✅ AWS S3 Storage for Media Uploads  
✅ Role-Based Access Control  

---

## 📌 Tech Stack
- **Backend**: Django, DRF, SimpleJWT  
- **Database**: MySQL 
- **Storage**: AWS S3  
- **Authentication**: JWT Tokens  


Please Configure S3

SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/multi_tenant_db
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_STORAGE_BUCKET_NAME=your_s3_bucket_name
