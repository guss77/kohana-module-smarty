# Copyright (c) 2007, Taboola.com
# All rights reserved.

%define dist            tbl
%define section         Servers/Internet
%define svnrev			0

%{!?_with_compress: %{!?_without_compress: %define _with_compress 1}}

# -----------------------------------------------------------------------------

Summary:        Templating engine for Kohana 3
Name:           kohana-module-smarty
Version:        3.2.4
Release:        2.%{svnrev}%{dist}
Group:          %{section}
License:        BSD
URL:            http://github.com/guss77/kohana-module-smarty
Packager:       Oded Arbel <oded@geek.co.il> 
BuildArch:      noarch
Source0:        %{name}-%{version}.tar.gz
# add patches, if any, here
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u})
# build and runtime requirements here

Requires:		kohana >= 3.0
Requires:		php-pear-Twig

%description
This is a module for the Kohana PHP framework that integrates the Smarty Template Engine. 
It also provides a framework for other rendering plugins and provides a simple framework 
for extensions of the Kohana Template Controller class to return more than one type of 
output which is particularly useful in AJAX applications.

# -----------------------------------------------------------------------------

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %{name}

# -----------------------------------------------------------------------------

%build

# -----------------------------------------------------------------------------

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/kohana/modules/smarty
for dir in classes config smarty_plugins views thirdparty; do
	rsync -a $dir/ $RPM_BUILD_ROOT%{_datadir}/kohana/modules/smarty/$dir/
done

# -----------------------------------------------------------------------------

%clean
rm -rf $RPM_BUILD_ROOT

# -----------------------------------------------------------------------------

%files
%defattr(-,root,root,0755)
%{_datadir}/kohana/modules/smarty

%changelog
* Sun Mar 29 2011 Oded Arbel <oded@geek.co.il>  0:3.2.4-2tbl
- Update module to work with Kohana 3.1

* Sun Dec 19 2010 Oded Arbel <oded@geek.co.il>  0:3.2.4-1tbl
- rebase on personal fork as preperation for submitting upstream

* Sun Aug 29 2010 Oded Arbel <oded@geek.co.il>  0:3.2.3-3tbl
- Add patch for PHP 5.1 support

* Sun Aug 29 2010 Oded Arbel <oded@geek.co.il>  0:3.2.3-2tbl
- Fix installation path

* Sun Aug 29 2010 Oded Arbel <oded@taboola.com>  0:3.2.3-1tbl
- Initial package
