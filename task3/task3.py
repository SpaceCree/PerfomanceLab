import json
import os
import sys

def get_values(tests, results):
    for test in tests:
        test_id = test.get("id")
        if test_id in results:
            test["value"] = results[test_id]["value"]
        if "values" in test:
            get_values(test["values"], results)

def main(tests_file_path, values_file_path):
    with open(tests_file_path, "r") as tests_file:
        tests_data = json.load(tests_file)["tests"]

    with open(values_file_path, "r") as values_file:
        values_data = json.load(values_file)["values"]

    results = {item["id"]: item for item in values_data}

    get_values(tests_data, results)


    directory = os.path.dirname(tests_file_path)


    report_file_path = os.path.join(directory, "report.json")

    with open(report_file_path, "w") as report_file:
        json.dump(tests_data, report_file, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(" python filename.py tests.json values.json")
        sys.exit(1)

    tests_file_path = sys.argv[1]
    values_file_path = sys.argv[2]

    main(tests_file_path, values_file_path)
