# 特殊数据处理
import time
import datetime


class EspecialData(object):
    # 获取房间折扣价格
    def get_discounts_price(self,price, discount):
        if discount:
            roomPrice = price * (100 - int(discount)) / 100
        else:
            roomPrice = price
        newPrice = '%0.2f'%(round(roomPrice,2))
        return newPrice

    # 获取营业日
    # def get_business_day(self):
    #     return time.strftime('%Y-%m-%d', time.localtime())

    # 获取营业日期：
    def get_business_day(self):
        return datetime.datetime.now().strftime('%Y-%m-%d')

    # 生成一个时间（生成入住、离店时间）
    def get_target_time(self,days):
        targetTime = (datetime.datetime.now() + datetime.timedelta(days=days)).strftime('%Y-%m-%d %H:%M:%S')
        return targetTime

    # 生成一个时间（YYYYMMMDDHHMMSS格式）datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    def get_order_time(self):
        orderTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        return orderTime

    # 生成一个日期
    def get_target_date(self,days):
        targetDate = (datetime.datetime.now() + datetime.timedelta(days=days)).strftime('%Y-%m-%d')
        return targetDate

    # 生成一个日期6
    def get_target_date6(self,days):
        targetDate = (datetime.datetime.now() + datetime.timedelta(days=days)).strftime('%Y%m%d')
        return targetDate

    # str类型的日期转换为时间戳(10位)
    def get_time_stamp(self,timeStr):
        # 转为时间数组
        timeArray = time.strptime(timeStr,'%Y-%m-%d')
        timestamp = int(time.mktime(timeArray))
        return timestamp

    # str类型的日期转换为13位的时间戳
    def get_time_stamp13(self,timeStr):
        timeArray = datetime.datetime.strptime(timeStr,'%Y-%m-%d %H:%M:%S')
        # 10位
        timeStamp = str(int(time.mktime(timeArray.timetuple())))
        # 3位，秒
        timeMicrosecond = str('%06d'%timeArray.microsecond)[0:3]
        timeStamp = timeStamp + timeMicrosecond
        return int(timeStamp)


    # 生成一个字符串类型随机数
    def get_random_num(self):
        nowTime = time.time()*100
        return int(nowTime)
    def get_target_datetime(self, hours):
        now = datetime.datetime.now()
        #        now = datetime.datetime(2021,7,21,21,00,000)
        target_date = datetime.datetime.today().date()
        target_time = datetime.time( 22, 30, 00, 000 )
        target = datetime.datetime.combine( target_date, target_time )
        if (target - now).seconds < hours * 60 * 60:
            targetDate = target.strftime( '%Y-%m-%d %H:%M:%S' )
        else:
            targetDate = (datetime.datetime.now() + datetime.timedelta( hours=hours )).strftime( '%Y-%m-%d %H:%M:%S' )
        return targetDate



if __name__ == '__main__':
    es = EspecialData()
    st = es.get_target_date(-1)
    # et = es.get_target_date(1)
    # at = es.get_time_stamp(st)
    # at1 = es.get_time_stamp13(st)
    # lt = es.get_time_stamp13(et)
    print(type(st),st)
    # print(type(et),et)
    # print(type(at),at)
    # print(type(at),at1)
    # print(type(lt),lt)



