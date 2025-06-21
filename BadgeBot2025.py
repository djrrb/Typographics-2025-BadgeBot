import csv
import random
from utils import hex2rgb
pt = 72

myHeadlineFont='/Users/david/Documents/Education/Clients/Typographics-2025/assets/Tick-Regular.otf'
myAffiliationFont = 'Export'

        
colors = {
    'cover-bg': hex2rgb('#000000'),
    'overprint': hex2rgb('#FB5A3D'),
    'blue': hex2rgb('#0051ff')
    }


blueColor = (77/255, 170/255, 248/255)                        
redColor = (234/255, 51/255, 35/255)
    
exceptionsList = [
    'Tobias Frere-Jones',
    'Elizabeth Carey Smith',
    'Sarah Cadigan-Fried',
    'Carima El-Behairy',
    'Cara Di Edwardo'
    ]


def getRandom():
    return random.random()*random.choice([-1, 1])


def drawSafeBadge(myName, myAffiliation, drawNewPage=False, topRowValue=0):
    w, h = 4*pt, 3*pt
    if drawNewPage:
        newPage(w, h)
    #with savedState():
    #    scale(.1975)
    fill(*blueColor)
    rect(0, 0, w, h)
    
    m = 8
    mw = w - m*2
    bottom = 8
    mh = h - m - bottom

    affiliationOffset = 20
    tfs = 85
    leadingMultiplier = .9
    trackingValue=12/1000
    
    for word in myName.split(' '):
        wordFS = FormattedString(word, font=myHeadlineFont, fontSize=tfs, tracking=trackingValue*tfs)
        wordWidth = textSize(wordFS)[0]
        if wordWidth > mw:
            tfs = mw/wordWidth * tfs
            
    lines = []
    words = []
    lineTotal = 0
    spaceWidth = textSize(FormattedString(' ', font=myHeadlineFont, fontSize=tfs, tracking=trackingValue*tfs))[0]
    for word in myName.split(' '):
        wordFS = FormattedString(word, font=myHeadlineFont, fontSize=tfs, tracking=trackingValue*tfs)
        wordWidth = textSize(wordFS)[0]
        if lineTotal + wordWidth > mw:
            lines.append(words)
            lineTotal = 0
            words = []
        words.append(word)
        lineTotal += wordWidth
    if words:
        lines.append(words)
        
    if len(lines) > 2:
        print('three lines')
        tfs = 65

    
    
    lines = []
    words = []
    lineTotal = 0
    spaceWidth = textSize(FormattedString(' ', font=myHeadlineFont, fontSize=tfs, tracking=trackingValue*tfs))[0]
    for word in myName.split(' '):
        wordFS = FormattedString(word, font=myHeadlineFont, fontSize=tfs, tracking=trackingValue*tfs)
        wordWidth = textSize(wordFS)[0]
        if lineTotal + wordWidth > mw:
            lines.append(words)
            lineTotal = 0
            words = []
        words.append(word)
        lineTotal += wordWidth
    if words:
        lines.append(words)
        
    titleHeight = mh
    yOffset = 5
    if myAffiliation:
        bottom += affiliationOffset
        titleHeight -= affiliationOffset
        yOffset += affiliationOffset*.25


    fs = FormattedString(myName, font=myHeadlineFont, fontSize=tfs, lineHeight=tfs*leadingMultiplier, fill=(1, 1, 0, .5), align="center")
    
    
    fill(1, 0, 0, .5)
    
    
    textWidth, textHeight = textSize(fs, width=mw)
    yOffset += 0
    xOffset = (mw-textWidth)/2

    #fill(0, 1, 0, .5)
    #rect(m+xOffset, bottom+yOffset, textWidth, textHeight)
    
    print(yOffset)
    
    textBoxOffset = tfs*.025
    
    nameBox = (m, bottom+yOffset+textBoxOffset, mw, textHeight)
    #textBox(fs, nameBox)
    
    m += 5
    mw -= 10
    mh -= 10
    
    #fill(0, .5)
    #rect(0, 0, width(), height())
    
    bp1 = BezierPath()
    bp2 = BezierPath()
    bp2.beginPath()
    
    bp2.moveTo((m - random.random() * m/2, m - random.random() * m/2 ))
    bp2.lineTo((m+mw + random.random() * m/2, m - random.random() * m/2 ))
    bp2.lineTo((m+mw + random.random() * m/2, m+mh + random.random() * m/2))
    bp2.lineTo((m - random.random() * m/2, m+mh + random.random() * m/2))
    bp2.closePath()
    
    theBox = bp2.copy()

    font(myHeadlineFont, tfs)
    yAdvance = height()/2 + yOffset
    if len(lines) == 1:
        yAdvance -= tfs/2
    
    with savedState():
        #translate(m, bottom+yOffset+textBoxOffset*2+textHeight)
        #oval(-10, -10, 20, 20)
        # draw lines
        fsCopy = fs.copy()
        #translate(0, -tfs*leadingMultiplier)
        if len(lines) == 1:
            yOffset -= 10
        for line in lines:
            xAdvance = m
            with savedState():
                line = ' '.join(line)
                print('LINE', line)
                lineFS = FormattedString(line, font=myHeadlineFont, fontSize=tfs, tracking=trackingValue*tfs)
                lineWidth = textSize(lineFS)[0]
                xOffset = (mw-lineWidth)/2
                xAdvance += xOffset
                fill(1, 1, 1)
                #text(line, (xOffset, -tfs*leadingMultiplier))
                previousLetterWidth = 0
                previousLetter = ''
                for letter in line:
                    comboFS = FormattedString(previousLetter+letter, font=myHeadlineFont, fontSize=tfs, tracking=trackingValue*tfs) 
                    letterFS = FormattedString(letter, font=myHeadlineFont, fontSize=tfs, tracking=trackingValue*tfs) 
                    letterWidth = textSize(letterFS)[0]
                    kern = textSize(comboFS)[0] - letterWidth - previousLetterWidth
                    
                    xAdvance += kern
                    
                    
                    bounce = getRandom()* 75/1000*tfs
                
                    bpLetter = BezierPath()
                    
                    bpLetter.text(letter, (xAdvance, yAdvance), font=myHeadlineFont, fontSize=tfs)
                    print(line, letter, ord(letter), bpLetter)
                    try:
                        bpLetterWidth = bpLetter.bounds()[2] - bpLetter.bounds()[0]
                        bpLetterHeight = bpLetter.bounds()[3] - bpLetter.bounds()[1]
                    except:
                        bpLetterWidth = 0
                        bpLetterHeight = tfs/3
                    bpLetter.rotate(getRandom()*3.5, (xAdvance+bpLetterWidth/2, yAdvance+bpLetterHeight/2))
                    bpLetter.translate(0, bounce)

                    bp1 = bp1.union(bpLetter)


                    bpLetter = BezierPath()
                    
                    displace = random.choice([-20/1000*tfs, 20/1000*tfs])
                    bpLetter.text(letter, (xAdvance+displace, yAdvance-displace), font=myHeadlineFont, fontSize=tfs)


                    try:
                        bpLetterWidth = bpLetter.bounds()[2] - bpLetter.bounds()[0]
                        bpLetterHeight = bpLetter.bounds()[3] - bpLetter.bounds()[1]
                    except:
                        bpLetterWidth = 0
                        bpLetterHeight = tfs

                    bpLetter.rotate(getRandom()*3.5, (xAdvance+bpLetterWidth/2, yAdvance+bpLetterHeight/2))
                    bpLetter.translate(0, bounce)
                    
                    
                    bp2 = bp2.difference(bpLetter)
                    
                    
                    translate(letterWidth)
                    xAdvance += letterWidth
                    
                    previousLetterWidth = letterWidth
                    previousLetter = letter
  
            #translate(0, -tfs*leadingMultiplier)
            yAdvance -= tfs*leadingMultiplier
    

        fill(1)   
        drawPath(bp1)
        fill(*redColor)
        #blendMode('multiply')
        fill(0)
        bp3 = bp2.difference(bp1)
        #bp3 = bp3.difference(theBox)
        drawPath(bp3)
        fill(*redColor)
        bp3 = bp2.intersection(bp1)
        drawPath(bp3)

    affiliationFS = FormattedString(myAffiliation, font=myAffiliationFont, fontSize=12, lineHeight=12, fill=colors['overprint'], align="center")


    textBox(affiliationFS, (0, 0, width(), 28))







