import json
import redis
import random
import time
import datetime
import threading
from pyspark import  SparkContext
def makeRedisData(size):
    redisTool = redis.Redis("192.168.200.73","6379",0);
    redisTool2 = redis.Redis("192.168.200.73","6379",1);
    redisTool3 = redis.Redis("192.168.200.73","6379",2);
    redisTool4 = redis.Redis("192.168.200.73","6379",3);
    redisList = [redisTool,redisTool2,redisTool3,redisTool4]
    files = open('/home/apuser/datamake/vinlistforTripCan.csv','w',encoding='utf-8')
    print('vehicle_id,target_date,ig_on,ig_off',file=files)
    for redisU in redisList:
        # print(str(makeHashVinData(vinlist)))
        vinlist = makeVinCode(size);
        # json.dumps(makeHashVinData(vinlist))
        yyyyMMddHH = time.strftime("%Y%m%d%H",time.localtime())
        redisU.hset(name = yyyyMMddHH+"_index",mapping = makeHashVinData(vinlist))
        for vin in vinlist:
            redisU.hset(name= yyyyMMddHH+"_"+vin,mapping = makeJson(vin,files));
        
    return 'Redis Data Make Finished';

# 生成vin号
def makeVinCode(size):
    index = 0;
    vinList = [];
    while(index<size):
        vin = "TESTVIN"+''.join(random.sample('QWERTYUIOPASDFGHJKLZXCVBNM',5))+"0000"+''.join(random.sample('1234567890',4))
        vinList.append(vin);
        index = index + 1;
    return vinList;
# 根据时间和vinlist 生成对应的hash vin数据 
def makeHashVinData(vinList):
    print('make vin Data')
    dict = {};
    for vin in vinList:
        dict[vin] = vin;
    return dict;
##
# YYYYMMDDHH_LVGE41353NG001002
# #
def makeJson(vinKey,files):
    vin = vinKey
    # igon = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    today =  datetime.datetime.now();
    # 计算偏移量
    offset_lower = datetime.timedelta(hours=-1,minutes=-random.randint(1,45))
    offset_upper = datetime.timedelta(hours=-3,minutes=-random.randint(1,45))
    # 生成 ig on/off
    igon = (today+offset_lower).strftime("%Y-%m-%d %H:%M:%S");
    igoff = (today + offset_upper).strftime("%Y-%m-%d %H:%M:%S") 
    target_date = (today+offset_lower).strftime("%Y-%m-%d");
    size =  ''.join(random.sample('123456789',1)).join(random.sample('1234567890',3))
    tripCnt =  ''.join(random.sample('123456789',1)).join(random.sample('1234567890',2))
    #将生成vin保存文文件，方便之后TripCan数据制作
    print(','.join([vin,target_date,igon,igoff]) ,file=files)
    return {
        "vehicle_id":vin,
        "trip_cnt":tripCnt,
        "ig_on":igon,
        "ig_off":igoff,
        "size":size
    }
def makeSparkDat(csv_url):
    spark = SparkContext( 'local[3]', 'pyspark').getOrCreate()
    ds = spark.textFile(csv_url)
    def f(r):
        print(r,"/home/apuser/datamake/child/vinlistforTripCan.csv")
    all = ds.repartition(3).mapPartitions(f).collect()
    print(all,'/home/apuser/datamake/read.csv')
# makeSparkDat('/home/apuser/datamake/vinlistforTripCan.csv')
def multiThreadTask(size):
    t1 = threading.Thread(target=makeRedisData, args=(size,))
    t2 = threading.Thread(target=makeRedisData, args=(size,))
    t3 = threading.Thread(target=makeRedisData, args=(size,))
    t4 = threading.Thread(target=makeRedisData, args=(size,))
    t5 = threading.Thread(target=makeRedisData, args=(size,))
    t6 = threading.Thread(target=makeRedisData, args=(size,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    # 将 t1 和 t2 加入到主线程中
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
multiThreadTask(200000)

