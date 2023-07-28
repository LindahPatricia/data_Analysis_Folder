
import mysql.connector
import threading
import multiprocessing
import time

# context manager
# A context manager for opening and closing a file


class FileManger(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


# with FileManger('linda.txt', 'r') as opened_file:
  #  print(opened_file.read())

print()
exit

print("# A context manager for managing a database connection.")


class DatabaseConnection:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def __enter__(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )
        return self.connection

    def __exit__(self, exc_type,  exc_value, exc_traceback):
        if self.connection:
            self.connection.close()

        if exc_type is not None:
            # Handle any exceptions raised within the `with` block
            print(f"An error occurred: {exc_value}")

        # Return False to re-raise any exceptions occurred within the `with` block
        return False


    # Establishing a database connection using the context manager
with DatabaseConnection('localhost', "school", "root", "") as connection:
    if connection.is_connected():
        # Perform database operations
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM fees')
        for row in cursor:
            print(row)

print()

# s how a multithreading and multiprocessing  that allows us to run the function for different amounts of time.
# multiple threads and multiple processes

# example of thread
# Create function


def print_numbers():
    for i in range(1, 6):
        print(f"Thread 1: {i}")


def print_letters():
    for letter in ["a", "b", "c"]:
        print(f"Thread 2: {letter}")


thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("----thread function)")


def sleep(sleep_sec=0.5):
    print(f'Thread Sleeping for {sleep_sec} seconds')
    time.sleep(sleep_sec)
    print('Thread Finished sleeping')


if __name__ == "__main__":
    start_time = time.perf_counter()
    threads = []

    # Create 5 threads and start them
    for i in range(5):
        t = threading.Thread(target=sleep, args=(1.0,))
        t.start()
        threads.append(t)

    # Join all the threads
    for t in threads:
        t.join()

    finish_time = time.perf_counter()

    print(f"Program finished in {finish_time - start_time:.3f} seconds")

print()

print("----process function)")
# processes


def sleep(sleep_sec=0.5):
    print(f'process Sleeping for {sleep_sec} seconds')
    time.sleep(sleep_sec)
    print('process Finished sleeping')


if __name__ == "__main__":
    start_time = time.perf_counter()
    processes = []

    # Creates 5 processes then starts them
    for i in range(5):
        p = multiprocessing.Process(target=sleep, args=(1.0,))
        p.start()
        processes.append(p)

    # Joins all the processes
    for p in processes:
        p.join()

    finish_time = time.perf_counter()

    print(f"Program finished in {finish_time - start_time:.3f} seconds")
