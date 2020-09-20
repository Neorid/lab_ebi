from abc import abstractmethod, ABC

from services.request.board_find import BoardFind
from services.request.boards_create import BoardCreate
from services.responses.board_find_res import BoardFindRes
from services.responses.board_res import BoardRes


class BoardBound(ABC):
    @abstractmethod
    def create(self, request: BoardCreate) -> BoardRes:
        pass

    @abstractmethod
    def find(self, request: BoardFind) -> BoardFindRes:
        pass