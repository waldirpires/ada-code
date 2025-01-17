class Solution:
    def readBinaryWatch(self, turnedOn):
        output = []
        for h in range(12):
            for m in range(60):
                # converte os valores em binário e conta a quantidade de zeros e uns
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    output.append(f"{h}:{m:02d}") # trata a formatação
        return output

solution = Solution()
solutions = solution.readBinaryWatch(8)
for solution in solutions:
  print(solution)

# Initialize an empty list to store the output.
# Loop through all possible combinations of hours and minutes from 0 to 11 and 0 to 59 respectively.
# For each combination, count the number of set bits in the binary representation of hours and minutes by using the count() method of the string representation of the binary number.
# Check if the total number of set bits equals the input parameter turnedOn.
# If it does, format the hours and minutes into a string with the required format of "HH:MM" and append it to the output list.
# Return the output list.