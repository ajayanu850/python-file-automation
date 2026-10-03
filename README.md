# Python CSV & JSON File Automation

A Python automation tool that automatically discovers CSV test-result files, combines the results, analyzes PASS/FAIL/SKIP statistics, generates module-wise summaries, and creates CSV and JSON reports.

## Problem

QA and validation teams may receive multiple CSV test-result files every day.

Manually combining these files and calculating test statistics can be repetitive and time-consuming.

## Solution

This Python tool automatically:

- Finds all CSV files inside the input folder
- Reads test-result data
- Validates required CSV columns
- Combines multiple CSV files
- Counts PASS, FAIL, and SKIP results
- Identifies failed test IDs
- Generates module-wise statistics
- Creates a combined CSV report
- Creates a JSON summary report
- Handles missing folders and invalid files

## Technologies Used

- Python
- CSV
- JSON
- File Handling
- Exception Handling
- OS Module
- Git
- GitHub

## Input Format

Example CSV:

```csv
test_id,module,status,duration
TC001,Login,PASS,2.5
TC002,Login,FAIL,3.1
TC003,Dashboard,PASS,1.8
```

## Project Structure

```text
python-file-automation/
│
├── README.md
├── file_automation.py
│
├── input/
│   ├── day1_results.csv
│   └── day2_results.csv
│
├── output/
│   ├── combined_results.csv
│   └── summary_report.json
│
└── Screenshots/
    └── automation_output.png
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/ajayanu850/python-file-automation.git
```

Move into the project:

```bash
cd python-file-automation
```

Run:

```bash
python file_automation.py
```

## Example Output

```text
CSV files found: 2

--- Test Automation Summary ---

Total Tests: 10
Passed: 6
Failed: 3
Skipped: 1

Failed Test IDs:
- TC002
- TC005
- TC008
```

## Module Summary

Example:

```text
Module: Login
Total: 3
Passed: 2
Failed: 1
Skipped: 0
```

The program generates module-wise statistics for every module found in the input data.

## Generated Reports

### combined_results.csv

Combines results from all input CSV files into one report.

### summary_report.json

Contains:

- Total test count
- Passed test count
- Failed test count
- Skipped test count
- Failed test IDs
- Module-wise statistics

## Project Screenshot

![Python File Automation Output](Screenshots/automation_output.png)

## Skills Demonstrated

- Python automation
- CSV processing
- JSON generation
- Automatic file discovery
- Data aggregation
- File validation
- Exception handling
- Report generation
- Git version control

## Freelance Use Cases

This type of automation can be adapted for:

- QA test-result processing
- CSV data consolidation
- Daily report automation
- Log/report processing
- JSON report generation
- Repetitive file-processing workflows
