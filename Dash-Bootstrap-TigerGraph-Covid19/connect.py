import pyTigerGraph as tg
from config import host, un, graph, pw

hostname = host
username = un
graphname = graph
password = pw
conn = None


def getConnection():
    try:
        conn = tg.TigerGraphConnection(host=hostname,
                                    graphname=graphname,
                                    username=username,
                                    password=password,
                                    useCert=False, 
                                    version='3.0.5',
                                    dev=True
                                    ) #usercert=false
        secret = None #conn.createSecret()
        
        token = None
        return conn            
    except Exception as e:
        print(e)
        print('There was an error. Make sure to start your box and try again')

