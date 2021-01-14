import base64, ast
import pandas as pd

def decode_game_state(state):
    decoded = base64.b64decode(state)
    dict_string = decoded.decode("UTF-8")
    data = ast.literal_eval(dict_string)
    df = pd.DataFrame(data)
    grid = pd.DataFrame(df['gridObj'])
    grid = grid.drop(grid.index[0])
    grid.reset_index(inplace=True)

    mine_coordinates = []
    for i in grid['gridObj']:
        del i[0]    

    for i, j in enumerate(grid['gridObj']):
        for k, m in enumerate(j):
            if m < 0:
                mine_coordinates.append((i+1, k+1))
    return mine_coordinates