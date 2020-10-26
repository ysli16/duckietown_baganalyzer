# Bag Analyzer

## Preparation
0. Clone this repository

1. Copy the bags of interest to folder '/data'

2. Go to '/pakages' folder, edit the python script 'analyzer.py', replace `<Bag_Name>` in this line

`bag = rosbag.Bag('/data/<Bag_Name>')`

with actual bag name.

## Exection
### Build image
Run command

`dts devel build -f `

### Run container with mounted volume

Run command

`docker run -it -v <path_to_repo>/data:/data/ duckietown/duckietown_baganalyzer:v2-amd64`

Replace `<path_to_repo>` with the absolute directory to where this repository is stored.
