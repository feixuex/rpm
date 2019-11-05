%global debug_package %{nil}

Name:       qatzip
Version:    1.0.1
Release:    beta1%{?dist}
Summary:    Tool for enable gzip acceleration
License:    BSD
Group:      QAT/Base
URL:        https://github.com/intel/QATzip
Source0:    https://github.com/intel/QATzip/%{name}-%{version}.tar.gz


%description
QATzip is a user space library which builds on top of the Intel QuickAssist
Technology user space library, to provide extended accelerated compression and
decompression services by offloading the actual compression and decompression
request(s) to the Intel Chipset Series. QATzip produces data using the standard
gzip format (RFC1952) with extended headers. The data can be decompressed with a
compliant gzip implementation. QATzip is design to take full advantage of the
performance provided by Intel QuickAssist Technology.

%package devel
Summary: Development components for the libqatzip package
Group: QAT/Development

Requires:  qatzip  = %{version}-%{release}

%description devel
Development components for the libqatzip package

%prep
%setup -q

%build
./configure --prefix=$RPM_BUILD_ROOT --libdir=$RPM_BUILD_ROOT/usr/lib64
make


%install
install -D -m 0755 docs/QATzip-man.pdf %{buildroot}%{_datadir}/QATzip-man.pdf
install -D -s -m 0755 utils/qzip %{buildroot}%{_bindir}/qzip
install -D -m 0644 man/qzip.1 %{buildroot}%{_mandir}/man1/qzip.1
install -D -s -m 0755 src/libqatzip.so.%{version} %{buildroot}%{_libdir}/libqatzip.so.%{version}
ln -s libqatzip.so.%{version} %{buildroot}%{_libdir}/libqatzip.so
ln -s libqatzip.so.%{version} %{buildroot}%{_libdir}/libqatzip.so.0
install -D -m 0644 include/qatzip.h %{buildroot}%{_includedir}/qatzip.h
install -D -m 0644 include/qz_utils.h %{buildroot}%{_includedir}/qz_utils.h
install -D -m 0644 src/qatzip_internal.h %{buildroot}%{_includedir}/qatzip_internal.h


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc LICENSE README.md
%{_libdir}/libqatzip.so.*
%{_bindir}/qzip
%{_mandir}/man1/qzip.1*
%{_datadir}/QATzip-man.pdf


%files devel
%doc LICENSE README.md 
%defattr(-,root,root,-)
%{_includedir}/qatzip.h
%{_includedir}/qz_utils.h
%{_includedir}/qatzip_internal.h
%{_libdir}/libqatzip.so

%changelog
* Sun Sep 29 2019 Fei XueX <feix.xue@intel.com> 1.0.1-beta1
- Release 1.0.1
* Tue Jul 9 2019 Joel Schuetze <joel.d.schuetze@intel.com>
- Release 1.0.0

