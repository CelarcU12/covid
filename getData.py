import json
import requests

params = {'from':'2020-10-01T00:00:00Z',
            'to':'2020-10-101T00:00:00Z'}
#res = requests.get('https://api.covid19api.com/country/slovenia/status/confirmed', params=params)

#print(res.json())

#cases = []
#for el in res.json():
#    print(el['Date'] + ": "+str(el['Cases']))
#    cases.append(el['Cases'])

#zadnij14=cases[-14:]
#stPrimerov14 = zadnij14[-1]-zadnij14[0]
#print("Število primerov zadnih 14 dni: "+ str(stPrimerov14))
#print(" Na 100 000   -> " + str(stPrimerov14/2000000*100000))

def get14(country='slovenia', populacija=2000000):
    url = 'https://api.covid19api.com/country/'+country+'/status/confirmed'
    res = requests.get(url,params=params)
    cases = []
    for el in res.json():
        #print(el['Date'] + ": "+str(el['Cases']))
        cases.append(el['Cases'])
  #  cases.append(cases[-1]+700)
    zadnij14=cases[-14:]
    stPrimerov14 = zadnij14[-1]-zadnij14[0]
    print("Zadnja meritev %s" % (cases[-1]-cases[-2]))
    return stPrimerov14/populacija*100000

countryes={'slovenia': 2000000,'croatia':4058000, 'austria':8859000,'italy':60360000}

for key  in countryes:
    print('con   '+ key)
    print('pop '+ str(countryes[key]))

    print('Za državo %s je 14 dnevna incidenca %s' % (key, get14(key, countryes[key])))