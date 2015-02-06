%define prj     Auth

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:		horde-auth
Version:	0.1.1
Release:	6
Summary:	Horde Authentication API
License:	LGPL
Group:		Networking/Mail
Url:		http://pear.horde.org/index.php?package=%{prj}
Source0:	%{prj}-%{version}.tgz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
Requires(pre):  php-pear
Requires:	horde-framework
Requires:	horde-datatree
Requires:	horde-form
Requires:	horde-secret
Requires:	horde-util
Requires:	horde-history
Requires:	kolab-server
Requires:	php-pear
Requires:	php-gettext
Requires:	php-pear-Net_IMSP
Suggests:	php-sasl
Suggests:	php-pam_auth
BuildRequires:	php-pear
BuildRequires:  php-pear-channel-horde


%description
The Auth:: class provides a common abstracted interface into the various
backends for the Horde authentication system.
 This package contains implementations for:
 * A Horde Application
 * Composite Auth Driver
 * Custom SQL
 * Cyrus with SQL Support
 * Dummy Auto Login
 * FTP
 * HTTP
 * IMAP
 * IMSP
 * IP Based
 * Kerberos
 * Kolab
 * LDAP
 * Microsoft Active Directory
 * Shibboleth
 * System Login
 * PAM
 * Passwd File
 * Radius
 * SASL
 * SMB (smbauth extension)
 * SMB (smbclient)
 * SQL

Optional php extensions: pam_auth and sasl

%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package*.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%dir %{peardir}/Horde/Auth
%dir %{peardir}/Horde/Auth/Signup
%{xmldir}/%{prj}.xml
%{peardir}/Horde/Auth.php
%{peardir}/Horde/Auth/Signup.php
%{peardir}/Horde/Auth/Signup/datatree.php
%{peardir}/Horde/Auth/Signup/sql.php
%{peardir}/Horde/Auth/application.php
%{peardir}/Horde/Auth/auto.php
%{peardir}/Horde/Auth/composite.php
%{peardir}/Horde/Auth/customsql.php
%{peardir}/Horde/Auth/cyrsql.php
%{peardir}/Horde/Auth/cyrus.php
%{peardir}/Horde/Auth/ftp.php
%{peardir}/Horde/Auth/http.php
%{peardir}/Horde/Auth/http_remote.php
%{peardir}/Horde/Auth/imap.php
%{peardir}/Horde/Auth/imsp.php
%{peardir}/Horde/Auth/ipbasic.php
%{peardir}/Horde/Auth/kolab.php
%{peardir}/Horde/Auth/krb5.php
%{peardir}/Horde/Auth/ldap.php
%{peardir}/Horde/Auth/login.php
%{peardir}/Horde/Auth/msad.php
%{peardir}/Horde/Auth/pam.php
%{peardir}/Horde/Auth/passwd.php
%{peardir}/Horde/Auth/peclsasl.php
%{peardir}/Horde/Auth/radius.php
%{peardir}/Horde/Auth/shibboleth.php
%{peardir}/Horde/Auth/smb.php
%{peardir}/Horde/Auth/smbclient.php
%{peardir}/Horde/Auth/sql.php



%changelog
* Mon Jul 26 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.1.1-4mdv2011.0
+ Revision: 560373
- Increased release for rebuild

* Thu Mar 18 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.1.1-3mdv2010.1
+ Revision: 524824
- increased rel version
- replaced Requires(pre): %%{_bindir}/pear with Requires(pre): php-pear
  increased rel version

* Sat Feb 27 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.1.1-2mdv2010.1
+ Revision: 512488
- bumped up release
- added Requires:  php-pear-Net_IMSP

* Sat Feb 27 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.1.1-1mdv2010.1
+ Revision: 512256
- replaced PreRequ with Requires(pre)
- import horde-auth


