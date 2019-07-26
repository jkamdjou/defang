defang
======

Defangs and refangs malicious URLs

Usage
-----

- As a script: use the `defang` command to defang or "refang"
  content, supporting
  both stdin/stdout streams as well as to/from files on disk::

        $ echo http://evil.example.com/malicious.php | defang
        hXXp://evil.example[.]com/malicious.php

- As a library::

        >>> from defang import defang
        >>> url = "http://evil.example.com/malicious.php"
        >>> defang(url)
        'hXXp://evil.example[.]com/malicious.php'

- We've added a few new keyword argument options::

        >>> defang(url, colon=True)
        'hXXp[:]//evil.example[.]com/malicious.php'
        >>> defang(url, all_dots=True)
        'hXXp://evil[.]example[.]com/malicious.php'

Releases
--------

0.5.0:
  - added new options to defang
  - `all_dots=True` will turn all dots into [.] and not just the one before the TLD
  - `colon=True` will translate http:// into http[:]// as well as other protocols
0.4.0:
  - added support for URIs with IPv4
0.3.0:
  - added some regex fixes and arbitrary protocol defanging
