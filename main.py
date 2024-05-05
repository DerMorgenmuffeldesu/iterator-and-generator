from asyncio import sleep


class FlatIterator:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.flatten_list = [item for sublist in list_of_lists
                             for item in sublist]
        
    def __iter__(self):
        return self.FlatIteratorIterator(self.flatten_list)

    class FlatIteratorIterator:
        def __init__(self, flatten_list):
            self.flatten_list = flatten_list
            self.index = 0
            
        def __iter__(self):
            return self
    
        def __next__(self):
            if self.index < len(self.flatten_list):
                item = self.flatten_list[self.index]
                self.index += 1
                return item
            else:
                raise StopIteration
        
def test_1():
    
    list_of_lists_1 = [
        ['a', 'b', 'c'], 
        ['d', 'e', 'f', 'h', False], 
        [1, 2, None]
    ]
    
    for flat_iterator_item, check_item in zip(
        FlatIterator(list_of_lists_1),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item
    
    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    
    #for item in FlatIterator(list_of_lists_1):
        #print(item)
    print(', '.join(str(item) for item in FlatIterator(list_of_lists_1)))
    
    
if __name__ == '__main__':
    test_1() 
    
# 2

import types

def flat_generator(list_of_lists):
    for sublist in list_of_lists:
        for item in sublist:
            yield item
    
def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'], 
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    
    #flat_iterator = flat_generator(list_of_lists_1)
    for flat_iterator_item, check_item in zip(
        flat_generator(list_of_lists_1),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item
        
    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    
    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
    
    print(', '.join(str(item) for item in flat_generator(list_of_lists_1)))

    
if __name__ == '__main__':
    test_2()