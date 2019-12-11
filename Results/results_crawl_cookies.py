import math
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def getAverageTotal_And_ThirdPartyCookies(df):
    total_cookies_set = 0
    total_third_party_cookies_set = 0
    for i in range(0,len(df)):
        total_cookies_set = total_cookies_set + df.iloc[i][3]
        total_third_party_cookies_set = total_third_party_cookies_set + df.iloc[i][4]
    print(total_cookies_set)
    print(total_third_party_cookies_set)
    average_cookies_set_business = total_cookies_set/len(df)
    average_third_party_cookies_set_business = total_third_party_cookies_set/len(df)
    return np.round(average_cookies_set_business,decimals=0),np.round(average_third_party_cookies_set_business,decimals=0)

if __name__ == "__main__":
    
    #print(df)
    average_cookies_list = []
    average_third_party_cookies_list = []
    
    df = pd.read_csv('C:\\Users\\HP\\Documents\\Privacy\\Privacy-Project\\crawl_data_business.csv',sep=',')
    avg_total, avg_third_party = getAverageTotal_And_ThirdPartyCookies(df)
    average_cookies_list.append(avg_total)
    average_third_party_cookies_list.append(avg_third_party)

    df = pd.read_csv('C:\\Users\\HP\\Documents\\Privacy\\Privacy-Project\\crawl_data_social_media.csv',sep=',')
    avg_total, avg_third_party = getAverageTotal_And_ThirdPartyCookies(df)
    average_cookies_list.append(avg_total)
    average_third_party_cookies_list.append(avg_third_party)

    df = pd.read_csv('C:\\Users\\HP\\Documents\\Privacy\\Privacy-Project\\crawl_data_news.csv',sep=',')
    avg_total, avg_third_party = getAverageTotal_And_ThirdPartyCookies(df)
    average_cookies_list.append(avg_total)
    average_third_party_cookies_list.append(avg_third_party)

    df = pd.read_csv('C:\\Users\\HP\\Documents\\Privacy\\Privacy-Project\\crawl_data_universities.csv',sep=',')
    avg_total, avg_third_party = getAverageTotal_And_ThirdPartyCookies(df)
    average_cookies_list.append(avg_total)
    average_third_party_cookies_list.append(avg_third_party)

    df = pd.read_csv('C:\\Users\\HP\\Documents\\Privacy\\Privacy-Project\\crawl_data_shopping.csv',sep=',')
    avg_total, avg_third_party = getAverageTotal_And_ThirdPartyCookies(df)
    average_cookies_list.append(avg_total)
    average_third_party_cookies_list.append(avg_third_party)

    
    print(average_cookies_list)
    print(average_third_party_cookies_list)

    names_sites = ['Business','Social Media','News','Universities','Shopping']
    y_pos = np.arange(len(names_sites))
    plt.bar(y_pos,average_third_party_cookies_list,align='center',alpha=0.5)
    plt.xticks(y_pos,names_sites)
    plt.ylabel('Avg. no of Third party cookies')
    plt.xlabel('Domains')
    plt.title('Avg. no. of Third party cookies set vs. domain')
    plt.show()

    
    