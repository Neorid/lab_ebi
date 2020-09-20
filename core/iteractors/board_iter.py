from services.boundaries.board_bound import BoardBound
from services.request.board_find import BoardFind
from services.request.boards_create import BoardCreate
from services.responses.board_find_res import BoardFindRes
from services.responses.board_res import BoardRes


class BoardIter(BoardBound):


    def create(self, request: BoardCreate) -> BoardRes:

        pass

    def find(self, request: BoardFind) -> BoardFindRes:
        pass