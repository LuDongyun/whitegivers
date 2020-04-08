'''
Author: Enoch2090
Blog: enoch2090.me
Also visit whitegivers.com!
Generate a word cloud file in the working directory. The word cloud file can be used as input for the [word_cloud](https://amueller.github.io/word_cloud/cli.html) generation.
'''
import os
import argparse
import sys
import markdown


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--dir", help="The directory where your source folder at.")
    return parser.parse_args()


def count(file_list):
    tag_base = {}
    for file in file_list:
        f = open(file, "r")
        content = f.read()
        f.close()
        md = markdown.Markdown(extensions=['meta'])
        md.convert(content)
        try:
            tags = md.Meta['tags'][1::]
            for tag in tags:
                tag_cleared = tag.replace('- ', '')
                if tag_cleared in tag_base:
                    tag_base[tag_cleared] += 1
                else:
                    tag_base[tag_cleared] = 1
        except:
            pass
    return tag_base


def scan(dirc, file_list):
    os.chdir(dirc)
    dir_list = os.listdir(dirc)
    for item in dir_list:
        if os.path.isfile(os.path.join(dirc, item)) and (('.md' in item) or ('.txt' in item) or ('.markdown' in item)):
            file_list.append(os.path.join(dirc, item))
        if os.path.isdir(os.path.join(dirc, item)):
            file_list = scan(os.path.join(dirc, item), file_list)
        else:
            pass
    return file_list


def write_as_file(tag_base, dirc):
    with open(dirc+'/wordcloud.txt', 'w') as f:
        t = ''
        for tag, count in tag_base.items():
            for i in range(count):
                t = t + ' ' + tag
        print(t)
        f.write(t)
    return


if __name__ == "__main__":

    args = parse_args()
    if args.dir == None:
        print("Argument missing: directory")
    else:
        cwd = os.getcwd()
        file_list = []
        file_list = scan(args.dir, file_list)
        tags = count(file_list)
        write_as_file(tags, cwd)
