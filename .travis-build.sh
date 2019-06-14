#!/bin/bash
set -exo pipefail

image=$1

if [[ $image =~ ^centos: ]]
then
    pkgcmd="yum"
    builddep="yum-builddep"
    sed -i '/^tsflags=/d' /etc/yum.conf
    yum install -q -y epel-release
    yum install -q -y @buildsys-build
    yum install -q -y yum-utils
    yum install -q -y git
    yum install -q -y rpmdevtools
    yum install -q -y yum-plugin-copr
    yum install -q -y pv
    yum copr enable -q -y simc/stable
elif [[ $image =~ ^fedora: ]]
then
    pkgcmd="dnf"
    builddep="dnf builddep"
    sed -i '/^tsflags=/d' /etc/dnf/dnf.conf
    dnf install -q -y --allowerasing @buildsys-build
    dnf install -q -y 'dnf-command(builddep)'
    dnf install -q -y git
    dnf install -q -y rpmdevtools
    dnf install -q -y pv
    dnf copr enable -q -y simc/stable
fi

$builddep -q -y python-eccodes.spec

if [[ $image =~ ^fedora: || $image =~ ^centos: ]]
then
    mkdir -p ~/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
    cp python-eccodes.spec ~/rpmbuild/SPECS/
    spectool -g -R -S ~/rpmbuild/SPECS/python-eccodes.spec
    set +x
    rpmbuild -ba ~/rpmbuild/SPECS/python-eccodes.spec 2>&1 | pv -q -L 3k
else
    echo "Unsupported image"
    exit 1
fi
