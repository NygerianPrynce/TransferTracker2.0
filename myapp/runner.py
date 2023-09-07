# runner.py

import sys
import os
import json

# Add the parent directory to the sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


from . import functionz

from django.http import JsonResponse

def findSearchedItemz(search):
    result = functionz.findSearchedItem(search)
    return result


def findDailyTransferz(pids, cids, lids):
    result = functionz.findDailyTransfers(pids, cids, lids)
    return result


#https://code.visualstudio.com/docs/python/tutorial-django