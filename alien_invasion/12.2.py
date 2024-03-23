# 12.2 安装Pygame

# 12.2.1 使用pip安装Python包

# 检查是否安装了pip：
# Linux和OS X系统：pip --version或pip3 --version，打印pip版本信息则安装成功
# Windows系统：python -m pip --version或python -m pip3 --version，打印pip版本信息则安装成功

# 安装pip：
# 通过网站https://bootstrap.pypa.io/get-pip.py、https://pip.pypa.io 等获取get-pip.py
# Linux和OS X系统：在get-pip.py所在目录运行sudo python get-pip.py或sudo python3 get-pip.py
# Windows系统：在get-pip.py所在目录运行python get-pip.py或python3 get-pip.py

# 12.2.2 在Linux系统中安装Pygame

# Python 2.7
# 安装Pygame：sudo apt-get install python-pygame

# Python 3
# 安装Pygame依赖的库：sudo apt-get install 库名
# Pygame依赖库：基础功能：python3-dev或python3.5-dev、mercurial、libsdl-image1.2-dev、libsdl2-dev、libsdl-ttf2.0-dev
#     声音等高级功能：libsdl-mixer1.2-dev、libportmidi-dev、libswscale-dev、libsmpeg-dev、libavformat-dev、libavcodec-dev、python-numpy

# 安装Pygame：pip install --user hg+http://bitbuck.org/pygame/pygame
#     或pip3 install --user hg+http://bitbuck.org/pygame/pygame
# 检查是否安装了Pygame：打开python终端会话，输入import pygame，不报错则安装成功

# 12.2.3 在OS X系统中安装Pygame

# 安装Homebrew：xcode-select --install
#     ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/
#         master/install)"
# 检查是否安装了Homebrew：brew doctor，打印Your system is ready to brew.则安装成功

# 安装Pygame依赖库：brew install 库名
# Pygame依赖库：基础功能：hg、sdl、sdl_image、sdl_ttf
#     声音等高级功能：sdl_mixer、portmidi

# 安装Pygame：pip install --user hg+http://bitbuck.org/pygame/pygame
#     或pip3 install --user hg+http://bitbuck.org/pygame/pygame
# 检查是否安装了Pygame：打开python终端会话，输入import pygame，不报错则安装成功

# 12.2.4 在Windows系统中安装Pygame
# 通过网站https://bitbucket.org/pygame/pygame/downloads、
#     http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame 等获取安装文件
# .exe文件：运行它
# .whl文件：python -m pip install --user 文件名
