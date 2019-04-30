import random
from collections import Counter
import os


def createRandomPopulation(populationSize):
  population = []
  for i in range(populationSize):
    newMember = ""
    for j in range(32):
      newMember = newMember + str(random.randint(0, 1))
    population.append(newMember)
  return population


def costFunction(member):
  x = int(member[:16], 2)
  y = int(member[16:], 2)
  return (x**2) - (y**2)


def assessPopulation(population):
  return [[costFunction(member), member] for member in population]


def sumFitness(populationResults):
  sum = 0
  for item in populationResults:
    sum += item[0]
  return sum

def checkConvergence(population):
  # Figure out most frequent in list and get percetage of total
  c = Counter(population)
  rate = c.most_common(1)[0][1] / float(len(population))
  return rate >= .95

def setupGA(populationSize, mutationRate, crossoverRate):
  # create random population
  originalPopulation = createRandomPopulation(populationSize)
  population = originalPopulation

  iterations = 0
  while checkConvergence(population) is not True:
    iterations += 1
    populationResults = assessPopulation(population)
    bestPopulation = [] # get the fittest population
    for i in range(populationSize):
      randIndex1 = random.randint(0,populationSize-1)
      randIndex2 = random.randint(0,populationSize-1)
      if populationResults[randIndex1][0] > populationResults[randIndex2][0]:
        bestPopulation.append(populationResults[randIndex1]) 
      else: 
        bestPopulation.append(populationResults[randIndex2]) 
    
    mutatedPopulation = []
    for i in range(populationSize):
      # random chance based on mutation rate
      if random.random() <= mutationRate:
        member = bestPopulation[i][1]
        randMutationIndex = random.randint(0,31)
        if member[randMutationIndex] == "0":
          member = member[:randMutationIndex] + "1" + member[randMutationIndex + 1:]
        else:
          member = member[:randMutationIndex] + "0" + member[randMutationIndex + 1:]
        mutatedPopulation.append(member)
      else:
        mutatedPopulation.append(bestPopulation[i][1])
    
    # do crossover
    crossoverPopulation = []
    for i in range(populationSize):
      member = str(mutatedPopulation[i])
      if random.random() <= crossoverRate:
        randCrossoverIndex = random.randint(0,31)
        randCrossoverMember = mutatedPopulation[random.randint(0,populationSize-1)]
        crossoverPopulation.append(member[0:randCrossoverIndex] + randCrossoverMember[randCrossoverIndex:])
      else:
        crossoverPopulation.append(member)
    
    population = crossoverPopulation
    
    # if os.name == 'nt':
    #   clear = lambda: os.system('cls')
    #   clear()
    # else:
    #   clear = lambda: os.system('clear')
    #   clear()
    # for item in population:
    #   print(item)
  # print("-----")
  # print("Converged at 95% Successfully.")
  return iterations

    


# min, max, step
populationSize = [20, 500, 20]
mutationRates = [0.001, 0.005, 0.01, 0.05, 0.1]
crossoverRates = [0.6, 0.7, 0.8, 0.9, 1]

testList = []
for population in range(populationSize[0], populationSize[1], populationSize[2]):
  for mutation in mutationRates:
    for crossover in crossoverRates:  
      # population size, mutation rate, crossover rate
      print("Testing:", population, " population size")
      print("Testing:", mutation, " mutation rate")
      print("Testing:", crossover, " crossover rate")
      print("-----")
      testList.append([setupGA(population, mutation, crossover), population, mutation, crossover])

sorted(testList, key=lambda x: x[0])
print("BEST")
print("Iterations, Population, Mutation Rate, Crossover Rate")
print(testList[0])

