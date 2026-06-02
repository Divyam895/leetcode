class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m=len(board)
        n=len(board[0])
        ls=[[0 for _ in range(n)] for _ in range(m)] 
        for i in range(0,m):
            for j in range(0,n):
                c=0
                if (i-1)>=0:
                    if board[i-1][j]==1:
                        c+=1
                    if (j-1)>=0:
                        if board[i-1][j-1]==1:
                            c+=1
                    if (j+1)<n:
                        if board[i-1][j+1]==1:
                            c+=1
                if (j-1)>=0:
                    if board[i][j-1]==1:
                        c+=1
                    if (i+1)<m:
                        if board[i+1][j-1]==1:
                            c+=1
                if (j+1)<n:
                    if board[i][j+1]==1:
                        c+=1
                    if (i+1)<m:
                        if board[i+1][j+1]==1:
                            c+=1
                if (i+1)<m:
                    if board[i+1][j]==1:
                        c+=1
                if board[i][j]==1:
                    if c<2:
                        ls[i][j]=0
                    if c==2 or c==3:
                        ls[i][j]=1
                    if c>3:
                        ls[i][j]=0
                if board[i][j]==0:
                    if c==3:
                        ls[i][j]=1
        board[:]=ls
                    