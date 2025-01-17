class Solution:
    def canMeasureWater(self, jug1: int, jug2: int, t: int) -> bool:
        j1=0
        j2=0

        q=[]
        q.append((j1,j2))

        vis=set()


        while(len(q))>0:

            rem=q.pop(0)

            j1=rem[0]
            j2=rem[1]

            if j1==t or j2==t or j1+j2==t:
                return True



            if (j1,j2) in vis:
                continue

            vis.add((j1,j2))

            q.append((jug1,j2))
            q.append((j1,jug2))
            q.append((0,j2))
            q.append((j1,0))
            q.append((jug1,jug2))
            x=0
            if jug1<jug2:
                x=jug1-j1
                if j2-x>=0:
                    q.append((j1+x,j2-x))

                if j2<=jug1:
                    q.append((j2,0))

                if j2-jug1>=0:
                    q.append((jug1,j2-jug1))


            else:
                x=jug2-j2
                if j1-x>=0:
                    q.append((j1-x,j2+x))
                if j1<=jug2:
                    q.append((0,j1))

                if j1-jug2>=0:
                    q.append((j1-jug2,jug2))

        return False
