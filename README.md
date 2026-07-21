# Revenue Cycle Management Agent

> An AI-powered Healthcare Revenue Cycle Management (RCM) system built using **FastAPI**, **Microsoft AutoGen 0.7.5**, **React TypeScript**, and **Streamlit**. The application automates healthcare insurance claim processing through a collaborative multi-agent workflow consisting of Claims Processing, Claim Validation, and Billing Review agents.

---

# Table of Contents

- Overview
- Features
- Solution Architecture
- Technology Stack
- Project Structure
- Backend Application
- React Frontend
- Streamlit Frontend
- Installation
- Running the Applications
- REST API
- Sample Request
- Sample Response
- Multi-Agent Workflow
- Logging
- Future Enhancements
- License

---

# Overview

Revenue Cycle Management (RCM) is a critical healthcare process responsible for managing insurance claims, billing, reimbursement, and payment workflows.

This project demonstrates how AI Agents can automate various RCM activities using AutoGen, reducing manual effort while improving claim accuracy and processing efficiency.

The system orchestrates multiple specialized AI agents that collaboratively:

- Validate patient and claim information
- Detect billing inconsistencies
- Review insurance claims
- Generate billing recommendations
- Produce structured summaries for healthcare administrators

---

# Features

## AI Multi-Agent Workflow

- Claims Processing Agent
- Claim Validation Agent
- Billing Review Agent
- AutoGen Agent Collaboration
- LLM-powered decision making
- Automated claim summarization

---

## Backend

- FastAPI REST APIs
- Pydantic validation
- Layered architecture
- Structured logging
- Global exception handling
- Health endpoints
- CORS support
- Async API implementation

---

## React Frontend

- React 19
- TypeScript
- Vite
- Axios API integration
- Markdown rendering
- Clean claim submission UI
- AI response visualization

---

## Streamlit Dashboard

- Interactive claim form
- AI response viewer
- Summary cards
- JSON response visualization
- Rapid healthcare demonstrations

---

# Solution Architecture

```
                +---------------------+
                | React Frontend      |
                +----------+----------+
                           |
                           |
                +----------v----------+
                | FastAPI Backend     |
                +----------+----------+
                           |
              Revenue Cycle Service
                           |
        -----------------------------------
        |                |               |
        |                |               |
+-------v------+ +--------v------+ +------v------+
| Claims Agent | | Validation    | | Billing     |
|              | | Agent         | | Agent       |
+--------------+ +---------------+ +-------------+
                           |
                    Final AI Response
```

---

# Technology Stack

## Backend

- Python
- FastAPI
- AutoGen 0.7.5
- Pydantic
- Loguru
- AsyncIO

---

## Frontend

### React

- React 19
- TypeScript
- Axios
- Vite
- React Markdown

### Streamlit

- Streamlit
- Requests
- Python

---

# Project Structure

```
Revenue_Cycle_Management_Agent
│
├── backend
│   └── revenue-cycle-management-agent-python-app
│       ├── agents
│       ├── config
│       ├── implementation
│       ├── models
│       ├── routers
│       ├── services
│       ├── utils
│       ├── logs
│       └── main.py
│
├── ui
│   ├── reactjs
│   │   └── revenue-cycle-management-agent-reactjs-app
│   │
│   └── streamlit
│       └── revenue-cycle-management-agent-streamlit-app
│
├── requirements.txt
└── README.md
```

---

# Backend Application

## Main Components

### Agents

- Claims Agent
- Validation Agent
- Billing Agent

---

### Router

```
POST /revenue-cycle/process-claim
```

Processes healthcare insurance claims.

---

### Service Layer

Responsible for:

- Agent orchestration
- Request handling
- AI workflow execution

---

### Models

Request Model

```
ClaimRequest
```

Response Model

```
RevenueCycleResponse
```

---

# React Frontend

Located at

```
ui/reactjs/revenue-cycle-management-agent-reactjs-app
```

## Features

- Claim submission form
- API integration
- Markdown AI output
- Summary cards
- Clean responsive UI

---

## Install

```bash
cd ui/reactjs/revenue-cycle-management-agent-reactjs-app

npm install
```

Run

```bash
npm run dev
```

Default URL

```
http://localhost:5173
```

---

# Streamlit Frontend

Located at

```
ui/streamlit/revenue-cycle-management-agent-streamlit-app
```

Run

```bash
cd ui/streamlit/revenue-cycle-management-agent-streamlit-app

pip install -r requirements.txt

streamlit run app.py
```

Default URL

```
http://localhost:8501
```

---

# Backend Installation

Navigate to backend

```bash
cd backend/revenue-cycle-management-agent-python-app
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r ../../requirements.txt
```

Configure environment variables

Create

```
.env
```

Example

```text
OPENAI_API_KEY=your_api_key
OPENAI_MODEL=gpt-4
```

Run FastAPI

```bash
uvicorn main:app --reload
```

Backend URL

```
http://localhost:8000
```

Swagger UI

```
http://localhost:8000/docs
```

---

# REST API

## Root

```
GET /
```

Returns application information.

---

## Health

```
GET /health
```

Returns backend health status.

---

## Revenue Cycle Health

```
GET /revenue-cycle/health
```

---

## Application Information

```
GET /revenue-cycle/info
```

---

## Process Claim

```
POST /revenue-cycle/process-claim
```

---

# Sample Request

```json
{
  "claim_id": "CLM10001",
  "patient_id": "PAT10001",
  "patient_name": "John Doe",
  "insurance_provider": "Blue Cross",
  "diagnosis": "Hypertension",
  "procedure": "Consultation",
  "claim_amount": 250.00
}
```

---

# Sample Response

```json
{
  "success": true,
  "claim_status": "Validated",
  "billing_status": "Approved",
  "validation_status": "Passed",
  "summary": "The insurance claim has been successfully validated and forwarded for billing."
}
```

---

# Multi-Agent Workflow

```
Incoming Claim
        │
        ▼
Claims Processing Agent
        │
        ▼
Validation Agent
        │
        ▼
Billing Agent
        │
        ▼
AI Generated Summary
        │
        ▼
REST API Response
```

---

# Logging

The application uses **Loguru** for centralized logging.

Generated log files

```
logs/

├── revenue_cycle_management.log
├── healthcare.log
└── error.log
```

Features

- Rotating logs
- Compressed archives
- Request logging
- Exception logging
- API execution tracking

---

# Future Enhancements

- HL7/FHIR integration
- EHR interoperability
- ICD-10 validation
- CPT code verification
- Fraud detection
- Denial prediction
- Prior authorization automation
- Payment posting automation
- Dashboard analytics
- Multi-tenant deployment
- Docker support
- Kubernetes deployment
- Azure OpenAI integration
- ML-based claim approval prediction

---

# License

This project is intended for educational and research purposes.

Healthcare AI applications should comply with applicable regulations such as HIPAA, GDPR, and local healthcare data privacy standards before production deployment.

---