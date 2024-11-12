import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# Define the URL
url = "http://myapi-lb-1595571151.us-east-1.elb.amazonaws.com/api/load"

# Function to make a single request
def make_request():
    response = requests.get(url)
    return response.status_code, response.text

# Function to execute requests in batches of 5
def execute_requests_in_batches(total_requests, batch_size):
    with ThreadPoolExecutor(max_workers=batch_size) as executor:
        futures = []
        for i in range(total_requests):
            futures.append(executor.submit(make_request))

            # When the batch size is reached, wait for all futures to complete
            if len(futures) % batch_size == 0:
                for future in as_completed(futures):
                    status_code, response_text = future.result()
                    print(f"Status Code: {status_code}, Response: {response_text[:100]}")
                futures.clear()

            print(f'=== batch {i} ===')

# Example: Execute 20 requests in batches of 5
execute_requests_in_batches(total_requests=10000, batch_size=1)
