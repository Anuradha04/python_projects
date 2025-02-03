

# Email Summarizer using Simple Gmail and Transformers

This project demonstrates how to use Simple Gmail and Hugging Face Transformers to read Gmail messages and summarize their content.

## Prerequisites

- Google Developer Console account
- Google Colab
- Simple Gmail library
- Hugging Face Transformers library

## Installation

Install the required libraries:

```sh
pip install simplegmail transformers txtai
```

## Setup

### Step 1: Set Up Google Developer Console

1. Navigate to [Google Developer Console](https://console.developers.google.com/).
2. Create a new project.
3. Go to **API Overview**.
4. Open **API Library** and enable the **Gmail API**.
5. Open **OAuth consent screen** and add test users.

### Step 2: Create OAuth Credentials

1. Navigate to **Credentials**.
2. Create new credentials and select **OAuth Client ID**.
3. Download the credentials JSON file.
4. Rename the file to `client_secret.json`.

### Step 3: Configure Authentication

1. Upload `client_secret.json` to your Colab environment.
2. Initialize the Gmail object:

```python
from google.colab import files
from simplegmail import Gmail

# Upload the client_secret.json file to Colab
uploaded = files.upload()

# Initialize Gmail object
gmail = Gmail()  # It will open a link for OAuth authentication
```

### Step 4: Handle Verification

Follow the authentication link provided in the Colab output. Paste the authentication code in the prompt provided.

### Step 5: Setting Parameters and Filters

```python
def get_query_params():
    query_params = {}

    # Get 'read' status
    while True:
        read_input = input("Enter 'read' status (True/False) or press Enter to skip: ")
        if read_input == '':
            break  # Skip this field if user presses Enter
        elif read_input.lower() in ['true', 'false']:
            query_params["read"] = read_input.lower() == 'true'
            break
        else:
            print("Invalid input. Please enter 'True' or 'False'.")

    # Get 'recipient'- new
    while True:
        recipient_input = input("Enter recipient email(s) (comma-separated) or press Enter to skip: ")
        if recipient_input == '':
            break
        elif all('@' in email.strip() for email in recipient_input.split(',')):
            query_params["recipient"] = [email.strip() for email in recipient_input.split(',')]
            break
        else:
            print("Invalid input. Please enter valid email addresses.")

    # Get 'sender'
    while True:
        sender_input = input("Enter sender email(s) (comma-separated) or press Enter to skip: ")
        if sender_input == '':
            break  # Skip this field if user presses Enter
        elif all('@' in email.strip() for email in sender_input.split(',')):
            query_params["sender"] = [email.strip() for email in sender_input.split(',')]
            break
        else:
            print("Invalid input. Please enter valid email addresses.")

    # Get 'newer_than'
    while True:
        newer_than_input = input("Enter 'newer_than' duration (e.g., '5 day') or press Enter to skip: ")
        if newer_than_input == '':
            break  # Skip this field if user presses Enter
        try:
            number, unit = newer_than_input.split()
            query_params["newer_than"] = (int(number), unit)
            break
        except ValueError:
            print("Invalid input for 'newer_than'. It should be in the format: ' '")

    # Get 'labels'
    while True:
        labels_input = input("Enter labels (comma-separated, e.g., 'CATEGORY_FORUMS, INBOX') or press Enter to skip: ")
        if labels_input == '':
            break  # Skip this field if user presses Enter
        elif all(label.strip() for label in labels_input.split(',')):
            query_params["labels"] = [[label.strip()] for label in labels_input.split(',')]
            break
        else:
            print("Invalid input. Please enter valid labels.")
    # Get 'subject'
    while True:
        subject_input = input("Enter subject keyword(s) (comma-separated) or press Enter to skip: ")
        if subject_input == '':
            break
        query_params["subject"] = subject_input.split(',')
        break

    return query_params

query_params = get_query_params()
print("\nGenerated query_params:")
print(query_params)

promo_query = construct_query(query_params)

output = gmail.get_messages(query=promo_query)
```
