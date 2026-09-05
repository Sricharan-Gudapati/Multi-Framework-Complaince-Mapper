#!/usr/bin/env python3
"""
Author: Sricharan Gudapati
Role: GRC & Information Security Analyst
Project: Multi-Framework Compliance Mapper
Description: Automates the cross-walking of technical baseline configurations 
             against NIST CSF, ISO 27001:2022, and SOC 2 Trust Services Criteria.
"""

import json

def load_compliance_data(filepath="controls_mapping.json"):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {filepath} not found. Please ensure controls_mapping.json is in the directory.")
        return None

def generate_compliance_report(data):
    if not data:
        return
    
    controls = data.get("total_controls", data.get("technical_controls", []))
    total = len(controls)
    implemented = sum(1 for c in controls if c["status"] == "Implemented")
    
    print("=" * 60)
    print(" GRC AUTOMATED MULTI-FRAMEWORK COMPLIANCE REPORT")
    print("=" * 60)
    print(f"Total Technical Controls Evaluated: {total}")
    print(f"Fully Implemented Controls: {implemented}")
    print(f"Compliance Baseline Readiness: {int((implemented/total)*100)}%\n")
    
    print("Cross-Framework Mapping Details:")
    print("-" * 60)
    for ctrl in controls:
        print(f"[{ctrl['control_id']}] {ctrl['control_name']}")
        print(f"  Description: {ctrl['description']}")
        print(f"  Status: {ctrl['status']}")
        print(f"  Mappings -> NIST: {ctrl['framework_mappings']['NIST_CSF']} | "
              f"ISO 27001: {ctrl['framework_mappings']['ISO_27001']} | "
              f"SOC 2: {ctrl['framework_mappings']['SOC_2']}")
        print("-" * 60)

if __name__ == "__main__":
    compliance_data = load_compliance_data()
    if compliance_data:
        generate_compliance_report(compliance_data)

  Implement Python complaince reporting engine and CLI parser
