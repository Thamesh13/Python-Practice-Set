import requests

try:
    response = requests.get("http://127.0.0.1:5000/Student")
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
    student_data = response.json()
    print(student_data)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
