#luge
1.Tencent是一个使用Scrapy框架对腾讯招聘网站某些有效信息进行了高效抓取，抓取下来的信息可以使用Mysql/mangoDB数据库存储
2.manhua是对腾讯动漫免费漫画进行爬取，使用seleuium + Chrome + requests + 多进程的方法，即使一直优化，爬取的效率还是不高，因为网速的原因，
效率一直很难提升，腾讯漫画采用的是异步加载的方式对漫画进行加载，且使用常用的driver.execute_script()加载JS的方式不能触发鼠标滚轮事件，
目测应该是被禁用了，但是点击事件可以触发，我采用的是切换到对页阅读，然后点击下一页（异步加载）到最后，然后在一次性爬取所有图片的地址，
使用requests方法拿到图片的文件流，保存到本地，但是由于多进程的问题，网速是一个硬伤，有极少部分爬取的图片不全，下次在进行优化吧
