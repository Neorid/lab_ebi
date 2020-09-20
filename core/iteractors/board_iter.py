from core.entities.boards import Phone
from services.boundaries.board_bound import BoardBound
from services.request.board_find import BoardFind
from services.request.boards_create import BoardCreate
from services.responses.board_find_res import BoardFindRes
from services.responses.board_res import BoardRes


class BoardIter(BoardBound):
    base = {}
    count = 0

    def create(self, request: BoardCreate) -> BoardRes:
        phone = Phone(name=request.name,
                      price=request.price,
                      quantity=request.quantity,
                      years=request.years,
                      id=self.count)
        self.base[self.count] = phone
        self.count += 1
        return BoardCreate(phone.id)

    def find(self, request: BoardFind) -> BoardFind:
        id = request.id
        phone = self.base.get(id, None)
        if phone:
            return BoardFind(id=phone.id,
                             name=phone.name,
                             price=phone.price,
                             quantity=phone.quantity,
                             years=phone.years)
        raise Exception('Phone error')