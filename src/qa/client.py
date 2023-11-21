"""
A client sending request to the Flask server 'http://localhost:8085/query'.
"""
import requests
import json

def query_fn(query, method):
    url = 'http://localhost:8085/query'
    params = {'query': query, 'qa': method}
    response = requests.get(url, params=params)
    # print(response.json())
    print(json.dumps(response.json(), indent=4))

def main():
    try:
        while True:
            query = input("Enter your query: ")
            method = input("Enter your method: ")
            query_fn(query, method)
    except KeyboardInterrupt:
        print("\nClient stopped by user")
        return

if __name__ == '__main__':
    main()

