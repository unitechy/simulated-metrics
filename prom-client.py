import random
import time
from prometheus_client import start_http_server, Gauge

# Define a list of metric names
metric_names = ['cpu_utilization', 'memory_usage', 'network_traffic']

# Define Prometheus gauges for each metric
cpu_utilization_gauge = Gauge('cpu_utilization', 'CPU Utilization')
memory_usage_gauge = Gauge('memory_usage', 'Memory Usage')
network_traffic_gauge = Gauge('network_traffic', 'Network Traffic')

# Define a function to generate random metric values
def generate_metrics():
    metrics = {}
    for name in metric_names:
        # Generate a random value between 0 and 100
        value = random.randint(0, 100)
        # Add the metric name and value to the dictionary
        metrics[name] = value
    return metrics

# Start the Prometheus HTTP server
start_http_server(8000)

# Define a loop to generate metrics every 10 seconds
while True:
    metrics = generate_metrics()
    # Set the Prometheus gauges to the generated metric values
    cpu_utilization_gauge.set(metrics['cpu_utilization'])
    memory_usage_gauge.set(metrics['memory_usage'])
    network_traffic_gauge.set(metrics['network_traffic'])
    # Wait for 10 seconds before generating the next set of metrics
    time.sleep(10)
