#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from datetime import datetime as dt
import argparse

__author__ = "song.yang"
__version__ = "1.0.0"

def parse_args():
    parse = argparse.ArgumentParser(description='Automatically create new blog post.')
    parse.add_argument('title',metavar='Title',
                       help='')
    parse.add_argument('-d','--dest', dest='rootpath',
                       help='Specify the root directory of jekyll blog. Default is the current directory.')
    parse.add_argument('-t','--tags', dest='tags',
                       help='The tag(s) of the blog.')
    parse.add_argument('-c','--categories', dest='categories',
                       help='The category(ies) of the blog.')
    parse.add_argument('-p','--type',dest='filetype', metavar='FileType',
                       default='markdown',choices=['markdown','texttile','html'],
                       help='Blog File Type. Default type is markdown.')
    args = parse.parse_args()
    return args

class NewPost():

    def __init__(self, args):
        self.title = args.title
        self.rootpath = args.rootpath
        self.tags = args.tags
        self.categories = args.categories
        self.filetype = args.filetype
        self.current_dir = os.getcwd()
        self.post_base_dir = '_posts'

        if not self.rootpath:
            self.rootpath = self.current_dir

        self.post_dir = os.path.join(self.rootpath,self.post_base_dir)
        self.file_name = self.__gen_file_name()
        self.file_content = self.__gen_file_content()
        self.create_file = os.path.join(self.rootpath, self.post_base_dir, self.file_name)

    def __gen_file_name(self):
        date = dt.now().strftime('%Y-%m-%d')
        name = '-'.join(title for title in self.title.split())
        suffix = self.filetype
        return '{0}-{1}.{2}'.format(date, name, suffix)

    def __gen_file_content(self):
        date = dt.now().strftime('%Y-%m-%d %H:%M:%S')
        content = '---\nlayout: post\ntitle: "{0}"\ndate: {1}\n'.format(self.title, date)
        if self.categories:
            content += 'categories: {}\n'.format(self.categories)
        if self.tags:
            content += 'tags: {}\n'.format(self.tags)
        content += '---\n'
        return content


    def create_post(self):
        with open(self.create_file, 'a') as file:
            file.write(self.file_content)
        print "Done create new post."

def pos_new_blog():
    args = parse_args()
    new_post = NewPost(args)
    new_post.create_post()


if __name__ == '__main__':
    pos_new_blog()

