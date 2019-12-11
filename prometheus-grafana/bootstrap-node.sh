#!/usr/bin/env bash
sudo apt-get update

# create downloads directory so that we can download all the packages
# which are required during provisioning process
mkdir /home/vagrant/Downloads
cd /home/vagrant/Downloads

exp_vers="0.18.1"
# create directory for node_exporter which can be used to send ubuntu metrics to the prometheus server
mkdir -p /home/vagrant/Prometheus/node_exporter
cd /home/vagrant/Prometheus/node_exporter

# download node_exporter
wget https://github.com/prometheus/node_exporter/releases/download/v$exp_vers/node_exporter-$exp_vers.linux-amd64.tar.gz -O /home/vagrant/Downloads/node_exporter-$exp_vers.linux-amd64.tar.gz

# extract node_exporter
tar -xvzf /home/vagrant/Downloads/node_exporter-${exp_vers}.linux-amd64.tar.gz

# create a symbolic link of node_exporter
sudo ln -s /home/vagrant/Prometheus/node_exporter/node_exporter-${exp_vers}.linux-amd64/node_exporter /usr/bin

cd /home/vagrant/Prometheus/node_exporter/node_exporter-${exp_vers}.linux-amd64

# edit node_exporter configuration file and add configuration so that it will automatically start in next boot
cat <<EOF > /etc/init/node_exporter.conf
# Run node_exporter-${exp_vers}.linux-amd64
start on startup
script
   /usr/bin/node_exporter
end script
EOF

# start service of node_exporter
nohup sudo sh -c 'node_exporter > node_exporter.log 2>&1 &'
