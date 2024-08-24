import logging
import time
import random
import json
import sys

DEFAULT_LOG_FILE = 'application.log'
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

def setup_logging(log_file):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_file)
    stdout_handler = logging.StreamHandler(sys.stdout)

    formatter = logging.Formatter(LOG_FORMAT)
    file_handler.setFormatter(formatter)
    stdout_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)

def load_config(config_file):
    with open(config_file, 'r') as f:
        return json.load(f)

def generate_log(log_messages):
    log_level = random.choice(list(log_messages.keys()))
    message = random.choice(log_messages.get(log_level))
    logging.log(int(log_level), message)

def main():
    setup_logging(DEFAULT_LOG_FILE)
    log_messages = load_config('config.json')
    
    print(f"Logging to {DEFAULT_LOG_FILE} and stdout with intervals between 1 and 5 seconds.")

    while True:
        try:
            generate_log(log_messages)
            time.sleep(random.uniform(0.2, 1))  # Generate logs at random intervals
        except KeyboardInterrupt:
            print('Interrupted by user.')
            break

if __name__ == "__main__":
    main()
