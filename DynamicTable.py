class DynamicTable:

    def __init__(self):
        self.values = []
        self.trace = []
        self.score = None

    def initTable(self, seq1, seq2):
        for i in range(len(seq2) + 1):
            newRow = [0] * (len(seq1) + 1)
            newTraceRow = [''] * (len(seq1) + 1)
            self.trace.append(newTraceRow)
            self.values.append(newRow)

        self.x = (len(seq1) + 1)
        self.y = (len(seq2) + 1)
        self.one = seq1
        self.two = seq2
        self.fillTable()

    def fillTable(self):
        for i in range(1, self.x):
            self.values[0][i] = i * 5
            self.trace[0][i] = self.one[i-1]

        for i in range(1, self.y):
            self.values[i][0] = i * 5
            self.trace[i][0] = self.two[i-1]

        for i in range(1, self.y):
            for j in range(1, self.x):
            
                top = self.values[i-1][j]
                left = self.values[i][j-1]
                dia = self.values[i-1][j-1]

                leftValue = left + 5
                topValue = top + 5
                diagonalValue = dia + 1

                if self.two[i-1] == self.one[j-1]:
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

    def getScore(self):
        return self.values[self.y - 1][self.x - 1]

    def getTraces(self):
        
        current = self.trace[self.y - 1][self.x - 1]
        currentTop = self.y - 1
        currentLeft = self.x - 1
        goAgain = True

        string1 = ''
        string2 = ''

        return ''

        # while goAgain:


        
