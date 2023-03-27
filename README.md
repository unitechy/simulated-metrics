# simulated-metrics

#Random.py
This code defines a list of metric names and a function generate_metrics that generates random values for each metric. It then enters an infinite loop that generates metrics every 10 seconds and prints them to the console. You can modify the metric names and the generate_metrics function to generate different types of metrics.

To publish the generated metrics to Prometheus, you will need to expose an HTTP endpoint that serves the metrics in the Prometheus format. Refer to prom-client.py

This code defines Prometheus gauges for each metric and sets their values to the generated metric values in the generate_metrics function. It then starts a Prometheus HTTP server on port 8000 using the start_http_server function. You can modify the metric names and the generate_metrics function to generate different types of metrics.

Once you have started the Python script, you can visit http://localhost:8000/metrics to see the generated metrics in the Prometheus format. You can then configure Prometheus to scrape this endpoint by adding the following configuration to the prom.yml file. 

The configuration in prom.yml tells Prometheus to scrape the http://localhost:8000/metrics endpoint every 10 seconds and collect the metrics.
