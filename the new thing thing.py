import csv

individuals = []
groups = []

def importCSVFile(fileName):
  table = []
  with open(fileName, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
      rowEntries = []
      for entry in row:
        rowEntries.append(entry)
      table.append(row)
    return table

def stripTable(table):
  newTable = []
  for i in range(len(table)):
    if i != 0:
      row = []
      for j in range(len(table[i])):
        if j != 0:
          row.append(table[i][j])
      newTable.append(row)
  return newTable

def addIndividuals(strippedTable):
  for row in strippedTable:
    name = row[0]

    classStr = row[1]
    under13 = None
    alone = True
    if row[3] == "Yes":
      alone = False
    if classStr == "First Class":
      pass
    else:
      activity = row[6]
      bathroom = row[5]
    if alone:
      age = row[8]
    else:
      if row[7] == "Yes":
        under13 = True
      elif row[7] == "No":
        under13 = False
      size = row[4]
    if alone:
      individuals.append(Individual(name, age, activity, bathroom, classStr))
    else:
      groups.append(Group(name, under13, size))

def importAllThePeople(fileName):
  addIndividuals(stripTable(importCSVFile(fileName)))

class Individual(object):
  def __init__(self, name, age, activity, bathroom, classStr):
    self.name = name
    self.age = age
    self.activity = activity
    self.bathroom = bathroom
    self.classStr = classStr

class Group(object):
  def __init__(self, name, under13, size):
    self.name = name
    self.under13 = under13
    self.size = size

class Seat(object):
  def __init__(self, rowNum, seatNum, position, classStr):
    self.rowNum = rowNum;
    self.seatNum = seatNum;
    self.position = position;
    self.classStr = classStr;

class Plane(object):
  def __init__(self, model):
    self.rows = []  
    if model == "757-300":
      for i in range(0, 6):
        self.rows.append([])
        for j in range(0, 4):
          self.rows[i].append([])
          position = "aisle";
          if j == 0 or j == 3:
            position = "window";
          self.rows[i][j] = Seat(i, j, position, "first");

      self.rows[6] = [Seat(7, 1, "window", "econ"), Seat(7, 2, "aisle", "econ")];
      self.rows[7] = [Seat(8, 1, "window", "econ"), Seat(8, 2, "middle", "econ"), Seat(8, 3, "aisle", "econ")];
      for i in range(8, 40):
        for j in range(0,6):
          position = "aisle";
          if j == 0 or j == 5:
            position = "window";
          elif j == 1 or j == 4:
            position = "middle";
          self.rows[i][j] = Seat(i, j, position, "econ");


plane = Plane("757-300")
importAllThePeople("Input (Responses) - Form Responses 1.csv")