import datetime
import requests

# URL of the HTTP resource you want to download
url = "https://forms.office.com/formapi/DownloadExcelFile.ashx?formid=hAVkUEAqFkKoS5s-4PP2z1wb2iT-DClDo45v6kOeyAlUNVBFMThJRExGMVJVODJETElaM1hCQUw4USQlQCN0PWcu&timezoneOffset=300&__TimezoneId=America/Bogota&minResponseId=1&maxResponseId=58"


# Define your cookies as a dictionary
cookies = {
    "MUID" : "0816D2CC34B96F1436FAC18430B964D4; RpsAuthNonce=ec66d92d-a70b-4533-a247-d42baec76ca3; FormsWebSessionId=84600f79-b036-4025-a64a-a26f4f03fd65; __RequestVerificationToken=pfedIYUmlBQ-5PDHGIzq_jgxK7riRHJJ3uTOILTvPmhynDvkZWjTRFIK8vBz_ESupd1JfH0y2jlvFSDabaahfTGNWE7anDecdTWPmvexRxU1; AADAuth.forms=eyJ0eXAiOiJKV1QiLCJyaCI6IjAuQVFZQWhBVmtVRUFxRmtLb1M1cy00UFAyejlKWnBjbXJlaE5QcHUzbjZjVXE3SWNHQU4wLiIsImFsZyI6IlJTMjU2Iiwia2lkIjoiVDFTdC1kTFR2eVdSZ3hCXzY3NnU4a3JYUy1JIn0.eyJhdWQiOiJjOWE1NTlkMi03YWFiLTRmMTMtYTZlZC1lN2U5YzUyYWVjODciLCJpc3MiOiJodHRwczovL2xvZ2luLm1pY3Jvc29mdG9ubGluZS5jb20vNTA2NDA1ODQtMmE0MC00MjE2LWE4NGItOWIzZWUwZjNmNmNmL3YyLjAiLCJpYXQiOjE3MDEwMTYyODQsIm5iZiI6MTcwMTAxNjI4NCwiZXhwIjoxNzAxMDIwMTg5LCJhaW8iOiJBVVFBdS84VkFBQUE2aFZ3YVZqR3pKWXBOMU9ONi9BeG1zZU5JRlNoek5kKzluSXpZdzFZQjNZZDdkOW1sZ0l1c0RCVTBVU2wzQThidDk3NFhlYVZKTnhEb01pdFJFZG1Gdz09IiwiYXpwIjoiYzlhNTU5ZDItN2FhYi00ZjEzLWE2ZWQtZTdlOWM1MmFlYzg3IiwiYXpwYWNyIjoiMiIsImZhbWlseV9uYW1lIjoiVklMTEFESUVHTyBHT05aQUxFWiIsImdpdmVuX25hbWUiOiJWQUxFTlRJTkEiLCJuYW1lIjoiVklMTEFESUVHTyBHT05aQUxFWiBWQUxFTlRJTkEiLCJvaWQiOiIzOWY2MjNkNy1mMjMzLTQ3MDAtYjQ3NS0yMDE0YjAwNmIwMjMiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJ2YWxlbnRpbmEudmlsbGFkaWVnb0BtYWlsLmVzY3VlbGFpbmcuZWR1LmNvIiwicHVpZCI6IjEwMDMzRkZGQTc3QzAyMTciLCJzY3AiOiJDaGFubmVsLlJlYWRCYXNpYy5BbGwgQ2hhbm5lbE1lbWJlci5SZWFkLkFsbCBDaGFubmVsTWVzc2FnZS5TZW5kIENoYXQuQ3JlYXRlIENoYXQuUmVhZFdyaXRlIENoYXRNZXNzYWdlLlNlbmQgRGlyZWN0b3J5LlJlYWQuQWxsIEZpbGVzLlJlYWRXcml0ZSBGaWxlcy5SZWFkV3JpdGUuQWxsIEdyb3VwLlJlYWQuQWxsIE1haWwuU2VuZCBNYWlsYm94U2V0dGluZ3MuUmVhZCBQZW9wbGUuUmVhZCBUZWFtLlJlYWRCYXNpYy5BbGwgVXNlci5SZWFkIFVzZXIuUmVhZC5BbGwiLCJzdWIiOiJrYlFpVE1QS0NadGVxdDBGNEZGRURmbHlITzg1SUFhbnNjMEVfNHBPYmdNIiwidGlkIjoiNTA2NDA1ODQtMmE0MC00MjE2LWE4NGItOWIzZWUwZjNmNmNmIiwidXBuIjoidmFsZW50aW5hLnZpbGxhZGllZ29AbWFpbC5lc2N1ZWxhaW5nLmVkdS5jbyIsInV0aSI6IlpaZHlKQ19xVTB5WG1EWWZZbmVsQWciLCJ2ZXIiOiIyLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdfQ.LQMqaSNPndpWQQsn-724bDsl19j-FESHPjN4OoeIH98i9E_wrpyvA-EHtO_2eptxYgU8Omc8MOUTlaJ_-aOuIVbOkyEe8bRAbxVFKFKy29V_WhXiYwnGZ-mT5-BKu16Fp3h_JRcXWO1T7aZCk0IF7H6CoLI9ot25w3XRDHYKqO3OSS3pF7B-4DKxyn7nNFaD4t4LbBrXUiw_qBh70osMVwFC34Xl93MrpFnf-FlkGtv2ihS9EPqaFZHgpM5opuOPqVtwjEtHAwlfFX4-JqZsEZAzWpZZ6IXJMesxcZPZOX31Q1rTUS53qIle3qplzIyHwG2Bf9goqSrkiBCb4QDPSA; OIDCAuth.forms=AdBAyKbF86ZmpCjDr1nFGTkoJwVUO5pb4cEgCMjzk58nOnlguMvAew-5MKdBIJ7OMlGhSrrB3kVIh-qHpN4MNDO087x5Rzyd0nlK9xN2IqsTLj2LfZ4bl5lNaMY1ATkYxZVW1GHI0HArJvpjVztVJ804RDg8BVGfMqDYUwse8ja9IKT3YOUVSZzMD-2d8y2Qj5z5lpm4YY_cIdo6r-IQEeitSAPoVhIFAPK6MDrIQxVrQdL0Rfats-2Fxp3jKI2tL7VfoPhP_nWYRiQIPeXv-41JGFPQjVepL0DchVwjYs5DSlckK42sGjKxu_BZrsespi8aUfZ9ePeyCXg75OS5WPPSbpsQMMqYM7dmGgtkNXXRY1He5lDErJep626-qzoNTgS7LPsEWL5w9BQ0TLUFXoGy3ccFqustkmuG_9zQWUm7LkRhxchDAh5Bj0lgUdUB2RqqrzK90tKYjBOTy8PD2Emk9kO6uzeZhXZdBMguzLJhHlQ0ABCnvSqiPbD4DAHSxw_N8yiNlvOlpdKis1sJkedLsNWXBzXA_wnT9Aahqq9gc0lnzb-ZDCLTiruhWGpxoD9ckyHjlHiu4anMFvsM_iALAa1lPI-hev8aK01alhLdRePlR1rHn1gCjHH-Bj03Grtt0L-Qzn0BJz2C1D1WdSQW4QHwFfCNGxEUFVIs6Wd5UV5whUyCVD-tNs31xAFmyNBsRbOHkOkuKGQRSO8u-5EyqrK5KYOjtgkRvs1xzmDkGfuqpDhvDzFC12Cig7YHzJSDayEFfWft4vflNEQ8a9hT84r7HhjQBqrJXh-iV7oMewUJ4oJUoUyQaOzJ-0JMqnAjWfxXFbPLumdf7j5UfceoUKnNh5f6pfO0inUeS0Gtl32Xcg8Vvjscdg8y2GzFCi6QCkYBXopU-oDBqAhzlwNInNNqITDEsXlo06M2dTeykPmq9CpGpvx5yDX7IumMIw_M7NWwHz2OP1riorrIJ-Auy2k4oTyVP4i_JVcFwuMPWqQXRF8w9kpHI5qvcruFvKfEJIu2MMuRtE9elWZuVhVuQwAgKD_0Hagw9zltRK1GzsKCU3T8u_jaB0AuOea8sx-pW1eL7fCKcqcUIwwjvmyMD0z_sU5Wys6fuktKV8zHp9eck1jTiolCtCWq44a2ug"
    # Add more cookies as needed
}

# Define the headers with the Cache-Control header set to no-cache
headers = {
    "Cache-Control": "no-cache"
}

# Create a session to manage and persist cookies
session = requests.Session()

# Set the cookies in the session
session.cookies.update(cookies)

# Send an HTTP GET request with cookies and the Cache-Control header and Make requests using the session
response = session.get(url, cookies=cookies, headers=headers)


# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the current date and time
    current_datetime = datetime.datetime.now()
    
    # Format the date and time as "YYYY-MM-DD-HHHH"
    formatted_datetime = current_datetime.strftime("%Y-%m-%d")
    
    # Specify the file path using the formatted date and time
    file_path = f"encuesta-estudiantes-{formatted_datetime}.xlsx"

    # Save the response content to a file
    with open(file_path, "wb") as file:
        file.write(response.content)

    print(f"File has been downloaded and saved as '{file_path}'.")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")

# When you're done with the session, you can close it to free up resources
session.close()