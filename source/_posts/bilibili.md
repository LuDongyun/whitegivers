---
title: b站视频内嵌
date: 2020-04-08 18:07:57
tags:
    -技术
---
# 使用tags插件创建hexo博客b站视频内嵌
在需要内嵌b站视频的地方添加```tags```：
```
{% bilibili video-link-here %}
```
其中，视频连接可在b站视频嵌入代码链接中找到，具体位置如下：
![1](/bilibili/1.jpg)
```
<iframe src="//player.bilibili.com/player.html?aid=4298139&bvid=BV1ts411z7M9&cid=6953474&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
```
```
aid=4298139&bvid=BV1ts411z7M9&cid=6953474&page=1
```
截取其中视频号码部分,将其放入tags中即可。
最终效果如下：
```
{% bilibili aid=4298139&bvid=BV1ts411z7M9&cid=6953474&page=1 %}
```
{% bilibili aid=4298139&bvid=BV1ts411z7M9&cid=6953474&page=1 %}
