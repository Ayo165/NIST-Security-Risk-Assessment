# Security Risk Assessment & GRC Automation

## 📝 Objective
This project demonstrates the ability to conduct a formal Security Risk Assessment for a fictional organization, aligning vulnerabilities and threats with the **NIST Cybersecurity Framework (CSF)**. To elevate standard GRC (Governance, Risk, and Compliance) processes, a custom Python tool was developed to programmatically calculate, categorize, and prioritize risk scores based on Likelihood and Impact matrices.

## 🛠️ Frameworks & Technologies Used
*   **Framework:** NIST Cybersecurity Framework (Identify, Protect, Detect, Respond, Recover)
*   **Compliance & GRC:** Qualitative Risk Analysis, Threat Modeling, Control Recommendations
*   **Automation:** Python (for risk calculation and prioritization logic)

## 🗺️ Assessment Process

### 1. Risk Identification (Identify)
The assessment began by mapping out the organization's critical assets and identifying the most pressing threat scenarios, including ransomware deployment, unpatched external infrastructure, employee susceptibility to phishing, and cloud misconfigurations.

### 2. Automated Risk Evaluation (Python Integration)
Rather than manually calculating risk levels in a spreadsheet, a Python script (`risk_calculator.py`) was engineered to automate the evaluation process. 
*   The script ingests threat scenarios alongside numerical Likelihood (1-5) and Impact (1-5) values.
*   It multiplies these metrics to generate a quantitative Risk Score.
*   The logic then automatically sorts and categorizes the threats into qualitative ratings (`CRITICAL`, `HIGH`, `MEDIUM`, `LOW`), ensuring a mathematically consistent and unbiased prioritization of vulnerabilities.

### 3. Control Recommendations (Protect & Detect)
Based on the programmatic output of the Python calculator, prioritized NIST-aligned controls were recommended to mitigate the highest risks:
*   **Phishing Compromise (Score: 15 - CRITICAL):** Recommended the enforcement of FIDO2-compliant Multi-Factor Authentication (MFA) and routine simulated phishing campaigns (NIST PR.AT-1).
*   **Unpatched Web Server (Score: 16 - CRITICAL):** Recommended the deployment of an automated Vulnerability Management program to scan and patch external-facing assets strictly within a 14-day SLA (NIST ID.RA-1).
*   **Ransomware on DC (Score: 15 - CRITICAL):** Advised implementing immutable, offline backups and Endpoint Detection and Response (EDR) solutions on all critical servers (NIST PR.DS-1, PR.IP-4).

## 💡 Conclusion
This assessment illustrates the intersection of compliance and technical engineering. By aligning organizational threats with the NIST CSF and utilizing Python to automate the quantitative risk analysis, the final output provides management with a clear, data-driven roadmap for deploying security controls where they are needed most.
