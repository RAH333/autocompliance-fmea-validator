"""
The orchestration file that executes the full end-to-end analysis and renders clear console reports.
"""
from src.parser import load_json_file
from src.fmea_engine import generate_dfmea
from src.compliance_checker import run_compliance_audit
from tabulate import tabulate

def main():
    print("=" * 70)
    print(" AUTOMOTIVE E&E COMPLIANCE & D-FMEA ANALYSIS PIPELINE")
    print("=" * 70)
    
    # Load assets
    system_data = load_json_file("data/sample_architecture.json")
    safety_rules = load_json_file("config/safety_rules.json")
    
    print(f"\nAnalyzing Subsystem: {system_data['system_name']}\n")
    
    # Step 1: Compliance Audit Block
    print("-" * 50)
    print("1. PROCESS COMPLIANCE AUDIT REPORT (ASPICE / ISO 26262)")
    print("-" * 50)
    audit_reports = run_compliance_audit(system_data)
    for report in audit_reports:
        print(f"Component: {report['component']}")
        print(f"Status:    {report['status']}")
        print(f"Findings:  {', '.join(report['violations'])}")
        print("." * 40)

    # Step 2: Automated D-FMEA Matrix Generation Block
    print("\n" + "-" * 50)
    print("2. GENERATED DESIGN FMEA (D-FMEA) MATRIX")
    print("-" * 50)
    fmea_headers = ["Item", "Type", "Failure Mode", "Local Effect", "S", "O", "D", "RPN", "Recommended Action"]
    fmea_data = generate_dfmea(system_data, safety_rules)
    
    print(tabulate(fmea_data, headers=fmea_headers, tablefmt="grid"))

if __name__ == "__main__":
    main()
  
