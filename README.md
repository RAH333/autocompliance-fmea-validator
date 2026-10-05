# autocompliance-fmea-validator


# Description:

Automated D-FMEA generation and ASPICE/ISO-26262 compliance verification engine for automotive E&E systems (ECUs, eAxles, and Sensors).

An Automated Automotive E&E Architecture Analysis & ASPICE/FMEA Compliance Tool.

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

