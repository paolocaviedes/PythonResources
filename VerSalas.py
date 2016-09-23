#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import ast
import json

url = "https://api.ciscospark.com/v1/rooms"

headers = {
    'authorization': "Bearer MmRhNTAyMTAtOGJkOS00NDE2LTgwZGQtYWYyNDIyOTY3YTA0ODQyODA3MTEtMzdh",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "3b06edb2-fbdd-0d52-c3ae-1e9dc60b2698"
    }


response = requests.request("GET", url, headers=headers)
json= response.json()


listaValues=json.values()[0]
for dictRoom in listaValues:
	print dictRoom