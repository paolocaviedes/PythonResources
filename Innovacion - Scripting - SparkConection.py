import requests

url = "https://api.ciscospark.com/v1/messages"

payload = "{\r\n  \"roomId\" : \"Y2lzY29zcGFyazovL3VzL1JPT00vMTQ1NWQyNDYtMTdkMS0zYzJmLThkZjAtNTQ3ZTVlNTFkMTEw\",\r\n  \"text\": \"Buenos Dias Adolfo\"\r\n}"
headers = {
    'authorization': "Bearer MmRhNTAyMTAtOGJkOS00NDE2LTgwZGQtYWYyNDIyOTY3YTA0ODQyODA3MTEtMzdh",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "8851d330-8954-e2d0-5b6a-9f07cbf8b34c"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)