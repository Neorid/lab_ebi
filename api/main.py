# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import jsonify as jsonify

from core.iteractors.board_iter import BoardIter
from services.request.board_find import BoardFind

boundary = BoardIter()


def print_hi(phone_id):
    try:
        response = boundary.find(BoardFind(phone_id))
        res = {'id': response.id,
               'name': response.name,
               'price': response.price,
               'quantity': response.quantity,
               'years': response.years}
        return jsonify({'phone': res})
    except Exception as e:
        return str(e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')


