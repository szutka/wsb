import requests

def fetchNASAimages(query):
    url = "https://images-api.nasa.gov/search"
    headers = {
        "Accept": "application/json"
    }
    params = {
        "q": query,
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Nie udalo sie pobrac danych, kod: {response.status_code}")

def main():
    query = input("Podaj slowo kluczowe: ")

    try:
        data = fetchNASAimages(query)
        items = data.get("collection", {}).get("items", [])

        if not items:
            print("Brak wynikow dla zapytania.")
            return

        for item in items[:5]:
            item_data = item.get("data", [])

            if item_data:
                title = item_data[0].get("title", "brak tytulu")
                print(f"Tytule: {title}")

                links = item.get("links", [])
                if links:
                    print(f"Link: {links[0].get('href', 'brak linku')}")

                print("-" * 40)

    except Exception as e:
        print(f"Blad dla wyszukiwanego zapytania: {e}")

if __name__ == "__main__":
    main()