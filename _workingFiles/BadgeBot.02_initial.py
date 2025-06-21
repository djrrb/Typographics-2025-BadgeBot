import csv
import random
from utils import hex2rgb
pt = 72

myHeadlineFont = '../assets/Multiplexed overlay fonts/HWTKonop-6Line.otf'
myAffiliationFont = '../assets/Pastiche Grotesque/Pastiche Grotesque v1 OT-CFF/PasticheGrotesque-Regular.otf'
mySerifFont = '../assets/Boogy Brut/Desktop fonts/BoogyBrutPoster-Black.otf'

myOverprintFonts = [
    ('../assets/Multiplexed overlay fonts/Dark_Academia.otf', -.01),
    ('../assets/Multiplexed overlay fonts/Boogy_Brut_Wild_WEB-White.otf', -.15),
    ('../assets/Multiplexed overlay fonts/Boogy_Brut_Wild_WEB-Black.otf', -.15),
    ('../assets/Multiplexed overlay fonts/BalezeV01-One.otf', -.15),
    ]
        
colors = {
    'cover-bg': hex2rgb('#000000'),
    'overprint': hex2rgb('#FB5A3D'),
    'blue': hex2rgb('#0051ff')
    }
    

def drawSafeBadge(myName, myAffiliation):
    newPage(4*pt, 3*pt)
    with savedState():
        scale(.1975)
        #image('/Users/david/Desktop/IMG_1080.jpeg', (-62, -71))
    fill(0, 1)
    rect(0, 0, width(), height())
    
    bigFontSize = 49
    theString = 'TYPOGR'
    with savedState():

        fs = FormattedString(theString, fontSize=bigFontSize, fill=colors['blue'], font=myHeadlineFont)
        text(fs, (-3, 178))
        myOverprintFont, myOverprintOffset = random.choice(myOverprintFonts)

        fsOverprint = FormattedString(theString, fontSize=bigFontSize, fill=colors['overprint'], font=myOverprintFont, baselineShift=myOverprintOffset*bigFontSize/2)
        blendMode('screen')
        text(fsOverprint, (-3, 178))
    
    theString = 'APHICS'
    with savedState():
        fs = FormattedString(theString, fontSize=bigFontSize, fill=colors['blue'], font=myHeadlineFont)
        text(fs, (-3, 0))
        myOverprintFont, myOverprintOffset = random.choice(myOverprintFonts)

        fsOverprint = FormattedString(theString, fontSize=bigFontSize, fill=colors['overprint'], font=myOverprintFont, baselineShift=myOverprintOffset*bigFontSize)
        blendMode('screen')
        text(fsOverprint, (-3, 0))
    
    
    
        m = 25
        mw = width() - m*2
        mh = height() - m
        tfs = 35
    
    
        for word in myName.split(" "):
            theFontSize = 50
            fs = FormattedString(
                word[0], 
                font=myHeadlineFont, 
                fontSize=theFontSize, 
                lineHeight=theFontSize, 
                fill=colors['overprint'],
            )
            fsOverprint = FormattedString(
                word[0], 
                font=myOverprintFont, 
                fontSize=theFontSize, 
                lineHeight=theFontSize, 
                baselineShift=myOverprintOffset*theFontSize,
                fill=colors['blue']
                )
            #text(fs, (m-10, mh-70-10))
            text(fsOverprint, (m-10, mh-70-5))
    
            fs = FormattedString(word, font=mySerifFont, fontSize=tfs, lineHeight=tfs*.9, fill=1)
            
            text(fs, (m, mh-70))
            translate(95, 0)
        #fs.append('\n'+myAffiliation, font=myAffiliationFont, fontSize=17, lineHeight=17, fill=colors['overprint'])
        #textBox(fs, (m, 0, mw, mh-50))








def drawMyBadge(myName, myAffiliation):
    myName = myName.upper()
    m = 25
    mw = width() - m*2
    mh = height() - m
    
    fontSizes = {
        7: mw/7,
        6: mw/6,
        5: mw/5,
        4: mw/4,
        3: mw/3,
        }

    
    print(myName)
    for charsPerLine in [3, 4, 5, 6, 7]:
        for breakChar in ['', '\n']:
            theFontSize = fontSizes[charsPerLine]


            fs = FormattedString(
                '', 
                font=myHeadlineFont, 
                fontSize=theFontSize, 
                lineHeight=theFontSize, 
                fill=colors['overprint'],
            )


            
            myOverprintFont, myOverprintOffset = random.choice(myOverprintFonts)
            
            myBaseColor = colors['overprint']
            myOverprintColor = colors['blue']

            fsOverprint = FormattedString(
                '', 
                font=myOverprintFont, 
                fontSize=theFontSize, 
                lineHeight=theFontSize, 
                baselineShift=myOverprintOffset*theFontSize,
                fill=colors['blue']
                )
        
            words = myName.split(' ')
            words[0] = 'O' +words[0] 
            for wordIndex, word in enumerate(words):
                fs.append(
                    word, 
                    fill=myBaseColor
                )
                print(myOverprintFont)
                newOverprintFont = myOverprintFont
                while newOverprintFont == myOverprintFont:
                   newOverprintFont, newOverprintOffset = random.choice(myOverprintFonts)
                myOverprintFont = newOverprintFont
                myOverprintOffset = newOverprintOffset

   
                fsOverprint.append(
                    word, 
                    font=myOverprintFont, 
                    baselineShift=myOverprintOffset*theFontSize,
                    fill=myOverprintColor
                )
                if wordIndex % 2:
                    myOverprintColor = colors['blue']
                    myBaseColor = colors['overprint']
                else:
                    myOverprintColor = colors['overprint']
                    myBaseColor = .8, .8, 1
 
        
                if wordIndex != len(words) - 1:
                    
                    fs.append(breakChar, fill=(0, 0, 0, 0))
                    fsOverprint.append(breakChar)
            
            
            overflow = textOverflow(fs, (m, m, mw, mh))
            if overflow and overflow != ' ':
                continue
            
            newPage(4*pt, 3*pt)
            fill(*colors['cover-bg'])
            rect(0, 0, width(), height())

            
            with savedState():
                textBox(fs, (m, 10, mw+10, mh))
                blendMode('screen') 
                textBox(fsOverprint, (m, 10, mw+10, mh))
    
            fsAffiliation = FormattedString(myAffiliation, fontSize=10, font=myAffiliationFont, fill=colors['overprint'], lineHeight=10)
            textBox(fsAffiliation, (m, m-15, width(), 12))



with open('../csvs/attendees.csv', encoding="utf-8") as myCSV:
    myCSVReader = csv.reader(myCSV)
    myTick = 0
    for rowNumber, myLine in enumerate(myCSVReader):
        #if rowNumber == 0:
        #    continue
        myFirstName = str(myLine[3])
        myLastName = str(myLine[4])
        myName = myFirstName.strip() + ' ' + myLastName.strip()
        
        myName = myName.replace('-', '−')
        myAffiliation = str(myLine[13])

        #drawMyBadge(myName, myAffiliation)
        drawSafeBadge(myName, myAffiliation)
        
        myTick += 1
        if myTick > 10:
            break
        