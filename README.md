# Multi-Framework-Compliance-Mapper

## 📌 Business Problem
Growing enterprises often suffer from "control bloat"—wasting capital and engineering hours by treating security frameworks (like NIST CSF, ISO 27001, and SOC 2) as completely separate silos. This results in redundant controls, audit fatigue, and inflated compliance overhead.

## 🎯 Solution
The **Multi-Framework-Compliance-Mapper** is a lightweight Python utility designed to ingest technical security configurations, map them dynamically, and evaluate coverage across multiple regulatory frameworks simultaneously. It demonstrates how a single technical control can satisfy multiple audit requirements, streamlining compliance operations and reducing overhead.

## 🛠️ Frameworks Supported
- **NIST Cybersecurity Framework (CSF)**
- **ISO/IEC 27001:2022**
- **SOC 2 Trust Services Criteria**

## 🚀 How It Works
1. **Control Ingestion:** Loads baseline technical configurations and security mappings from a structured JSON database (`controls_mapping.json`).
2. **Cross-Mapping:** Cross-references each control against NIST, ISO, and SOC 2 requirements simultaneously.
3. **Gap Analysis & Reporting:** Outputs a clear CLI report showing compliance coverage percentages and missing control gaps across frameworks.

## ⚙️ Usage Instructions
Clone the repository and execute the script via terminal:
```bash
python3 mapper.py
