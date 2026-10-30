# 🛒 E2E E-Commerce Test Suite - QA Automation & Manual Testing

This repository contains the comprehensive documentation and test automation for the e-commerce platform **[Practice Software Testing](https://practicesoftwaretesting.com/)** and its respective **[API v4](https://api-v4.practicesoftwaretesting.com/)**. The project encompasses detailed E2E manual testing, API validations via Postman, and integration automation using Python, Selenium WebDriver and Pytest.

## 🎯 Project Objective
To ensure the quality and stability of the critical business workflows of the e-commerce platform by implementing a scalable automation architecture (Page Object Model) and documenting actual versus expected behavior, including the identification of critical bugs in the production environment.

## 🛠️ Technologies Used
* **Language:** Python 3.10+
* **Web Automation (UI):** Selenium WebDriver
* **API Automation:** `requests`
* **Testing Framework:** Pytest, pytest-html (for reporting)
* **Design Pattern:** POM (Page Object Model)
* **Manual & API Testing:** Postman, Google Sheets/Excel

## 📋 Testing Scope (Test Cases)
A total of 23 Test Cases were designed and executed, covering the following application areas:

1. **Login and Authentication (TC_LOG_01 to 05):** Validation of mandatory fields, valid credentials, and error handling (400 Bad Request) via API and UI.
2. **Catalog and Search (TC_CAT_01 to 06):** Verification of category filters, price sorting, value limits, and GET search endpoints.
3. **Cart, Price, and Checkout (TC_CPC_07 to 23):** Complex workflow of adding/removing products, blocking out-of-stock items (422 Unprocessable Entity), subtotal calculation, user access validation, and payment processing.

### 🐞 Critical Bug Report
During the execution of scenario **TC_CPC_22 (Invoice appears in Order History)**, a severe defect was identified in the production environment:
* **Expected Behavior:** After completing an order, the invoice should be detailed and listed with the status 'Completed'. Via API, the `/invoices/{invoiceId}` endpoint must return HTTP 200 with the invoice payload.
* **Actual Behavior:** The invoices page remains blank (UI). In the API, the request returns **404 Requested item not found**.
* **Severity:** Critical (Prevents the user from obtaining the purchase receipt).

## 👩‍💻 Author

### Isabela Bueno Silva
I am a Junior Quality Assurance (QA) Analyst with fluent English, a strong analytical mindset, and sharp attention to detail. Currently available for international remote freelance projects and contract opportunities.

Transitioning from a solid background in Data Analysis and Educational Project Management, I bring a unique perspective to software testing: I understand user behavior (UX) and know how to translate complex requirements into rigorous test scenarios to ensure high product quality and seamless usability.

**🛠️ My Tech Stack & QA Expertise:** 
✔ Testing Types: Manual Testing, Exploratory Testing, E2E, Regression Testing, Web & Mobile Testing. 
✔ Tools & Frameworks: Jira (Bug Reporting), Postman (API Testing), DevTools, Git/GitHub. 
✔ Automation: Python, Selenium WebDriver, Pytest. 
✔ Methodologies: Agile (Scrum/Kanban), Test Case Creation.

Throughout my recent projects, I have developed comprehensive Test Cases, executed end-to-end (E2E) automated workflows using Python, and successfully managed Bug Reporting via Jira. I am highly adaptable, comfortable working in asynchronous remote teams, and obsessed with delivering bug-free applications.

📩 Let's connect! I am currently taking on freelance/contract roles and would love to help your engineering team ship better, reliable software. Reach me directly at: isabelabueno.tech@gmail.com / www.linkedin.com/in/isabelabuenosilva
