#!/bin/bash
hexo clean
hexo g
hexo d
rm -rf build.log
hexo g --deploy 2>&1 | tee /www/sourcecode/build.log
pm2 stop all
