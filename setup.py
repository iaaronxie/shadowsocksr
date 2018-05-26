import codecs
from setuptools import setup


with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="shadowsocks",
    version="2.6.12",
    license='http://www.apache.org/licenses/LICENSE-2.0',
    description="A fast tunnel proxy that help you get through firewalls",
    author='clowwindy',
    author_email='clowwindy42@gmail.com',
    url='https://github.com/shadowsocks/shadowsocks',
    packages=['shadowsocks', 'shadowsocks.crypto'], # 对指定目录下的文件进行打包
    
    # 找到当前目录下的 shadowsocks 包，并且 README.rst 和 LICENSE 都要安装到该目录下
    # 需要当前目录下有 MANIFEST.in 文件 include 需要包含的文件
    package_data={
        'shadowsocks': ['README.rst', 'LICENSE']
    },
    install_requires=[],
    
    # 为全局安装 sslocal 和 ssserver 脚本，脚本定义文件分别位于 shadowsocks/local 和shaodwsocks/server 文件
    entry_points="""
    [console_scripts]
    sslocal = shadowsocks.local:main
    ssserver = shadowsocks.server:main
    """,
    
    # 包含包的成熟度、支持的平台类型等信息
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: Proxy Servers',
    ],
    long_description=long_description,
)
