#!/usr/bin/env python
# coding: utf-8

# Calculate metrics for a Roam graph

import csv

from roam_data.roam.graph import Graph
from collections import defaultdict

# TODO: add tests


def get_metrics_for(graph_file_name: str, csv_file_name: str):
    graph= Graph.from_file(graph_file_name)
    daily_posts = defaultdict(list)
    for page in graph.pages:
        try:
            d = page.create_time.date()
        except Exception as e:
            print('page: ', page.title)
            raise e
        daily_posts[d].append(page)
    with open(csv_file_name,'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['date','posts','entries'])
        for d in sorted(daily_posts.keys()):
            count = sum(len(page.children) for page in daily_posts[d])
            writer.writerow((d, len(daily_posts[d]), count))











