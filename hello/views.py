from django.http import HttpResponse
from django.shortcuts import render
import urllib.request
import json
import pkg_resources
import subprocess
import sys
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

def index(request):
    allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.
    data = {'param':{'bld':1}}
    body = str.encode(json.dumps(data))
    url = 'http://52.141.0.146:80/api/v1/service/tsop-skt-tower-main/score'
    api_key = 'JbixWfRonFXDehmdbHcPit4rbyZJpsog' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib.request.Request(url, body, headers)
    try:
        response = urllib.request.urlopen(req)
        result = response.read()
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))

    result = json.loads(result)
    result = json.loads(result['df1'])
    return render(request, "tables/index.html", context = result)

def oa_control(request):
    allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.
    data = {'param':{'bld':1}}
    body = str.encode(json.dumps(data))
    url = 'http://52.141.0.146:80/api/v1/service/tsop-skt-ocb-control/score'
    api_key = 'kwea4NGIHAlBO1g5P6M4fQ5dVSb2D5Lz' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib.request.Request(url, body, headers)
    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        result = json.loads(result.decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
    values = json.loads(result['table'])
    values['Tcount'] = result['count']
    values['time'] = result['time']
    return render(request, "tables/oa_control.html", context = values)

def enthalpy_control(request):
    allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.
    data = {'param': {'bld': '1' }}
    body = str.encode(json.dumps(data))
    url = 'http://52.141.0.146:80/api/v1/service/tsop-skt-ahu-economizer/score'
    api_key = 'UrAzVhOgxF0xvmYeWHN48CqaVf42Fx5L' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib.request.Request(url, body, headers)
    try:
        response = urllib.request.urlopen(req)
        result = response.read()
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
        print(error.info())
    values = json.loads(result)
    values['table'] = json.loads(values['table'])
    return render(request, "tables/enthalpy_control.html", context = values)

def ahu_optimal_control(request):
    allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.
    data = {'param': {'bld': '1' }}
    body = str.encode(json.dumps(data))
    url = 'http://52.141.0.146:80/api/v1/service/tsop-skt-tower-ahu-opts/score'
    api_key = 'AaRZN1f0iWPfXuMnXCI3qrGMAHqtJcJB' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib.request.Request(url, body, headers)
    try:
        response = urllib.request.urlopen(req)
        result = response.read()
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
        print(error.info())
    values = json.loads(result)
    values['outs'] = json.loads(values['outs'])
    values['ahu_opts'] = json.loads(values['ahu_opts'])
    values['tables'] = json.loads(values['tables'])
    return render(request, "tables/ahu_optimal_control.html", context = values)

def elec_consumption(request):
    return render(request, "tables/elec_consumption.html")

def elec_peak(request):
    return render(request, "tables/elec_peak.html")
