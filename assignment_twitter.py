import os
import string
import operator
import sys


def get_max_users(n):
        with open ('Newzealand.txt','r') as f:
                lines = f.readlines()

        dic = {}
        for line in lines:
                username = line.split()[0]
                if username in dic.keys():
                        dic[username] += 1
                else:
                        dic[username] = 1
        dic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
        write_to = open('1.txt', 'w')
        write_to.write("The top n users who have tweeted the most for the entire timeline:\n")
        for i in range(n):
                write_to.write(dic[i][0]+"\n")

        write_to.close()

def users_max_followers(n):
        with open('Newzealand.txt', 'r') as f:
                lines = f.readlines()

        dic = {}
        for line in lines:
                split_space = line.split()
                followers = int(split_space[-2])
                username = split_space[0]
                if username not in dic.keys():
                        dic[username] = followers
        dic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
        write_to = open('3.txt', 'w')
        write_to.write("The top n users who have the maximum followers:\n")
        for i in range(n):
                write_to.write(dic[i][0] + "\n")
        write_to.close()

def max_retweets(n):
        with open('Newzealand.txt', 'r') as f:
                lines = f.readlines()

        dic = {}
        for line in lines:
                split_space = line.split()
                leng_line = len(split_space) - 2
                tweet = ""
                for i in range(3, leng_line):
                        tweet += split_space[i] + " "
                if tweet not in dic.keys():
                        dic[tweet] = int(split_space[-1])


        dic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
        write_to = open('4.txt', 'w')
        write_to.write("The top n tweets which have the maximum retweet count.:\n")
        for i in range(n):
                write_to.write(dic[i][0] + "\n")
        write_to.close()


if __name__ == '__main__':

        if len(sys.argv) > 1:

                n = int(sys.argv[1])
                get_max_users(n)
                users_max_followers(n)
                max_retweets(n)
        else:
                print("Please put n as argument")