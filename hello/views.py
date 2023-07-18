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
    url = 'http://20.214.223.234:80/api/v1/service/aihvac-skt-web-ttower-main/score'
    api_key = 'HHd1fwMBSdBu485LtOxP2D8lzkY4ax9B' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    
    try:
        req = urllib.request.Request(url, body, headers)
        response = urllib.request.urlopen(req)
        result = response.read()
        result = json.loads(result)
        result = json.loads(result['df1'])
    except urllib.error.HTTPError as error:
        result = {"dbt":{"0":0.0},"rh":{"0":0.0},"wt":{"0":0.0},"x":{"0":0.0},
                  "h":{"0":0.0},"PM10":{"0":"0"},"PM25":{"0":"0"},"time":{"0":"00월 00일 00시 00분"}}

    
    
    return render(request, "tables/index.html", context = result)

def oa_control(request):
    allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.
    data = {'param':{'bld':1}}
    body = str.encode(json.dumps(data))
    url = 'http://20.214.223.234:80/api/v1/service/aihvac-skt-occ-count/score'
    api_key = 'j5cTayYSnWEA6y6nINJXf9ZMgyQuMdRi' # Replace this with the API key for the web service
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
    url = 'http://20.214.223.234:80/api/v1/service/aihvac-skt-ahu-economizer/score'
    api_key = '58WoICsiZYhsi8eUbXbzWhSHVgeYqvAO' # Replace this with the API key for the web service
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
    url = 'http://20.214.223.234:80/api/v1/service/aihvac-skt-web-ttower-ahuopts/score'
    api_key = '4RDbxMhFp1ieh6kuAHPLzQdOMJvwJNAQ' # Replace this with the API key for the web service
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
