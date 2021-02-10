from random import random, shuffle

def checkGrid(grid, where=False):
    for i in range(3):
        if abs(sum(grid[i])) == 3:
            player = sum(grid[i])//3 
            return player 
    for j in range(3):
        if abs(sum([ grid[i][j] for i in range(3)])) == 3:
            player = sum([ grid[i][j] for i in range(3)])//3
            return player
    if abs(sum([grid[i][i] for i in range(3)])) == 3:
        player = sum([grid[i][i] for i in range(3)])//3
        return player
    if abs(sum([grid[2-i][i] for i in range(3)])) == 3:
        player = sum([grid[2-i][i] for i in range(3)])//3
        return player
    return 0

def minimax(grid, empty_cells, cell, player):
    i, j = cell[0], cell[1]
    grid[i][j] = player

    if len(empty_cells) == 1:
        ev = checkGrid(grid)
        grid[i][j] = 0
        return ev

    if checkGrid(grid) == player:
        grid[i][j] = 0
        return player
    
    k = empty_cells.index(cell)
    empty_cells_tmp = [
        cell for l, cell in enumerate(empty_cells) if l != k
    ]
    l = len(empty_cells_tmp)
    minmax = [
        minimax(grid, empty_cells_tmp, empty_cells_tmp[i], -player) for i in range(l) 
        ]
    grid[i][j] = 0
    return min(minmax) if player == 1 else max(minmax)
    

def best_move(grid, empty_cells, player):
    evals = [minimax(grid, empty_cells, cell, player) for cell in empty_cells]
    if player == 1:
        return empty_cells[evals.index(max(evals))] 
    else:
        return empty_cells[evals.index(min(evals))] 




#####################################
# Partie correspondant au jeu H vs PC
#####################################
def computer_play(grid):
    empty_cells = get_empty_cells(grid)
    winner = checkGrid(grid)
    if (len(empty_cells) == 0 or winner != 0):
        return {
        'row': None, 
        'col': None,
        'winner': winner,
        'where': where(grid)
        }
    else:
        row, col = best_move(grid, empty_cells, -1)
        grid[row][col] = -1
        return {
        'row': row, 
        'col': col,
        'winner': checkGrid(grid),
        'where': where(grid)
        }

def computer_play_easy(grid):
    empty_cells = get_empty_cells(grid)
    winner = checkGrid(grid)
    if (len(empty_cells) == 0 or winner != 0):
        return {
        'row': None, 
        'col': None,
        'winner': winner,
        'where': where(grid)
        }
    else:
        shuffle(empty_cells)
        row, col = empty_cells[0] 
        grid[row][col] = -1
        return {
        'row': row, 
        'col': col,
        'winner': checkGrid(grid),
        'where': where(grid)
        }

def computer_play_medium(grid):
    alea = random()
    return computer_play(grid) if alea > 0.5 else computer_play_easy(grid)

def get_empty_cells(grid):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                empty_cells.append((i, j))
    return empty_cells

def where(grid):
    where = ''
    for i in range(3):
        if abs(sum(grid[i])) == 3:
            where += 'h' + str(i) 
    for j in range(3):
        if abs(sum([ grid[i][j] for i in range(3)])) == 3:
            where += 'v' + str(j) if where == '' else ',v' +str(j)
    if abs(sum([grid[i][i] for i in range(3)])) == 3:
        where += 'd' if where == '' else ',d'
    if abs(sum([grid[2-i][i] for i in range(3)])) == 3:
        where += 'D'if where == '' else ',D'
    return where

#######################################################################################################################
# Ce qui suit n'est pas encore utilisé. Cela pourra servir à optimiser les calculs mais c'est juste histoire de dire...
#######################################################################################################################

def get_symetries(grid):
    symetries = ''
    #On teste l'axe vertical
    is_grid_symetric_along_v = True
    for i in range(3):
        is_grid_symetric_along_v &= grid[i][0] == grid[i][2]
    if is_grid_symetric_along_v:
        symetries += 'v'
    
    # On teste l'axe horizontal
    is_grid_symetric_along_h = True
    for i in range(3):
        is_grid_symetric_along_h &= grid[0][i] == grid[2][i]
    if is_grid_symetric_along_h:
        symetries += 'h'

    # On teste la première diagonale
    is_grid_symetric_along_d = True
    for i in range(3):
        for j in range(i+1, 3):
            is_grid_symetric_along_d &= grid[i][j] == grid[j][i]
    if is_grid_symetric_along_d:
        symetries += 'd'
    
    # On teste la deuxième diagonale 
    is_grid_symetric_along_D = True
    for i in range(3):
        for j in range(i+1, 3):
            is_grid_symetric_along_D &= grid[i][j] == grid[2-j][2-i]
    if is_grid_symetric_along_D:
        symetries += 'D'

    return symetries