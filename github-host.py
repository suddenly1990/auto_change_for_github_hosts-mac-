#!/usr/bin/env python
#coding=utf-8
#功能 ：自动设置github.com的host ip
#日期 ：2021-09-25 
#作者：Dark-Athena
#email ：darkathena@qq.com
#说明：自动从备选ip清单中寻找最低延时IP，设置到本地host中，需要使用管理员权限运行
"""
Copyright DarkAthena(darkathena@qq.com)

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import ping3
from python_hosts import Hosts, HostsEntry

iplist=list((
"13.250.177.223",
"52.69.186.44",
"140.82.112.4",
"52.74.223.119",
"15.164.81.167",
"140.82.113.3",
"13.229.188.59",
"140.82.112.3",
"140.82.114.3",
"20.205.243.166",
"52.192.72.89",
"140.82.121.3",
"140.82.113.4",
"52.78.231.108",
"13.114.40.48",
"140.82.114.4",
"140.82.121.4"
))
PingTime=0.0
MinTime=999.0
for k in iplist:
    PingTime=ping3.ping(k,timeout=1,unit='ms')
    if not PingTime:
        PingTime=5000.0
    if PingTime<MinTime:
        MinTime=PingTime
        FastIp=k
    print(k+','+str(int(PingTime)))
print('最快IP是:'+FastIp+' 延迟'+str(int(MinTime))+'ms')

my_hosts = Hosts()
new_entry = HostsEntry(entry_type='ipv4', address= FastIp, names=['github.com'])
hosts11 = my_hosts.add([new_entry])
my_hosts.write()

