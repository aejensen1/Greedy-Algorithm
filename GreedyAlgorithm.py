# Title: Greedy Algorithm
# Description: This program demonstrates the greedy algorithm in graph theory using python
# Author: Anders Jensen
# Version: 12-11-2024

# create weighted graph using adjacency matrix (European flight schedule problem)
# use 6 rows and 6 columns to represent 6 cities
# index 0 represents London
# index 1 represents Berlin
# index 2 represents Paris
# index 3 represents Rome
# index 4 represents Madrid
# index 5 represents Vienna

INF = float('inf') # when there aren't any flights between two cities

cities = ['London', 'Berlin', 'Paris', 'Rome', 'Madrid', 'Vienna']

graph = [
    [0, 325, 160, 280, 250, 425],
    [325, 0, 415, 550, 675, 375],
    [160, 415, 0, 495, 215, 545],
    [280, 550, 495, 0, 380, 480],
    [250, 675, 215, 380, 0, 730],
    [425, 375, 545, 480, 730, 0]
]

# Get the starting city from the user
userInput = input("Enter the starting city: ")
startCity = cities.index(userInput)
print("Starting city: ", cities[startCity])

# Greedy Algorithm function
def greedyAlgorithm(graph, startCity):
    numCities = len(graph)
    visited = [False] * numCities
    visited[startCity] = True
    totalMiles = 0
    currentCity = startCity
    print("Flight route: ")

    for i in range(numCities - 1):
        minDistance = INF
        nextCity = -1
        # Find the nearest unvisited city
        for j in range(numCities):
            if not visited[j] and graph[currentCity][j] < minDistance:
                minDistance = graph[currentCity][j]
                nextCity = j
        # Move to the next city
        visited[nextCity] = True
        totalMiles += minDistance
        print(cities[currentCity], "to", cities[nextCity], "is", minDistance, "miles")
        currentCity = nextCity
    # Return to the starting city
    print(cities[currentCity], "to", cities[startCity], "is", graph[currentCity][startCity], "miles")
    totalMiles += graph[currentCity][startCity]

    print("Total miles: ", totalMiles)

greedyAlgorithm(graph, startCity)