## SHEET FUNCTIONS

def drawCropMarks(rows, cols, boxWidth, boxHeight, badgeWidth, badgeHeight, margin):
    # assuming we are in the top right, draw crop marks
    with savedState():
        stroke(1)
        for row in range(rows+1):
            line((-margin, -row*badgeHeight), (-margin/2, -row*badgeHeight))
            line((boxWidth+margin, -row*badgeHeight), (boxWidth+margin/2, -row*badgeHeight))
        for col in range(cols+1):
            line((col*badgeWidth, margin), (col*badgeWidth, margin/2))
            line((col*badgeWidth, -boxHeight-margin/2), (col*badgeWidth, -boxHeight-margin))









def drawSheets(data, w, h, sheetWidth=8.5*pt, sheetHeight=11*pt, badgeWidth=None, badgeHeight=None, margin=.25*pt, multiple=2, pattern=None):
    """
    Make a sheet of badges for printing purposes.
    """

    if not badgeWidth:
        badgeWidth = w
    if not badgeHeight:
        badgeHeight = h

    # determine available space
    boxWidth = sheetWidth - margin * 2
    boxHeight = sheetHeight - margin * 2
    # determine number of columns and rows
    cols = int ( boxWidth / badgeWidth )
    rows = int ( boxHeight / badgeHeight )

    # reset the box space based on the badge size, rather than the page size
    boxWidth = cols * badgeWidth
    boxHeight = rows * badgeHeight


    #setup first page
    newPage(sheetWidth, sheetHeight)
    topRow = True
    # fill the sheet with the background color, as a rudimentary bleed
    
    #rect(0, sheetHeight-boxHeight-margin-margin, sheetWidth, boxHeight+margin*2)
    # move to the top left corner, which is where we will start
    translate(margin, sheetHeight-margin)
    # draw crop marks
    drawCropMarks(rows, cols, boxWidth, boxHeight, badgeWidth, badgeHeight, margin)
    # drop down to the bottom left corner to draw the badges
    translate(0, -badgeHeight)

    # loop through data
    rowTick = 0
    colTick = 0
    for i, rowData in enumerate(data[:]):
        name, company = rowData

        bleedLeft = 100
        bleedRight = 0
        prevColor = None
        usedPatterns = []
        usedColorPalettes = []
        for m in range(multiple):
            # draw the badge without setting the page size
            
            if colTick == 0:
                bleedLeft = 100
                bleedRight = 0
            else:
                bleedLeft = 0
                bleedRight = 100
                
            if topRow:
                topRowValue = 40
            else:
                topRowValue = 0
                
            drawSafeBadge(
                name,
                company,
                topRowValue=topRowValue
            )
            translate(badgeWidth, 0)

            # if we have made it to the last column, translate back and start the next one
            if colTick == cols - 1:
                translate(-badgeWidth*cols, 0)
                translate(0, -badgeHeight)
                colTick = 0
                topRow = False


                # if we have made it to the last row (and there is still more data), start a new page
                if rowTick == rows - 1 and i != len(data) - 1:
                    # setup a new page
                    newPage(sheetWidth, sheetHeight)
                    topRow = True
                    # fill the sheet with the background color, as a rudimentary bleed
                    #rect(0, sheetHeight-boxHeight-margin-margin, sheetWidth, boxHeight+margin*2)
                    # move to the top left corner, which is where we will start
                    translate(margin, sheetHeight-margin)
                    # draw crop marks
                    drawCropMarks(rows, cols, boxWidth, boxHeight, badgeWidth, badgeHeight, margin)
                    # drop down to the bottom left corner to draw the badges
                    translate(0, -badgeHeight)
                    rowTick = 0
                else:
                    rowTick += 1
            else:
                colTick += 1



