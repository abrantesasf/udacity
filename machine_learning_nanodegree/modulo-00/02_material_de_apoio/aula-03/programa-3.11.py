#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 14:49:21 2018

@author: abrantesasf
"""

import numpy as np
import pandas as pd


def avg_medal_count():
    '''
    Using the dataframe's apply method, create a new Series called 
    avg_medal_count that indicates the average number of gold, silver,
    and bronze medals earned amongst countries who earned at 
    least one medal of any kind at the 2014 Sochi olympics.  Note that
    the countries list already only includes countries that have earned
    at least one medal. No additional filtering is necessary.
    
    You do not need to call the function in your code when running it in the
    browser - the grader will do that automatically when you submit or test it.
    '''

    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea', 
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]
    
    olympic_medal_counts = {'country_name': pd.Series(countries),
                            'gold'        : pd.Series(gold),
                            'silver'      : pd.Series(silver),
                            'bronze'      : pd.Series(bronze)
                           }    
    df = pd.DataFrame(olympic_medal_counts)
    
    avg_medal_count = np.mean(df[['gold', 'silver', 'bronze']])
    # ou:
    avg_medal_count = df[['gold', 'silver', 'bronze']].apply(np.mean)
    # ou:
    avg_medal_count = df[['gold', 'silver', 'bronze']].mean()
    
    return avg_medal_count

avg_medal_count()
