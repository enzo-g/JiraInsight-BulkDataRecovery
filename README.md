# Jira Insight Bulk Correction Script

## Overview
This Python script is designed to correct objects in Jira Insight that may have been assigned incorrect values during a bulk update. The script uses the Jira Insight REST API to retrieve the object history and update the CSV file, which can be reimported to correct the objects in Jira Insight.

## Input Preparation

### Step 1: Filter Computers in Jira Insight

Log in to your Jira instance. Navigate to the Insight dashboard and locate the 'Computers' object type. Use the Insight filter to identify all computers that are assigned to incorrect users.

### Step 2: Export Object List from Jira

After you have filtered the list of problematic computers, locate the 'Export' option at the top-right corner of the screen. Click on 'Export' and select to export only the "Key" values for each object. Save this list in a text file, one key per line.

## How to Use

1. **Edit the Script**: Open the script in a text editor and modify the following variables:

    - `JIRA_URL`: Set this to the URL of your Jira instance.
    
    - `API_TOKEN`: Replace `YOUR_API_TOKEN` with the API token generated from your Jira instance.
    
    - `EMAIL`: Replace `YOUR_EMAIL_ADDRESS` with the email address that corresponds to the API token.

    - `input_file_path`: Path to the input TXT file containing one Jira object "Key" per line.
    
    - `output_file_path`: Path where the output CSV file will be saved.

    Modify the filter criteria in the `filter_old_value` function to filter the old value based on the actor and date.

    - `ACTOR_NAME`: Name of the person that made the unwanted change

    - `YYYY-MM-DDTHH`: Date of his action

3. **Run the Script**: Execute the script from the command line.

    ```
    python JiraInsight-BulkDataRecovery.py
    ```

## Output

The script will generate a CSV file with corrected object information. The CSV will contain the following columns:

- **Label**: The label of the object in Jira Insight.
- **Jira Object ID**: The unique ID of the object.
- **Old Value**: The old value that was replaced during the bulk change.

Process to re-import that CSV in Jira Insight through "Configure > Tab Import"

## Progress Monitoring

The script will print the progress percentage to the console. It will also print timestamps indicating when the export process started and ended.

