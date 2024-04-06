class IntegerContainerImpl():

    def __init__(self):
        # TODO: implement
        # Initialize an attribute 'container' to an empty list
        self.container = []

    # TODO: implement interface methods here
    def add(self, value: int) -> int:
        self.container.append(value)
        print(self.container)
        return len(self.container)
    
    def delete(self, value: int) -> bool:
        if value in self.container:
            self.container.remove(value)
            return True
        return False
    
    def get_median(self) -> int:
        self.container.sort()
        index = len(self.container)
        mid = index // 2
        if index == 0:
            return None
        elif index % 2 == 0:
            return self.container[mid-1]
        else:
            return self.container[mid]
    
container = IntegerContainerImpl()
print('Adding Numbers...')
print(f'Adding 5: {container.add(5)}')
print(f'Adding 10: {container.add(10)}')
print(f'Adding 5: {container.add(4)}')
print(f'Adding 5: {container.add(9)}')
print(f'Adding 5: {container.add(7)}')


print('\nDeleting Numbers...')
# print(f'Deleting 5: {container.delete(5)}')
# print(f'Deleting 1: {container.delete(1)}')

print(f'\nContainer: {container.container}')
container.get_median()
print(f'\nSorted Container: {container.container}')

# 
print('\nGetting median...')
print(f'Median: {container.get_median()}')