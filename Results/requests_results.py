import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tld import get_tld,get_fld
import json
import networkx as nx

def drawNetworkDiagram(types_website,blocked_domains_all):
    g = nx.Graph()
    c = []
    carach = pd.DataFrame(columns=['ID', 'myvalue'])
    for type_website in types_website:
        carach = carach.append(pd.Series([type_website, 'group1'], index=carach.columns), ignore_index=True)
        g.add_node(type_website)
    
    #print(carach)
    #carach = pd.DataFrame({ 'ID':['business','social_media','news','universities','shopping'], 'myvalue':['group1','group1','group1','group1','group1'] })
    #c.append('yellow')
    # c.append('red')
    # c.append('purple')
    # c.append('green')
    # c.append('blue')
    blocked_domains_common = set()
    i = 0
    for blocked_domain_type in blocked_domains_all:
        for blocked_domain in blocked_domain_type:
            if(g.has_node(blocked_domain) and (blocked_domain not in blocked_domains_common)):
                blocked_domains_common.add(blocked_domain)
                carach = carach.append(pd.Series([blocked_domain, 'group2'], index=carach.columns), ignore_index=True)
            else:
                g.add_node(blocked_domain)
            g.add_edge(types_website[i],blocked_domain)                 
        i = i +1


def drawNetworkDiagram_Lumen_common(tracker_list_lumen,tracker_list_OpenWPM,common_tracker_list):
    g = nx.Graph()
    c = []
    carach = pd.DataFrame(columns=['ID', 'myvalue'])
    g.add_node('OpenWPM')
    g.add_node('Lumen')
    for blocked_sites in tracker_list_lumen:
        carach = carach.append(pd.Series([blocked_sites, 'group1'], index=carach.columns), ignore_index=True)
        g.add_node(blocked_sites)
        g.add_edge('Lumen',blocked_sites)

    for blocked_sites in tracker_list_OpenWPM:
        carach = carach.append(pd.Series([blocked_sites, 'group2'], index=carach.columns), ignore_index=True)
        g.add_node(blocked_sites)
        g.add_edge('OpenWPM',blocked_sites)
    
    for blocked_sites in common_tracker_list:
        carach = carach.append(pd.Series([blocked_sites, 'group3'], index=carach.columns), ignore_index=True)
        g.add_node(blocked_sites)
        g.add_edge('Lumen',blocked_sites)
        g.add_edge('OpenWPM',blocked_sites)



    # blocked_domains_common = set()
    # i = 0
    # for blocked_domain_type in blocked_domains_all:
    #     for blocked_domain in blocked_domain_type:
    #         if(g.has_node(blocked_domain) and (blocked_domain not in blocked_domains_common)):
    #             blocked_domains_common.add(blocked_domain)
    #             carach = carach.append(pd.Series([blocked_domain, 'group2'], index=carach.columns), ignore_index=True)
    #         else:
    #             g.add_node(blocked_domain)
    #         g.add_edge(types_website[i],blocked_domain)                 
    #     i = i +1
    # for each_website_type in blocked_domains_all:   
    #     for each_domain in each_website_type:
    #         if(each_domain not in blocked_domains_common):
    #             carach = carach.append(pd.Series([each_domain, 'group3'], index=carach.columns), ignore_index=True)

    #print(blocked_domains_common)
    carach= carach.set_index('ID')
    carach=carach.reindex(g.nodes())
    carach['myvalue']=pd.Categorical(carach['myvalue'])
    print(carach['myvalue'].cat.codes)
    cmap = plt.cm.Set1
    #print(cmap)
    #node_color=carach['myvalue'].cat.codes
    nx.draw(g,node_size=1500,node_color=carach['myvalue'].cat.codes,cmap=plt.cm.Set2,linewidths=0.4,font_size=7, with_labels=True, dpi=100000)
    plt.title('Common trackers found in Lumen and OpenWPM')
    plt.show()

def get_trackers_specific_site(df,list,trackers):
    for i,row in df.iterrows():
        blocked_urls_l = row['blocked_urls']
        blocked_urls_l = blocked_urls_l[:-1]
        blocked_urls_l = blocked_urls_l[1:]
        s = "'"+","
        blocked_urls_l = blocked_urls_l.split(s)
        if row['hostname_site'] in list:
            for blocked_url in blocked_urls_l:
                blocked_url = blocked_url.strip()
                blocked_url = blocked_url[1:]
                if len(blocked_url) > 0:
                #res = get_tld(urls,as_object=True)
                    fld = get_fld(blocked_url)
                    trackers.add(fld)
    return trackers

def getAverageRequest(df):
    total_request = 0
    for index,row in df.iterrows():
        total_request = total_request + row['total_requests']
    return total_request/len(df)

def getAverageBlockedRequest(df):
    total_blocked_request = 0
    for index,row in df.iterrows():
        total_blocked_request = total_blocked_request + row['no_blocked_requests']
    return total_blocked_request/len(df)

def getAverageThirdPartyRequest(df):
    total_third_party_request = 0
    for index,row in df.iterrows():
        total_third_party_request = total_third_party_request + row['no_third_party_requests']
    return total_third_party_request/len(df)

