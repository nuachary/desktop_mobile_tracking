import json
import re
import sqlite3

import pandas as pd
import requests
from adblockparser import AdblockRules
from tld import get_fld


def read_file(file, rules):
    with open(file) as file:
        for line in file:
            rules.append(line)


def checkURL(adblock_rules,url,hostname,contains_image,contains_script):
    option = {}
    option['image'] = contains_image
    option['javascript'] = contains_script
    is_third_party_url = is_third_party(url,hostname)
    option['third-party'] = is_third_party_url
    #print(option)
    if adblock_rules.should_block(url, option):
        return True, is_third_party_url
    return False,is_third_party_url
    pass

def is_third_party(url,hostname):
    res_host = get_fld(hostname)
    res_url = get_fld(url)
    if res_host != res_url:
        return True
    return False

def get_content_type(list_header):
    for i in range(0,len(list_header)):
        if list_header[i][0] == 'content-type':
            return list_header[i][1]



def getMimetype(row):
    contains_image = False
    contains_script = False
    json_data = json.loads(row['headers'])
    content_type = get_content_type(json_data)
    if(content_type != None):
        if(content_type.startswith('image')):
            contains_image = True
        elif('javascript' in content_type):
            contains_script = True
    return contains_image,contains_script


if __name__ == "__main__":
    rules = []
    read_file('C:\\Users\\HP\\Documents\\Privacy\\Privacy-Project\\easylist.txt', rules)
    adblock_rules = AdblockRules(rules)
    conn = sqlite3.connect('C:\\Users\\HP\\Documents\\Privacy\\Privacy-Project\\crawl_data_shopping.sqlite')
    cur = conn.cursor()
    query = 'SELECT * from site_visits'
    df_crawl = pd.read_sql_query(query, conn)
    visit_ids = df_crawl.visit_id
    hostname_site = df_crawl.site_url

    map_visit_id_url_hostname = {}
    for i in visit_ids:
            map_visit_id_url_hostname[i] = hostname_site[i - 1]

    df_columns = ['visit_id','hostname_site','total_requests','no_blocked_requests','no_third_party_requests','blocked_urls']
    df_request_data = pd.DataFrame(columns= df_columns)
        
    for visit_id in visit_ids:
        sql_query = 'Select * from http_responses where visit_id ={0}'.format(visit_id)
        df_responses = pd.read_sql_query(sql_query, conn)
        sql_query_1 = 'Select * from http_responses where visit_id={0}'.format(visit_id)
        df_responses_request = pd.read_sql_query(sql_query_1,conn)
        hostname_site = map_visit_id_url_hostname[visit_id]
        
        blocked_urls_visit_id = 0
        blocked_urls = []
        no_third_party_urls = 0

        for index,row in df_responses.iterrows():
            if row['url'].startswith('http'):
                contains_image, contains_script = getMimetype(row)
                check_if_block, third_party = checkURL(adblock_rules,row['url'],hostname_site,contains_image,contains_script)
                if(check_if_block):
                    blocked_urls_visit_id = blocked_urls_visit_id + 1
                    blocked_urls.append(row['url'])
                if(third_party):
                    no_third_party_urls = no_third_party_urls + 1
            
        #df_request_data = df_request_data.append({'visit_id':visit_id, 'hostname_site':hostname_site, 'total requets':index+1,'no_blocked_requests':blocked_urls_visit_id, 'no_third_party_requests':no_third_party_urls, 'blocked_urls':blocked_urls}, ignore_index=True)
        df_request_data = df_request_data.append(pd.Series([visit_id, hostname_site, len(df_responses_request),blocked_urls_visit_id,no_third_party_urls,blocked_urls], index=df_request_data.columns), ignore_index=True)
        #print(df_request_data)
        #df_cookie_data.append(pd.Series([visit_id, hostname_site, total_cookies_set, len(third_party_cookie_hostnames), third_party_cookie_hostnames], index=df_cookie_data.columns ), ignore_index=True)
    #print(df_request_data)    
    df_request_data.to_csv('C:\\Users\\HP\\Documents\\Privacy\\Privacy-Project\\request_shopping_data.csv',sep=',')
            
            #df_requests_data = get_request_data(hostname_site, i, df_requests_data, df_request_param)
