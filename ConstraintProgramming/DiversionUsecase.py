from ortools.sat.python import cp_model

# Define the model
model = cp_model.CpModel()
graph = [{
    "runwayName" : "Toulouse Runway A",
    "runwayDistance" :5500
},
    {
        "runwayName": "Toulouse Runway B",
        "runwayDistance": 4500
    }
,
    {
        "runwayName": "Toulouse Runway C",
        "runwayDistance": 6500
    },
    {
        "runwayName": "Paris Runway A",
        "runwayDistance": 5200
    },
    {
        "runwayName": "Paris Runway B",
        "runwayDistance": 4200
    }
]

# Input Data
array = [5500, 4500, 6500, 5200, 4200]


# decision variables
x = [model.NewIntVar(0, 1, f'x{i}') for i in range(len(array))]

#Constraints
for i in range(len(array)):
    lit = model.NewBoolVar('')
    model.Add(lit == (array[i] > 5000))
    model.Add(x[i] == 1).OnlyEnforceIf(lit)
    model.Add(x[i] == 0).OnlyEnforceIf(lit.Not())


solver = cp_model.CpSolver()
status = solver.Solve(model)

#Solution
if status == cp_model.OPTIMAL:
    selected = [array[i] for i in range(len(array)) if solver.Value(x[i]) == 1]
    print(f"The selected numbers are: {selected}")
    for i in selected:
        for j in graph:
            if i == j["runwayDistance"]:
                print(f"Available runways - {j}")
else:
    print("No solution found.")
