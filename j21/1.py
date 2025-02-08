import requests

# Function to fetch user data from the API
def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    
    # Send a GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        users = response.json()  # Parse JSON response
        return users
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

# Function to display user data
def display_users(users):
    if users:
        for user in users:
            print(f"Name: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"City: {user['address']['city']}")
            print("-" * 40)

# Main function to run the app
def main():
    print("Fetching user data...")
    users = fetch_users()
    
    if users:
        display_users(users)

if __name__ == "__main__":
    main()
