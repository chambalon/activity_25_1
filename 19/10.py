def exist(board,word):
  rows, cols = len(board), len(board[0])
  
  def backtrack(r,c,index):
    if index == len(word):
      return True

    if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]):
      return False
    
    temp, board[r][c] = board[r][c], '#'
    if (backtrack(r+1,c,index+1) or backtrack(r-1,c,index+1) or backtrack(r,c+1,index+1) or backtrack(r,c-1,index+1)):
      return True

    board[r][c] = temp

    return False

  for r in range(rows):
    for c in range(cols):
      if backtrack(r,c,0):
        return True
  return False



board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]

word1 = exist(board,"ABCCED")
word2 = exist(board,"ABCB")
word3 = exist(board,"SEE")

print(word1)
print(word2)
print(word3)