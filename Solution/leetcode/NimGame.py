class NimGame(object):
    def canWinNim(self, n):
        """
        Problem state : You are playing the following Nim Game with your friend: There is a heap of stones on the table, 
                        each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. 
                        You will take the first turn to remove the stones.
                        Write a function to determine whether you can win the game given the number of stones in the heap.
                        For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, 
                        the last stone will always be removed by your friend.
        type n: int
        return type: bool
        Idea : <CORE>Value multiple by 4 return False, others return true
               <Explan>We already have sufficient hints in problem state and the example as below describe
               (1) We have ONE heap of stones
               (2) Both of players take turns to remove 1 to 3 stones.
               (3) You will take the first turn to remove the stones. The one who removes the last stone will be the winner.
               (4) If there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove,
               
               By (4) described, if one of the players meet the number of stones remained is 4 or a value multiple by 4 when take turns than the player WILL be the loser
               Because the opposite can take remain stone(s) no matter how many the player takes, or take stones which will keep the count that multiple by 4
               
        """
        if n%4 == 0:
            return False
        else:
            return True