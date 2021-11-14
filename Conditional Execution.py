ph= input('Enter the number of hours: ')
pr= input('Enter the @/hr in $: ')
try:
    fh=float(ph)
    fr=float(pr)
    if fh<40:
        tpy=(fh*fr)
    else:
        tpy=((40*fr)+((fh-40)*1.5*fr))
    print('To pay: ', tpy)

except:
    print('Not a valid input')
