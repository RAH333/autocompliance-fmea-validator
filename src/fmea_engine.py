"""
Generates potential failure modes, determines Risk Priority Numbers (RPN), and suggests corrective actions based on the inputs.
"""
def generate_dfmea(system_data, safety_rules):
    fmea_rows = []
    rules = safety_rules.get("failure_modes", {})
    
    for comp in system_data.get("components", []):
        comp_type = comp.get("type")
        comp_name = comp.get("name")
        
        if comp_type in rules:
            for failure in rules[comp_type]:
                severity = failure["severity"]
                # Determine occurrence based on ASPICE compliance status
                occurrence = 3 if comp.get("aspice_compliant") else 7
                # Determine detection based on ASIL level robustness
                asil = comp.get("iso26262_asil", "A")
                detection = 2 if asil in ["C", "D"] else 5
                
                rpn = severity * occurrence * detection
                
                # Propose engineering recommendation actions
                action = "Maintain current architecture design."
                if rpn > 100:
                    action = "CRITICAL: Introduce redundant hardware or enhance software diagnostics loop."
                elif not comp.get("aspice_compliant"):
                    action = "HIGH RISK: Establish strict ASPICE SWE.3 unit test traceability verification."

                fmea_rows.append([
                    comp_name, comp_type, failure["mode"], failure["effect"], 
                    severity, occurrence, detection, rpn, action
                ])
    return fmea_rows
  
