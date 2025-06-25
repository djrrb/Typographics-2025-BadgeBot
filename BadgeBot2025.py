import csv
import random
from utils import hex2rgb
pt = 72

myHeadlineFont='/Users/david/Documents/Education/Clients/Typographics-2025/assets/Tick-Regular.otf'
myAffiliationFont = 'Export'


blueColor = (0/255, 170/255, 255/255)                        
redColor = (255/255, 12/255, 12/255)
yellowColor = (255/255, 255/255, 0/255)
    
DEBUG = False

def getRandom():
    # return a random value between -1 and 1
    return random.random()*random.choice([-1, 1])
    
def getRandomRange(theMin, theMax, alsoNegative=True, multiplier=100):
    # return a random range, but don't worry as muchabout integers
    value = randint(int(theMin*multiplier), int(theMax*multiplier) ) / multiplier
    if alsoNegative:
        if random.random() > .5:
            value *= -1
    return value


def drawSafeBadge(myName, myAffiliation, drawNewPage=False, topRowValue=0):
    w, h = 4*pt, 3*pt
    if drawNewPage:
        newPage(w, h)
       
    # background 
    fill(*blueColor)
    rect(0, 0, w, h)

    # calculate outer margins
    m = 6
    mw = w - m*2
    bottom = 8
    mh = h - m - bottom

    # set some constants
    affiliationOffset = 20 # less room for name when affiliation is present
    tfs = 85 # the font size by default
    leadingMultiplier = .96 # the leading by default
    trackingValue=20/1000 # the tracking bydefault
    
    #for char in myName:
    #    if ord(char) > 128:
    #        leadingMultiplier = 1

    # reduce the font size to accomodate the longest word
    for word in myName.split(' '):
        wordFS = FormattedString(word, font=myHeadlineFont, fontSize=tfs, tracking=trackingValue*tfs)
        wordWidth = textSize(wordFS)[0]
        if wordWidth > mw:
            tfs = mw/wordWidth * tfs
        
    # try to arrange the words into lines
    lines = []
    words = []
    lineTotal = 0
    spaceWidth = textSize(FormattedString(' ', font=myHeadlineFont, fontSize=tfs, tracking=trackingValue*tfs))[0]
    for word in myName.split(' '):
        wordFS = FormattedString(word, font=myHeadlineFont, fontSize=tfs, tracking=trackingValue*tfs)
        wordWidth = textSize(wordFS)[0]
        if words and lineTotal + wordWidth > mw:
            lines.append(words)
            lineTotal = 0
            words = []
        if word:
            words.append(word)
        lineTotal += wordWidth# + spaceWidth
    if words:
        lines.append(words)
    
    # arrange the words into lines again
    # i'm not sure why i have this twice
    lines = []
    words = []
    lineTotal = 0
    spaceWidth = textSize(FormattedString(' ', font=myHeadlineFont, fontSize=tfs, tracking=trackingValue*tfs))[0]
    for word in myName.split(' '):
        wordFS = FormattedString(word, font=myHeadlineFont, fontSize=tfs, tracking=trackingValue*tfs)
        wordWidth = textSize(wordFS)[0]
        # make a new line
        print(lines, words, wordWidth, lineTotal)
        if words and lineTotal + wordWidth > (mw):
            lines.append(words)
            lineTotal = 0
            words = []
        if word:
            words.append(word)
        lineTotal += wordWidth# + spaceWidth
    if words:
        #if lineTotal + wordWidth > (mw):
        #    lines[-1] = lines[-1] + words
        #else:
        if True:
            lines.append(words)
   
    # make some exceptions for long names
    if len(lines) > 2: 
        if myAffiliation:
            tfs = min(tfs, 58)
        else:
            tfs = min(tfs, 64)
    if len(lines) > 3 and myName.startswith('MARTA REBECA'):
        lines = [lines[0], lines[1], lines[2]+lines[3]]
    if len(lines) > 2 and myName.startswith('SADIE RED'):
        tfs = 70
        lines = [lines[0], lines[1]+lines[2]]

    
    # okay now we are going to typeset the name
    yOffset = 8
    affiliationY = 0
    titleHeight = mh

    # move things around if an affiliate exists
    if myAffiliation:
        bottom += affiliationOffset
        titleHeight -= affiliationOffset
        yOffset += affiliationOffset*.25


    # this formatted string is FPO, we will not use it
    fs = FormattedString(myName, font=myHeadlineFont, fontSize=tfs, lineHeight=tfs*leadingMultiplier, fill=(1, 1, 0, .5), align="center")


    #fill(1, 0, 0, .5)

    # get the dimensions of the text
    textWidth, textHeight = textSize(fs, width=mw)

    # center the text
    xOffset = (mw-textWidth)/2

    #fill(0, 1, 0, .5)
    #rect(m+xOffset, bottom+yOffset, textWidth, textHeight)

    #print(lines)

    if DEBUG:
        textBoxOffset = tfs*.025
        nameBox = (m, bottom+yOffset+textBoxOffset, mw, textHeight)
        textBox(fs, nameBox)

    # we will draw a black box
    # we will increase the margins slightly
    # so that the names will overlap the margins
    m += 7
    mw -= 14
    mh -= 14

    if DEBUG:
        fill(0, .5)
        rect(0, 0, width(), height())

    
    # we will typeset into two main bezier paths
    # the first will just contain the letters
    # the second will contain the letters cut out of a background field
    bp1 = BezierPath()
    bp2 = BezierPath()

    # draw background rectangle
    bp2.beginPath()
    bp2.moveTo((m - random.random() * m/2, m - random.random() * m/2 ))
    bp2.lineTo((m+mw + random.random() * m/2, m - random.random() * m/2 ))
    bp2.lineTo((m+mw + random.random() * m/2, m+mh + random.random() * m/2))
    bp2.lineTo((m - random.random() * m/2, m+mh + random.random() * m/2))
    bp2.closePath()

    theBox = bp2.copy()

    font(myHeadlineFont, tfs)
    
    # start from half the height, plus offset
    yAdvance = h/2 + yOffset
    
    
    # center line, if one line
    if len(lines) == 1:
        yAdvance -= tfs/2

    # shift for 3 lines, this is very hacky and should be rewritten
    if len(lines) > 2:
        yAdvance += tfs/2 - 2

    with savedState():
        if DEBUG:
            translate(m, bottom+yOffset+textBoxOffset*2+textHeight)
            oval(-10, -10, 20, 20)
            

        #translate(0, -tfs*leadingMultiplier)
        # 
        if len(lines) == 1:
            yOffset -= 10
        
        if DEBUG:
            # draw first baseline
            with savedState():
               stroke(1, 0, 0)
               strokeWidth(5)
               line((0, yAdvance), (width(), yAdvance))

        
        # establish the bounce direction
        # this will alternate letter by letter
        bounceDirection = choice([-1, 1])
        
        # loop through each line
        for myLine in lines:
            # track xAdvance
            xAdvance = m
            with savedState():
                # join the words into a single string
                myLine = ' '.join(myLine)
                # get the width
                lineFS = FormattedString(myLine, font=myHeadlineFont, fontSize=tfs, tracking=trackingValue*tfs)
                lineWidth = textSize(lineFS)[0]
                # move the xOffset so the line is centered
                xOffset = (mw-lineWidth)/2
                # hang line-ending hyphens
                if myLine[-1] == '-':
                    xOffset += tfs/6
                # move our x position to the cenetered offset
                xAdvance += xOffset
                if DEBUG:
                    fill(1, 1, 1)
                    text(line, (xOffset, -tfs*leadingMultiplier))
                
                # keep track of the previous letter
                previousLetterWidth = 0
                previousLetter = ''
            
                # loop through each letter in the line
                for letter in myLine:
                    # get the combined width of the previous letter and the current letter
                    comboFS = FormattedString(previousLetter+letter, font=myHeadlineFont, fontSize=tfs, tracking=trackingValue*tfs) 
                    letterFS = FormattedString(letter, font=myHeadlineFont, fontSize=tfs, tracking=trackingValue*tfs) 
                    letterWidth = textSize(letterFS)[0]
                    # determine the kerning value by finding the difference between
                    # the combined width and the two letters’ setwidths
                    kern = textSize(comboFS)[0] - letterWidth - previousLetterWidth
                
                    # add kerning to the x advance
                    xAdvance += kern
                
                    # determine bounce for this letter
                    # a random portion of the font size and the bounce direction
                    bounce = randint(35, 55)/1000 * tfs * bounceDirection
                    # don't let accented chars bounce up
                    if ord(letter) > 128:
                        bounce = 55/1000 * tfs * -1
                    #bounce = 0

                    # change bounce direction
                    if bounceDirection == 1:
                        bounceDirection = -1
                    elif bounceDirection == -1:
                        bounceDirection = 1
            
                    # draw this letter into a path
                    bpLetter = BezierPath()
                    bpLetter.text(letter, (xAdvance, yAdvance), font=myHeadlineFont, fontSize=tfs)
                    # try to determine dimensions of letter
                    try:
                        bpLetterWidth = bpLetter.bounds()[2] - bpLetter.bounds()[0]
                        bpLetterHeight = bpLetter.bounds()[3] - bpLetter.bounds()[1]
                    except:
                        bpLetterWidth = 0
                        bpLetterHeight = tfs/3
                    # rotate from center of letter, if we know it
                    bpLetter.rotate(getRandomRange(2, 2, True), (xAdvance+bpLetterWidth/2, yAdvance+bpLetterHeight/2))
                    # incorporate the bounce
                    bpLetter.translate(0, bounce)

                    # add the letter to the main bezier path
                    bp1 = bp1.union(bpLetter)

                    # do it all again, this time with an offset and more rotation
                    bpLetter = BezierPath()
                    # shift things either one way or the other
                    # trying to avoid little shifts that are close to zero
                    displace = random.choice([-23/1000*tfs, 23/1000*tfs])
                    bpLetter.text(letter, (xAdvance+displace, yAdvance-displace), font=myHeadlineFont, fontSize=tfs)

                    # try to determine dimensions of letter
                    try:
                        bpLetterWidth = bpLetter.bounds()[2] - bpLetter.bounds()[0]
                        bpLetterHeight = bpLetter.bounds()[3] - bpLetter.bounds()[1]
                    except:
                        bpLetterWidth = 0
                        bpLetterHeight = tfs
                    # rotate and translate the letter
                    bpLetter.rotate(getRandomRange(2, 6, True), (xAdvance+bpLetterWidth/2, yAdvance+bpLetterHeight/2))
                    bpLetter.translate(0, bounce+getRandom()*2)
                
                    # add the letter to the larger bezierPath
                    bp2 = bp2.difference(bpLetter)
                
                    if DEBUG:
                        translate(letterWidth)
                    # advance to the next letter
                    xAdvance += letterWidth
                    
                    # set this as the previous letter
                    previousLetterWidth = letterWidth
                    previousLetter = letter
  
            if DEBUG:
                translate(0, -tfs*leadingMultiplier)
            # move to the next line
            yAdvance -= tfs*leadingMultiplier

        # once the bezier paths are complete, we will draw them to canvas

        # bp1 is white
        fill(1)   
        drawPath(bp1)
        
        # get the overlap, and draw it in black
        fill(0)
        bp3 = bp2.difference(bp1)
        drawPath(bp3)
        
        # draw the shifted portion in red
        fill(*redColor)
        bp4 = bp2.intersection(bp1)
        drawPath(bp4)
        



    # typeset the affiliation
    
    affiliationFS = FormattedString(myAffiliation, font=myAffiliationFont, fontSize=10, lineHeight=12, fill=yellowColor, align="center", tracking=1)
    
    # remove tracking and shrink font size for long affiliations
    if textOverflow(affiliationFS, (0, 0, mw, 12)):
        print('LONG AFFILIATION', affiliationFS)
        affiliationFS = FormattedString(myAffiliation, font=myAffiliationFont, fontSize=9, lineHeight=12, fill=yellowColor, align="center", tracking=0)

    # draw affiliation to canvas
    textBox(affiliationFS, (0, affiliationY, w, 28))




    


