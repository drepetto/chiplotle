
def find_file_dimensions(filename):
   '''
   returns [[minX, minY], [maxX, maxY]] found in hpgl file
   '''

   f = open(filename, 'r')

   allData = []

   for line in f:
      allData.append(line.strip())

   papd = []
   
   for block in allData:
      commands = block.rsplit(';')
      for command in commands:
         if command.startswith('PD') or command.startswith('PA'):
            papd.append(command)


   biggestX = -100000.0
   smallestX = 100000.0
   biggestY = -100000.0
   smallestY = 100000.0
   
   for command in papd:
      #have to catch single PD commands
     
      if len(command) > 2:
     
         data = command[2:].rsplit(',')
     
         dataX = float(data[0])
         dataY = float(data[1])
         
         if dataX > biggestX:
            biggestX = dataX
        
         if dataX < smallestX:
            smallestX = dataX
        
         if dataY > biggestY:
            biggestY = dataY
        
         if dataY < smallestY:
            smallestY = dataY
   
   #we didn't find any values!
   if biggestX == -100000.0 or biggestY == -100000.0 or \
      smallestX == 100000.0 or smallestY == 100000.0:
         return None
         
   return [[smallestX, smallestY], [biggestX, biggestY]]


