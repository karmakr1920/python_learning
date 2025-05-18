import requests

def fetch_random_users():
    url = 'https://api.freeapi.app/api/v1/public/randomusers/user/random'
    response = requests.get(url)
    # print(response.json())
    json_data = response.json()
    if json_data["statusCode"] == 200 and "data" in json_data:
        user_data = json_data["data"]
        firstname = user_data["name"]["first"]
        lastname = user_data["name"]["last"]
        email = user_data["email"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return firstname,lastname,username,email,country
    else:
        raise Exception("Failed to fetch user")

if __name__ == '__main__':
    firstname,lastname,username,email,country = fetch_random_users()
    print(f"Name: {firstname} {lastname} \nUsername: {username} \nEmail: {email} \nCountry: {country}")