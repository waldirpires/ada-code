class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        edges=[jug1Capacity,jug2Capacity,abs(jug2Capacity-jug1Capacity)]
        lst=[0]
        mx=max(jug1Capacity,jug2Capacity,targetCapacity)
        visited=[0]*1000001
        if targetCapacity>(jug1Capacity+jug2Capacity):
            return False
        visited[0]=1
        while lst:
            x=lst.pop(0)
            if x==targetCapacity:
                return True
            for i in edges:
                if x+i<=mx and visited[x+i]==0:
                    lst.append(x+i)
                    visited[x+i]=1
                if x-i>=0 and visited[x-i]==0:
                    lst.append(x-i)
                    visited[x-i]=1
        return False

