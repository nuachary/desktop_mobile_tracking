import pandas as pd
import sqlite3
from tld import get_fld


def get_cookie_data(hostname_site,visit_id,df_cookie_data,df_cookie_1):
    res_hostname_site = get_fld(hostname_site)
    print(res_hostname_site)
    total_cookies_set = 0
    no_third_party_cookies_set = 0
    third_party_cookie_hostnames = set()
    for index,df_1 in df_cookie_1.iterrows():
        if df_1['record_type'] == 'added-or-changed':
            total_cookies_set = total_cookies_set + 1
            hostname_cookie_setter = df_1['host']
            #print(hostname_cookie_setter.startswith('www'))
            if((hostname_cookie_setter.startswith('www.'))):
                hostname_cookie_setter = 'https://'+hostname_cookie_setter
            elif(hostname_cookie_setter.startswith('.')):
                hostname_cookie_setter = 'https://www'+hostname_cookie_setter
            else:
                hostname_cookie_setter = 'https://www.'+hostname_cookie_setter
            res_hostname_cookie_setter = get_fld(hostname_cookie_setter)
            #print(res_hostname_cookie_setter)
            if(res_hostname_site!=res_hostname_cookie_setter):
                third_party_cookie_hostnames.add(hostname_cookie_setter)
    # df_cookie_data['visit_id'] = visit_id
    # df_cookie_data['hostname_site'] = hostname_site
    # df_cookie_data['total_cookie_set'] = total_cookies_set
    # df_cookie_data['number_third_party_cookies_set'] = len(third_party_cookie_hostnames)
    # df_cookie_data['hostname_of_third_party_cookies'] = third_party_cookie_hostnames
    return df_cookie_data.append(pd.Series([visit_id, hostname_site, total_cookies_set, len(third_party_cookie_hostnames), third_party_cookie_hostnames], index=df_cookie_data.columns ), ignore_index=True)
    print(total_cookies_set)
    print(len(third_party_cookie_hostnames))
    print(third_party_cookie_hostnames)
                
if __name__ == "__main__":
    conn = sqlite3.connect('C:\\Users\\HP\\Documents\\Privacy\\Privacy-Project\\crawl_data_universities.sqlite')
    cur = conn.cursor() 
    #df_1 = cur.execute('SELECT * from crawl')
    query = 'SELECT * from crawl'
    query_1 = 'SELECT * from site_visits'
    df_2 = pd.read_sql_query(query,conn)
    #print(type(df_1))
    #print(df_1)
    print(type(df_2))
    print(df_2)
    query_2 = 'SELECT * from javascript_cookies'
    df_crawl = pd.read_sql_query(query_1,conn)
    print(df_crawl)
    visit_ids = df_crawl.visit_id
    hostname_site = df_crawl.site_url
    print(visit_ids)
    print(hostname_site)

    map_visit_id_url_hostname = {}
    for i in visit_ids:
            map_visit_id_url_hostname[i] = hostname_site[i-1]

    print(map_visit_id_url_hostname)

    df_crawl_cookies = pd.read_sql_query(query_2,conn) 
    print(df_crawl_cookies)
    df_cookies_params = df_crawl_cookies[['visit_id','record_type','expiry','host']]
    print(df_cookies_params)

    df_columns = ['visit_id','hostname_site','total_cookies_set','number_third_party_cookies_set','hostname_of_third_party_cookies']
    df_cookie_data = pd.DataFrame(columns= df_columns)
    for i in visit_ids:
            sql_query_cookie = 'Select * from javascript_cookies where visit_id ={0}'.format(i)
            df_cookies = pd.read_sql_query(sql_query_cookie,conn)
            hostname_site = map_visit_id_url_hostname[i]
            df_cookie_1 = df_cookies[['visit_id','record_type','expiry','host']]
            df_cookie_data = get_cookie_data(hostname_site,i,df_cookie_data,df_cookie_1)

    df_cookie_data.to_csv('C:\\Users\\HP\\Documents\\Privacy\\Privacy-Project\\crawl_data_universities.csv',sep=',')
    print(df_cookie_data)
    #print(df_cookies)

