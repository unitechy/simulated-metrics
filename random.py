import random
import time

# Define a list of metric names
metric_names = ['CPU Utilization', 'Memory Usage', 'Network Traffic']

# Define a function to generate random metric values
def generate_metrics():
    metrics = {}
    for name in metric_names:
        # Generate a random value between 0 and 100
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
