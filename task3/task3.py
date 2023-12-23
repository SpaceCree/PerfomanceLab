import json
def get_values(tests, results):
    for test in tests:
        test_id = test.get("id")
        if test_id in results:
            test["value"] = results[test_id]["value"]
        if "values" in test:
            get_values(test["values"], results)
def main():

    with open("tests.json", "r") as tests_file:
        tests_data = json.load(tests_file)["tests"]

    with open("values.json", "r") as values_file:
        values_data = json.load(values_file)["values"]

    results = {item["id"]: item for item in values_data}

    get_values(tests_data, results)

    with open("report.json", "w") as report_file:
        json.dump(tests_data, report_file, indent=2)

if __name__ == "__main__":
    main()
