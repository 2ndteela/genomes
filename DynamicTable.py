class DynamicTable:

    def __init__(self):
        self.values = []
        self.trace = []
        self.score = None

    def initTable(self, seq1, seq2, banded):
        if not banded:
            for i in range(len(seq2) + 1):
                newRow = [0] * (len(seq1) + 1)
                newTraceRow = [''] * (len(seq1) + 1)
                self.trace.append(newTraceRow)
                self.values.append(newRow)

            self.x = (len(seq1) + 1)
            self.y = (len(seq2) + 1)
            self.top = seq1
            self.left = seq2
            self.fillTable()
        
        else:
            for i in range(len(seq2) + 1):
                newRow = [float('inf')] * 7
                newTraceRow = [''] * 7

                self.values.append(newRow)
                self.trace.append(newTraceRow)

            self.x = (len(seq1) + 1)
            self.y = (len(seq2) + 1)
            self.top = seq1
            self.left = seq2
            self.fillBanded()

    def fillTable(self):
        for i in range(1, self.x):
            self.values[0][i] = i * 5
            self.trace[0][i] = self.top[i-1]

        for i in range(1, self.y):
            self.values[i][0] = i * 5
            self.trace[i][0] = self.left[i-1]

        for i in range(1, self.y):
            for j in range(1, self.x):
            
                top = self.values[i-1][j]
                left = self.values[i][j-1]
                dia = self.values[i-1][j-1]

                leftValue = left + 5
                topValue = top + 5
                diagonalValue = dia + 1

                if self.left[i-1] == self.top[j-1]:
                    diagonalValue = dia - 3
                
                if leftValue <= diagonalValue and leftValue <= topValue:
                    self.values[i][j] = leftValue
                    self.trace[i][j] = 'L'
                
                elif topValue <= diagonalValue and topValue <= leftValue:
                    self.values[i][j] = topValue
                    self.trace[i][j] = 'T'

                else: 
                    self.values[i][j] = diagonalValue
                    self.trace[i][j] = 'D'

    def fillBanded(self):
        for i in range(0, 4):
            self.values[i][0] = i * 5
            self.values[0][i] = i * 5

        xOffset = 0
        xEnd = 4

        for i in range(1, self.y):
            
            xStart = 1 if xOffset == 0 else 0

            for j in range(xStart, xEnd):

                top = self.values[i-1][j]
                left = self.values[i][j-1]
                dia = self.values[i-1][j-1]

                leftValue = left + 5
                topValue = top + 5
                diagonalValue = dia + 1

                xLetterIdx = i + xOffset - 1

                xLetter = self.top[xLetterIdx]
                yLetter = self.left[i-1]
                
                if yLetter == xLetter:
                    diagonalValue = dia - 3

            if  xEnd < 7:
                xEnd = xEnd + 1
            

    def getScore(self):
        return self.values[self.y - 1][self.x - 1]

    def getTraces(self):
        
        current = self.trace[self.y - 1][self.x - 1]
        currentY = self.y - 1
        currentX = self.x - 1
        stringPosX = currentX - 1
        stringPosY = currentY - 1
        goAgain = True

        topString = '' 
        leftString = ''

        while goAgain:
            if current == 'D':
                topString = self.top[stringPosX] + topString 
                leftString = self.left[stringPosY] + leftString
                currentY = currentY - 1
                currentX = currentX - 1
                stringPosX = stringPosX - 1
                stringPosY = stringPosY - 1

            elif current == 'L':
                leftString = '-' + leftString
                topString = self.top[stringPosX] + topString
                currentX = currentX - 1
                stringPosX = stringPosX - 1

            elif current == 'T':
                topString = '-' + topString
                leftString = self.left[stringPosY] + leftString
                currentY = currentY - 1
                stringPosY = stringPosY - 1

            else:
                goAgain = False
            
            current = self.trace[currentY][currentX]

        top = topString[0:100] 
        left = leftString[0:100]

        return(top, left)


        
