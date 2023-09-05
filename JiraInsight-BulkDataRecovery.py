import requests
import json
import csv
import datetime

def get_label(api_url, object_id, auth_tuple):
    url = f"{api_url}/rest/insight/1.0/object/{object_id}"
    response = requests.get(url, auth=auth_tuple, headers={'Content-Type': 'application/json'})
    if response.status_code != 200:
        return None
    return response.json().get('label', '')

def get_history(api_url, object_id, auth_tuple):
    url = f"{api_url}/rest/insight/1.0/object/{object_id}/history"
    params = {'abbreviate': 'false'}
    response = requests.get(url, params=params, auth=auth_tuple, headers={'Content-Type': 'application/json'})
    if response.status_code != 200:
        return None
    return response.json()

def filter_old_value(response_json):
    return [
        entry['oldValue']
        for entry in response_json
        if entry['actor']['name'] == 'ACTOR_NAME' and entry['created'].startswith("YYYY-MM-DDTHH")
    ]
# Replace ACTOR_NAME by the name of the person that made the unwanted change and YYYY-MM-DDTHH by the date of his action.

# Define your Jira instance URL and API Token
JIRA_URL = 'JIRA_INSTANCE_URL' #Example: https://myjira.demo.com
API_TOKEN = 'YOUR_API_TOKEN' #Example: API Token of your user or password.
EMAIL = 'YOUR_EMAIL_ADDRESS'

# Create authentication tuple
auth_tuple = (EMAIL, API_TOKEN)

# File Paths
input_file_path = 'PATH_TO_INPUT_FILE'
output_file_path = 'PATH_TO_OUTPUT_FILE'

# Get the current time and print it to indicate when the export started
start_time = datetime.datetime.now()
print(f"Export started at {start_time}")

# Get the total number of lines in the input file for progress calculation
with open(input_file_path, 'r') as infile:
    total_lines = sum(1 for line in infile)

# Open input file and output file
with open(input_file_path, 'r') as infile, open(output_file_path, 'w', newline='') as outfile:
    csv_writer = csv.writer(outfile)
    csv_writer.writerow(["Label", "Jira Object ID", "Old Value"])  # write header
    current_line = 0

    for line in infile:
        current_line += 1
        object_id = line.strip()

        # Get label information
        label = get_label(JIRA_URL, object_id, auth_tuple)

        history = get_history(JIRA_URL, object_id, auth_tuple)
        if history is not None:
            old_values = filter_old_value(history)
            for old_value in old_values:
                csv_writer.writerow([label, object_id, old_value])

        # Calculate and print progress
        progress = (current_line / total_lines) * 100
        print(f"\rProgress: {progress:.2f}%", end="")

# Get the current time and print it to indicate when the export ended
end_time = datetime.datetime.now()
print(f"\nExport ended at {end_time}")

print("Script has finished running. Check the output CSV file.")JiraInsight-BulkDataRecovery.py
