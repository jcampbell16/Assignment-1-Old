# Get constants
nAme = str(input('Please insert your name:'))  # Users name
aGe = int(input('Please enter your age:'))  # Users age
cLaSs_Code = str(input('Please insert your class code(either B, D or W): ').upper())  # Class code that reads both upper and lower case
rEnT = int(input('Please insert how many days the car was rented: '))  # Rental days amount
# Calculate the rounding to weeks for 'W' code
if rEnT % 7 == 0:
    wEEks = rEnT//7
else:
    wEEks = (rEnT//7)+1

sTarT_Ode = int(input('Please enter the starting odometer reading: '))  # Beginning odometer number
eNd_Ode = int(input('Please enter the ending odometer reading: '))  # End number of odometer
tOtAl_Km = int(eNd_Ode - sTarT_Ode)  # Complete number of Km
avKMD = tOtAl_Km/rEnT  # Average number of km per day
avKMW = float(tOtAl_Km/wEEks)  # Average number of km per week

# Do class code B
if cLaSs_Code == 'B':
    if aGe < 25:
        tOtAl = ((20*rEnT) + (10*rEnT) + (0.30*tOtAl_Km))
        tOtAl= ("%.2f" % tOtAl)
        print ("\n{}\nAge:{}\nClass Code: {} \nDays rented: {} \nOdometer at beginning of rental: {} \nOdometer at end of rental: {} \nTotal km: {} \nYour total cost is ${}.".format(nAme,aGe,cLaSs_Code,rEnT,sTarT_Ode,eNd_Ode,tOtAl_Km,tOtAl))
    else:
        tOtAl = ((20*rEnT) + (0.30*tOtAl_Km))
        tOtAl= ("%.2f" % tOtAl)
        print("\n{}\nAge:{}\nClass Code:{}\nDays rented:{}\nOdometer at beginning of rental:{}\nOdometer at end of rental:{}\nTotal km:{}\nYour total cost is ${}.".format(nAme,aGe,cLaSs_Code,rEnT,sTarT_Ode,eNd_Ode,tOtAl_Km,tOtAl))
# Do class code D
elif cLaSs_Code == 'D':
    if aGe < 25:
        if avKMD >= 100:
                tOtAl = ((50*rEnT) + (10*rEnT)+ (0.30*(avKMD-100)*rEnT))
                tOtAl= ("%.2f" % tOtAl)
                print("\n{}\nAge:{}\nClass Code:{}\nDays rented:{}\nOdometer at beginning of rental:{}\nOdometer at end of rental:{}\nTotal km:{}\nYour total cost is ${}.".format(nAme,aGe,cLaSs_Code,rEnT,sTarT_Ode,eNd_Ode,tOtAl_Km,tOtAl))
        else:
                tOtAl = ((50 * rEnT) + (10*rEnT))
                tOtAl= ("%.2f" % tOtAl)
                print("\n{}\nAge:{}\nClassCode:{}\nDays rented:{}\nOdometer at beginning of rental:{}\nOdometer at end of rental:{}\nTotal km:{}\nYour total cost is ${}.".format(nAme,aGe,cLaSs_Code,rEnT,sTarT_Ode,eNd_Ode,tOtAl_Km,tOtAl))
    else:
        if avKMD >= 100:
                tOtAl = ((50*rEnT) + ((.30*(avKMD-100)) * rEnT))
                tOtAl= ("%.2f" % tOtAl)
                print("\n{}\nAge:{}\nClass Code:{}\nDays rented:{}\nOdometer at beginning of rental:{}\nOdometer at end of rental:{}\nTotal km:{}\nYour total cost is ${}.".format(nAme,aGe,cLaSs_Code,rEnT,sTarT_Ode,eNd_Ode,tOtAl_Km,tOtAl))
        else:
                tOtAl = (50*rEnT)
                tOtAl= ("%.2f" % tOtAl)
                print("\n{}\nAge:{}\nClass Code:{}\nDays rented:{}\nOdometer at beginning of rental:{}\nOdometer at end of rental:{}\nTotal km:{}\nYour total cost is ${}.".format(nAme,aGe,cLaSs_Code,rEnT,sTarT_Ode,eNd_Ode,tOtAl_Km,tOtAl))
# Class code W
elif cLaSs_Code == 'W':
    if aGe < 25:
        if avKMW <= 1000:
                tOtAl = ((200*wEEks)+ (10*rEnT))
                tOtAl= ("%.2f" % tOtAl)
                print("\n{}\nAge:{}\nClass Code:{}\nDays rented:{}\nOdometer at beginning of rental:{}\nOdometer at end of rental:{}\nTotal km:{}\nYour total cost is ${}.".format(nAme,aGe,cLaSs_Code,rEnT,sTarT_Ode,eNd_Ode,tOtAl_Km,tOtAl))
        elif 1000 < avKMW <= 2000:
            tOtAl = ((200*wEEks) + (50*wEEks) + (10*rEnT))
            tOtAl= ("%.2f" % tOtAl)
            print("\n{}\nAge:{}\nClass Code:{}\nDays rented:{}\nOdometer at beginning of rental:{}\nOdometer at end of rental:{}\nTotal km:{}\nYour total cost is ${}.".format(nAme,aGe,cLaSs_Code,rEnT,sTarT_Ode,eNd_Ode,tOtAl_Km,tOtAl))
        else:
            tOtAl= ((200*wEEks) + (100*wEEks) + ((0.3*(avKMW-2000)) + (10*rEnT)))
            tOtAl= ("%.2f" % tOtAl)
            print("\n{}\nAge:{}\nClass Code:{}\nDays rented:{}\nStarting odometer at beginning of rental:{}\nOdometer at end of rental:{}\nTotal km:{}\nYour total cost is ${}.".format(nAme,aGe,cLaSs_Code,rEnT,sTarT_Ode,eNd_Ode,tOtAl_Km,tOtAl))
    else:
        if avKMW <= 1000:
            tOtAl= (200*wEEks)
            tOtAl= ("%.2f" % tOtAl)
            print("\n{}\nAge:{}\nClass Code:{}\nDays rented:{}\nOdometer at beginning of rental:{}\nOdometer at end of rental:{}\nTotal km:{}\nYour total cost is ${}.".format(nAme,aGe,cLaSs_Code,rEnT,sTarT_Ode,eNd_Ode,tOtAl_Km,tOtAl))
        elif 1000 < avKMW <= 2000:
            tOtAl= ((200*wEEks) + (50*wEEks))
            tOtAl= ("%.2f" % tOtAl)
            print("\n{}\nAge:{}\nClass Code:{}\nDays rented:{}\nOdometer at beginning of rental:{}\nOdometer at end of rental:{}\nTotal km:{}\nYour total cost is ${}.".format(nAme,aGe,cLaSs_Code,rEnT,sTarT_Ode,eNd_Ode,tOtAl_Km,tOtAl))
        else:
            tOtAl = ((200*wEEks) + (100*wEEks) + (0.3*((avKMW - 2000)*wEEks)))
            tOtAl= ("%.2f" % tOtAl)
            print("\n{}\nAge:{}\nClass Code:{}\nDays rented:{}\nOdometer at beginning of rental:{}\nOdometer at end of rental:{}\nTotal km:{}\nYour total cost is ${}.".format(nAme,aGe,cLaSs_Code,rEnT,sTarT_Ode,eNd_Ode,tOtAl_Km,tOtAl))
else:
    print('\n{} \n Age: {} \n You have entered the invalid class code: {}.\n Please try again.'.format(nAme,aGe,cLaSs_Code))
