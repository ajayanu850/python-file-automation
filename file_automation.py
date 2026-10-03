import csv
import json
import os


input_files = [
    "input/day1_results.csv",
    "input/day2_results.csv"
]

all_results = []

pass_count = 0
fail_count = 0
skip_count = 0

failed_tests = []


for file_name in input_files:

    with open(file_name, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            all_results.append(row)

            if row["status"] == "PASS":
                pass_count += 1

            elif row["status"] == "FAIL":
                fail_count += 1
                failed_tests.append(row["test_id"])

            elif row["status"] == "SKIP":
                skip_count += 1


total_tests = len(all_results)


os.makedirs("output", exist_ok=True)


with open("output/combined_results.csv", "w", newline="") as file:

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


summary = {
    "total_tests": total_tests,
    "passed": pass_count,
    "failed": fail_count,
    "skipped": skip_count,
    "failed_tests": failed_tests
}


with open("output/summary_report.json", "w") as file:

    json.dump(
        summary,
        file,
        indent=4
    )


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

print("\nReports generated successfully.")
