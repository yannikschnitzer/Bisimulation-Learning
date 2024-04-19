FROM --platform=linux/amd64 ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && \
    apt-get install -y git build-essential && \
    apt-get install -y sudo && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt install -y python3.10 && \
    apt-get install -y python3-pip && \
    apt-get install -y curl && \
    curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10 && \
    pip3 install --upgrade pip && \
    mkdir CAV24

# Install nuXmv
WORKDIR /CAV24
RUN apt-get install -y wget && \
    wget https://nuxmv.fbk.eu/theme/download.php?file=nuXmv-2.0.0-linux64.tar.gz && \
    tar -xvzf download.php\?file\=nuXmv-2.0.0-linux64.tar.gz && \
    rm download.php\?file\=nuXmv-2.0.0-linux64.tar.gz 

# Install Ultimate
WORKDIR /CAV24
RUN apt-get install -y openjdk-11-jdk && \ 
    apt install -y maven && \
    apt install -y zip && \
    git clone https://github.com/ultimate-pa/ultimate
WORKDIR /CAV24/ultimate/releaseScripts/default
RUN ./makeFresh.sh

# Install CPAChecker
WORKDIR /CAV24
RUN wget https://cpachecker.sosy-lab.org/CPAchecker-2.3-unix.zip && \
    unzip CPAchecker-2.3-unix.zip && \
    rm CPAchecker-2.3-unix.zip  && \
    apt-get install -y openjdk-17-jdk openjdk-17-jre

# Intstall Z3
WORKDIR /
RUN git clone https://github.com/Z3Prover/z3.git 
WORKDIR /z3
RUN python3 ./scripts/mk_make.py
WORKDIR /z3/build
RUN make && \
    make install

# Get artifact and libraries 
WORKDIR /CAV24 
RUN git clone https://github.com/yannikschnitzer/Bisimulation-Learning.git 
RUN pip install -r Bisimulation-Learning/requirements.txt
