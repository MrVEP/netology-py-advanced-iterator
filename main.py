import data


class FlatIteratorFixed:

    def __init__(self, lists: list):
        self.lists = sum(lists, [])

    def __iter__(self):
        self.counter = -1
        return self

    def __next__(self):
        if self.counter == len(self.lists)-1:
            raise StopIteration
        self.counter += 1
        return self.lists[self.counter]


def flat_generator_fixed(lists: list):
    counter = 0
    lists = sum(lists, [])
    while counter < len(lists):
        yield lists[counter]
        counter += 1


class FlatIterator:

    def __init__(self, lists: list):
        self.lists = lists
        self.IsNested = False
        self.nested = None
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.IsNested:
            try:
                return next(self.nested)
            except StopIteration:
                self.IsNested = False

        if self.counter == len(self.lists):
            raise StopIteration

        item = self.lists[self.counter]
        self.counter += 1

        if not isinstance(item, list):
            return item

        if len(item) == 0:
            self.counter += 1

        self.nested = FlatIterator(item)
        self.IsNested = True
        return self.__next__()


def flat_generator(lists: list):
    counter = 0
    while counter < len(lists):
        if isinstance(lists[counter], list):
            for nested_item in flat_generator(lists[counter]):
                yield nested_item
        else:
            yield lists[counter]
        counter += 1


if __name__ == '__main__':
    for i in FlatIteratorFixed(data.my_list):
        print(i)
    print('_'*100)
    flat_list = [item for item in FlatIteratorFixed(data.my_list)]
    print(flat_list)
    print('_' * 100)
    for i in flat_generator_fixed(data.my_list):
        print(i)
    print('_' * 100)
    for i in FlatIterator(data.my_nested_list):
        print(i)
    print('_'*100)
    for i in flat_generator(data.my_nested_list):
        print(i)
