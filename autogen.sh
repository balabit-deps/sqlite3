#!/bin/bash

mkdir -p m4
libtoolize -i -c -f
aclocal -I m4
autoconf
