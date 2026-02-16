# Swag Labs (SauceDemo) - End-to-End QA Project

## Project Overview
This project demonstrates a comprehensive QA process for the **Swag Labs** e-commerce website. 
It covers the entire STLC (Software Testing Life Cycle), from initial planning to automated execution and final reporting.

## Documentation & Methodology
The project includes full testing documentation, synchronized for maximum traceability:
* **STP (Software Test Plan):** Defining strategies, resources, and scope.
* **STD (Software Test Description):** 20 detailed test cases covering Login, Inventory, Cart, and Checkout flows.
* **STR (Software Test Report):** Summary of execution results and release recommendations.
* **Bug Report:** Detailed documentation of defects found during testing.

## Automation Suite
The automation is built using **Python** & **Playwright** following the **Page Object Model (POM)** pattern.

### Key Features:
* **Traceability:** Automated tests are synchronized with STD IDs (e.g., TC-01, TC-02).
* **Cross-Browser Testing:** Configured for reliable execution.
* **Test Coverage:** Includes Sanity, Positive/Negative Login, and complex UI/Functional flows.

### Critical Bug Found:
During testing, a **Blocker** defect was identified in the `error_user` profile: The "Finish" button fails to respond during the checkout process, preventing order completion. This is documented in the STR and Bug Report.

## Technology Stack
* **Language:** Python
* **Test Framework:** Pytest
* **Automation Tool:** Playwright
* **Pattern:** Page Object Model (POM)
* **Reporting:** Pytest-HTML / Console

## How to Run the Tests
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ShaniP-Git/SwagLabs-QA-Automation]

