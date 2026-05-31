# IP-threat-intelligence-enrichment
Python-based Threat Intelligence automation tool for bulk IP reputation enrichment using AbuseIPDB APIs.

## Overview

This project automates bulk IP reputation analysis using Python and Threat Intelligence APIs.

The tool reads IP addresses from TXT/Excel files and enriches them with:

* Reputation Score
* Country Information
* ISP Details

using AbuseIPDB REST APIs.

---

## Features

* Bulk IP enrichment
* Reputation score retrieval
* Country and ISP extraction
* TXT file input support
* Excel report generation
* Exception handling
* API integration automation

---

## Technologies Used

* Python
* REST APIs
* Requests Library
* Pandas
* OpenPyXL
* Threat Intelligence APIs

---

## Input Format

Example TXT file:

8.8.8.8
1.1.1.1

---

## Output

Excel report containing:

* IP Address
* Reputation Score
* Country
* ISP

---

## Output

Screenshots attached

---

## Installation

Install required packages:

pip install pandas requests openpyxl

---

## Run the Script

python ip_enrichment.py

---

## Future Enhancements

* VirusTotal integration
* Streamlit dashboard
* IOC enrichment automation
* SIEM integration
* AI-assisted threat analysis

