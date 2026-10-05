"""
Performs programmatic process audits against standardized ASPICE and ISO 26262 frameworks.
"""
def run_compliance_audit(system_data):
    audit_results = []
    for comp in system_data.get("components", []):
        passed = True
        flags = []
        
        if not comp.get("aspice_compliant"):
            passed = False
            flags.append("Missing ASPICE bi-directional requirement traceability link.")
            
        if comp.get("iso26262_asil") in ["C", "D"] and not comp.get("aspice_compliant"):
            passed = False
            flags.append("Safety Critical ASIL-C/D requires rigid software verification pipeline.")
            
        status = "PASSED ✅" if passed else "FAILED ❌"
        audit_results.append({
            "component": comp["name"],
            "status": status,
            "violations": flags if flags else ["None"]
        })
    return audit_results
  
