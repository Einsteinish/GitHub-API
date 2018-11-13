#! /usr/bin/env python2
import json
import requests
import time
import calendar
import argparse
import sys
import operator

DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
WEEK_IN_SECOND = 604800

def count_commits(repo, weeks, sort):

    # Get commit activity via Github REST API v3 with Python's requests module
    r = requests.get('https://api.github.com/repos/%s/stats/commit_activity' % repo)

    repos = json.loads(r.content)
    # sample : [{'days': [0, 0, 0, 0, 0, 0, 0], 'total': 0, 'week': 1511053200}, ... ]

    # calculate time cut in weeks
    current_epoctime = calendar.timegm(time.gmtime())
    week_cut = current_epoctime-(weeks)*WEEK_IN_SECOND

    # initialize commits for the days of a week
    commits = [0]*7
    # loop through commits week by week. Cut by input 'weeks'
    for r in repos:
       if r['week'] >= week_cut:
           for i,d in enumerate(r['days']):
               commits[i] += d

    # average commits per week
    commits = [c/weeks for c in commits]

    # construct dictionary from the two list : zip(DAYS, commits)
    # then, sort it (default: descending)
    days_commits = dict(zip(DAYS, commits))
    days_commits = sorted(days_commits.items(), key = operator.itemgetter(1), reverse = (sort == 'dsc'))
    # sample :  days_commits =  [('Wednesday', 75.95), ('Thursday', 73.7), ... ]

    print('\n--- Commits (average) ---')
    for item in days_commits:
        print('%s %.1f' %(item[0],item[1]))

    print('\n--- The most commits ---')
    if sort == 'dsc':
        index = 0  # top
    else:
        index = 6  # bottom
    print('%s %.1f' %(days_commits[index][0],days_commits[index][1]))


# setup args including default values and input error handling
def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Github API - stats of commits')
    #parser.add_argument('repo', metavar='repository name', type=str, help='user/repo')
    parser.add_argument('-r', nargs='?', default='kubernetes/kubernetes')
    parser.add_argument('-w', nargs='?', default='52')
    parser.add_argument('-s', nargs='?', default='dsc')
    results = parser.parse_args(args)
    return (results.r, results.w, results.s)

# MAIN
if __name__ == '__main__':

    '''
    Count Github commits via 'stats/commit_activity' - using REST API v3
    Usage :  python ask_ki.py -r kubernetes/kubernetes -w=36 -s=dsc
    (note) All args are optional: '-r', '-w', and '-s'
    '''

    r, w, s = check_arg(sys.argv[1:])
    print('Inputs: repo=%s weeks=%s sort=%s' %(r,w,s))

    # call github api
    count_commits(repo=r, weeks=int(w), sort=s)

    