def getBlockedDomains(df):
    blocked_domains= set()
    for index,row in df.iterrows():
        blocked_urls_l = row['blocked_urls']
        blocked_urls_l = blocked_urls_l[:-1]
        blocked_urls_l = blocked_urls_l[1:]
        s = "'"+","
        blocked_urls_l = blocked_urls_l.split(s)
        #print(index)
        for urls in blocked_urls_l:
            urls = urls.strip()
            urls = urls[1:]
            if len(urls) > 0:
                #res = get_tld(urls,as_object=True)
                fld = get_fld(urls)
                #fld_2 = res.fld
                #print(fld)
                #print(fld_2)
                blocked_domains.add(fld)
    return blocked_domains

if __name__ == "__main__":
    avg_requests_all = []
    avg_blocked_requests_all = []
    avg_third_party_requests_all = []
    types_websites= ['business','social_media','news','universities','shopping']
    path_to_file = 'C:\\Users\HP\\Documents\\Privacy\\Privacy-Project\\Results\\request_data\\request'
    blocked_domains_all = []
    list = ['https://www.cnbc.com/','https://www.pinterest.com/','https://www.macys.com/,https://www.wsj.com/',
    'https://www.ebay.com/',
    'https://www.washingtonpost.com',
    'https://www.amazon.com/',
    'https://www.homedepot.com/',
    'https://www.reddit.com/',
    'https://www.nytimes.com/',
    'https://www.theguardian.com/us',
    'https://www.walmart.com/',
    'https://www2.hm.com/en_us/index.html',
    'https://www.facebook.com/',
    'https://news.google.com/',
    'https://www.target.com/',
    'https://www.youtube.com/',
    'https://news.yahoo.com/',
    'https://www.usatoday.com/',
    'https://www.indeed.com/',
    'https://www.ikea.com/']
    trackers = set()
    for i in types_websites:
        path = path_to_file+'_'+i+'_'+'data.csv'
        df = pd.read_csv(path,sep=",")
        print(df.iloc[:,2])
        get_trackers_specific_site(df,list,trackers)
        avg_requests =  getAverageRequest(df)
        avg_blocked_requests = getAverageBlockedRequest(df)
        avg_third_party_requests = getAverageThirdPartyRequest(df)
        avg_requests_all.append(avg_requests)
        avg_blocked_requests_all.append(avg_blocked_requests)
        avg_third_party_requests_all.append(avg_third_party_requests)
        blocked_domains_all.append(getBlockedDomains(df))

    print('Blocked domains Business')
    print(blocked_domains_all[0])
    print('Blocked domains Social Media')
    print(blocked_domains_all[1])
    print('Blocked domains News')
    print(blocked_domains_all[2])
    print('Blocked domains Universities')
    print(blocked_domains_all[3])
    print('Blocked domains Shopping')
    print(blocked_domains_all[4])
    print(avg_requests_all)
    print(avg_blocked_requests_all)
    print(avg_third_party_requests_all)

    print('Trackers common for Lumen')
    print(trackers)    
    print('\n')
    names_sites = ['Business','Social Media','News','Universities','Shopping']
    y_pos = np.arange(len(names_sites))
    plt.bar(y_pos,avg_blocked_requests_all,align='center',alpha=0.5)
    plt.xticks(y_pos,names_sites)
    plt.ylabel('Avg. no of blocked requests')
    plt.xlabel('Domains')
    plt.title('Avg. no. of blocked requests vs. domain')
    plt.show()
    print('Average blocked requests',avg_blocked_requests_all)

    plt.bar(y_pos,avg_third_party_requests_all,align='center',alpha=0.5)
    plt.xticks(y_pos,names_sites)
    plt.ylabel('Avg. no of third party requests')
    plt.xlabel('Domains')
    plt.title('Avg. no. of third party requests vs. domain')
    plt.show()
    print('Average third party requets all',avg_third_party_requests_all)

    
    # i = 0
    # for name_type in types_websites:
    #     drawNetworkDiagram(name_type,blocked_domains_all[i])
    #     i = i + 1
    tracker_list_lumen = ['crashlytics.com','appsflyer','scorecardresearch','omtrdc.net','urbanairship','branch.io','insightexpress','demdex.net','sectigo.com','apptentative','adobetm.com','assetsadobe.com']
    tracker_list_OpenWPM = ['moatads.com', 'wsod.com', 'adtechus.com', '3lift.com', 'confiant-integrations.global.ssl.fastly.net','criteo.com','akamaihd.net', 'adsrvr.org', 'criteo.net', 'atwola.com', 'media.net', 'deepintent.com', 'serverbid.com','polarcdn-terrax.com', 'sonobi.com','trustx.org', 'ads-twitter.com', 'redditstatic.com', 'openx.net', 'indexww.com', 'casalemedia.com']
    tracker_list_common = ['doubleclick.net', 'doubleverify.com', 'googlesyndication','amazon-adsystem.com', 'adsafeprotected.com', 'googleanalytics.com', 'ampproject.org', 'adnxs.com', 'rubiconproject.com', 'pubmatic.com', 'aaxads.com','accountkit']
    drawNetworkDiagram(types_websites,blocked_domains_all)
    drawNetworkDiagram_Lumen_common(tracker_list_lumen,tracker_list_OpenWPM,tracker_list_common)

    ##Task 3
    
    
    pass
