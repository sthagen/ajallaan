# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/ajallaan/blob/default/etc/sbom/cdx.json) with SHA256 checksum ([ecf70554 ...](https://git.sr.ht/~sthagen/ajallaan/blob/default/etc/sbom/cdx.json.sha256 "sha256:ecf70554651f310e38033671ec65387139c4fefb212b345abcdab70d3fc56916")).
<!--[[[end]]] (checksum: 0f3e2c1b4c577bd3cdf072968bf9bdd7)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                    | Version                                            | License     | Author                             | Description (from packaging data)                                                                        |
|:--------------------------------------------------------|:---------------------------------------------------|:------------|:-----------------------------------|:---------------------------------------------------------------------------------------------------------|
| [attrs](https://www.attrs.org/en/stable/changelog.html) | [23.1.0](https://pypi.org/project/attrs/23.1.0/)   | MIT License | Hynek Schlawack <hs@ox.cx>         | Classes Without Boilerplate                                                                              |
| [httpx](https://github.com/encode/httpx)                | [0.24.1](https://pypi.org/project/httpx/0.24.1/)   | BSD License | Tom Christie <tom@tomchristie.com> | The next generation HTTP client.                                                                         |
| [msgspec](https://jcristharif.com/msgspec/)             | [0.18.2](https://pypi.org/project/msgspec/0.18.2/) | BSD License | Jim Crist-Harif                    | A fast serialization and validation library, with builtin support for JSON, MessagePack, YAML, and TOML. |
<!--[[[end]]] (checksum: d1487cf86505acc1c7945c07e2440652)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                                | Version                                                | License                              | Author                                   | Description (from packaging data)                                                   |
|:--------------------------------------------------------------------|:-------------------------------------------------------|:-------------------------------------|:-----------------------------------------|:------------------------------------------------------------------------------------|
| [anyio](https://anyio.readthedocs.io/en/stable/versionhistory.html) | [3.7.1](https://pypi.org/project/anyio/3.7.1/)         | MIT License                          | Alex Grönholm <alex.gronholm@nextday.fi> | High level compatibility layer for multiple asynchronous event loop implementations |
| [certifi](https://github.com/certifi/python-certifi)                | [2023.5.7](https://pypi.org/project/certifi/2023.5.7/) | Mozilla Public License 2.0 (MPL 2.0) | Kenneth Reitz                            | Python package for providing Mozilla's CA Bundle.                                   |
| [h11](https://github.com/python-hyper/h11)                          | [0.14.0](https://pypi.org/project/h11/0.14.0/)         | MIT License                          | Nathaniel J. Smith                       | A pure-Python, bring-your-own-I/O implementation of HTTP/1.1                        |
| [httpcore](https://github.com/encode/httpcore)                      | [0.17.3](https://pypi.org/project/httpcore/0.17.3/)    | BSD License                          | Tom Christie                             | A minimal low-level HTTP client.                                                    |
| [idna](https://github.com/kjd/idna)                                 | [3.4](https://pypi.org/project/idna/3.4/)              | BSD License                          | Kim Davies <kim@cynosure.com.au>         | Internationalized Domain Names in Applications (IDNA)                               |
| [rfc3986](http://rfc3986.readthedocs.io)                            | [2.0.0](https://pypi.org/project/rfc3986/2.0.0/)       | Apache Software License              | Ian Stapleton Cordasco                   | Validating URI References per RFC 3986                                              |
| [sniffio](https://github.com/python-trio/sniffio)                   | [1.3.0](https://pypi.org/project/sniffio/1.3.0/)       | Apache Software License; MIT License | Nathaniel J. Smith                       | Sniff out which async library your code is running under                            |
<!--[[[end]]] (checksum: 7463334b7b1cd3ef3ef94501702ef1cc)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
attrs==23.1.0
httpx==0.24.1
├── certifi [required: Any, installed: 2023.5.7]
├── httpcore [required: >=0.15.0,<0.18.0, installed: 0.17.3]
│   ├── anyio [required: >=3.0,<5.0, installed: 3.7.1]
│   │   ├── exceptiongroup [required: Any, installed: 1.1.2]
│   │   ├── idna [required: >=2.8, installed: 3.4]
│   │   └── sniffio [required: >=1.1, installed: 1.3.0]
│   ├── certifi [required: Any, installed: 2023.5.7]
│   ├── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   └── sniffio [required: ==1.*, installed: 1.3.0]
├── idna [required: Any, installed: 3.4]
└── sniffio [required: Any, installed: 1.3.0]
msgspec==0.18.2
````
<!--[[[end]]] (checksum: 4055da2932f5f8d4e2ca6e0b7ca11957)-->
