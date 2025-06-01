import concurrent.futures
import requests
import os

def downloadFile(url_name):
    url, name = url_name
    print(f"Started Downloading {name}")
    response = requests.get(url)
    
    os.makedirs("files", exist_ok=True)
    with open(f"files/file{name}.jpg", "wb") as f:
        f.write(response.content)
    print(f"Finished Downloading {name}")
    return f"file{name}.jpg downloaded"

def main():
    url = "https://picsum.photos/2000/3000"
    tasks = [(url, i) for i in range(10)]  # reduce count to 10 for testing

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(downloadFile, tasks)

        for result in results:
            print(result)

if __name__ == "__main__":
    main()
