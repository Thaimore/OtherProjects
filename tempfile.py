import json
import tempfile
import os
import sys

exp_dict = {}
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
try:
    with open(storage_path, 'x') as f:
        pass
except FileExistsError:
    with open(storage_path, 'r') as f:
        saver = json.load(f)
        exp_dict.update(saver)


def key_giver(key_name):
    global exp_dict
    if key_name in exp_dict:
        print(*exp_dict[key_name], sep=', ')
    else:
        print(None)


def key_add(key_name, value_add):
    global exp_dict
    if key_name in exp_dict:
        exp_dict[key_name] += (value_add,)
    else:
        adder = {key_name: (value_add,)}
        exp_dict.update(adder)


if len(sys.argv) == 5:
    key_add(sys.argv[2], sys.argv[4])
else:
    key_giver(sys.argv[2])
with open(storage_path, 'w') as f:
    saver = json.dumps(exp_dict)
    f.write(saver)
