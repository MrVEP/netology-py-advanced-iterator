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
        yield flat_list[counter]
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
