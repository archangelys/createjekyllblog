createjekyllblog
================

usage: newpost.py [-h] [-d ROOTPATH] [-t TAGS] [-c CATEGORIES] [-p FileType]
                  Title

Automatically create new blog post.

positional arguments:
  Title

optional arguments:

  -h, --help            show this help message and exit
  
  -d ROOTPATH, --dest ROOTPATH
  
                        Specify the root directory of jekyll blog. Default is
                        
                        the current directory.
                        
  -t TAGS, --tags TAGS  The tag(s) of the blog.
  
  -c CATEGORIES, --categories CATEGORIES
  
                        The category(ies) of the blog.
                        
  -p FileType, --type FileType
  
                        Blog File Type. Default type is markdown.
