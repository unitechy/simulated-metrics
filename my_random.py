import random
import time

# Define a list of metric names
metric_names = [
    'CPU Utilization',
    'Memory Usage',
    'Network Traffic',
    'Request Rate',
    'Error Rate',
    'Duration (ms)'
]

# Define a function to generate random metric values
def generate_metrics():
    metrics = {}
    for name in metric_names:
        if name == 'Duration (ms)':
            # Generate a random duration between 1 and 1000 milliseconds
            value = random.randint(1, 1000)
        elif name == 'Request Rate':
            # Generate a random request rate between 0 and 1000 requests per second
            value = random.randint(0, 1000)
        elif name == 'Error Rate':
            # Generate a random error rate between 0 and 10 percent
            value = round(random.uniform(0, 10), 2)
        else:
            # Generate a random value between 0 and 100 for other metrics
            value = random.randint(0, 100)
        # Add the metric name and value to the dictionary
        metrics[name] = value
    return metrics

# Define a loop to generate metrics every 10 seconds
while True:
    metrics = generate_metrics()
    # Print the current timestamp and the generated metrics
    print(f'{time.time()} - {metrics}')
    # Wait for 10 seconds before generating the next set of metrics
    time.sleep(10)
