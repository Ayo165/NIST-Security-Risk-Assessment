import csv

def calculate_risk_level(likelihood, impact):
    """
    Calculates the risk score and returns the qualitative risk level.
    Score = Likelihood (1-5) x Impact (1-5)
    """
    score = likelihood * impact
    
    if score >= 15:
        return score, "CRITICAL"
    elif score >= 10:
        return score, "HIGH"
    elif score >= 5:
        return score, "MEDIUM"
    else:
        return score, "LOW"

def assess_risks(risk_data):
    """
    Processes a list of identified risks and outputs prioritized results.
    """
    print("-" * 60)
    print(f"{'Risk Scenario':<30} | {'Score':<5} | {'Risk Level':<10}")
    print("-" * 60)
    
    for item in risk_data:
        scenario = item['scenario']
        likelihood = item['likelihood']
        impact = item['impact']
        
        score, level = calculate_risk_level(likelihood, impact)
        
        print(f"{scenario:<30} | {score:<5} | {level:<10}")
    print("-" * 60)

if __name__ == "__main__":
    # Simulated input data for a fictional organization
    company_risks = [
        {"scenario": "Ransomware on Domain Controller", "likelihood": 3, "impact": 5},
        {"scenario": "Unpatched Web Server Exploit", "likelihood": 4, "impact": 4},
        {"scenario": "Employee Phishing Compromise", "likelihood": 5, "impact": 3},
        {"scenario": "Physical Theft of Laptop", "likelihood": 2, "impact": 2},
        {"scenario": "Cloud Storage Misconfiguration", "likelihood": 3, "impact": 4}
    ]
    
    print("\nExecuting NIST-Aligned Risk Assessment Calculator...")
    assess_risks(company_risks)
