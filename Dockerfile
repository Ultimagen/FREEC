FROM ubuntu:20.04 as build

ENV DEBIAN_FRONTEND=noninteractive

ARG BUILD_ARCH=skylake

WORKDIR /build

RUN apt-get update && \
    apt-get -y install \
        make \
        clang \
        pkg-config \
        libssl-dev

COPY ./ ./

RUN make all ARCH=${BUILD_ARCH}

FROM staphb/samtools:1.16

SHELL ["/bin/bash", "-c"]
RUN ln -s /usr/bin/python3 /usr/bin/python

RUN apt-get update && apt-get install --no-install-recommends -y \
    python3-pip \
    ; \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*
RUN pip install pyfaidx

COPY --from=build /build/freec /
RUN ln -s /freec /usr/bin/freec
COPY scripts/generate_controlFREEC_config.py /

CMD ["/bin/bash"]
