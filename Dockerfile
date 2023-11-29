FROM staphb/samtools:1.16

SHELL ["/bin/bash", "-c"]
RUN ln -s /usr/bin/python3 /usr/bin/python

RUN apt-get update && apt-get install --no-install-recommends -y \
    python3-pip \
    ; \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*
RUN pip install pyfaidx

COPY src/freec /
RUN ln -s /freec /usr/bin/freec
COPY scripts/generate_controlFREEC_config.py /

CMD ["/bin/bash"]