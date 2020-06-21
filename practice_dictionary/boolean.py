import string
#freshman = 'freshman'
#sophomore = 'sophomore'
#junior = 'junior'
#senior = 'senior'
college = None
COE = None
CMSE = None
ASMSU_tax = 21
FM_Radio_tax = 3
State_news_tax = 5
JMC_tax = 7.5
while True:
    resident = input("Is student a resident of Michigan?:(Enter 'yes' or 'no' only)")
    resident = resident.lower()
    try:
        if resident == 'yes' or resident == 'no':
            break
        else:
            print("response must be either 'yes' or 'no'")
            continue
    except:
        print ('Invalid data')
        continue
if resident == 'no':
    while True:
        international = input("Does student reside outside the United States?: (Enter 'yes' or 'no' only)")
        international = international.lower()
        try:
            if international == 'yes' or international == 'no':
                break
            else:
                print("response must be either 'yes' or 'no'")
                continue
        except:
            print ('Invalid input')
            continue
else:
    international = 'no'
while True:
    level = input("Please enter your level:'freshman','sophomore', 'junior','senior':")
    level = level.lower()
    try:
        if level == 'freshman' or level == 'sophomore' \
        or level == 'junior' or level == 'senior':
            break
        else:
            print('Invalid input, please try again')
            continue
    except:
        print('Invalid data')
        continue
if level == 'junior' or level == 'senior':
    while True:
        college = input("Is your college--'business','engineering','health','sciences', or 'none'?")
        college = college.lower()
        try:
            if college == 'business' or college == 'engineering' or college == 'health' or college == 'sciences' or college == 'none':
                break
            else:
                print('Invalid input, please try again')
                continue
        except:
          print("Invalid input, please try again")
          continue
if level == 'junior' or level == 'senior':
    while True:
        CMSE = input ("Is your major, CMSE (i.e. Computational Mathematics and Engineering)?: (Enter 'yes' or 'no')")
        CMSE = CMSE.lower()
        try:
            if CMSE == 'yes' or CMSE == 'no':
                break
            else:
                print('Invalid input, please try again')
        except:
            print ("Invalid input, please try again")
            continue
if level == 'freshman' or level == 'sophomore':
    while True:
        COE = input ("Were you admitted to College of Engineering?: (Enter 'yes' or 'no')")
        COE = COE.lower()
        try:
            if COE == 'yes' or COE == 'no':
                break
            else:
                print('Invalid input, please try again')
        except:
            print ("Invalid input, please try again")
            continue
if college == None or college == 'none':
    while True:
        JMC = input("Is student in James Madison College?: (Enter 'yes' or 'no')")
        JMC = JMC.lower()
        try:
            if JMC == 'yes' or JMC == 'no':
                break
            else:
                 print('Invalid input, please try again')
        except:
            print('Invalid input, please try again')
            continue
else:
    JMC = 'no'
while True:
    credits = input('Please enter the amount of credits taken this semester: ')
    credits = float(credits)
    try:
        if credits > 0: break
        else:
            print('Invalid input. The number of credits must be a positive number.')
    except:
        print ('Invalid input. Please enter a positive number for credits.')
        continue
print(resident)
print(international)
print(level)
print(college)
print(CMSE)
print(COE)
print(JMC)
print(credits)
if resident == 'yes' and level == 'freshman':
    if credits > 18:
        basic = 7230 + (credits - 18) * 482
    elif credits > 11:
        basic = 7230
    else:
        basic = credits * 482
if resident == 'yes' and level == 'sophomore':
    if credits > 18:
        basic = 7410 + (credits - 18) * 494
    elif credits > 11:
        basic = 7410
    else:
        basic = credits * 494
if resident == 'yes' and (level == 'junior' or level == 'senior') and (college == 'business' or college == 'engineering'):
    if credits > 18:
        basic = 8595 + (credits - 18) * 573
    elif credits > 11:
        basic = 8595
    else:
        basic = credits * 573
if resident == 'yes' and (level == 'junior' or level == 'senior') and (college == 'health' or college == 'sciences' or college == 'none'):
    if credits > 18:
        basic = 8325 + (credits - 18) * 555
    elif credits > 11:
        basic = 8325
    else:
        basic = credits * 555
if resident != 'yes' and (level == 'freshman' or level ==' sophomore'):
    if credits > 18:
        basic = 19863 + (credits - 18) * 1325.50
    elif credits > 11:
        basic = 19863
    else:
        basic = 1325.90 * credits
if resident != 'yes' and (level == 'junior' or level == 'senior') and (college == 'health' or college == 'sciences' or college == 'none'):
    if credits > 18:
        basic = 20501 + (credits - 18) * 1366.75
    elif credits > 11:
        basic = 20501
    else:
        basic = 1366.75 * credits
if resident != 'yes' and (level == 'junior' or level == 'senior') and (college == 'business' or college == 'engineering'):
    if credits > 18:
        basic = 20786 + (credits - 18) * 1385.75
    elif credits > 11:
        basic = 20786
    else:
        basic = 1385.75 * credits
if college == 'business' and (level == 'junior' or level == 'senior'):
    if credits > 4:
        basic = basic + 226
    else:
        basic = basic + 113
if college == 'engineering':
    if credits > 4:
        basic = basic + 670
        print(basic)
    else:
        basic = basic + 113
if college == 'health' or college == 'sciences' and (level == 'junior' or level == 'senior'):
    if credits > 4:
        basic = basic + 100
    else:
        basic = basic + 50
if CMSE == 'yes' and (level == 'junior' or level == 'senior'):
    if credits > 4:
        basic = basic + 670
    else:
        basic = basic + 402
if international == 'yes':
    if credits > 4:
        basic = basic + 750
    else:
        basic = basic + 375
basic = basic + ASMSU_tax
basic = basic + FM_Radio_tax
if credits > 6:
    basic = basic + State_news_tax
if JMC == 'yes':
    basic = basic + JMC_tax
print("$",format(basic, ",.2f"))
