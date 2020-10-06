-x() {
    sudo apt install python3-pip ipython3
    pip3 install python-sat[pblib,aiger]
    pip3 install python-sat
    cd Reductor
    python3 3sat_to_xsat.py $*
}

$1 $2