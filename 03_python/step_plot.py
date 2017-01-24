# Import Stuff
import matplotlib.pyplot as plt

# Define Variables:
inputList = []
outputList = []

# Heaviside step function
# ------------------------------------------------------------------------
def heaviside(x):
   """Heaviside step function"""
   theta = None
   if x < 0:
       theta = 0.
   elif x == 0:
       theta = 0.5
   else:
       theta = 1.

   return theta
# ------------------------------------------------------------------------


# Generate Input List
# ------------------------------------------------------------------------
def GenerateInput():
   inputList = [-3, -2, -1, 0, 1, 2, 3]
   return inputList
# ------------------------------------------------------------------------

inputList = GenerateInput()

for x in range(len(inputList)):
   outputList.append(heaviside(inputList[x]))
   
for n in range(len(inputList)):
   print("X Values: " + str(inputList[n]) + "        Theta(X) Values: " + str(outputList[n]))

# Plot it

plt.plot(inputList, outputList, '-o', color="green", linewidth=2)
plt.show()

# x = 3
# theta = heaviside(x) 
# print("Theta(" + str(x) + ") = " + str(theta))



