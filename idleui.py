

from collections import defaultdict
from copy import deepcopy
from poketcg import PokeData


def welcome() -> None:
    '''Displays text when the program starts'''
    print('Program has started.\n')



def show_current_query(query: {str: [str]}) -> None:
    '''Displays the user's current search query'''
    print('\nCurrent search query:', '\n None' if len(query) == 0 else '')
    for name, items in sorted(query.items()):
        print(f'{name}: ' + ', '.join(sorted(items)))
    print()



def prompt_user(history: [PokeData]) -> PokeData:
    '''
    Prompts and takes user input to build a search query to send to the
    Pokemon TCG API.
    '''
    query = defaultdict(set)
    while True:
        command = input(
            'Enter a command:\n' +
            '[a]dd {type} {name}\n' +
            '[d]el {name}\n' +
            '[p]rev\n' +
            '[s]ubmit\n' +
            '[q]uit\n\n>>> '
            )

        c_type, *p = command.rstrip().split(' ')

        try:
            if c_type == 'q' or c_type == 'quit':
                return None
            elif c_type == 's' or c_type == 'submit':
                return PokeData(query)
            elif c_type == 'p' or c_type == 'prev':
                query = deepcopy(history[-1].query())
            elif c_type == 'a' or c_type == 'add':
                query[p[0]].add(p[1])
            elif c_type == 'd' or c_type == 'del':
                if p[0] in query:
                    del query[p[0]]
                else:
                    for name, items in query.items():
                        if p[0] in items:
                            items.remove(p[0])
                            if len(items) == 0:
                                del query[name]
        except IndexError:
            print('Invalid command.')
            del query[p[0]]
                
        show_current_query(query)



def process(data: PokeData) -> None:
    '''Displays the retrieved data from the Pokemon TCG API'''
    results = data.result()
    if results != None:
        print(results)
    print()



def goodbye() -> None:
    '''Displays text when the program ends'''
    print('\nProgram has stopped running.')


    
def run() -> None:
    history = []
    welcome()
    while (data := prompt_user(history)):
        process(data)
        history.append(data)
    goodbye()
    


if __name__ == '__main__':
    run()
