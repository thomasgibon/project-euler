# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 22:53:30 2015

@author: gibon
"""

import itertools

def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns a list of primes < n """
    sieve = [True] * n # initializes
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*int((n-i*i-1)/(2*i)+1) # i square and all subsequent multiples of i
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def is_prime(k):
    if k <= 1:
        return False
    if k == 2:
        return True
    else:
        i = 2
        while i <= int(k**0.5):
            if k % i == 0:
                return False
            i += 1
        return True

# From http://blog.dreamshire.com/project-euler-60-solution/
primes = rwh_primes(10000)
set_size = 5

def make_chain(chain):
    if len(chain) == set_size: # If the chain is 5-item long
        return chain           # return it
    for p in primes:
        if p > chain[-1] and all_prime(chain+[p]): # If the prime is higher than the last in chain AND all pairs are prime
            new_chain = make_chain(chain+[p])      # 
            if new_chain:
                return new_chain
    return False  
        
def all_prime(chain):
    return all(is_prime(int(str(p[0]) + str(p[1]))) for p in itertools.permutations(chain, 2))

chain = 0

while not chain:
    chain = make_chain([primes.pop(0)])

n = sum(chain)

# Own brute force, takes forever

ub = 1000

p = rwh_primes(ub)

notFound = True

#for i in range(len(p)):
#    for j in range(i):
#        if int(str(p[i]) + str(p[j])) in p and int(str(p[j]) + str(p[i])) in p and notFound:
#            for k in range(j):
#                if  int(str(p[i]) + str(p[k])) in p and int(str(p[k]) + str(p[i])) in p \
#                and int(str(p[j]) + str(p[k])) in p and int(str(p[k]) + str(p[j])) in p and notFound:
#                    print(p[i],p[j],p[k])
#                    for l in range(k):
#                        if  int(str(p[i]) + str(p[l])) in p and int(str(p[l]) + str(p[i])) in p \
#                        and int(str(p[j]) + str(p[l])) in p and int(str(p[l]) + str(p[j])) in p \
#                        and int(str(p[k]) + str(p[l])) in p and int(str(p[l]) + str(p[k])) in p and notFound:
#                            print(p[i],p[j],p[k],p[l])                            
#                            for m in range(l):
#                                if  int(str(p[i]) + str(p[m])) in p and int(str(p[m]) + str(p[i])) in p \
#                                and int(str(p[j]) + str(p[m])) in p and int(str(p[m]) + str(p[j])) in p \
#                                and int(str(p[k]) + str(p[m])) in p and int(str(p[m]) + str(p[k])) in p \
#                                and int(str(p[l]) + str(p[m])) in p and int(str(p[m]) + str(p[l])) and notFound:
#                                    sol = [p[i],p[j],p[k],p[l],p[m]]
#                                    print(sol)
#                                    notFound = False
#    if notFound == False:
#        break

#for i in range(len(p)):
#    for j in range(i):
#        if is_prime(int(str(p[i]) + str(p[j]))) and is_prime(int(str(p[j]) + str(p[i]))) and notFound:
#            for k in range(j):
#                if  is_prime(int(str(p[i]) + str(p[k]))) and is_prime(int(str(p[k]) + str(p[i]))) \
#                and is_prime(int(str(p[j]) + str(p[k]))) and is_prime(int(str(p[k]) + str(p[j]))) and notFound:
#                    for l in range(k):
#                        if  is_prime(int(str(p[i]) + str(p[l]))) and is_prime(int(str(p[l]) + str(p[i]))) \
#                        and is_prime(int(str(p[j]) + str(p[l]))) and is_prime(int(str(p[l]) + str(p[j]))) \
#                        and is_prime(int(str(p[k]) + str(p[l]))) and is_prime(int(str(p[l]) + str(p[k]))) and notFound:
#                            print(p[i],p[j],p[k],p[l])
#                            for m in range(l):
#                                if  is_prime(int(str(p[i]) + str(p[m]))) and is_prime(int(str(p[m]) + str(p[i]))) \
#                                and is_prime(int(str(p[j]) + str(p[m]))) and is_prime(int(str(p[m]) + str(p[j]))) \
#                                and is_prime(int(str(p[k]) + str(p[m]))) and is_prime(int(str(p[m]) + str(p[k]))) \
#                                and is_prime(int(str(p[l]) + str(p[m]))) and is_prime(int(str(p[m]) + str(p[l]))) and notFound:
#                                    sol = [p[i],p[j],p[k],p[l],p[m]]
#                                    print(sol)
#                                    notFound = False
#    if notFound == False:
#        break

# REALLY???
#for i in range(len(p)):
#    for j in range(i):
#        if is_prime(int(str(p[i]) + str(p[j]))):
#            if is_prime(int(str(p[j]) + str(p[i]))) and notFound:
#                for k in range(j):
#                    if is_prime(int(str(p[i]) + str(p[k]))):
#                        if is_prime(int(str(p[k]) + str(p[i]))):
#                            if is_prime(int(str(p[j]) + str(p[k]))):
#                                if is_prime(int(str(p[k]) + str(p[j]))) and notFound:
#                                    for l in range(k):
#                                        if  is_prime(int(str(p[i]) + str(p[l]))):
#                                            if is_prime(int(str(p[l]) + str(p[i]))):
#                                                if is_prime(int(str(p[j]) + str(p[l]))):
#                                                    if is_prime(int(str(p[l]) + str(p[j]))):
#                                                        if is_prime(int(str(p[k]) + str(p[l]))):
#                                                            if is_prime(int(str(p[l]) + str(p[k]))) and notFound:
#                                                                print(p[i],p[j],p[k],p[l])
#                                                                for m in range(l):
#                                                                    if  is_prime(int(str(p[i]) + str(p[m]))):
#                                                                        if is_prime(int(str(p[m]) + str(p[i]))):
#                                                                            if is_prime(int(str(p[j]) + str(p[m]))):
#                                                                                if is_prime(int(str(p[m]) + str(p[j]))):
#                                                                                    if is_prime(int(str(p[k]) + str(p[m]))):
#                                                                                        if is_prime(int(str(p[m]) + str(p[k]))):
#                                                                                            if is_prime(int(str(p[l]) + str(p[m]))):
#                                                                                                if is_prime(int(str(p[m]) + str(p[l]))) and notFound:
#                                                                                                    sol = [p[i],p[j],p[k],p[l],p[m]]
#                                                                                                    print(sol)
#                                                                                                    notFound = False
#    if notFound == False:
#        break     


for i in range(len(p)):
    j_list = [a for a in p[i+1:] if is_prime(int(str(p[i]) + str(a))) and is_prime(int(str(a) + str(p[i])))]
    for j in j_list:
        k_list = [b for b in p[i+1:] if is_prime(int(str(j) + str(b))) and is_prime(int(str(b) + str(j)))]
        inters = set(j_list) & set(k_list)
        if inters:
            print(inters)
#    for j in range(i):
        