class Solution:
   def count1s(self, n):
       counter = 0
       while n>0:
           counter += n%2
           n //=2
       return counter


   def readBinaryWatch(self, turnedOn):
       output = []

       for hour in range(12):
           for minute in range(60):
               #print("Checking " + str(hour) + ":" + str(minute))
               # contabiliza a quantidade de LEDS para cada hora e minuto
               leds = self.count1s(hour) + self.count1s(minute)
               if leds==turnedOn:
                   if minute<10: # tratar os minutos antes de 10
                       output.append( str(hour)+":0"+ str(minute) )
                   else:
                       output.append( str(hour)+":"+ str(minute) )

       return output

solution = Solution()
solutions = solution.readBinaryWatch(8)
for solution in solutions:
  print(solution)