#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import argparse
import requests
from multiprocessing import Pool, Manager

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",}
requests.packages.urllib3.disable_warnings()

pathlist=['/v1/api-docs','/v2/api-docs','/v3/api-docs']


def getTargets(filepath):
    fr = open(filepath, 'r')
    ips=fr.readlines()
    fr.close()
    return ips


def saveinfo(result):
    if result:
        fw=open('result.txt','a')
        fw.write(result+'\n')
        fw.close()

def poolmana(ips):
    p = Pool(30)
    q = Manager().Queue()
    for i in ips:
        i=i.replace('\n','')
        p.apply_async(combinedCheck, args=(i,q))
    p.close()
    p.join()
    print('Completed Scanning>>>>>\nCheck this out：result.txt')


def xxljobCheck(url):
    url_tar1 = url + '/xxl-job-admin'
    url_tar2 = url + '/api'
    r1 = requests.get(url_tar1, headers=headers, verify=False, timeout=5)
    r2 = requests.get(url_tar2, headers=headers, verify=False, timeout=5)
    r3 = requests.get(url, headers=headers, verify=False, timeout=5)
    if r1.status_code == 200 and "任务调度中心" in r1.text:
        print("XXL-JOB Admin Center found! You may try weak passwords now! Target Path:{}".format(url_tar1))
        saveinfo("XXL-JOB Admin Center found! You may try weak passwords now! Target Path:{}".format(url_tar1))

    if "xxl.rpc" in r2.text:
        print("XXL-JOB Admin Center Unauthorized api found! Try Hessian deserialization RCE! Target Path:{}".format(url_tar2))
        saveinfo("XXL-JOB Admin Center found! You may try weak passwords now! Target Path:{}".format(url_tar2))

    if "Invalid Req" in r3.text:
        print("XXL-JOB Executor REST api found! Try unauthorized of scheduling RCE! Target Path:{}".format(url))
        saveinfo("XXL-JOB Admin Center found! You may try weak passwords now! Target Path:{}".format(url))


def k8sCheck(url):
    url_tar = url + '/runningpods'
    r = requests.get(url_tar, headers=headers, verify=False, timeout=5)
    if r.status_code == 200 and "PodList" in r.text:
        print("K8S Api found! You may take over the k8s cluster! Target Path:{}".format(url_tar))
        saveinfo("K8S Api found! You may take over the k8s cluster! Target Path:{}".format(url_tar))


def swaggerCheck(url):
    for i in pathlist:
        url_tar=url+i
        r=requests.get(url_tar)
        if r.status_code == 200 and "Swagger" in r.text:
            print("Swagger Documents may found,Check Path:{}".format(url_tar))
            saveinfo("Swagger Documents may found,Check Path:{}".format(url_tar))


def nacosCheck(url):
    url_tar = url +'/nacos'
    r = requests.get(url_tar, headers=headers, timeout=5, verify=False)
    if r.status_code == 200 and "Nacos" in r.text:
        print("Nacos console found! Try weak passwords or authentication bypass! Target Path:{}".format(url_tar))
        saveinfo("Nacos console found! Try weak passwords or authentication bypass! Target Path:{}".format(url_tar))


def flinkCheck(url):
    url_tar = url + '/flink'
    r = requests.get(url_tar, headers=headers, timeout=5, verify=False)
    if r.status_code == 200 and "Flink" in r.text:
        print("Unauthorized access of Flink Console Found! Try RCE! Target Path:{}".format(url_tar))
        saveinfo(("Unauthorized access of Flink Console Found! Try RCE! Target Path:{}".format(url_tar)))

def combinedCheck(url,q):
    nacosCheck(url)
    k8sCheck(url)
    xxljobCheck(url)
    swaggerCheck(url)
    flinkCheck(url)



def run(filepath):
    ips=getTargets(filepath)
    poolmana(ips)


if __name__== '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest='file', help="Load targets from file")
    parser.add_argument("-t", "--target", dest='target', help="Specify your scanning target")
    args = parser.parse_args()
    if args.file:
        run(args.file)
    if args.target:
        combinedCheck(args.target)



