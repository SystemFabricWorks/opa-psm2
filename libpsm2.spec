#
#  This file is provided under a dual BSD/GPLv2 license.  When using or
#  redistributing this file, you may do so under either license.
#
#  GPL LICENSE SUMMARY
#
#  Copyright(c) 2015 Intel Corporation.
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of version 2 of the GNU General Public License as
#  published by the Free Software Foundation.
#
#  This program is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  Contact Information:
#  Intel Corporation, www.intel.com
#
#  BSD LICENSE
#
#  Copyright(c) 2015 Intel Corporation.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions
#  are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in
#      the documentation and/or other materials provided with the
#      distribution.
#    * Neither the name of Intel Corporation nor the names of its
#      contributors may be used to endorse or promote products derived
#      from this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Copyright (c) 2014-2015 Intel Corporation. All rights reserved.
#
Summary: Intel PSM Libraries
Name: libpsm2
Version: 10.1.0
Release: 1
License: BSD or GPLv2
URL: https://github.com/01org/opa-psm2/
# ERRATA: need to push the tarball upto github for the review for Fedora.
Source0: https://github.com/01org/opa-psm2/releases/download/10_1/%{name}-%{version}.tar.gz

# The OPA product is supported on x86 64 only:
ExclusiveArch: x86_64
BuildRequires: libuuid-devel
BuildRequires: systemd

%package devel
Summary: Development files for Intel PSM
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libuuid-devel

%package compat
Summary: Compat library for Intel PSM
Requires: %{name}%{?_isa} = %{version}-%{release}

%description
The PSM Messaging API, or PSM API, is the low-level
user-level communications interface for the Intel(R) OPA
family of products. PSM users are enabled with mechanisms
necessary to implement higher level communications
interfaces in parallel environments.

%description devel
Development files for the Intel PSM library

%description compat
Support for MPIs linked with PSM versions < 2

%prep
%setup -q -n libpsm2-%{version}

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/libpsm2.so.2.1
%{_libdir}/libpsm2.so.2
%{_udevrulesdir}/40-psm.rules

%files devel
%{_libdir}/libpsm2.so
%{_includedir}/psm2.h
%{_includedir}/psm2_mq.h
%{_includedir}/psm2_am.h
%{_includedir}/hfi1diag

%files compat
%{_libdir}/psm2-compat/libpsm_infinipath.so.1
%{_udevrulesdir}/40-psm-compat.rules
/etc/modprobe.d/libpsm2-compat.conf
%{_sbindir}/libpsm2-compat.cmds

%changelog
* Tue Apr 05 2016 Paul Reger <paul.j.reger@intel.com> - 10.1.0
- Upstream PSM2 source code for Fedora.
