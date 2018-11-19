

# Installing Neuroshare

Following instructions are for Linux, simplified from [here](https://pythonhosted.org/neuroshare/).

Download the library files MultiChannel Systms
for Linux [here](http://download.multichannelsystems.com/download_data/software/neuroshare/nsMCDLibrary_Linux64_3.7b.tar.gz).
Extract the contents and copy the two library files in the folder `nsMCDLibrary`
to `/usr/lib/neuroshare` like so:

```
sudo cp <>/nsMCDLibrary.so /usr/lib/neuroshare
sudo cp <>/nsAPItypes.h /usr/lib/neuroshare
```


Create a new conda environment with the following command
```bash
conda create -n neuroshare python=3.7,pip,numpy,matplotlib
source activate neuroshare
git clone https://github.com/G-Node/python-neuroshare
python setup.py install
```



# Errors

The errors do not natively show up in Python, this list might help:

|Error| Meaning|
|---|---|
|_capi.error" neuroshare-error(-3) | File not found |
