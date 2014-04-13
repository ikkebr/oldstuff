module TrabalhoGrafos where

import List 

type Id = Int

type Weight = Int

type Edge = ( Id, Id )

type Graph = [ ( Edge, Weight ) ]

data Cost = Finite Weight | Infinity
        deriving (Eq, Ord, Show)

type PathCost = (Cost, Id)

e1 :: Graph
e1 = [ 
 ( ( 0, 1 ), 1 ),
 ( ( 0, 2 ), 3 ),
 ( ( 0, 4 ), 6 ),
 ( ( 1, 2 ), 1 ),
 ( ( 1, 3 ), 3 ),
 ( ( 2, 0 ), 1 ),
 ( ( 2, 1 ), 2 ),
 ( ( 2, 3 ), 1 ),
 ( ( 3, 0 ), 3 ),
 ( ( 3, 4 ), 2 ),
 ( ( 4, 3 ), 1 ),
 ( ( 5, 2 ), 9 ) ]     

e2 :: Graph
e2 = [ ( ( 0, 1 ), 1 ),
       ( ( 1, 2 ), 4 ) ]

e3 :: Graph
e3 = [ ( ( 0, 1 ), 1 ),
       ( ( 0, 2 ), 3 ),
       ( ( 1, 0 ), 2 ),
       ( ( 3, 0 ), 4 ),
       ( ( 3, 1 ), 6 ),
       ( ( 3, 2 ), 5 ) ]	
-----------------------------------------------------------------

-- retorna o total de edges em um grafo
edges :: Graph -> Int
edges a = length a

-- retorna a soma de todos os vertices do grafo
weightTotal :: Graph -> Weight
weightTotal a = sum [ c | ((a,b),c) <- a ]

-- retorna todos os nodos de um grafo
nodes :: Graph -> [ Id ]
nodes a = nub ( sort ( [ a  | ((a,b),c) <-a ] ++ [ b | ((a,b),c) <- a] ) )

-- adiciona dois custos
addCosts :: Cost -> Cost -> Cost
addCosts (Finite a) (Finite b) = Finite (a+b)
addCosts Infinity a = Infinity
addCosts a Infinity = Infinity

-- procura o custo de um caminho no grafo
lookUp :: Edge -> Graph -> Cost
lookUp (a,b) c = head ([Finite f | ((d,e),f) <-c, d==a, e==b]++[ Infinity ])


-- menor caminho usando djikstra, recebe um grafo e retorna o menor custo ateh 0
allPaths :: Graph -> [ PathCost ]
allPaths a  = fa a [] []

{- função auxiliar, ou Faz Acontecer
recebe um grafo, lista dos menores custos jah encontrados,
lista dos menors custos que ainda falta apurar e retorna
magicamente o valor esperado
-}
fa :: Graph -> [ PathCost ] -> [ PathCost ] ->  [ PathCost ]
fa a [] [] = fa a ( [head (inicia a)] ) (tail (inicia a))
fa a b [] = sort b
{-
bom, se a lista dos menores custos jah encontradores existir
e se existirem caminhos a serem calculados entao faz uma chamada
recursiva pegando o elemento mais recentemente adicionado a lista
de menores custos jah encontrados e recalcula o custos de (todos)
que continuam na lista dos nao encontrados. se o custo que estiver
nessa lista for menor do que a soma do custo do elemento mais 
recentemente adicionado na lista dos jah encontrados ao custo para
percorrer entre ele e o elemento da lista dos nao encontrados entao
ele eh removido da lista e no lugar entra o custo vindo dessa soma.
ao final do processo o elemento que tiver o menor valor eh promovido
para a lista dos jah encontrados e todos os que continuam na outra
lista sao recalculados, agora tendo como base esse ultimo valor.
funciona? funciona.
-}
fa a ((b,t):x) c = fa a ( [head ((sort(([( minimum [k, addCosts (lookUp (t,m) a) b] , m) |(k,m)<- c]))))]++x++[(b,t)]) (tail( sort( [ (minimum( [k, addCosts (lookUp(t,m)a) b] ),m) | (k,m) <- c ])))

-- inicia buscando os caminhos diretos entre 0 e i
inicia :: Graph -> [ PathCost ]
inicia a  = sort [(lookUp (0,k) a, k) | k <- (nodes a)]


-- usando Floyd-Warshall
allPaths2 :: Graph -> [ PathCost ]
allPaths2 a = fwallPaths a (nodes a)

menorCaminho :: Edge -> Graph -> [Id] -> Cost
menorCaminho (a,b) c [] = lookUp (a,b) c
{-
esse eh mais facil de explicar
o menor caminho entre a b ou eh a-b direto ou
um caminho que vai de a-k e outro que vai de k-b
-}
menorCaminho (a,b) c (k:j) = minimum [ (menorCaminho (a,b) c j), addCosts  (menorCaminho (a,k) c j) (menorCaminho (k,b) c j) ]

fwallPaths :: Graph -> [Id] -> [ PathCost ]
fwallPaths c [] = []
fwallPaths c (k:j) = [ (menorCaminho (0,k) c (tail (nodes c)), k) ]++ fwallPaths c j

