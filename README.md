# autocompliance-fmea-validator


# Description:

Automated D-FMEA generation and ASPICE/ISO-26262 compliance verification engine for automotive E&E systems (ECUs, eAxles, and Sensors).

An Automated Automotive E&E Architecture Analysis & ASPICE/FMEA Compliance Tool.

# AutoCompliance-FMEA Validator

An automated pipeline designed to audit automotive E&E (Electrical/Electronic) system configurations against process compliance matrices (**ASPICE** & **ISO 26262**) and mathematically compute **D-FMEA Risk Priority Numbers (RPN)** to flag critical supplier risks before PPAP/APQP milestones.

## Features
- **Automated D-FMEA Mapping:** Derives structural severity, occurrences, and detection ratings programmatically based on unit properties.
- **Process Gap Analysis:** Automatically flags software engineering architecture blocks lacking compliance documentation records.
- **Actionable Supplier Risk Mitigation:** Targets high-risk components with structural recommendations tailored to Automotive Supplier Technical Assistance (STA) tracks.

## Quick Start
```bash
# Install dependencies
pip install -r requirements.txt

# Execute validation workflow pipeline
python main.py
```


This project simulates the exact workflow of an STA (Supplier Technical Assistance) Engineer. It takes a simulated system design file (like a JSON representation of an ECU, sensor network, or eAxle architecture) and automatically parses it to:
1. Generate an automated D-FMEA (Design Failure Mode and Effects Analysis) matrix.
2. Verify compliance traceabilities against ASPICE (SYS.3/SWE.3) and ISO 26262 functional safety requirements.
3. Output a production-ready compliance validation report.


```
autocompliance-fmea-validator/
├── config/
│   └── safety_rules.json
├── data/
│   └── sample_architecture.json
├── src/
│   ├── __init__.py
│   ├── parser.py
│   ├── fmea_engine.py
│   └── compliance_checker.py
├── main.py
├── requirements.txt
└── README.md
```

