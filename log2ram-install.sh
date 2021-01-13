# Install log2ram 

set -e

sudo apt install rsync

cd /home/pi

wget https://github.com/azlux/log2ram/archive/master.tar.gz -O log2ram.tar.gz
tar xf log2ram.tar.gz
rm log2ram.tar.gz

cd /home/pi/log2ram-master

sudo ./install.sh

rm -r /home/pi/log2ram-master

echo "Log2Ram installed"
