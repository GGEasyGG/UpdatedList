from typing import Union, List, Tuple


class UpdatedList(list):
    def __init__(self, arg: Union[List[Union[int, float]], Tuple[Union[int, float], ...]]) -> None:
        if not isinstance(arg, (list, tuple)):
            raise TypeError('"UpdatedList" can be created only based on a list or a tuple')
        else:
            if all(isinstance(elem, (int, float)) for elem in arg):
                super().__init__(arg)
            else:
                raise TypeError('"UpdatedList" elements must be of type int or float')

    def __add__(self, other: 'UpdatedList') -> 'UpdatedList':  # type: ignore
        if not isinstance(other, UpdatedList):
            raise TypeError('Only the "UpdatedList" can be added to the "UpdatedList"')

        if len(self) < len(other):
            new_list = [elem for elem in self]
            new_list.extend([0] * (len(other) - len(self)))
            result = UpdatedList([new_list[i] + other[i] for i in range(len(other))])
        elif len(self) > len(other):
            new_list = [elem for elem in other]
            new_list.extend([0] * (len(self) - len(other)))
            result = UpdatedList([new_list[i] + self[i] for i in range(len(self))])
        else:
            result = UpdatedList([other[i] + self[i] for i in range(len(self))])

        return result

    def __sub__(self, other: 'UpdatedList') -> 'UpdatedList':
        if not isinstance(other, UpdatedList):
            raise TypeError('Only the "UpdatedList" can be subtracted')

        if len(self) < len(other):
            new_list = [elem for elem in self]
            new_list.extend([0] * (len(other) - len(self)))
            result = UpdatedList([new_list[i] - other[i] for i in range(len(other))])
        elif len(self) > len(other):
            new_list = [elem for elem in other]
            new_list.extend([0] * (len(self) - len(other)))
            result = UpdatedList([self[i] - new_list[i] for i in range(len(self))])
        else:
            result = UpdatedList([self[i] - other[i] for i in range(len(self))])

        return result

    def __eq__(self, other: 'UpdatedList') -> bool:  # type: ignore
        if not isinstance(other, UpdatedList):
            raise TypeError('Only the "UpdatedList" can be compared')

        if sum(self) != sum(other):
            return False
        else:
            return True

    def __le__(self, other: 'UpdatedList') -> bool:  # type: ignore
        if not isinstance(other, UpdatedList):
            raise TypeError('Only the "UpdatedList" can be compared')

        if sum(self) <= sum(other):
            return True
        else:
            return False

    def __lt__(self, other: 'UpdatedList') -> bool:  # type: ignore
        if not isinstance(other, UpdatedList):
            raise TypeError('Only the "UpdatedList" can be compared')

        if sum(self) < sum(other):
            return True
        else:
            return False
