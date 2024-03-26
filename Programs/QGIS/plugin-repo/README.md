---
title: QGIS Plugin Repository
tags: studies, programação, qgis, python, plugin
use: Plugin Development
languages: NULL
dependences: QGIS3
---

<details> <summary>Table of Contents 🔖</summary>

</details>

# QGIS Plugin Repository

## [QGIS 3 Plugin Tutorial – Set up a Plugin Repository Explained](https://gis-ops.com/qgis-3-plugin-tutorial-set-up-a-plugin-repository-explained/)
> - [phpQGISrepository](https://gitlab.com/GIS-projects/phpQGISrepository) (`PHP`)

This tutorial explains and give the option to set the Pluing in the `localhost` (docker option) or in a Apache Server, using the first option the program builds a simple webpage along QGis interface to manage the plugins.

![Step 4](https://github.com/gis-ops/tutorials/raw/master/qgis/static/img/repo_add.png)
> font: [gis-ops.com](https://gis-ops.com/qgis-3-plugin-tutorial-set-up-a-plugin-repository-explained/)

### Docker

Although the server reads the all the information from the `metadata.txt` file and displays it in the webpage, the QGis only read the update information when the manager is opened, so the user needs to close and open the manager to see the updates (*i need to lookup if its a configuration of the server application*)

I therm of the image, the size of the image is 1.06GB, and the container uses (*needs metrics*)GB of memory, the container exposes the port `8082`.

Some (at current commit `4ae332b1fa87b49ed0e2c22c15aed115f403c1ab`) vulnerabilities (*fixable packages*) were found by the Docker Scout:

|Package|Vulnerabilities||||
|---|:---:|:---:|:---:|:---:|
|stdlib 1.19.1|2C|17H|8M| 0L|
|debian/libde265 1.0.11-0+deb10u4|5H|2M|0L|
|debian/imagemagick 8:6.9.10.23+dfsg-2.1+deb10u5|1H|3M|13L|
|debian/gnutls28 3.6.7-4+deb10u11|1H|2M|1L|
|debian/tiff 4.1.0+git191117-2~deb10u8|1H|1M|14L|
|debian/openssh 1:7.9p1-10+deb10u3|1H|1M|9L|
|debian/nss 2:3.42.1-1+deb10u7|1H|1M|4L|1U|
|debian/curl 7.64.0-4+deb10u7|1H|1M|4L|
|debian/ncurses 6.1+20181013-2+deb10u4|1H|0M|1L|
|debian/postgresql-11 11.22-0+deb10u1|1H|0M|0L|
|debian/python3.7 3.7.3-2+deb10u6|0H|1M|6L|
|debian/python2.7 2.7.16-2+deb10u3|0H|1M|6L||
|debian/tar 1.30+dfsg-6|0H|0M|4L|


## [qgis-plugins-xml](https://github.com/planetfederal/qgis-plugins-xml) (`Python-Flask`)

I'm getting an installation of `lxml` package:

```bash
Installing collected packages: wget, progress, MarkupSafe, lxml, itsdangerous, click, Werkzeug, Jinja2, Flask
Running setup.py install for wget ... done
Running setup.py install for progress ... done
Running setup.py install for lxml ... error
error: subprocess-exited-with-error

× Running setup.py install for lxml did not run successfully.
│ exit code: 1
╰─> [97 lines of output]
    Building lxml version 4.5.0.
    Building without Cython. 
    ERROR: b'/bin/sh: 1: xslt-config: not found\n'
    ** make sure the development packages of libxml2 and libxslt are installed **
    Using build configuration of libxslt
    running install
    /home/see7e/byon_scripts/qgs-plugin-repo/qgis-plugins-xml/venv/lib/python3.11/site-packages/setuptools/command/install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
    warnings.warn(
        running build
        running build_py
        creating build
        creating build/lib.linux-x86_64-3.11
        creating build/lib.linux-x86_64-3.11/lxml
        copying src/lxml/ElementInclude.py -> build/lib.linux-x86_64-3.11/lxml
        copying src/lxml/doctestcompare.py -> build/lib.linux-x86_64-3.11/lxml
        copying src/lxml/__init__.py -> build/lib.linux-x86_64-3.11/lxml      
        copying src/lxml/cssselect.py -> build/lib.linux-x86_64-3.11/lxml     
        copying src/lxml/pyclasslookup.py -> build/lib.linux-x86_64-3.11/lxml 
        copying src/lxml/builder.py -> build/lib.linux-x86_64-3.11/lxml       
        copying src/lxml/usedoctest.py -> build/lib.linux-x86_64-3.11/lxml    
        copying src/lxml/_elementpath.py -> build/lib.linux-x86_64-3.11/lxml  
        copying src/lxml/sax.py -> build/lib.linux-x86_64-3.11/lxml           
        creating build/lib.linux-x86_64-3.11/lxml/includes                    
        copying src/lxml/includes/__init__.py -> build/lib.linux-x86_64-3.11/lxml/includes
        creating build/lib.linux-x86_64-3.11/lxml/html                        
        copying src/lxml/html/soupparser.py -> build/lib.linux-x86_64-3.11/lxml/html      
        copying src/lxml/html/_html5builder.py -> build/lib.linux-x86_64-3.11/lxml/html   
        copying src/lxml/html/formfill.py -> build/lib.linux-x86_64-3.11/lxml/html        
        copying src/lxml/html/diff.py -> build/lib.linux-x86_64-3.11/lxml/html
        copying src/lxml/html/defs.py -> build/lib.linux-x86_64-3.11/lxml/html
        copying src/lxml/html/html5parser.py -> build/lib.linux-x86_64-3.11/lxml/html     
        copying src/lxml/html/__init__.py -> build/lib.linux-x86_64-3.11/lxml/html        
        copying src/lxml/html/_diffcommand.py -> build/lib.linux-x86_64-3.11/lxml/html    
        copying src/lxml/html/builder.py -> build/lib.linux-x86_64-3.11/lxml/html         
        copying src/lxml/html/_setmixin.py -> build/lib.linux-x86_64-3.11/lxml/html       
        copying src/lxml/html/usedoctest.py -> build/lib.linux-x86_64-3.11/lxml/html      
        copying src/lxml/html/clean.py -> build/lib.linux-x86_64-3.11/lxml/html           
        copying src/lxml/html/ElementSoup.py -> build/lib.linux-x86_64-3.11/lxml/html     
        creating build/lib.linux-x86_64-3.11/lxml/isoschematron 
        copying src/lxml/isoschematron/__init__.py -> build/lib.linux-x86_64-3.11/lxml/isoschematron
        copying src/lxml/etree.h -> build/lib.linux-x86_64-3.11/lxml
        copying src/lxml/etree_api.h -> build/lib.linux-x86_64-3.11/lxml
        copying src/lxml/lxml.etree.h -> build/lib.linux-x86_64-3.11/lxml     
        copying src/lxml/lxml.etree_api.h -> build/lib.linux-x86_64-3.11/lxml 
        copying src/lxml/includes/xpath.pxd -> build/lib.linux-x86_64-3.11/lxml/includes  
        copying src/lxml/includes/schematron.pxd -> build/lib.linux-x86_64-3.11/lxml/includes
        copying src/lxml/includes/etreepublic.pxd -> build/lib.linux-x86_64-3.11/lxml/includes
        copying src/lxml/includes/xmlparser.pxd -> build/lib.linux-x86_64-3.11/lxml/includes 
        copying src/lxml/includes/tree.pxd -> build/lib.linux-x86_64-3.11/lxml/includes       
        copying src/lxml/includes/xmlschema.pxd -> build/lib.linux-x86_64-3.11/lxml/includes 
        copying src/lxml/includes/c14n.pxd -> build/lib.linux-x86_64-3.11/lxml/includes   
        copying src/lxml/includes/xmlerror.pxd -> build/lib.linux-x86_64-3.11/lxml/includes  
        copying src/lxml/includes/relaxng.pxd -> build/lib.linux-x86_64-3.11/lxml/includes
        copying src/lxml/includes/xinclude.pxd -> build/lib.linux-x86_64-3.11/lxml/includes  
        copying src/lxml/includes/config.pxd -> build/lib.linux-x86_64-3.11/lxml/includes 
        copying src/lxml/includes/uri.pxd -> build/lib.linux-x86_64-3.11/lxml/includes    
        copying src/lxml/includes/dtdvalid.pxd -> build/lib.linux-x86_64-3.11/lxml/includes
        copying src/lxml/includes/__init__.pxd -> build/lib.linux-x86_64-3.11/lxml/includes  
        copying src/lxml/includes/lxml-version.h -> build/lib.linux-x86_64-3.11/lxml/includes
        copying src/lxml/includes/etree_defs.h -> build/lib.linux-x86_64-3.11/lxml/includes  
        creating build/lib.linux-x86_64-3.11/lxml/isoschematron/resources     
        creating build/lib.linux-x86_64-3.11/lxml/isoschematron/resources/rng 
        copying src/lxml/isoschematron/resources/rng/iso-schematron.rng -> build/lib.linux-x86_64-3.11/lxml/isoschematron/resources/rng
        creating build/lib.linux-x86_64-3.11/lxml/isoschematron/resources/xsl 
        copying src/lxml/isoschematron/resources/xsl/XSD2Schtrn.xsl -> build/lib.linux-x86_64-3.11/lxml/isoschematron/resources/xsl
        copying src/lxml/isoschematron/resources/xsl/RNG2Schtrn.xsl -> build/lib.linux-x86_64-3.11/lxml/isoschematron/resources/xsl
        creating build/lib.linux-x86_64-3.11/lxml/isoschematron/resources/xsl/iso-schematron-xslt1
        copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_svrl_for_xslt1.xsl -> build/lib.linux-x86_64-3.11/lxml/isoschematron/resources/xsl/iso-schematron-xslt1                                         
        copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_dsdl_include.xsl -> build/lib.linux-x86_64-3.11/lxml/isoschematron/resources/xsl/iso-schematron-xslt1                                           
        copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_schematron_message.xsl -> build/lib.linux-x86_64-3.11/lxml/isoschematron/resources/xsl/iso-schematron-xslt1                                     
        copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_abstract_expand.xsl -> build/lib.linux-x86_64-3.11/lxml/isoschematron/resources/xsl/iso-schematron-xslt1                                        
        copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_schematron_skeleton_for_xslt1.xsl -> build/lib.linux-x86_64-3.11/lxml/isoschematron/resources/xsl/iso-schematron-xslt1
        copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/readme.txt -> build/lib.linux-x86_64-3.11/lxml/isoschematron/resources/xsl/iso-schematron-xslt1
        running build_ext
        building 'lxml.etree' extension
        creating build/temp.linux-x86_64-3.11
        creating build/temp.linux-x86_64-3.11/src
        creating build/temp.linux-x86_64-3.11/src/lxml
        x86_64-linux-gnu-gcc -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -DCYTHON_CLINE_IN_TRACEBACK=0 -Isrc -Isrc/lxml/includes -I/home/see7e/byon_scripts/qgs-plugin-repo/qgis-plugins-xml/venv/include -I/usr/include/python3.11 -c src/lxml/etree.c -o build/temp.linux-x86_64-3.11/src/lxml/etree.o -w
        src/lxml/etree.c:289:12: fatal error: longintrepr.h: No such file or directory
            289 |   #include "longintrepr.h"
                |            ^~~~~~~~~~~~~~~
        compilation terminated.
        Compile failed: command '/usr/bin/x86_64-linux-gnu-gcc' failed with exit code 1
        creating tmp
        cc -I/usr/include/libxml2 -c /tmp/xmlXPathInitd3m7_ccy.c -o tmp/xmlXPathInitd3m7_ccy.o
        /tmp/xmlXPathInitd3m7_ccy.c:1:10: fatal error: libxml/xpath.h: No such file or directory
            1 | #include "libxml/xpath.h"
                |          ^~~~~~~~~~~~~~~~
        compilation terminated.
        *********************************************************************************
        Could not find function xmlCheckVersion in library libxml2. Is libxml2 installed?
        *********************************************************************************
        error: command '/usr/bin/x86_64-linux-gnu-gcc' failed with exit code 1
        [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: legacy-install-failure

× Encountered error while trying to install package.
╰─> lxml
```

Tried installing separately:

1.  Cython:
    
    ```bash
    pip install Cython
    ```
    
2.  Reinstalling `lxml`:
    
    ```bash
    pip install --upgrade --force-reinstall lxml==4.5.0
    ```

Or even installing manualy the dependencies manualy:

    ```bash
    sudo apt-get install libxml2-dev libxslt-dev
    pip install --upgrade --force-reinstall lxml==4.5.0
    ```

    OS: Ubuntu 22.04.4 LTS on Windows 10 x86_64
    Kernel: 5.15.133.1-microsoft-standard-WSL2
    Shell: bash 5.1.16
    Terminal: Windows Terminal

But the error still persists. Issue opened at [lxml Importing error #9](https://github.com/planetfederal/qgis-plugins-xml/issues/9)


## [QGIS-Django](https://github.com/qgis/QGIS-Django) (`Python-Django`)

> [!NOTE]
> I need to test, my current environment is inside of WSL2 and therefor I can't run `docker-compose` and if i use the current Docker Engine (in windows) i can't build from the `Makefile`... I know, it sucks.

---

In order to avoid these problems, I will try to create myself a `Django` project and try to implement the `QGIS` plugin repository in it, here is the [link](https://github.com/see7e/light-QGIS-plugin-repo) to the repository.