def getData(path='../csvs/Badges_June_11_8am.csv'):
    myData = []
    with open(path, encoding="utf-8") as myCSV:
        myCSVReader = csv.reader(myCSV)
        myTick = 0
        for rowNumber, myLine in enumerate(myCSVReader):
            if rowNumber == 0:
                continue
            myFirstName = str(myLine[0])
            myLastName = str(myLine[1])
            myName = myFirstName.strip() + ' ' + myLastName.strip()
            if myName in exceptionsList:
                myName = myFirstName.strip() + '\n' + myLastName.strip()
            if myName == 'Vera van de Seyp':
                myName = 'Vera van\nde Seyp'
            if myName == 'Sherry Muyuan He':
                myName = 'Sherry\nMuyuan He'
            #myName = myName.replace('-', '−')
            myName = myName.replace('ö', 'ö')
            myAffiliation = str(myLine[26])
            if myAffiliation == 'The Unemployed Philosophers Guild':
                myAffiliation = 'The Unemployed\nPhilosophers Guild'
            elif myAffiliation == 'Natural History Museum of Los Angeles County':
                myAffiliation = 'Natural History Museum of\nLos Angeles County'
            if myAffiliation.lower() in ['n/a', 'na', 'student', 'unemployed', 'usa', 'freelance', 'none', 'self-employed', ] or myAffiliation == myName:
                myAffiliation = ''

            myData.append((myName, myAffiliation))
        
            myTick += 1
            #if myTick > 100:
            #    break
    return myData
        
        
data = getData()
#drawSheets(data, 4*pt, 3*pt)
#saveImage('~/desktop/sheets.pdf')
newDrawing()
for row in data:
    drawSafeBadge(row[0], row[1], True)
saveImage('~/desktop/individuals.pdf')