## SHEET FUNCTIONS

def drawCropMarks(rows, cols, boxWidth, boxHeight, badgeWidth, badgeHeight, margin):
    # assuming we are in the top right, draw crop marks
    with savedState():
        stroke(0)
        for row in range(rows+1):
            line((-margin, -row*badgeHeight), (-margin/2, -row*badgeHeight))
            line((boxWidth+margin, -row*badgeHeight), (boxWidth+margin/2, -row*badgeHeight))
        for col in range(cols+1):
            line((col*badgeWidth, margin), (col*badgeWidth, margin/2))
            line((col*badgeWidth, -boxHeight-margin/2), (col*badgeWidth, -boxHeight-margin))








# draw sheets of badges
# this is pretty much the same as previous years
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


# process data
def getData(path=""):
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

            # in a few instances, break at hyphen
            if myName == 'Doris Palmeros-McManus':
                myName = 'Doris Palmeros- McManus'
            if myName == 'Miroslava Polyakova-Grigorieva':
                myName = 'Miroslava Polyakova- Grigorieva'
            if myName == 'Naia Lee-Hendricks':
                myName = 'Naia Lee- Hendricks'
            if myName == 'Andrea Trabucco-Campos':
                myName = 'Andrea Trabucco- Campos'
            if myName == 'Tobias Frere-Jones':
                myName = 'Tobias Frere- Jones'
            #myName = myName.replace('-', '−')

    
            # make uppercase    
            myName = myName.upper()
            
            # replace MC with Mc
            myName = myName.replace(' MC', " Mc")
    
    
    
            myAffiliation = str(myLine[2])

            if myAffiliation.lower() in ['n/a', 'na', 'student', 'unemployed', 'usa', 'freelance', 'none', 'self-employed', ] or myAffiliation == myName:
                myAffiliation = ''

            #go = False
            #for char in myName:
            #    if ord(char) > 128:
            #        go = True
            #if not go:
            #    continue
                
            myData.append((myName, myAffiliation))
        
            myTick += 1
            #if myTick > 100:
            #    break
    return myData
        

if __name__ == "__main__":

    data = getData('../csvs/Badges - 6 23 10 am.csv')
    
    #if DEBUG:
    #    data = data[:10]


    makeSheetsPDF = True
    makeIndividualsPDF = True
        


    if makeSheetsPDF:
        drawSheets(data, 4*pt, 3*pt)
        saveImage('~/desktop/sheets.pdf')

        if makeIndividualsPDF:
            newDrawing()

    if makeIndividualsPDF:
        for i,row in enumerate(data):
           drawSafeBadge(row[0], row[1], True)
        saveImage('~/desktop/individuals.pdf')