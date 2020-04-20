from files.tasks import main
from files.conditions import condition

if __name__ == '__main__':
    while True:
        try:
            # user picks the task
            i = input('\nPick the task : ')

            # task's condition prints
            condition(i)

            # certain task calls
            main(func=i)()
            #print(f'Task number {i}')
        #except (ValueError, IndexError):
        except (ValueError):
            print("Pick the task, again")
        except EOFError:

            # use CTRL+D to escape from script
            print("Goodbye")
            exit()