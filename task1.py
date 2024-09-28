import queue
import random
import time

request_queue = queue.Queue()

# Лічильник
request_id = 1

def generate_request():
    global request_id
    new_request = f"Request {request_id}"
    request_queue.put(new_request)
    print(f"Generated: {new_request}")
    request_id += 1

def process_request():
    if not request_queue.empty():
        current_request = request_queue.get()
        print(f"Processing: {current_request}")
    else:
        print("Queue is empty, nothing to process.")

# Головний цикл програми
try:
    while True:
        # Випадковий час для генерації заявки імітуючи нерегулярні запити
        if random.random() > 0.3:
            generate_request()

        # Випадковий час для обробки заявки
        if random.random() > 0.5:
            process_request()

        # Випадкова затримка
        time.sleep(random.uniform(0.5, 2))

except KeyboardInterrupt:
    print("Program stopped.")
