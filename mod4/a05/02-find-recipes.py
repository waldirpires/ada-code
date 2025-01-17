from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        supplies=set(supplies)
        graph=defaultdict(list)
        n=len(recipes)
        #dicionario in_degree
        in_degree=defaultdict(int)
        # criando a lista de adjacencia
        for i in range(n):
            u=recipes[i]
            for v in ingredients[i]:
                graph[v].append(u)
                in_degree[u]+=1
        # criando o deque de suplies
        q=deque([i for i in supplies])
        # enquanto houver elementos na deque
        while q:
            curr_supp=q.popleft()
            # para cada vizinho do no corrente
            for nei in graph[curr_supp]:
                #decrementa o grau de entrada
                in_degree[nei]-=1
                # se ele tiver gra de entrada zero, ele pode entrar na queue
                if in_degree[nei]==0: q.append(nei)
        ans=[]
        # para cada uma das receitas
        for recipe in recipes:
            # se o grau da receita for maior menor ou igual a zero, adicionar
            if in_degree[recipe]<=0: ans.append(recipe)
        return ans