from ortools.sat.python import cp_model


def main():
    # Data
    airportDistanceMatrix = [[10000, 800, 900, 1100, 10000, 10000, 10000, 10000, 10000],
                             [10000, 10000, 10000, 10000, 900, 800, 10000, 10000, 10000],
                             [10000, 10000, 10000, 10000, 10000, 700, 10000, 10000, 10000],
                             [10000, 10000, 10000, 10000, 10000, 10000, 950, 10000, 10000],
                             [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 800],
                             [10000, 10000, 10000, 10000, 10000, 10000, 10000, 850, 1200],
                             [10000, 10000, 10000, 10000, 10000, 10000, 10000, 750, 10000],
                             [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 500],
                             [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]]
    numOfAirports = len(airportDistanceMatrix)

    solver = cp_model.CpModel()

    # Decision Variables
    x = {}
    for i in range(numOfAirports):
        for j in range(numOfAirports):
            x[i, j] = solver.NewBoolVar(f'x[{numOfAirports},{numOfAirports}]')

    # Constraint 1
    for i in range(numOfAirports):
        solver.Add(
            sum([x[i, j] for j in range(numOfAirports)]) - sum([x[j, i] for j in range(numOfAirports)]) == 0)
    # Constraint 2
    solver.Add(sum([x[0, j] for j in range(numOfAirports)]) == 1)
    # Constraint 3
    solver.Add(sum([x[j, 8] for j in range(numOfAirports)]) == 1)

    # Objective function
    objective_terms = []
    for i in range(numOfAirports):
        for j in range(numOfAirports):
            objective_terms.append(airportDistanceMatrix[i][j] * x[i, j])
    solver.Minimize(sum(objective_terms))

    solver1 = cp_model.CpSolver()
    status = solver1.Solve(solver)

    # Print solution.
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f'Total cost = {solver1.ObjectiveValue() - 10000}\n')
        for aiport1 in range(numOfAirports):
            for aiport2 in range(numOfAirports):
                if solver1.BooleanValue(x[aiport1, aiport2]) and aiport1 != 8:
                    print(f'Departure Airport  {aiport1}  Arrival Airport {aiport2}.' +
                          f' total distance travelled = {airportDistanceMatrix[aiport1][aiport2]}')
    else:
        print('No solution found.')


if __name__ == '__main__':
    main()

