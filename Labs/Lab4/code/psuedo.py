def minimax(node, alpha, beta, depth, player):
    if(depth == MAX_DEPTH or gameWon() == True):
        return estimateE(node.gameState) #Calculates E(x) for the game state represented by the current node

    if(player == 1):
        best = -1
        for n in nodes.children:
            evalFuture = minimax(node, alpha, beta, depth - 1, 2)
            alpha = max(evalFuture, alpha)
            best = max(evalFuture, best)
            if(alpha >= beta):
                break
        return best
    else:
        worst = 1
        for n in nodes.children:
            evalFuture = minimax(node, alpha, beta, depth - 1, 2)
            beta = min(evalFuture, beta)
            worst = max(evalFuture, worst)
            if(alpha >= beta):
                break
        return worst
