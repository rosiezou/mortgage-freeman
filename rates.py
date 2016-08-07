from collections import namedtuple
fixedplans = namedtuple("fixedplans", "discrate irate period")


listofinterestrates = [0.0275, 0.03375, 0.02875, 0.03, 0.03875, 0.04, 0.04125, 0.0425, 0.04375, 0.045, 0.04625, 0.0475,
                       0.04875, 0.05]
listofperiods = [5, 10, 15, 20, 25, 30]
fiveyradjrate = 0.03456
sevenyradjrate = 0.03412
amtborrowed = 450000  # specified by user input
upperlimit = 1500  # results from client data

# v is a dictionary of discount rates with
#    the keys being the rates and values being
#    listof(iRate, nPeriod) pairs
v = []

for i in listofinterestrates:
    for n in listofperiods:
        m = fixedplans(discrate=1/(1+i) ** n, irate=i, period=n)
        v.append(m)
#print(discountrates)

fixedpayments = []
for i in v:
    fixedpayments.append([(amtborrowed * i[1]/(1-i[0]**i[2]))/12, [i[1], i[2]]])

#fixedpayments.sort()

#fixedfinalretval = list(filter(lambda x: x[0] <= upperlimit, list(fixedpayments)))[-3:]
#print(fixedfinalretval)

adjpayments = []
adjpayments.append([(amtborrowed * 0.03456 / (1 - 1 / (1 + 0.03456) ** 30))/12, "5-year Adjustable starting at 2.75%"])
adjpayments.append([(amtborrowed * 0.03412 / (1 - 1 / (1 + 0.03412) ** 30))/12, "7-year Adjustable starting at 2.875%"])



def insurancetype(purchase):
    # retval = 0
    if purchase == "house":
        # monthly payment + monthly property tax + monthly insurance
        map(lambda x: x[0] + float(2127 / 12) + float(952 / 12), fixedpayments)
        map(lambda x: x[0] + float(2127 / 12) + float(952 / 12), adjpayments)
        # retval = financingplansfixed(amt)[0] + float(2127/12) + float(952/12)
    elif purchase == "car":
        # monthly payment + monthly insurance
        map(lambda x: x[0] + float(412 / 12) + float(2374 / 12), fixedpayments)
        map(lambda x: x[0] + float(412 / 12) + float(2374 / 12), adjpayments)
        # retval = financingplansfixed(amt)[0] + float(412/12) + float(2374/12)


insurancetype("house")

fixedpayments.sort()
adjpayments.sort()

fixedfinalretval = list(filter(lambda x: x[0] <= upperlimit, list(fixedpayments)))[-3:]
print(fixedfinalretval)
adjpaymentsfinal = list(filter(lambda x: x[0] <= upperlimit, list(adjpayments)))
print(adjpayments)