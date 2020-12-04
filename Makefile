#.PHONY all

HOST?=pisound

all: install
.PHONY: hostname
hostname:
        echo "hostname function"
        sudo sed -i 's/$(hostname)/$(HOST)/g' /etc/hosts
        sudo sed -i 's/$(hostname)/$(HOST)/g' /etc/hostname

jacktrip:
        git clone https://github.com/jacktrip/jacktrip.git $@
        cd $a/src && ./build
        cd ../builddir && sudo make install
        cd

.PHONY: install
install: hostname
#       touch hostname
#       touch jacktrip
#       @cd jacktrip && git pull

.PHONY: foo-docker
foo-docker: install
        @cd jacktrip && docker build
