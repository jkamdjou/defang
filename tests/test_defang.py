import os
import sys
from defang import defang, refang

rootdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path = [rootdir] + sys.path


def test_defang():
    for fanged, defanged in (
        ('example.org',
         'example[.]org'),
        ('http://example.org',
         'hXXp://example[.]org'),
        ('example.org\nbadguy.example.org\n',
         'example[.]org\nbadguy.example[.]org\n'),
        ('http://1.22.33.111/path',
         'hXXp://1[.]22.33.111/path'),
        ('HTTP://EVIL-guy.badguy.NET',
         'hXXp://EVIL-guy.badguy[.]NET'),
        ('ssh://foobar.example.org/',
         '(ssh)://foobar.example[.]org/'),
        ('ftp://foo-bar.example.org',
         'fXp://foo-bar.example[.]org'),
        ('http://sub.domain.org/path/to?bad=stuff',
         'hXXp://sub.domain[.]org/path/to?bad=stuff'),
        ('ftp://user:pass@example.com/dir',
         'fXp://user:pass@example[.]com/dir'),
        ('ftp://user:pass@127.13.1.2/dir',
         'fXp://user:pass@127[.]13.1.2/dir'),
    ):
        assert defang(fanged) == defanged


def test_refang():
    for fanged, defanged in (
        ('example.org',
         'example[.]org'),
        ('http://example.org',
         'hXXp://example[.]org'),
        ('example.org\nbadguy.example.org\n',
         'example[.]org\nbadguy.example[.]org\n'),
        ('http://EVIL-guy.badguy.NET',
         'hXXp://EVIL-guy.badguy[.]NET'),
        ('ssh://foobar.example.org/',
         '(ssh)://foobar.example[.]org/'),
        ('ftp://foo-bar.example.org',
         'fXp://foo-bar.example[.]org'),
        ('http://sub.domain.org/path/to?bad=stuff',
         'hXXp://sub.domain[.]org/path/to?bad=stuff'),
        ('gopher://badstuff.org/',
         '(gopher)://badstuff[.]org/'),
        ('s3://something.amazon.com/testing?zxc=zxc',
         's3://something[DOT]amazon(dot)com/testing?zxc=zxc'),
        ('''
https://otherstuff.org
badstuff.org
goodstuff.org/and/path
foo://newstuff.org/what?foo=true
bar-baz://crazy.stuff.other.foo.co.uk
''',
         '''
hXXps://otherstuff(DOT)org
badstuff[DOT]org
goodstuff[.]org/and/path
foo://newstuff(.)org/what?foo=true
bar-baz://crazy[.]stuff(DOT)other[dot]foo(.)co.uk
'''),
    ):
        assert refang(defanged) == fanged
