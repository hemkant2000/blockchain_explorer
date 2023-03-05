from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from web3 import Web3
from collections import defaultdict
import json
from hexbytes import HexBytes




def index(request):
    return render(request, 'block_exp_app1/index.html')


class AttributeDictEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, int):
            return str(obj)
        elif isinstance(obj, HexBytes):
            return obj.hex()
        elif isinstance(obj, str):
            return obj
        elif isinstance(obj, list):
            return str(obj)
        else:
            return super(AttributeDictEncoder, self).default(obj)

w3 =  Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/c23493e43a7e411aba08209478828351'))
print(w3.isConnected())
block= w3.eth.get_block('latest')
dict1 = {}
for x,y in block.items():
    print(x, end=" == ")
    js = json.dumps(y, cls = AttributeDictEncoder)
    dict1[x] = js
    print(js)

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        # Do something with the data
        w3 =  Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/c23493e43a7e411aba08209478828351'))
        print(w3.isConnected())

        if name.isdecimal():
            name = int(name)
        block = w3.eth.get_block(name)
        dict1 = {}
        for x,y in block.items():
            print(x, end=" == ")
            js = json.dumps(y, cls = AttributeDictEncoder)
            dict1[x] = js
          
        context = {
        "block" : dict1,
        }
        return render(request, 'block_exp_app1/success.html', context)
    else:
        return render(request, 'block_exp_app1/form.html')

def submit_form1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        # Do something with the data
        w3 =  Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/c23493e43a7e411aba08209478828351'))
        print(w3.isConnected())

        trans = w3.eth.get_transaction(name)
        dict1 = {}
        for x,y in trans.items():
            print(x, end=" == ")
            js = json.dumps(y, cls = AttributeDictEncoder)
            dict1[x] = js
        
        context = {
        "trans" : dict1,
        }
        return render(request, 'block_exp_app1/trans_succ.html', context)
    else:
        return render(request, 'block_exp_app1/transaction.html')

