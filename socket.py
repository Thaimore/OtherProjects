import socket
import time


class ClientError(Exception):
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = socket.socket()
        self.sock.settimeout(self.timeout)
        self.sock.connect((self.host, self.port))

    def put(self, metric_name, value, timestamp=None):
        self.metric_name = metric_name
        self.value = value
        try:
            pass
            #if not self.metric_name or not self.value:
                #raise ClientError
        except:
            raise ClientError
        self.timestamp = timestamp
        if self.timestamp:
            self.timestamp = int(self.timestamp)
        try:
            if not self.timestamp:
                self.timestamp = int(time.time())
            g = 'put ' + str(self.metric_name) + ' ' + str(self.value) + ' ' + str(self.timestamp) + '\n'
            g = g.encode('utf8')
            self.sock.sendall(bytes(g))
            data = self.sock.recv(1024)
            data = data.decode('utf8')
            if data != 'ok\n\n':
                raise ClientError
            else:
                return data
        except:
            raise ClientError

    def get(self, metrics):
        self.metrics = metrics
        try:
            g = 'get ' + str(self.metrics) + '\n'
            g = g.encode('utf8')
            self.sock.sendall(bytes(g))
            data = self.sock.recv(1024)
            data = data.decode('utf8')
            print(data)
            empty_dict = {}
            if not data.startswith('ok') or not data.endswith('\n\n'):
                raise ClientError
            if data == 'ok\n\n':
                return empty_dict
            data = data.split('\n')
            del data[0], data[-1], data[-1]
            for i in data:
                i = i.split(' ')
                i[2] = float(i[2])
                i[2] = int(i[2])
                if i[0] in empty_dict:
                    empty_dict[i[0]] += [(i[2], float(i[1]))]
                else:
                    a = {i[0]: [(i[2], float(i[1]))]}
                    empty_dict.update(a)
            for i in empty_dict:
                empty_dict[i].sort()
            return empty_dict
        except:
            raise ClientError

a = Client('127.0.0.1', 10001)

a.put('test_same_timestamp', 0.0, 1503319740)
a.put('test_same_timestamp', 100.99, 1503319743)
a.put('test_same_timestamp', 0.0, 1503319740)
a.put('test_same_timestamp', 100.99, 1503319743)
a.get('test_same_timestamp')


'''''''''
a.put('test_multivalue_key', 12.5, 1503319743)
a.put('test_multivalue_key', 10.678, 1503319748)
a.put('some_test', 21.0, 1503319740)
a.put('test_multivalue_key', 12.0, 1503319740)
a.get('test_multivalue_key')
'''''''''