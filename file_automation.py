import csv
import json
import os


input_dir = "input"
output_dir = "output"

all_results = []

pass_count = 0
fail_count = 0
skip_count = 0

failed_tests = []

module_summary = {}


# Check whether input folder exists
if not os.path.exists(input_dir):
    print("Error: input folder not found.")
    exit()


# Automatically find all CSV files
input_files = []

for file_name in os.listdir(input_dir):

    if file_name.lower().endswith(".csv"):

        full_path = os.path.join(
            input_dir,
            file_name
        )

        input_files.append(full_path)


# Check whether CSV files exist
if not input_files:

    print("Error: No CSV files found in input folder.")
    exit()


print("CSV files found:", len(input_files))


for file_name in input_files:

    print("Processing:", file_name)

    try:

        with open(
            file_name,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            required_columns = {
                "test_id",
                "module",
                "status",
                "duration"
            }

            if not required_columns.issubset(
                reader.fieldnames or []
            ):

                print(
                    "Skipping file - missing required columns:",
                    file_name
                )

                continue


            for row in reader:

                status = row["status"].strip().upper()
                module = row["module"].strip()

                all_results.append(row)


                if status == "PASS":

                    pass_count += 1

                elif status == "FAIL":

                    fail_count += 1

                    failed_tests.append(
                        row["test_id"]
                    )

                elif status == "SKIP":

                    skip_count += 1


                # Create module entry if not already present
                if module not in module_summary:

                    module_summary[module] = {
                        "total": 0,
                        "passed": 0,
                        "failed": 0,
                        "skipped": 0
                    }


                module_summary[module]["total"] += 1


                if status == "PASS":

                    module_summary[module]["passed"] += 1

                elif status == "FAIL":

                    module_summary[module]["failed"] += 1

                elif status == "SKIP":

                    module_summary[module]["skipped"] += 1


    except FileNotFoundError:

        print("File not found:", file_name)

    except Exception as error:

        print(
            "Error processing file:",
            file_name,
            error
        )


total_tests = len(all_results)


os.makedirs(
    output_dir,
    exist_ok=True
)


# Generate combined CSV report
combined_file = os.path.join(
    output_dir,
    "combined_results.csv"
)


with open(
    combined_file,
    "w",
    newline="",
    encoding="utf-8"
) as file:

    fieldnames = [
        "test_id",
        "module",
        "status",
        "duration"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerows(all_results)


# Create summary dictionary
summary = {

    "total_tests": total_tests,

    "passed": pass_count,

    "failed": fail_count,

    "skipped": skip_count,

    "failed_tests": failed_tests,

    "module_summary": module_summary
}


# Generate JSON report
summary_file = os.path.join(
    output_dir,
    "summary_report.json"
)


with open(
    summary_file,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        summary,
        file,
        indent=4
    )


# Display overall summary
print("\n--- Test Automation Summary ---")

print("Total Tests:", total_tests)
print("Passed:", pass_count)
print("Failed:", fail_count)
print("Skipped:", skip_count)


print("\nFailed Test IDs:")

if failed_tests:

    for test_id in failed_tests:

        print("-", test_id)

else:

    print("No failed tests")


# Display module summary
print("\n--- Module Summary ---")

for module, result in module_summary.items():

    print("\nModule:", module)

    print(" Total:", result["total"])
    print(" Passed:", result["passed"])
    print(" Failed:", result["failed"])
    print(" Skipped:", result["skipped"])


print("\nReports generated successfully.")
