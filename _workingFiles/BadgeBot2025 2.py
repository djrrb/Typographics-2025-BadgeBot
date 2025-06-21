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
    
    
exceptionsList = [
    'Tobias Frere-Jones',
    'Elizabeth Carey Smith',
    'Sarah Cadigan-Fried',
    'Carima El-Behairy',
    'Cara Di Edwardo'
    ]

def drawSafeBadge(myName, myAffiliation, drawNewPage=False, topRowValue=0):
    w, h = 4*pt, 3*pt
    if drawNewPage:
        newPage(w, h)
    #with savedState():
    #    scale(.1975)
    fill(0, 1)
    rect(0, 0, w, h)
    
    m = 10
    mw = w - m*2
    bottom = 10
    mh = h - m - bottom

    affiliationOffset = 25
    tfs = 85
    leadingMultiplier = .95
    trackingValue=15/1000
    
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
        
    
    if myAffiliation:
        bottom += affiliationOffset
        mh -= affiliationOffset


    fs = FormattedString(myName, font=myHeadlineFont, fontSize=tfs, lineHeight=tfs*leadingMultiplier, fill=(1, 1, 0, .5), align="center")
    
    affiliationFS = FormattedString(myAffiliation, font=myAffiliationFont, fontSize=15, lineHeight=15, fill=colors['overprint'], align="center")
    
    fill(1, 0, 0, .5)
    #rect(m, bottom, mw, mh)
    
    
    textWidth, textHeight = textSize(fs, width=mw)
    yOffset = (mh-textHeight)/2
    xOffset = (mw-textWidth)/2

    #fill(0, 1, 0, .5)
    #rect(m+xOffset, bottom+yOffset, textWidth, textHeight)
    
    print(yOffset)
    
    textBoxOffset = tfs*.025
    
    nameBox = (m, bottom+yOffset+textBoxOffset, mw, textHeight)
    #textBox(fs, nameBox)

    textBox(affiliationFS, (0, 0, width(), 25))
    
    #fill(0, .5)
    #rect(0, 0, width(), height())

    font(myHeadlineFont, tfs)
    with savedState():
        translate(m, bottom+yOffset+textBoxOffset*2+textHeight)
        #oval(-10, -10, 20, 20)
        # draw lines
        fsCopy = fs.copy()
        translate(0, -tfs*leadingMultiplier)
        for line in lines:
            with savedState():
                line = ' '.join(line)
                print('LINE', line)
                lineFS = FormattedString(line, font=myHeadlineFont, fontSize=tfs, tracking=trackingValue*tfs)
                lineWidth = textSize(lineFS)[0]
                xOffset = (mw-lineWidth)/2
                fill(1, 1, 1)
                #text(line, (xOffset, -tfs*leadingMultiplier))
                previousLetterWidth = 0
                previousLetter = ''
                for letter in line:
                    comboFS = FormattedString(previousLetter+letter, font=myHeadlineFont, fontSize=tfs, tracking=trackingValue*tfs) 
                    letterFS = FormattedString(letter, font=myHeadlineFont, fontSize=tfs, tracking=trackingValue*tfs) 
                    letterWidth = textSize(letterFS)[0]

                
                    kern = textSize(comboFS)[0] - letterWidth - previousLetterWidth
                    
                    
                    def getRandom():
                        return random.random()*random.choice([-1, 1])
                    
                    
                    blueColor = (77/255, 170/255, 248/255)                        
                    redColor = (234/255, 51/255, 35/255)
                    
                    translate(kern)
                    jiggle = 40/1000 * tfs
                    with savedState():
                        translate(xOffset)
                        #fill(1, 0, 0)
                        #oval(-2, -2, 4, 4)
                        blendMode('normal')
                        translate(0, getRandom()*jiggle)
                        
                        
                        colorScheme = choice(
                            [(redColor, blueColor)]
                        )

                        with savedState():
                            redShift = 0
                            
                            rotate(randint(-3, 3), center=(letterWidth/2, tfs/3))
                            translate(randint(-2, 2), randint(-4, 4))
                            fill(*colorScheme[0])                        
                            text(letter, (0, 0))
                        with savedState():
                            blueShift = 0
                            
                            rotate(randint(-3, 3), center=(letterWidth/2, tfs/3))
                            translate(randint(-2, 2), randint(-4, 4))
                            fill(*colorScheme[1])                        
                            text(letter, (0, 0))
                        with savedState():
                            rotate(getRandom()*3, center=(letterWidth/2, tfs/3))
                            blendMode('normal')
                            fill(1, 1)
                            text(letter, (0, 0))
                    translate(letterWidth)
                    previousLetterWidth = letterWidth
                    previousLetter = letter
            
            translate(0, -tfs*leadingMultiplier)
    
    
    
def wackyTextBox(fs, box, tfs, mw, yOffset, lines, leadingMultiplier=.87):

        # while fsCopy:
        #     with savedState():
        #         beforeOverflow = fsCopy.copy()
        #         fsCopy = textOverflow(fsCopy, (tbX, tbY, tbW, tfs))
        #         print(fs, fsCopy)
        #         index = str(fs).index(str(fsCopy))
        #         print(index)
        #         lines[-1] = lines[-1]:
        #         lines.append(fsCopy[:index+1])
        #     translate(0, -tfs*.87)
        print(lines)
        


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
drawSheets(data, 4*pt, 3*pt)
saveImage('~/desktop/sheets.pdf')
newDrawing()
for row in data:
    drawSafeBadge(row[0], row[1], True)
saveImage('~/desktop/individuals.pdf')