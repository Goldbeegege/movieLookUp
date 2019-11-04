# -*-coding:utf-8-*-
# @author: JinFeng
# @date: 2019/9/26 15:33

import requests
from lxml import etree
import re
#
# ret = requests.get("http://s.ygdy8.com/plus/so.php?typeid=1&keyword=%C3%FB%D5%EC%CC%BD%BF%C2%C4%CF").text
# res = re.findall(r"<a href=['\"](.*)['\"]>\[\d+\]</a>",ret)
# print(res)
# # html = etree.HTML(ret)
# # ret_list = html.xpath("//table[last()]")
# # for i in ret_list:
# #     print(i)
# import os
# ret = os.system('"D:\Program Files (x86)\Thunder9\Program\ThunderStart.exe" -StartType:DesktopIcon')
# pid = os.getpid()
# print(pid)
# print(ret)

# ret = requests.get("http://s.ygdy8.com/plus/so.php?typeid=16&keyword=%BB%F0%D3%B0%C8%CC%D5%DF").text
# res = re.findall(r"<a href=['\"](.*)['\"]>\[\d+\]</a>", ret)
# print(res)

# import os
#
# ret = os.path.expanduser("~")
# print(ret)
import time

# ret = requests.post(
#     "http://so.hao6v.com/e/search/index.php",
#     data={
#         "show":"title,Csmalltext",
#         "tempid":"1",
#         "keyboard":"蜘蛛侠".encode("gbk"),
#         "tbname":"article",
#     },
#     headers={
#         "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
#         "Content-Type":"application/x-www-form-urlencoded",
#     },
# ).text
# print(ret)


s = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>高级搜索 蜘蛛侠 - 66影视 - 迅雷电影下载_在线电影</title>
<meta name="keywords" content="高级搜索 蜘蛛侠 - 66影视 - 迅雷电影下载_在线电影" />
<meta name="description" content="高级搜索 蜘蛛侠 - 66影视 - 迅雷电影下载_在线电影" />
<link rel="stylesheet" rev="stylesheet" href="/images/style.css" type="text/css" />
<script type="text/javascript" src="/js/common.js"></script>
<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7" />
</head>
<body>
	<div id="header"><div id="top">  <a href="https://app.pp63.org/快看.apk" target=_blank>APP安卓版</a>&nbsp;&nbsp;
<a href="http://www.hao6v.com/dy/2012-12-07/19512.html" target=_blank>公告区</a>&nbsp;&nbsp;<a href="http://www.hao6v.com/dy/2019-01-02/32524.html" target="_blank">豆瓣2018榜单</a>&nbsp;&nbsp;
<a href="http://www.hao6v.com/gq/2012-09-01/18841.html" target=_blank><font color='#FF0000'>6v电影排行榜</font></a>&nbsp;&nbsp;
<a href="http://www.hao6v.com/dy/2011-09-20/16090.html" target=_blank>北美票房排行榜</a>&nbsp;&nbsp;
<a href="http://www.hao6v.com/s/007/" target=_blank>007电影全集</a>&nbsp;&nbsp;
<a href="http://www.hao6v.com/s/gf250/" target=_blank>IMDB250电影</a>&nbsp;&nbsp;
<a href="/s/gf/" target=_blank>高评分电影</a>&nbsp;&nbsp;
<a href="/s/hanguodianying/" target=_blank>美国电影</a>&nbsp;&nbsp;<a href="/s/xijudianying/" target=_blank>欧洲电影</a>&nbsp;&nbsp;<a href="/s/yazhoudianying/" target=_blank>亚洲电影</a>&nbsp;&nbsp;<a href="/s/mzdy/" target=_blank>美洲电影</a> &nbsp;<a href="http://www.hao6v.com/e/tool/gbook/?bid=1" target=_blank>访客留言</a></div>
    	<div class="log"><a href="/">6V电影</a></div>
        <div class="topad"><script src="/d/f4.js"></script></div>
<div class="cr"></div>
        <div id="menu">
      <p><a href="http://www.hao6v.com/">首页</a>  <a href="http://www.hao6v.com/dy/" target=_blank>2019最新电影</a> <a href="http://www.hao6v.com/gydy/" target=_blank>国语配音电影</a> <a href="http://www.hao6v.com/zydy/" target=_blank>微电影</a> <a href="http://www.hao6v.com/gq/" target=_blank>经典高清电影</a> <a href="http://www.hao6v.com/jddy/" target=_blank>动画电影</a> <a href="http://www.hao6v.com/3D/" target=_blank>3D电影</a> <a href="http://www.hao6v.com/s/shoujiMP4dianying/" target=_blank>MP4手机电影</a> <a href="http://www.hao6v.com/dlz/" target=_blank>国剧</a> <a href="http://www.hao6v.com/rj/" target=_blank>日韩剧</a> <a href="http://www.hao6v.com/mj/" target=_blank>欧美剧</a> <a href="http://www.hao6v.com/zy/" target=_blank>综艺节目</a> <a href="http://www.hao6v.com/s/gangtaidianying/" target=_blank>港台电影</a> <a href="http://www.hao6v.com/s/jingdiandianying/" target=_blank>日韩电影</a> </p>
      <p class="bg"><a href="http://www.66e.cc/" target=_blank>66影视网</a> 专题分类：<a href="http://www.hao6v.com/s/xiju/" target=_blank>喜剧</a><a href="http://www.hao6v.com/s/dongzuo/" target=_blank>动作</a><a href="http://www.hao6v.com/s/aiqing/" target=_blank>爱情</a><a href="http://www.hao6v.com/s/kehuan/" target=_blank>科幻</a><a href="http://www.hao6v.com/s/qihuan/" target=_blank>奇幻</a><a href="http://www.hao6v.com/s/shenmi/" target=_blank>神秘</a><a href="http://www.hao6v.com/s/huanxiang/" target=_blank>幻想</a><a href="http://www.hao6v.com/s/kongbu/" target=_blank>恐怖</a><a href="http://www.hao6v.com/s/zhanzheng/" target=_blank>战争</a><a href="http://www.hao6v.com/s/maoxian/" target=_blank>冒险</a><a href="http://www.hao6v.com/s/jingsong/" target=_blank>惊悚</a><a href="http://www.hao6v.com/s/juqingpian/" target=_blank>剧情</a><a href="http://www.hao6v.com/s/zhuanji/" target=_blank>传记</a><a href="http://www.hao6v.com/s/lishi/" target=_blank>历史</a><a href="http://www.hao6v.com/s/jilu/" target=_blank>纪录</a><a href="http://www.hao6v.com/s/yindudianying/" target=_blank>印度电影</a>  <a href="http://www.hao6v.com/s/guochandianying/" target=_blank>国产电影</a> <a href="http://www.hao6v.com/s/xijudianying/" target=_blank>欧洲电影</a> <a href="http://www.hao6v.com/s/zhuanti/" target=_blank>专题推荐</a> </p>
        </div>
  </div>

<div id="a960"> <script src="/d/f1.js"></script> </div>
<div id="search">
<div class="ser">
<form action="/e/search/index.php" method="post" name="searchform" id="searchform">
<input type="hidden" name="show" value="title,smalltext" />
<input type="hidden" name="tempid" value="1" />

<span>站内搜索：<input name="keyboard" type="text" size="32" id="keyboard" class="inputText" /></span>
<span class="sect"><select name="tbname">
<option value="article">全站</option>
</select></span>
<span><input type="image" class="inputSub" src="/images/search.gif" /></span>
</form>
</span>
</div>
<div class="help">
<a href="http://www.hao6v.com/dy/2010-10-11/12868.html" target="_blank">6v电影下载帮助与教程<br />电影知识新手必看</a>
</div>
<INPUT type="button" value='收藏本影片' id="copy" onclick="javascript:d=document;window.external.AddFavorite(''+d.location.href+'', ''+d.title+'')">
<div class="help">

<!-- Baidu Button BEGIN -->
    <div id="bdshare" class="bdshare_t bds_tools get-codes-bdshare">
        <span class="bds_more">分享到：</span>
        <a class="bds_qzone"></a>
        <a class="bds_tsina"></a>
        <a class="bds_tqq"></a>
        <a class="bds_renren"></a>
        <a class="bds_baidu"></a>
        <a class="bds_copy"></a>
        <a class="bds_qq"></a>
    </div>
<script type="text/javascript" id="bdshare_js" data="type=tools&amp;uid=267792" ></script>
<script type="text/javascript" id="bdshell_js"></script>
<script type="text/javascript">
	document.getElementById("bdshell_js").src = "http://bdimg.share.baidu.com/static/js/shell_v2.js?t=" + new Date().getHours();
</script>
<!-- Baidu Button END -->
</div>
</div>

<div id="main">
<div class="box">
        	<div class="t">您的位置：<a href='/index.html'>首页</a>&nbsp;>&nbsp;高级搜索</div>
 <tr> 
                                        <td height="100%" valign="top"> <form name=search_news method=post action='http://www.hao6v.com/e/search/index.php' onsubmit='return search_check(document.search_news);'>
                        <table width="100%" border="0" cellspacing="1" cellpadding="3">
                          <input type=hidden name=show value="title">
						  <input type=hidden name=tempid value="1">
                          <tr> 
                            <td height="20">关键字： 
                              <input name="keyboard" type="text" id="keyboard" value="国语配音" size="32">
                              <select name="tbname" id="tbname">
                                <option value="article">迅雷资源</option>
                              </select> 
                              <input type="submit" name="Submit22" value="搜索"> 
                              &nbsp; 
                                     </td>
                              &nbsp; <input type="button" name="Submit" value="高级搜索" onclick="self.location.href='../../../search'">
                              (多个关键字请用&quot;空格&quot;格开) </td>
                          </tr>
                        </table>
                      </form>
                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1" bgcolor="E8F5FB">
                        <tr> 
                          <td height="25">系统搜索到约有<strong>21</strong>项符合<strong>蜘蛛侠</strong>的查询结果</td>
                        </tr>
                      </table>
                       
                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">
        <tr> 
          <td><div align="center">
			  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">
                <tr> 
                  
            <td width="41%" height="25"><font color="#663333">・[<a href=/dy/>2019最新电影</a>]<span class="blue14"><a href=/dy/2019-09-12/ZZXYXYZ.html target=_blank><font color='#FF0000'>2019高分科幻《蜘蛛侠：英雄远征》1080p.国英双语.BD中英双字</font></a></span></font></td>
                  <td width="59%"><font color="#666666">发布时间：2019-09-20 16:57:29</font></td>
                </tr>
              </table>
            </div></td>
        </tr>
        <tr> 
          <td bgcolor="#EBF3FA"> 
            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">
              <tr> 
                <td>◎译　　名　蜘蛛侠：英雄远征 / 新蜘蛛侠2 / 蜘蛛侠2 / 蜘蛛侠2：离家出走(豆友译名) / 蜘蛛侠2：英雄离乡 / 蜘蛛侠2：远离家乡 / 蜘蛛侠：决战千里(港) / 蜘蛛侠：归来2 / 蜘蛛侠：离家日(台)</td>
              </tr>
              <tr>
                <td><a href="/dy/2019-09-12/ZZXYXYZ.html" target="_blank">/dy/2019-09-12/ZZXYXYZ.html</a></td>
              </tr>
            </table>
			</td>
        </tr>
      </table>
                       
                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">
        <tr> 
          <td><div align="center">
			  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">
                <tr> 
                  
            <td width="41%" height="25"><font color="#663333">・[<a href=/jddy/>动画电影</a>]<span class="blue14"><a href=/jddy/2018-12-27/ZZXPXYZ.html target=_blank><font color='#FF0000'>2018高分动画《蜘蛛侠：平行宇宙.加长版》1080p.BD中英双字</font></a></span></font></td>
                  <td width="59%"><font color="#666666">发布时间：2019-03-24 21:32:06</font></td>
                </tr>
              </table>
            </div></td>
        </tr>
        <tr> 
          <td bgcolor="#EBF3FA"> 
            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">
              <tr> 
                <td>◎译　　名　蜘蛛侠：平行宇宙 / Spider-Man: a New Universe / 蜘蛛人：新宇宙(台) / 蜘蛛侠：平行世界 / 蜘蛛侠：新纪元 / 蜘蛛侠：跳入蜘蛛宇宙(港)<br />
◎片　　名　Spider-Man: Into the Spid</td>
              </tr>
              <tr>
                <td><a href="/jddy/2018-12-27/ZZXPXYZ.html" target="_blank">/jddy/2018-12-27/ZZXPXYZ.html</a></td>
              </tr>
            </table>
			</td>
        </tr>
      </table>
                       
                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">
        <tr> 
          <td><div align="center">
			  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">
                <tr> 
                  
            <td width="41%" height="25"><font color="#663333">・[<a href=/3D/>3D</a>]<span class="blue14"><a href=/3D/2017-10-29/30073.html target=_blank>《蜘蛛侠:英雄归来》左右3D版</a></span></font></td>
                  <td width="59%"><font color="#666666">发布时间：2017-10-29 23:13:48</font></td>
                </tr>
              </table>
            </div></td>
        </tr>
        <tr> 
          <td bgcolor="#EBF3FA"> 
            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">
              <tr> 
                <td>◎译　　名　蜘蛛侠：英雄归来/蜘蛛侠：强势回归(港)/蜘蛛人：返校日(台)/新蜘蛛侠/蜘蛛侠：归来/蜘蛛侠：回家/蜘蛛侠：返校季/蜘蛛侠：返校节/蜘蛛侠：归乡/蜘蛛侠：新复仇者<br />
◎片　　名　Spi</td>
              </tr>
              <tr>
                <td><a href="/3D/2017-10-29/30073.html" target="_blank">/3D/2017-10-29/30073.html</a></td>
              </tr>
            </table>
			</td>
        </tr>
      </table>
                       
                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">
        <tr> 
          <td><div align="center">
			  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">
                <tr> 
                  
            <td width="41%" height="25"><font color="#663333">・[<a href=/dy/>2019最新电影</a>]<span class="blue14"><a href=/dy/2017-08-27/ZZXYXGLTS.html target=_blank><font color='#FF0000'>2017动作科幻《蜘蛛侠：英雄归来》1080p.国英双语.BD中英双字</font></a></span></font></td>
                  <td width="59%"><font color="#666666">发布时间：2017-10-04 01:17:24</font></td>
                </tr>
              </table>
            </div></td>
        </tr>
        <tr> 
          <td bgcolor="#EBF3FA"> 
            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">
              <tr> 
                <td>◎译　　名　蜘蛛侠：英雄归来/蜘蛛侠：强势回归(港)/蜘蛛人：返校日(台)/新蜘蛛侠/蜘蛛侠：归来/蜘蛛侠：回家/蜘蛛侠：返校季/蜘蛛侠：返校节/蜘蛛侠：归乡/蜘蛛侠：新复仇者<br />
◎片　　名　Spi</td>
              </tr>
              <tr>
                <td><a href="/dy/2017-08-27/ZZXYXGLTS.html" target="_blank">/dy/2017-08-27/ZZXYXGLTS.html</a></td>
              </tr>
            </table>
			</td>
        </tr>
      </table>
                       
                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">
        <tr> 
          <td><div align="center">
			  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">
                <tr> 
                  
            <td width="41%" height="25"><font color="#663333">・[<a href=/gydy/>国语配音电影</a>]<span class="blue14"><a href=/gydy/2014-08-10/23698.html target=_blank>2014科幻大片《超凡蜘蛛侠2》BD国语配音中字1024高清</a></span></font></td>
                  <td width="59%"><font color="#666666">发布时间：2014-08-10 17:34:03</font></td>
                </tr>
              </table>
            </div></td>
        </tr>
        <tr> 
          <td bgcolor="#EBF3FA"> 
            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">
              <tr> 
                <td>◎译　　名　超凡蜘蛛侠2/蜘蛛人：惊奇再起2(台)/蜘蛛侠2：决战电魔 (港) <br />
◎片　　名　The Amazing Spider-Man 2<br />
◎年　　代　2014<br />
◎国　　家　美国 <br />
◎类　　别　动作/冒险/奇幻  <br />
◎语</td>
              </tr>
              <tr>
                <td><a href="/gydy/2014-08-10/23698.html" target="_blank">/gydy/2014-08-10/23698.html</a></td>
              </tr>
            </table>
			</td>
        </tr>
      </table>
                       
                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">
        <tr> 
          <td><div align="center">
			  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">
                <tr> 
                  
            <td width="41%" height="25"><font color="#663333">・[<a href=/3D/>3D</a>]<span class="blue14"><a href=/3D/2014-08-05/23651.html target=_blank>《超凡蜘蛛侠2》左右3D版</a></span></font></td>
                  <td width="59%"><font color="#666666">发布时间：2014-08-05 19:24:53</font></td>
                </tr>
              </table>
            </div></td>
        </tr>
        <tr> 
          <td bgcolor="#EBF3FA"> 
            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">
              <tr> 
                <td>◎译　　名　超凡蜘蛛侠2/蜘蛛人：惊奇再起2(台)/蜘蛛侠2：决战电魔 (港) <br />
◎片　　名　The Amazing Spider-Man 2<br />
◎年　　代　2014<br />
◎国　　家　美国 <br />
◎类　　别　动作/冒险/奇幻  <br />
◎语</td>
              </tr>
              <tr>
                <td><a href="/3D/2014-08-05/23651.html" target="_blank">/3D/2014-08-05/23651.html</a></td>
              </tr>
            </table>
			</td>
        </tr>
      </table>
                       
                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">
        <tr> 
          <td><div align="center">
			  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">
                <tr> 
                  
            <td width="41%" height="25"><font color="#663333">・[<a href=/yx/>单机游戏</a>]<span class="blue14"><a href=/yx/2013-09-22/21432.html target=_blank>《蜘蛛侠：破碎维度》简体中文版</a></span></font></td>
                  <td width="59%"><font color="#666666">发布时间：2013-09-22 18:14:25</font></td>
                </tr>
              </table>
            </div></td>
        </tr>
        <tr> 
          <td bgcolor="#EBF3FA"> 
            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">
              <tr> 
                <td> 中文名称：蜘蛛侠：破碎维度<br />
中文别名：蜘蛛人：破碎次元<br />
英文名称：Spider-Man: Shattered Dimensions<br />
发行时间：2010年<br />
游戏制作：Beenox / BTpigGames<br />
游戏发行：Activision / BTpig<br />
</td>
              </tr>
              <tr>
                <td><a href="/yx/2013-09-22/21432.html" target="_blank">/yx/2013-09-22/21432.html</a></td>
              </tr>
            </table>
			</td>
        </tr>
      </table>
                       
                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">
        <tr> 
          <td><div align="center">
			  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">
                <tr> 
                  
            <td width="41%" height="25"><font color="#663333">・[<a href=/gydy/>国语配音电影</a>]<span class="blue14"><a href=/gydy/2013-08-18/21192.html target=_blank>经典动作科幻《蜘蛛侠2》BD国语配音中字1024高清</a></span></font></td>
                  <td width="59%"><font color="#666666">发布时间：2013-08-18 18:06:24</font></td>
                </tr>
              </table>
            </div></td>
        </tr>
        <tr> 
          <td bgcolor="#EBF3FA"> 
            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">
              <tr> 
                <td> ◎译　　名　蜘蛛侠2 重剪切延长版 (又名：蜘蛛侠2.1进化版)<br />
◎片　　名　Spider-Man 2 Extended Cut (aka: Spider-Man 2.1)<br />
◎年　　代　2004<br />
◎国　　家　美国<br />
◎类　　别　动作/奇幻/科</td>
              </tr>
              <tr>
                <td><a href="/gydy/2013-08-18/21192.html" target="_blank">/gydy/2013-08-18/21192.html</a></td>
              </tr>
            </table>
			</td>
        </tr>
      </table>
                       
                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">
        <tr> 
          <td><div align="center">
			  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">
                <tr> 
                  
            <td width="41%" height="25"><font color="#663333">・[<a href=/gq/>经典高清电影</a>]<span class="blue14"><a href=/gq/2009-02-12/5899.html target=_blank>经典动作科幻《蜘蛛侠3》720p.国英双语.BD中英双字高清MKV版</a></span></font></td>
                  <td width="59%"><font color="#666666">发布时间：2013-05-14 00:56:57</font></td>
                </tr>
              </table>
            </div></td>
        </tr>
        <tr> 
          <td bgcolor="#EBF3FA"> 
            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">
              <tr> 
                <td>◎译　　名　蜘蛛侠3<br />
◎片　　名　Spider-Man 3<br />
◎年　　代　2007<br />
◎国　　家　美国<br />
◎类　　别　动作/冒险/惊悚<br />
◎语　　言　英语<br />
◎字　　幕　中英双字<br />
◎IMDB评分 6.8/10 (75,659 vot</td>
              </tr>
              <tr>
                <td><a href="/gq/2009-02-12/5899.html" target="_blank">/gq/2009-02-12/5899.html</a></td>
              </tr>
            </table>
			</td>
        </tr>
      </table>
                       
                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">
        <tr> 
          <td><div align="center">
			  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">
                <tr> 
                  
            <td width="41%" height="25"><font color="#663333">・[<a href=/gq/>经典高清电影</a>]<span class="blue14"><a href=/gq/2009-02-12/5898.html target=_blank>经典动作科幻《蜘蛛侠2》720p.国英双语.BD中英双字高清MKV版</a></span></font></td>
                  <td width="59%"><font color="#666666">发布时间：2013-05-14 00:55:48</font></td>
                </tr>
              </table>
            </div></td>
        </tr>
        <tr> 
          <td bgcolor="#EBF3FA"> 
            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">
              <tr> 
                <td>◎译　　名　蜘蛛侠2 重剪切延长版 (又名：蜘蛛侠2.1进化版)<br />
◎片　　名　Spider-Man 2 Extended Cut (aka: Spider-Man 2.1)<br />
◎年　　代　2004<br />
◎国　　家　美国<br />
◎类　　别　动作/奇幻/科幻</td>
              </tr>
              <tr>
                <td><a href="/gq/2009-02-12/5898.html" target="_blank">/gq/2009-02-12/5898.html</a></td>
              </tr>
            </table>
			</td>
        </tr>
      </table>
                       
                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">
        <tr> 
          <td><div align="center">
			  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">
                <tr> 
                  
            <td width="41%" height="25"><font color="#663333">・[<a href=/gq/>经典高清电影</a>]<span class="blue14"><a href=/gq/2009-02-12/5897.html target=_blank>经典动作科幻《蜘蛛侠1》720p.国英双语.BD中英双字高清MKV版</a></span></font></td>
                  <td width="59%"><font color="#666666">发布时间：2013-05-14 00:54:48</font></td>
                </tr>
              </table>
            </div></td>
        </tr>
        <tr> 
          <td bgcolor="#EBF3FA"> 
            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">
              <tr> 
                <td>◎译　　名　蜘蛛侠<br />
◎片　　名　Spider Man<br />
◎年　　代　2002<br />
◎国　　家　美国<br />
◎类　　别　动作/幻想/科幻/惊悚<br />
◎语　　言　英语<br />
◎字　　幕　中英双字<br />
◎IMDB评分 7.4/10 (80,752 v</td>
              </tr>
              <tr>
                <td><a href="/gq/2009-02-12/5897.html" target="_blank">/gq/2009-02-12/5897.html</a></td>
              </tr>
            </table>
			</td>
        </tr>
      </table>
                       
                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">
        <tr> 
          <td><div align="center">
			  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">
                <tr> 
                  
            <td width="41%" height="25"><font color="#663333">・[<a href=/gq/>经典高清电影</a>]<span class="blue14"><a href=/gq/2012-10-22/19196.html target=_blank>2012动作科幻《超凡蜘蛛侠》720p.国英双语.BD中英双字高清MKV版</a></span></font></td>
                  <td width="59%"><font color="#666666">发布时间：2013-04-15 17:09:48</font></td>
                </tr>
              </table>
            </div></td>
        </tr>
        <tr> 
          <td bgcolor="#EBF3FA"> 
            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">
              <tr> 
                <td>◎译　　名　超凡蜘蛛侠/蜘蛛侠：惊世现新(港)/蜘蛛人：惊奇再起(台)/神奇蜘蛛侠/蜘蛛侠4/新蜘蛛侠/蜘蛛侠前传<br />
◎片　　名　The Amazing Spiderman<br />
◎年　　代　2012<br />
◎国　　家　美国<br />
◎类</td>
              </tr>
              <tr>
                <td><a href="/gq/2012-10-22/19196.html" target="_blank">/gq/2012-10-22/19196.html</a></td>
              </tr>
            </table>
			</td>
        </tr>
      </table>
                       
                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">
        <tr> 
          <td><div align="center">
			  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">
                <tr> 
                  
            <td width="41%" height="25"><font color="#663333">・[<a href=/3D/>3D</a>]<span class="blue14"><a href=/3D/2013-02-24/20024.html target=_blank>《超凡蜘蛛侠》左右3D版</a></span></font></td>
                  <td width="59%"><font color="#666666">发布时间：2013-02-24 00:00:00</font></td>
                </tr>
              </table>
            </div></td>
        </tr>
        <tr> 
          <td bgcolor="#EBF3FA"> 
            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">
              <tr> 
                <td> ◎译　　名　超凡蜘蛛侠/蜘蛛侠：惊世现新(港)/蜘蛛人：惊奇再起(台)/神奇蜘蛛侠/蜘蛛侠4/新蜘蛛侠/蜘蛛侠前传<br />
◎片　　名　The Amazing Spiderman<br />
◎年　　代　2012<br />
◎国　　家　美国<br />
◎类</td>
              </tr>
              <tr>
                <td><a href="/3D/2013-02-24/20024.html" target="_blank">/3D/2013-02-24/20024.html</a></td>
              </tr>
            </table>
			</td>
        </tr>
      </table>
                       
                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">
        <tr> 
          <td><div align="center">
			  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">
                <tr> 
                  
            <td width="41%" height="25"><font color="#663333">・[<a href=/gydy/>国语配音电影</a>]<span class="blue14"><a href=/gydy/2012-10-28/19229.html target=_blank>2012动作科幻《超凡蜘蛛侠》BD国语配音中字1024高清</a></span></font></td>
                  <td width="59%"><font color="#666666">发布时间：2012-10-29 01:25:59</font></td>
                </tr>
              </table>
            </div></td>
        </tr>
        <tr> 
          <td bgcolor="#EBF3FA"> 
            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">
              <tr> 
                <td>◎译　　名　超凡蜘蛛侠/蜘蛛侠：惊世现新(港)/蜘蛛人：惊奇再起(台)/神奇蜘蛛侠/蜘蛛侠4/新蜘蛛侠/蜘蛛侠前传<br />
◎片　　名　The Amazing Spiderman<br />
◎年　　代　2012<br />
◎国　　家　美国<br />
◎类</td>
              </tr>
              <tr>
                <td><a href="/gydy/2012-10-28/19229.html" target="_blank">/gydy/2012-10-28/19229.html</a></td>
              </tr>
            </table>
			</td>
        </tr>
      </table>
                       
                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">
        <tr> 
          <td><div align="center">
			  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">
                <tr> 
                  
            <td width="41%" height="25"><font color="#663333">・[<a href=/dy/>2019最新电影</a>]<span class="blue14"><a href=/dy/2012-07-17/18539.html target=_blank><font color='#FF0000'>2012动作科幻大片《超凡蜘蛛侠/蜘蛛侠4》DVD中英双字</font></a></span></font></td>
                  <td width="59%"><font color="#666666">发布时间：2012-10-21 00:23:22</font></td>
                </tr>
              </table>
            </div></td>
        </tr>
        <tr> 
          <td bgcolor="#EBF3FA"> 
            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">
              <tr> 
                <td>◎译　　名　超凡蜘蛛侠/蜘蛛侠：惊世现新(港)/蜘蛛人：惊奇再起(台)/神奇蜘蛛侠/蜘蛛侠4/新蜘蛛侠/蜘蛛侠前传<br />
◎片　　名　The Amazing Spiderman<br />
◎年　　代　2012<br />
◎国　　家　美国<br />
◎类</td>
              </tr>
              <tr>
                <td><a href="/dy/2012-07-17/18539.html" target="_blank">/dy/2012-07-17/18539.html</a></td>
              </tr>
            </table>
			</td>
        </tr>
      </table>
                       
                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">
        <tr> 
          <td><div align="center">
			  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">
                <tr> 
                  
            <td width="41%" height="25"><font color="#663333">・[<a href=/mj/>欧剧.美剧连载</a>]<span class="blue14"><a href=/mj/2012-04-17/17868.html target=_blank>美剧动画《终极蜘蛛侠》第一季15/高清14</a></span></font></td>
                  <td width="59%"><font color="#666666">发布时间：2012-08-02 18:35:43</font></td>
                </tr>
              </table>
            </div></td>
        </tr>
        <tr> 
          <td bgcolor="#EBF3FA"> 
            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">
              <tr> 
                <td>中文片名: 终极蜘蛛侠 第一季<br />
英文片名: Ultimate Spider-Man Season 1<br />
剧集分类: 动画<br />
下载地址：http://www.dy131.com/<br />
在线观看：http://www.kan66.net/<br />
影片类型: 美剧  <br />
上影时间: 2</td>
              </tr>
              <tr>
                <td><a href="/mj/2012-04-17/17868.html" target="_blank">/mj/2012-04-17/17868.html</a></td>
              </tr>
            </table>
			</td>
        </tr>
      </table>
                       
                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">
        <tr> 
          <td><div align="center">
			  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">
                <tr> 
                  
            <td width="41%" height="25"><font color="#663333">・[<a href=/gydy/>国语配音电影</a>]<span class="blue14"><a href=/gydy/2008-03-22/1596.html target=_blank>经典科幻大片《蜘蛛侠3》DVD国语配音</a></span></font></td>
                  <td width="59%"><font color="#666666">发布时间：2011-08-18 14:08:29</font></td>
                </tr>
              </table>
            </div></td>
        </tr>
        <tr> 
          <td bgcolor="#EBF3FA"> 
            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">
              <tr> 
                <td> <br />
◎译　　名　蜘蛛侠3<br />
◎片　　名　Spider-Man 3<br />
◎年　　代　2007<br />
◎国　　家　美国<br />
◎类　　别　动作/冒险/惊悚/科幻<br />
◎语　　言　普通话<br />
◎字　　幕　中文等<br />
◎IMDB评分 6.8/10(77.</td>
              </tr>
              <tr>
                <td><a href="/gydy/2008-03-22/1596.html" target="_blank">/gydy/2008-03-22/1596.html</a></td>
              </tr>
            </table>
			</td>
        </tr>
      </table>
                       
                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">
        <tr> 
          <td><div align="center">
			  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">
                <tr> 
                  
            <td width="41%" height="25"><font color="#663333">・[<a href=/gydy/>国语配音电影</a>]<span class="blue14"><a href=/gydy/2007-12-18/569.html target=_blank>经典科幻大片《蜘蛛侠2》DVD国语配音</a></span></font></td>
                  <td width="59%"><font color="#666666">发布时间：2011-08-18 13:49:58</font></td>
                </tr>
              </table>
            </div></td>
        </tr>
        <tr> 
          <td bgcolor="#EBF3FA"> 
            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">
              <tr> 
                <td>◎译　　名　2<br />
◎片　　名　Spider-Man 2<br />
◎年　　代　2004<br />
◎国　　家　美国<br />
◎类　　别　动作/犯罪/剧情/幻想/爱情/科幻/惊悚<br />
◎语　　言　国语<br />
◎字　　幕　无字幕<br />
◎IMDB评分 7.8/10</td>
              </tr>
              <tr>
                <td><a href="/gydy/2007-12-18/569.html" target="_blank">/gydy/2007-12-18/569.html</a></td>
              </tr>
            </table>
			</td>
        </tr>
      </table>
                       
                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">
        <tr> 
          <td><div align="center">
			  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">
                <tr> 
                  
            <td width="41%" height="25"><font color="#663333">・[<a href=/gydy/>国语配音电影</a>]<span class="blue14"><a href=/gydy/2007-12-18/568.html target=_blank>经典科幻大片《蜘蛛侠1》DVD国语配音</a></span></font></td>
                  <td width="59%"><font color="#666666">发布时间：2011-08-18 13:49:57</font></td>
                </tr>
              </table>
            </div></td>
        </tr>
        <tr> 
          <td bgcolor="#EBF3FA"> 
            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">
              <tr> 
                <td>片 名：蜘蛛侠 Spider-Man (2002) <br />
导 演：萨姆&amp;middot;莱米 Sam Raimi <br />
主 演：威廉&amp;middot;达福 Willem Dafoe <br />
柯尔斯滕&amp;middot;邓斯特 Kirsten Dunst <br />
托比&amp;middot;马圭尔 Tobey Maguire</td>
              </tr>
              <tr>
                <td><a href="/gydy/2007-12-18/568.html" target="_blank">/gydy/2007-12-18/568.html</a></td>
              </tr>
            </table>
			</td>
        </tr>
      </table>
                       
                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">
        <tr> 
          <td><div align="center">
			  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">
                <tr> 
                  
            <td width="41%" height="25"><font color="#663333">・[<a href=/yx/>单机游戏</a>]<span class="blue14"><a href=/yx/2011-04-16/14602.html target=_blank>[蜘蛛侠：破碎维度][免安装中文汉化硬盘版]</a></span></font></td>
                  <td width="59%"><font color="#666666">发布时间：2011-04-16 21:15:52</font></td>
                </tr>
              </table>
            </div></td>
        </tr>
        <tr> 
          <td bgcolor="#EBF3FA"> 
            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">
              <tr> 
                <td>游戏名称：Spider-Man: Shattered Dimensions<br />
中文名称：蜘蛛侠：破碎维度<br />
游戏发行：Activision<br />
游戏制作：Beenox<br />
游戏语种：简体中文<br />
游戏类型：动作<br />
发行日期：2010年12月30日<br />
<br />
【安</td>
              </tr>
              <tr>
                <td><a href="/yx/2011-04-16/14602.html" target="_blank">/yx/2011-04-16/14602.html</a></td>
              </tr>
            </table>
			</td>
        </tr>
      </table>
                       </td>
                  </tr>
                  <tr> 
                    <td height="100%" valign="top"> <div align="center"><a title="总数">&nbsp;<b>21</b> </a>&nbsp;&nbsp;&nbsp;<b>1</b>&nbsp;<a href="/e/search/result/index.php?page=1&amp;searchid=218987">2</a>&nbsp;<a href="/e/search/result/index.php?page=1&amp;searchid=218987">下一页</a>&nbsp;<a href="/e/search/result/index.php?page=1&amp;searchid=218987">尾页</a></div></td>
                  </tr>
                  <tr> 
                    <td height="12" valign="top"></td>
                  </tr>  
</div>
</div>

<div id="footer">
	<p class="t"><a href="/index.html">网站留言</a> - <a href="/index.html">关于我们</a> - <a href="/index.html">广告业务</a> - <a href="/index.html">信息反馈</a> - <a href="/index.html">合作伙伴</a> - <a href="/index.html">网站地图</a></p>
	<p>Copyright &copy; 2009 <a href="http://www.hao6v.com"><b><font color=red>6VHAO</font>.COM</b></a> 版权所有<br />
	  渝ICP备09051310号
</div>
<span class="hidden"><script src=/d/tj.js></script></span>
"""

# html = etree.HTML(s)
# mov = html.xpath("//table//font[1]/a")
# # for movie in movie_list:
# #     print(movie.text)
# for movies in mov:
#     if "电影" in movies.text or "3D" in movies.text:
#         movie_list = movies.xpath("../span/a")
#         # movie_list = html.xpath("//table//font/span/a")
#         for index,movie in enumerate(movie_list):
#             href = movie.xpath("./@href")[0]
#             if movie.text is None:
#                 movie = movie.xpath("./font")[0]
#             if "蜘蛛侠" in movie.text:
#                 print("[{}]".format(movies.text) + movie.text)
#                 print(href)
# response = requests.get(
#     "http://so.hao6v.com/dy/2019-09-12/ZZXYXYZ.html",
#     headers={
#             "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
#             "Content-Type":"application/x-www-form-urlencoded",
#         },
# ).content

# res  = b'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\r\n<html xmlns="http://www.w3.org/1999/xhtml">\r\n<head>\r\n<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />\r\n<title>2019\xb8\xdf\xb7\xd6\xbf\xc6\xbb\xc3\xa1\xb6\xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xd3\xa2\xd0\xdb\xd4\xb6\xd5\xf7\xa1\xb71080p.\xb9\xfa\xd3\xa2\xcb\xab\xd3\xef.BD\xd6\xd0\xd3\xa2\xcb\xab\xd7\xd6\xa3\xac\xc3\xe2\xb7\xd1\xcf\xc2\xd4\xd8\xa3\xac\xd1\xb8\xc0\xd7\xcf\xc2\xd4\xd8\xa3\xac2019\xd7\xee\xd0\xc2\xb5\xe7\xd3\xb0\xa3\xac6v\xb5\xe7\xd3\xb0\xcf\xc2\xd4\xd8\xcd\xf8</title>\r\n<meta name="keywords" content="2019\xb8\xdf\xb7\xd6\xbf\xc6\xbb\xc3\xa1\xb6\xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xd3\xa2\xd0\xdb\xd4\xb6\xd5\xf7\xa1\xb71080p.\xb9\xfa\xd3\xa2\xcb\xab\xd3\xef.BD\xd6\xd0\xd3\xa2\xcb\xab\xd7\xd6\xcf\xc2\xd4\xd8\xa3\xac2019\xb8\xdf\xb7\xd6\xbf\xc6\xbb\xc3\xa1\xb6\xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xd3\xa2\xd0\xdb\xd4\xb6\xd5\xf7\xa1\xb71080p.\xb9\xfa\xd3\xa2\xcb\xab\xd3\xef.BD\xd6\xd0\xd3\xa2\xcb\xab\xd7\xd6\xd1\xb8\xc0\xd7\xcf\xc2\xd4\xd8" />\r\n<meta name="description" content="\xa1\xf2\xd2\xeb\xa1\xa1\xa1\xa1\xc3\xfb\xa1\xa1\xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xd3\xa2\xd0\xdb\xd4\xb6\xd5\xf7 / \xd0\xc2\xd6\xa9\xd6\xeb\xcf\xc02 / \xd6\xa9\xd6\xeb\xcf\xc02 / \xd6\xa9\xd6\xeb\xcf\xc02\xa3\xba\xc0\xeb\xbc\xd2\xb3\xf6\xd7\xdf(\xb6\xb9\xd3\xd1\xd2\xeb\xc3\xfb) / \xd6\xa9\xd6\xeb\xcf\xc02\xa3\xba\xd3\xa2\xd0\xdb\xc0\xeb\xcf\xe7 / \xd6\xa9\xd6\xeb\xcf\xc02\xa3\xba\xd4\xb6\xc0\xeb\xbc\xd2\xcf\xe7 / \xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xbe\xf6\xd5\xbd\xc7\xa7\xc0\xef(\xb8\xdb) / \xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xb9\xe9\xc0\xb42 / \xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xc0\xeb\xbc\xd2\xc8\xd5(\xcc\xa8) / \xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xd3\xa2\xd0\xdb\xb9\xe9\xc0\xb42 / \xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xd4\xb6\xc0\xeb\xb9\xca\xcf\xe7<br />\r\n\xa1\xf2\xc6\xac\xa1\xa1\xa1\xa1\xc3\xfb\xa1\xa1Spider-Man: Far from Home<br />\r\n\xa1\xf2\xc4\xea\xa1\xa1\xa1\xa1\xb4\xfa\xa1\xa12019<br />\r\n\xa1\xf2\xb2\xfa\xa1\xa1\xa1\xa1\xb5\xd8\xa1\xa1\xc3\xc0\xb9\xfa<br />\r\n\xa1\xf2\xc0\xe0\xa1\xa1\xa1\xa1\xb1\xf0\xa1\xa1\xb6\xaf\xd7\xf7 / \xbf\xc6\xbb\xc3 / \xc3\xb0\xcf\xd5<br />\r\n\xa1\xf2\xd3\xef\xa1\xa1\xa1\xa1\xd1\xd4\xa1\xa1\xb9\xfa\xd3\xa2\xcb\xab\xd3\xef<br />\r\n\xa1\xf2\xd7\xd6\xa1\xa1\xa1\xa1\xc4\xbb\xa1\xa1\xd6\xd0\xd7\xd6<br />\r\n\xa1\xf2\xc9\xcf\xd3\xb3\xc8\xd5\xc6\xda\xa1\xa12019-06-28(\xd6\xd0\xb9\xfa\xb4\xf3\xc2\xbd) / 2019-07-02(\xc3\xc0\xb9\xfa)<br />\r\n\xa1\xf2IMDb\xc6\xc0\xb7\xd6  7.9/10 from 161425 users<br />\r\n\xa1\xf2\xb6\xb9\xb0\xea\xc6\xc0\xb7\xd6\xa1\xa17.9/10 from 346048 users<br />\r\n\xa1\xf2\xc6\xac\xa1\xa1\xa1\xa1\xb3\xa4\xa1\xa1127\xb7\xd6\xd6\xd3<br />\r\n\xa1\xf2\xb5\xbc\xa1\xa1\xa1\xa1\xd1\xdd\xa1\xa1\xc7\xc7&amp;middot;\xce\xd6\xb4\xc4 Jon Watts<br />\r\n\xa1\xf2\xb1\xe0\xa1\xa1\xa1\xa1\xbe\xe7\xa1\xa1\xbf\xcb\xc0\xef\xcb\xb9&amp;middot;\xc2\xf3\xbf\xcb\xc4\xc9 Chris McKenna / \xb0\xa3\xc0\xef\xbf\xcb&amp;middot;\xc8\xf8\xc4\xac\xcb\xb9 Erik Sommers / \xca\xb7\xb5\xd9\xb7\xf2&amp;middot;\xb5\xcf\xcc\xd8\xbf\xdc Steve Ditko / \xcb\xb9\xcc\xb9&amp;middot;\xc0\xee Stan Lee<br />\r\n\xa1\xf2\xd6\xf7\xa1\xa1\xa1\xa1\xd1\xdd\xa1\xa1\xcc\xc0\xc4\xb7&amp;middot;\xba\xd5\xc0\xbc\xb5\xc2 Tom Holland<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1  \xd4\xde\xb4\xef\xd1\xc7 Zendaya<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1  \xbd\xdc\xbf\xcb&amp;middot;\xbc\xaa\xc2\xd7\xb9\xfe\xb6\xfb Jake Gyllenhaal<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1  \xbf\xdc\xb1\xcc&amp;middot;\xca\xb7\xc4\xaa\xb5\xc2\xcb\xb9 Cobie Smulders<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1  \xc8\xfb\xe7\xd1\xb6\xfb&amp;middot;\xbd\xdc\xbf\xcb\xd1\xb7 Samuel L. Jackson<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1  \xc7\xc7\xb6\xf7&amp;middot;\xb7\xd1\xc8\xe5 Jon Favreau<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1  \xc2\xea\xc0\xf6\xc9\xaf&amp;middot;\xcd\xd0\xc3\xb7 Mar" />\r\n<link rel="stylesheet" rev="stylesheet" href="/images/style.css" type="text/css" />\r\n<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7" />\r\n</head>\r\n<body>\r\n\t<div id="header"><div id="top">  <a href="https://app.pp63.org/\xbf\xec\xbf\xb4.apk" target=_blank>APP\xb0\xb2\xd7\xbf\xb0\xe6</a>&nbsp;&nbsp;\r\n<a href="http://www.hao6v.com/dy/2012-12-07/19512.html" target=_blank>\xb9\xab\xb8\xe6\xc7\xf8</a>&nbsp;&nbsp;<a href="http://www.hao6v.com/dy/2019-01-02/32524.html" target="_blank">\xb6\xb9\xb0\xea2018\xb0\xf1\xb5\xa5</a>&nbsp;&nbsp;\r\n<a href="http://www.hao6v.com/gq/2012-09-01/18841.html" target=_blank><font color=\'#FF0000\'>6v\xb5\xe7\xd3\xb0\xc5\xc5\xd0\xd0\xb0\xf1</font></a>&nbsp;&nbsp;\r\n<a href="http://www.hao6v.com/dy/2011-09-20/16090.html" target=_blank>\xb1\xb1\xc3\xc0\xc6\xb1\xb7\xbf\xc5\xc5\xd0\xd0\xb0\xf1</a>&nbsp;&nbsp;\r\n<a href="http://www.hao6v.com/s/007/" target=_blank>007\xb5\xe7\xd3\xb0\xc8\xab\xbc\xaf</a>&nbsp;&nbsp;\r\n<a href="http://www.hao6v.com/s/gf250/" target=_blank>IMDB250\xb5\xe7\xd3\xb0</a>&nbsp;&nbsp;\r\n<a href="/s/gf/" target=_blank>\xb8\xdf\xc6\xc0\xb7\xd6\xb5\xe7\xd3\xb0</a>&nbsp;&nbsp;\r\n<a href="/s/hanguodianying/" target=_blank>\xc3\xc0\xb9\xfa\xb5\xe7\xd3\xb0</a>&nbsp;&nbsp;<a href="/s/xijudianying/" target=_blank>\xc5\xb7\xd6\xde\xb5\xe7\xd3\xb0</a>&nbsp;&nbsp;<a href="/s/yazhoudianying/" target=_blank>\xd1\xc7\xd6\xde\xb5\xe7\xd3\xb0</a>&nbsp;&nbsp;<a href="/s/mzdy/" target=_blank>\xc3\xc0\xd6\xde\xb5\xe7\xd3\xb0</a> &nbsp;<a href="http://www.hao6v.com/e/tool/gbook/?bid=1" target=_blank>\xb7\xc3\xbf\xcd\xc1\xf4\xd1\xd4</a></div>\r\n    \t<div class="log"><a href="/">6V\xb5\xe7\xd3\xb0</a></div>\r\n        <div class="topad"><script src="/d/f4.js"></script></div>\r\n<div class="cr"></div>\r\n        <div id="menu">\r\n      <p><a href="http://www.hao6v.com/">\xca\xd7\xd2\xb3</a>  <a href="http://www.hao6v.com/dy/" target=_blank>2019\xd7\xee\xd0\xc2\xb5\xe7\xd3\xb0</a> <a href="http://www.hao6v.com/gydy/" target=_blank>\xb9\xfa\xd3\xef\xc5\xe4\xd2\xf4\xb5\xe7\xd3\xb0</a> <a href="http://www.hao6v.com/zydy/" target=_blank>\xce\xa2\xb5\xe7\xd3\xb0</a> <a href="http://www.hao6v.com/gq/" target=_blank>\xbe\xad\xb5\xe4\xb8\xdf\xc7\xe5\xb5\xe7\xd3\xb0</a> <a href="http://www.hao6v.com/jddy/" target=_blank>\xb6\xaf\xbb\xad\xb5\xe7\xd3\xb0</a> <a href="http://www.hao6v.com/3D/" target=_blank>3D\xb5\xe7\xd3\xb0</a> <a href="http://www.hao6v.com/s/shoujiMP4dianying/" target=_blank>MP4\xca\xd6\xbb\xfa\xb5\xe7\xd3\xb0</a> <a href="http://www.hao6v.com/dlz/" target=_blank>\xb9\xfa\xbe\xe7</a> <a href="http://www.hao6v.com/rj/" target=_blank>\xc8\xd5\xba\xab\xbe\xe7</a> <a href="http://www.hao6v.com/mj/" target=_blank>\xc5\xb7\xc3\xc0\xbe\xe7</a> <a href="http://www.hao6v.com/zy/" target=_blank>\xd7\xdb\xd2\xd5\xbd\xda\xc4\xbf</a> <a href="http://www.hao6v.com/s/gangtaidianying/" target=_blank>\xb8\xdb\xcc\xa8\xb5\xe7\xd3\xb0</a> <a href="http://www.hao6v.com/s/jingdiandianying/" target=_blank>\xc8\xd5\xba\xab\xb5\xe7\xd3\xb0</a> </p>\r\n      <p class="bg"><a href="http://www.66e.cc/" target=_blank>66\xd3\xb0\xca\xd3\xcd\xf8</a> \xd7\xa8\xcc\xe2\xb7\xd6\xc0\xe0\xa3\xba<a href="http://www.hao6v.com/s/xiju/" target=_blank>\xcf\xb2\xbe\xe7</a><a href="http://www.hao6v.com/s/dongzuo/" target=_blank>\xb6\xaf\xd7\xf7</a><a href="http://www.hao6v.com/s/aiqing/" target=_blank>\xb0\xae\xc7\xe9</a><a href="http://www.hao6v.com/s/kehuan/" target=_blank>\xbf\xc6\xbb\xc3</a><a href="http://www.hao6v.com/s/qihuan/" target=_blank>\xc6\xe6\xbb\xc3</a><a href="http://www.hao6v.com/s/shenmi/" target=_blank>\xc9\xf1\xc3\xd8</a><a href="http://www.hao6v.com/s/huanxiang/" target=_blank>\xbb\xc3\xcf\xeb</a><a href="http://www.hao6v.com/s/kongbu/" target=_blank>\xbf\xd6\xb2\xc0</a><a href="http://www.hao6v.com/s/zhanzheng/" target=_blank>\xd5\xbd\xd5\xf9</a><a href="http://www.hao6v.com/s/maoxian/" target=_blank>\xc3\xb0\xcf\xd5</a><a href="http://www.hao6v.com/s/jingsong/" target=_blank>\xbe\xaa\xe3\xa4</a><a href="http://www.hao6v.com/s/juqingpian/" target=_blank>\xbe\xe7\xc7\xe9</a><a href="http://www.hao6v.com/s/zhuanji/" target=_blank>\xb4\xab\xbc\xc7</a><a href="http://www.hao6v.com/s/lishi/" target=_blank>\xc0\xfa\xca\xb7</a><a href="http://www.hao6v.com/s/jilu/" target=_blank>\xbc\xcd\xc2\xbc</a><a href="http://www.hao6v.com/s/yindudianying/" target=_blank>\xd3\xa1\xb6\xc8\xb5\xe7\xd3\xb0</a>  <a href="http://www.hao6v.com/s/guochandianying/" target=_blank>\xb9\xfa\xb2\xfa\xb5\xe7\xd3\xb0</a> <a href="http://www.hao6v.com/s/xijudianying/" target=_blank>\xc5\xb7\xd6\xde\xb5\xe7\xd3\xb0</a> <a href="http://www.hao6v.com/s/zhuanti/" target=_blank>\xd7\xa8\xcc\xe2\xcd\xc6\xbc\xf6</a> </p>\r\n        </div>\r\n  </div>\r\n\r\n<div id="a960"><script src="/d/f1.js"></script> <script src="/d/f2.js"></script></div>\r\n<div id="search">\r\n<div class="ser">\r\n<form action="http://so.hao6v.com/e/search/index.php" method="post" name="searchform" id="searchform">\r\n<input type="hidden" name="show" value="title,smalltext" />\r\n<input type="hidden" name="tempid" value="1" />\r\n\r\n<span>\xd5\xbe\xc4\xda\xcb\xd1\xcb\xf7\xa3\xba<input name="keyboard" type="text" size="32" id="keyboard" class="inputText" /></span>\r\n<span class="sect"><select name="tbname">\r\n<option value="article">\xc8\xab\xd5\xbe</option>\r\n</select></span>\r\n<span><input type="image" class="inputSub" src="/images/search.gif" /></span>\r\n</form>\r\n</span>\r\n</div>\r\n<div class="help">\r\n<a href="http://www.hao6v.com/dy/2010-10-11/12868.html" target="_blank">6v\xb5\xe7\xd3\xb0\xcf\xc2\xd4\xd8\xb0\xef\xd6\xfa\xd3\xeb\xbd\xcc\xb3\xcc<br /><font color=\'#FF0000\'>\xce\xde\xb7\xa8\xcf\xc2\xd4\xd8\xb5\xc4\xbd\xf8\xc0\xb4\xbf\xb4\xbf\xb4</font></a>\r\n</div>\r\n<INPUT type="button" value=\'\xca\xd5\xb2\xd8\xb1\xbe\xd3\xb0\xc6\xac\' id="copy" onclick="javascript:d=document;window.external.AddFavorite(\'\'+d.location.href+\'\', \'\'+d.title+\'\')">\r\n<div class="help"><div class="bdsharebuttonbox"><a href="#" class="bds_more" data-cmd="more"></a><a href="#" class="bds_bdhome" data-cmd="bdhome" title="\xb7\xd6\xcf\xed\xb5\xbd\xb0\xd9\xb6\xc8\xd0\xc2\xca\xd7\xd2\xb3"></a><a href="#" class="bds_sqq" data-cmd="sqq" title="\xb7\xd6\xcf\xed\xb5\xbdQQ\xba\xc3\xd3\xd1"></a><a href="#" class="bds_weixin" data-cmd="weixin" title="\xb7\xd6\xcf\xed\xb5\xbd\xce\xa2\xd0\xc5"></a><a href="#" class="bds_douban" data-cmd="douban" title="\xb7\xd6\xcf\xed\xb5\xbd\xb6\xb9\xb0\xea\xcd\xf8"></a><a href="#" class="bds_mshare" data-cmd="mshare" title="\xb7\xd6\xcf\xed\xb5\xbd\xd2\xbb\xbc\xfc\xb7\xd6\xcf\xed"></a><a href="#" class="bds_qzone" data-cmd="qzone" title="\xb7\xd6\xcf\xed\xb5\xbdQQ\xbf\xd5\xbc\xe4"></a><a href="#" class="bds_tsina" data-cmd="tsina" title="\xb7\xd6\xcf\xed\xb5\xbd\xd0\xc2\xc0\xcb\xce\xa2\xb2\xa9"></a><a href="#" class="bds_tieba" data-cmd="tieba" title="\xb7\xd6\xcf\xed\xb5\xbd\xb0\xd9\xb6\xc8\xcc\xf9\xb0\xc9"></a><a href="#" class="bds_tqq" data-cmd="tqq" title="\xb7\xd6\xcf\xed\xb5\xbd\xcc\xda\xd1\xb6\xce\xa2\xb2\xa9"></a></div>\r\n<script>window._bd_share_config={"common":{"bdSnsKey":{},"bdText":"","bdMini":"1","bdMiniList":false,"bdPic":"","bdStyle":"0","bdSize":"16"},"share":{}};with(document)0[(getElementsByTagName(\'head\')[0]||body).appendChild(createElement(\'script\')).src=\'http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion=\'+~(-new Date()/36e5)];</script></div></div>\r\n<div id="main">\r\n\t<div class="col6">\r\n    \t<div class="box">\r\n        \t<div class="t">\xc4\xfa\xb5\xc4\xce\xbb\xd6\xc3\xa3\xba<a href="/index.html">\xca\xd7\xd2\xb3</a>&nbsp;>&nbsp;<a href="/dy/">2019\xd7\xee\xd0\xc2\xb5\xe7\xd3\xb0</a> > \xcf\xc2\xd4\xd8\xd2\xb3\xc3\xe6</div>\r\n            \t<h1>2019\xb8\xdf\xb7\xd6\xbf\xc6\xbb\xc3\xa1\xb6\xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xd3\xa2\xd0\xdb\xd4\xb6\xd5\xf7\xa1\xb71080p.\xb9\xfa\xd3\xa2\xcb\xab\xd3\xef.BD\xd6\xd0\xd3\xa2\xcb\xab\xd7\xd6</h1>\r\n\r\n<div id="endText"><div class="fl"><script type="text/javascript" src="http://www.hao6v.com/d/gg3001.js"></script></div><div class="fr"><script type="text/javascript" src="http://www.hao6v.com/d/js/acmsd/thea3.js"></script></div><div class="cr"></div><br />\r\n<strong><a href="/dy/2019-09-12/ZZXYXYZ.html">2019\xb8\xdf\xb7\xd6\xbf\xc6\xbb\xc3\xa1\xb6\xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xd3\xa2\xd0\xdb\xd4\xb6\xd5\xf7\xa1\xb71080p.\xb9\xfa\xd3\xa2\xcb\xab\xd3\xef.BD\xd6\xd0\xd3\xa2\xcb\xab\xd7\xd6</a> - \xc4\xda\xc8\xdd\xbd\xe9\xc9\xdc\xa3\xba</strong>\r\n<p><img alt="" src="https://tu.66vod.net/2019/3807.jpg" /></p>\r\n<p>\xa1\xf2\xd2\xeb\xa1\xa1\xa1\xa1\xc3\xfb\xa1\xa1\xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xd3\xa2\xd0\xdb\xd4\xb6\xd5\xf7 / \xd0\xc2\xd6\xa9\xd6\xeb\xcf\xc02 / \xd6\xa9\xd6\xeb\xcf\xc02 / \xd6\xa9\xd6\xeb\xcf\xc02\xa3\xba\xc0\xeb\xbc\xd2\xb3\xf6\xd7\xdf(\xb6\xb9\xd3\xd1\xd2\xeb\xc3\xfb) / \xd6\xa9\xd6\xeb\xcf\xc02\xa3\xba\xd3\xa2\xd0\xdb\xc0\xeb\xcf\xe7 / \xd6\xa9\xd6\xeb\xcf\xc02\xa3\xba\xd4\xb6\xc0\xeb\xbc\xd2\xcf\xe7 / \xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xbe\xf6\xd5\xbd\xc7\xa7\xc0\xef(\xb8\xdb) / \xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xb9\xe9\xc0\xb42 / \xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xc0\xeb\xbc\xd2\xc8\xd5(\xcc\xa8) / \xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xd3\xa2\xd0\xdb\xb9\xe9\xc0\xb42 / \xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xd4\xb6\xc0\xeb\xb9\xca\xcf\xe7<br />\r\n\xa1\xf2\xc6\xac\xa1\xa1\xa1\xa1\xc3\xfb\xa1\xa1Spider-Man: Far from Home<br />\r\n\xa1\xf2\xc4\xea\xa1\xa1\xa1\xa1\xb4\xfa\xa1\xa12019<br />\r\n\xa1\xf2\xb2\xfa\xa1\xa1\xa1\xa1\xb5\xd8\xa1\xa1<a href="http://www.hao6v.com/s/hanguodianying/" target="_blank"  title="\xc3\xc0\xb9\xfa\xb5\xe7\xd3\xb0">\xc3\xc0\xb9\xfa</a><br />\r\n\xa1\xf2\xc0\xe0\xa1\xa1\xa1\xa1\xb1\xf0\xa1\xa1<a href="http://www.hao6v.com/s/dongzuo/" target="_blank"  title="\xb6\xaf\xd7\xf7\xc6\xac">\xb6\xaf\xd7\xf7</a> / <a href="http://www.hao6v.com/s/kehuan/" target="_blank"  title="\xbf\xc6\xbb\xc3\xc6\xac">\xbf\xc6\xbb\xc3</a> / <a href="http://www.hao6v.com/s/maoxian/" target="_blank"  title="\xc3\xb0\xcf\xd5\xc6\xac">\xc3\xb0\xcf\xd5</a><br />\r\n\xa1\xf2\xd3\xef\xa1\xa1\xa1\xa1\xd1\xd4\xa1\xa1\xb9\xfa\xd3\xa2\xcb\xab\xd3\xef<br />\r\n\xa1\xf2\xd7\xd6\xa1\xa1\xa1\xa1\xc4\xbb\xa1\xa1\xd6\xd0\xd7\xd6<br />\r\n\xa1\xf2\xc9\xcf\xd3\xb3\xc8\xd5\xc6\xda\xa1\xa12019-06-28(<a href="http://www.hao6v.com/s/guochandianying/" target="_blank"  title="\xb9\xfa\xb2\xfa\xb5\xe7\xd3\xb0">\xd6\xd0\xb9\xfa</a>\xb4\xf3\xc2\xbd) / 2019-07-02(<a href="http://www.hao6v.com/s/hanguodianying/" target="_blank"  title="\xc3\xc0\xb9\xfa\xb5\xe7\xd3\xb0">\xc3\xc0\xb9\xfa</a>)<br />\r\n\xa1\xf2IMDb\xc6\xc0\xb7\xd6&nbsp; 7.9/10 from 161425 users<br />\r\n\xa1\xf2\xb6\xb9\xb0\xea\xc6\xc0\xb7\xd6\xa1\xa17.9/10 from 346048 users<br />\r\n\xa1\xf2\xc6\xac\xa1\xa1\xa1\xa1\xb3\xa4\xa1\xa1127\xb7\xd6\xd6\xd3<br />\r\n\xa1\xf2\xb5\xbc\xa1\xa1\xa1\xa1\xd1\xdd\xa1\xa1\xc7\xc7&middot;\xce\xd6\xb4\xc4 Jon Watts<br />\r\n\xa1\xf2\xb1\xe0\xa1\xa1\xa1\xa1\xbe\xe7\xa1\xa1\xbf\xcb\xc0\xef\xcb\xb9&middot;\xc2\xf3\xbf\xcb\xc4\xc9 Chris McKenna / \xb0\xa3\xc0\xef\xbf\xcb&middot;\xc8\xf8\xc4\xac\xcb\xb9 Erik Sommers / \xca\xb7\xb5\xd9\xb7\xf2&middot;\xb5\xcf\xcc\xd8\xbf\xdc Steve Ditko / \xcb\xb9\xcc\xb9&middot;\xc0\xee Stan Lee<br />\r\n\xa1\xf2\xd6\xf7\xa1\xa1\xa1\xa1\xd1\xdd\xa1\xa1\xcc\xc0\xc4\xb7&middot;\xba\xd5\xc0\xbc\xb5\xc2 Tom Holland<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1&nbsp; \xd4\xde\xb4\xef\xd1\xc7 Zendaya<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1&nbsp; \xbd\xdc\xbf\xcb&middot;\xbc\xaa\xc2\xd7\xb9\xfe\xb6\xfb Jake Gyllenhaal<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1&nbsp; \xbf\xdc\xb1\xcc&middot;\xca\xb7\xc4\xaa\xb5\xc2\xcb\xb9 Cobie Smulders<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1&nbsp; \xc8\xfb\xe7\xd1\xb6\xfb&middot;\xbd\xdc\xbf\xcb\xd1\xb7 Samuel L. Jackson<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1&nbsp; \xc7\xc7\xb6\xf7&middot;\xb7\xd1\xc8\xe5 Jon Favreau<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1&nbsp; \xc2\xea\xc0\xf6\xc9\xaf&middot;\xcd\xd0\xc3\xb7 Marisa Tomei<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1&nbsp; \xd1\xc5\xb8\xf7\xb2\xbc&middot;\xb0\xcd\xcc\xd8\xc0\xca Jacob Batalon<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1&nbsp; \xb0\xb2\xb8\xf1\xc8\xf0&middot;\xc0\xb5\xcb\xb9 Angourie Rice<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1&nbsp; \xc2\xed\xb6\xa1&middot;\xcb\xb9\xcb\xfe\xb6\xfb Martin Starr<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1&nbsp; \xc8\xf0\xc3\xd7&middot;\xba\xa3\xd2\xc0 Remy Hii<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1&nbsp; \xc5\xa6\xc2\xfc&middot;\xb0\xa2\xbf\xa8 Numan Acar<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1&nbsp; \xcd\xd0\xc4\xe1&middot;\xc0\xd7\xce\xd6\xc2\xde\xc0\xfb Tony Revolori<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1&nbsp; J&middot;B&middot;\xcb\xb9\xc4\xc2\xb7\xf2 J.B. Smoove<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1&nbsp; \xba\xd5\xc3\xd7\xbb\xf9&middot;\xc2\xed\xb5\xc2\xc0\xad Hemky Madera<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1&nbsp; \xb4\xf7\xce\xac\xc4\xc8&middot;\xce\xf7\xcb\xfe\xc0\xad\xc4\xb7 Davina Sitaram<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1&nbsp; \xd4\xbc\xc9\xaa\xb7\xf2&middot;\xc0\xca Joseph Long<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1&nbsp; \xc2\xb6\xcb\xbf&middot;\xbb\xf4\xc2\xe5\xbf\xcb\xcb\xb9 Ruth Horrocks<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1&nbsp; \xb9\xfe\xcd\xa2&middot;\xc5\xc1\xcc\xd8\xb6\xfb Hiten Patel<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1&nbsp; \xbd\xdc\xc2\xde\xb6\xf7&middot;\xb7\xb2&middot;\xbf\xb5\xc4\xfe\xcb\xb9\xb2\xae\xb8\xf1 Jeroen van Koningsbrugge<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1&nbsp; Leonys Delossantos<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1&nbsp; \xb2\xe9\xc0\xfb&middot;\xc0\xd9\xe6\xab&middot;\xb0\xa3\xcb\xb9\xbf\xfc\xb6\xfb Charlie Rhea Esqu&eacute;r<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1&nbsp; \xb7\xd1\xcb\xb9&middot;\xc2\xe5\xb8\xf9 Faith Logan<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1&nbsp; J&middot;K&middot;\xce\xf7\xc3\xc9\xcb\xb9 J.K. Simmons<br />\r\n\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1&nbsp; \xd0\xa1\xc2\xde\xb2\xae\xcc\xd8&middot;\xcc\xc6\xc4\xe1 Robert Downey Jr.</p>\r\n<p>\xa1\xf2\xbc\xf2\xa1\xa1\xa1\xa1\xbd\xe9&nbsp;</p>\r\n<p>\xa1\xa1\xa1\xa1\xd4\xda\xb8\xb4\xb3\xf0\xd5\xdf\xc1\xaa\xc3\xcb\xd6\xda\xd3\xa2\xd0\xdb\xb5\xc4\xc5\xac\xc1\xa6\xcf\xc2\xa3\xac\xd3\xda\xc3\xf0\xb0\xd4\xce\xde\xcf\xde\xca\xd6\xcc\xd7\xca\xc2\xbc\xfe\xd6\xd0\xbb\xaf\xd7\xf7\xce\xaa\xbb\xd2\xbd\xfd\xb5\xc4\xc8\xcb\xc3\xc7\xa3\xac\xd6\xd8\xd0\xc2\xbb\xd8\xb5\xbd\xc1\xcb\xc8\xcb\xca\xc0\xbc\xe4\xa3\xac\xd4\xf8\xbe\xad\xcf\xfb\xca\xa7\xb5\xc4\xd6\xa9\xd6\xeb\xcf\xc0 \xb1\xcb\xb5\xc3\xc5\xc1\xbf\xcb \xd2\xb2\xbb\xd8\xb9\xe9\xb5\xbd\xc1\xcb\xc6\xd5\xcd\xa8\xb5\xc4\xc9\xfa\xbb\xee\xd6\xae\xd6\xd0\xa3\xac\xca\xfd\xd4\xc2\xba\xf3\xa3\xac\xd6\xa9\xd6\xeb\xcf\xc0\xb1\xcb\xb5\xc3\xc5\xc1\xbf\xcb\xcb\xf9\xd4\xda\xb5\xc4\xd1\xa7\xd0\xa3\xbe\xd9\xd0\xd0\xc1\xcb\xc5\xb7\xd6\xde\xc2\xc3\xd3\xce\xa3\xac\xc5\xc1\xbf\xcb\xd2\xb2\xd4\xda\xc6\xe4\xd6\xd0\xa3\xac \xd4\xda\xc5\xb7\xd6\xdd\xcd\xfe\xc4\xe1\xcb\xb9\xc2\xc3\xd0\xd0\xca\xb1\xa3\xac\xd2\xbb\xb8\xf6\xbe\xde\xb4\xf3\xce\xde\xb1\xc8\xb5\xc4\xcb\xae\xb9\xd6\xcf\xae\xbb\xf7\xc1\xcb\xcd\xfe\xc4\xe1\xcb\xb9\xa3\xac\xb2\xbb\xb5\xd0\xb5\xd0\xc8\xcb\xb5\xc4\xd6\xa9\xd6\xeb\xcf\xc0\xd0\xd2\xb5\xc3\xd2\xbb\xce\xbb\xd7\xd4\xb3\xc6<a href="http://www.hao6v.com/s/shenmi/" target="_blank"  title="\xc9\xf1\xc3\xd8\xc6\xac">\xc9\xf1\xc3\xd8</a>\xbf\xcd\xb5\xc4\xc4\xd0\xd7\xd3\xb4\xee\xbe\xc8\xb2\xc5\xbb\xf7\xcd\xcb\xb5\xd0\xc8\xcb\xa3\xac\xd6\xae\xba\xf3 \xc9\xf1\xb6\xdc\xbe\xd6\xbe\xd6\xb3\xa4\xd5\xd2\xc9\xcf\xd5\xfd\xd4\xda\xc2\xc3\xd3\xce\xb5\xc4\xb1\xcb\xb5\xc3\xc5\xc1\xbf\xcb\xb2\xa2\xd2\xaa\xc7\xf3\xc6\xe4\xbc\xd3\xc8\xeb\xc9\xf1\xb6\xdc\xbe\xd6\xa3\xac\xb2\xa2\xb0\xb2\xc5\xc5<a href="http://www.hao6v.com/s/shenmi/" target="_blank"  title="\xc9\xf1\xc3\xd8\xc6\xac">\xc9\xf1\xc3\xd8</a>\xbf\xcd\xd0\xad\xd6\xfa\xc5\xc1\xbf\xcb\xa3\xac<a href="http://www.hao6v.com/s/shenmi/" target="_blank"  title="\xc9\xf1\xc3\xd8\xc6\xac">\xc9\xf1\xc3\xd8</a>\xbf\xcd\xd7\xd4\xb3\xc6\xc0\xb4\xd7\xd4\xc6\xe4\xcb\xfb\xd3\xee\xd6\xe6\xa3\xac\xb2\xa2\xb8\xe6\xd6\xaa\xd2\xbb\xc8\xba\xc3\xfb\xce\xaa\xd4\xaa\xcb\xd8\xd6\xda\xb5\xc4\xd0\xb0\xb6\xf1\xca\xc6\xc1\xa6\xd2\xd1\xbe\xad\xc8\xeb\xc7\xd6\xd5\xe2\xb8\xf6\xd3\xee\xd6\xe6\xc1\xcb\xa3\xac\xce\xaa\xc1\xcb\xca\xd8\xbb\xa4\xc0\xb4\xd6\xae\xb2\xbb\xd2\xd7\xb5\xc4\xba\xcd\xc6\xbd\xa3\xac\xd6\xa9\xd6\xeb\xcf\xc0\xbe\xf6\xb6\xa8\xd3\xeb<a href="http://www.hao6v.com/s/shenmi/" target="_blank"  title="\xc9\xf1\xc3\xd8\xc6\xac">\xc9\xf1\xc3\xd8</a>\xbf\xcd\xc1\xaa\xca\xd6\xa3\xac\xc8\xbb\xb6\xf8\xd4\xda<a href="http://www.hao6v.com/s/shenmi/" target="_blank"  title="\xc9\xf1\xc3\xd8\xc6\xac">\xc9\xf1\xc3\xd8</a>\xbf\xcd\xc4\xc7\xcd\xb7\xd5\xd6\xd6\xae\xd6\xd0\xa3\xac\xcb\xc6\xba\xf5\xd2\xfe\xb2\xd8\xd7\xc5\xca\xb2\xc3\xb4\xb2\xbb\xce\xaa\xc8\xcb\xd6\xaa\xb5\xc4\xd5\xe6\xcf\xe0&hellip;&hellip;</p>\r\n<p>\xa1\xf2\xbb\xf1\xbd\xb1\xc7\xe9\xbf\xf6&nbsp;</p>\r\n<p>\xa1\xa1\xa1\xa1\xb5\xda5\xbd\xec\xb6\xb9\xb0\xea\xb5\xe7\xd3\xb0\xc4\xea\xb6\xc8\xb0\xf1\xb5\xa5(2018)<br />\r\n\xa1\xa1\xa1\xa1\xd7\xee\xd6\xb5\xb5\xc3\xc6\xda\xb4\xfd\xb5\xc4\xcd\xe2\xd3\xef\xb5\xe7\xd3\xb0(\xcc\xe1\xc3\xfb)</p>\r\n<p><img alt="" src="https://tu.66vod.net/2019/3930.jpg" /></p>\r\n<p><hr />\r\n</p>\r\n<p><strong><span style="font-size: large"><span style="color: #ff0000">\xa1\xbe\xcf\xc2\xd4\xd8\xb5\xd8\xd6\xb7\xa1\xbf</span></span></strong></p>\r\n<p>\r\n<table cellspacing="1" cellpadding="10" width="100%" bgcolor="#0099cc" border="0">\r\n    <tbody>\r\n        <tr>\r\n            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px">\xd4\xda\xcf\xdf\xb9\xdb\xbf\xb4\xa3\xba<a target="_blank" href="https://www.66s.cc/kehuanpian/11844.html">https://www.66s.cc/kehuanpian/11844.html</a></td>\r\n        </tr>\r\n        <tr>\r\n            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px"><strong>\xc0\xb6\xb9\xe2\xb0\xe6</strong></td>\r\n        </tr>\r\n        <tr>\r\n            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px">\xb4\xc5\xc1\xa6\xa3\xba<a href="magnet:?xt=urn:btih:MIQSGKVDZDFVKMIOUDUTFNOD6BPNM2Q3&amp;dn=%e8%9c%98%e8%9b%9b%e4%be%a0%ef%bc%9a%e8%8b%b1%e9%9b%84%e8%bf%9c%e5%be%81%2e720p%2b1080p%2e%e5%9b%bd%e8%8b%b1%e5%8f%8c%e8%af%ad%2eBD%e4%b8%ad%e8%8b%b1%e5%8f%8c%e5%ad%97&amp;tr=udp%3a%2f%2f9%2erarbg%2eto%3a2710%2fannounce&amp;tr=udp%3a%2f%2f9%2erarbg%2eme%3a2710%2fannounce&amp;tr=http%3a%2f%2ftr%2ecili001%2ecom%3a8070%2fannounce&amp;tr=http%3a%2f%2ftracker%2etrackerfix%2ecom%3a80%2fannounce&amp;tr=udp%3a%2f%2fopen%2edemonii%2ecom%3a1337&amp;tr=udp%3a%2f%2ftracker%2eopentrackr%2eorg%3a1337%2fannounce&amp;tr=udp%3a%2f%2fp4p%2earenabg%2ecom%3a1337">\xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xd3\xa2\xd0\xdb\xd4\xb6\xd5\xf7.720p+1080p.\xb9\xfa\xd3\xa2\xcb\xab\xd3\xef.BD\xd6\xd0\xd3\xa2\xcb\xab\xd7\xd6.mp4</a></td>\r\n        </tr>\r\n        <tr>\r\n            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px">\xb5\xe7\xc2\xbf\xa3\xba<a href="ed2k://|file|%E8%9C%98%E8%9B%9B%E4%BE%A0%EF%BC%9A%E8%8B%B1%E9%9B%84%E8%BF%9C%E5%BE%81.1080p.%E5%9B%BD%E8%8B%B1%E5%8F%8C%E8%AF%AD.BD%E4%B8%AD%E8%8B%B1%E5%8F%8C%E5%AD%97[66%E5%BD%B1%E8%A7%86www.66Ys.Co].mp4|3749192287|96CE0CA3288DDCADDCFA9BB6FAC0FE21|h=NO6KVS427KMT5ZHKOBGGLMU23DDSITMU|/">\xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xd3\xa2\xd0\xdb\xd4\xb6\xd5\xf7.1080p.\xb9\xfa\xd3\xa2\xcb\xab\xd3\xef.BD\xd6\xd0\xd3\xa2\xcb\xab\xd7\xd6.mp4</a></td>\r\n        </tr>\r\n        <tr>\r\n            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px">\xb5\xe7\xc2\xbf\xa3\xba<a href="ed2k://|file|%E8%9C%98%E8%9B%9B%E4%BE%A0%EF%BC%9A%E8%8B%B1%E9%9B%84%E8%BF%9C%E5%BE%81.720p.%E5%9B%BD%E8%8B%B1%E5%8F%8C%E8%AF%AD.BD%E4%B8%AD%E8%8B%B1%E5%8F%8C%E5%AD%97[66%E5%BD%B1%E8%A7%86www.66Ys.Co].mp4|2168252504|BFC74C833CB77F33620443195D53305E|h=I3UYLPK6D7YKF7OZWPTYPDR4ICVAKTT6|/">\xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xd3\xa2\xd0\xdb\xd4\xb6\xd5\xf7.720p.\xb9\xfa\xd3\xa2\xcb\xab\xd3\xef.BD\xd6\xd0\xd3\xa2\xcb\xab\xd7\xd6.mp4</a></td>\r\n        </tr>\r\n        <tr>\r\n            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px"><strong>HD-web\xb0\xe6</strong></td>\r\n        </tr>\r\n        <tr>\r\n            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px">\xb4\xc5\xc1\xa6\xa3\xba<a href="magnet:?xt=urn:btih:O4MOF63K7OMYEZEHXOJSVP22ABMONNQC&amp;dn=%e8%9c%98%e8%9b%9b%e4%be%a0%ef%bc%9a%e8%8b%b1%e9%9b%84%e8%bf%9c%e5%be%81%2e1080p%2eHD%e4%b8%ad%e8%8b%b1%e5%8f%8c%e5%ad%97&amp;tr=udp%3a%2f%2f9%2erarbg%2eto%3a2710%2fannounce&amp;tr=udp%3a%2f%2f9%2erarbg%2eme%3a2710%2fannounce&amp;tr=http%3a%2f%2ftr%2ecili001%2ecom%3a8070%2fannounce&amp;tr=http%3a%2f%2ftracker%2etrackerfix%2ecom%3a80%2fannounce&amp;tr=udp%3a%2f%2fopen%2edemonii%2ecom%3a1337&amp;tr=udp%3a%2f%2ftracker%2eopentrackr%2eorg%3a1337%2fannounce&amp;tr=udp%3a%2f%2fp4p%2earenabg%2ecom%3a1337">\xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xd3\xa2\xd0\xdb\xd4\xb6\xd5\xf7.\xc3\xc0\xb0\xe6.\xce\xb4\xc9\xbe\xbc\xf5.1080p.HD\xd6\xd0\xd3\xa2\xcb\xab\xd7\xd6.mp4</a></td>\r\n        </tr>\r\n        <tr>\r\n            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px">\xb5\xe7\xc2\xbf\xa3\xba<a href="ed2k://|file|%E8%9C%98%E8%9B%9B%E4%BE%A0%EF%BC%9A%E8%8B%B1%E9%9B%84%E8%BF%9C%E5%BE%81.1080p.HD%E4%B8%AD%E8%8B%B1%E5%8F%8C%E5%AD%97[66%E5%BD%B1%E8%A7%86www.66Ys.Co].mp4|2037105042|B34FA8BF2AC9755775AFEF4FC5719245|h=7LPN3VOZE3P5552LMMAASVAHFJLRGU4U|/">\xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xd3\xa2\xd0\xdb\xd4\xb6\xd5\xf7.\xc3\xc0\xb0\xe6.\xce\xb4\xc9\xbe\xbc\xf5.1080p.HD\xd6\xd0\xd3\xa2\xcb\xab\xd7\xd6.mp4</a></td>\r\n        </tr>\r\n        <tr>\r\n            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px">\xb5\xe7\xc2\xbf\xa3\xba<a href="ed2k://|file|zz%E4%BE%A0%EF%BC%9A%E8%8B%B1x%E8%BF%9Cz.1080p.%E5%9B%BD%E8%8B%B1%E5%8F%8C%E8%AF%AD.HD%E4%B8%AD%E8%8B%B1%E5%8F%8C%E5%AD%97[66%E5%BD%B1%E8%A7%86www.66Ys.Co].mp4|2965195070|6AD6B753BB53F13CDC38EBEA704AB8B5|h=CYCAVV7RRHGQNA5QXMGHP5VR2TACYEWU|/">\xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xd3\xa2\xd0\xdb\xd4\xb6\xd5\xf7.1080p.\xb9\xfa\xd3\xa2\xcb\xab\xd3\xef.HD\xd6\xd0\xd3\xa2\xcb\xab\xd7\xd6\xce\xde\xcb\xae\xd3\xa1.mp4</a>&nbsp;\xa3\xa8\xb4\xf3\xc2\xbd\xb9\xab\xd3\xb3H265\xb0\xe6\xb1\xbe \xd0\xe8\xd2\xaa\xb2\xa5\xb7\xc5\xc6\xf7\xd6\xa7\xb3\xd6\xa3\xa9</td>\r\n        </tr>\r\n        <tr>\r\n            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px">\xcd\xf8\xc5\xcc\xc1\xb4\xbd\xd3\xa3\xba<a target="_blank" href="https://pan.baidu.com/s/1iw7qpPjJAiC3Dq9YL5j4Zw">https://pan.baidu.com/s/1iw7qpPjJAiC3Dq9YL5j4Zw</a> <br />\r\n            \xcc\xe1\xc8\xa1\xc2\xeb\xa3\xbata0g <br />\r\n            \xb8\xb4\xd6\xc6\xd5\xe2\xb6\xce\xc4\xda\xc8\xdd\xba\xf3\xb4\xf2\xbf\xaa\xb0\xd9\xb6\xc8\xcd\xf8\xc5\xcc\xca\xd6\xbb\xfaApp\xa3\xac\xb2\xd9\xd7\xf7\xb8\xfc\xb7\xbd\xb1\xe3\xc5\xb6</td>\r\n        </tr>\r\n    </tbody>\r\n</table>\r\n</p>\r\n<table cellspacing="1" cellpadding="10" width="100%" bgcolor="#0099cc" border="0">\r\n    <tbody>\r\n        <tr>\r\n            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px">\xc0\xb6\xb9\xe2\xd4\xad\xc5\xcc\xcf\xc2\xd4\xd8\xb5\xd8\xd6\xb7\xa3\xba<a target="_blank" href="http://www.dygang.com/1080p/20190920/43396.htm">http://www.dygang.com/1080p/20190920/43396.htm</a></td>\r\n        </tr>\r\n    </tbody>\r\n</table><div align="center"><div class="fl"><script type="text/javascript" src="http://www.hao6v.com/d/gg3002.js"></script></div><div class="fr"><script type="text/javascript" src="http://www.hao6v.com/d/f6.js"></script></div><div class="cr"></div></div>\r\n<div class="tps">\r\n\xc9\xcf\xd2\xbb\xc6\xaa <br> <a href="/dy/2019-09-12/FenShouGuiZhe.html" rel="prev" target="_blank">2019\xb0\xae\xc7\xe9\xbe\xe7\xc7\xe9\xa1\xb6\xb7\xd6\xca\xd6\xb7\xa8\xd4\xf2\xa1\xb71080p.HD\xb9\xfa\xd3\xef\xd6\xd0\xd7\xd6</a>\r\n<br>\r\n\xcf\xc2\xd2\xbb\xc6\xaa <br> <a href="/dy/2019-09-13/ShuDanYingXiong.html" rel="next" target="_blank">2019\xcf\xb2\xbe\xe7\xa1\xb6\xca\xf3\xb5\xa8\xd3\xa2\xd0\xdb\xa1\xb71080p.HD\xb9\xfa\xd3\xef\xd6\xd0\xd7\xd6</a>\r\n</div>\r\n<div class="tps">  <strong> 2019\xb8\xdf\xb7\xd6\xbf\xc6\xbb\xc3\xa1\xb6\xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xd3\xa2\xd0\xdb\xd4\xb6\xd5\xf7\xa1\xb71080p.\xb9\xfa\xd3\xa2\xcb\xab\xd3\xef.BD\xd6\xd0\xd3\xa2\xcb\xab\xd7\xd6 \xcf\xc2\xd4\xd8\xb0\xef\xd6\xfa\xa3\xba\xc8\xe7\xce\xde\xb7\xa8\xcf\xc2\xd4\xd8\xc7\xeb\xcf\xc8\xbf\xb4<a href="http://www.hao6v.com/dy/2010-10-11/12868.html" target="_blank">\xcf\xc2\xd4\xd8\xb0\xef\xd6\xfa</a>\r\n\xa1\xa3 </strong>  <br />  \r\n1.\xcf\xc2\xd4\xd8\xca\xb1\xd1\xb8\xc0\xd7\xc8\xed\xbc\xfe\xc8\xe7\xcc\xe1\xca\xbe\xa1\xae\xc8\xce\xce\xf1\xb4\xed\xce\xf3\xa3\xac\xce\xb4\xd6\xaa\xb4\xed\xce\xf3\xa3\xac\xc3\xf4\xb8\xd0\xd7\xca\xd4\xb4\xa3\xac\xce\xa5\xb9\xe6\xc4\xda\xc8\xdd\xa3\xac\xb0\xe6\xc8\xa8\xb5\xc8\xb5\xc8\xa1\xaf\xb6\xbc\xca\xc7\xd1\xb8\xc0\xd7\xc6\xc1\xb1\xce\xd7\xca\xd4\xb4\xb5\xc4\xb1\xed\xcf\xd6\xa3\xac\xba\xcd6v\xce\xde\xb9\xd8\xa1\xa3\xc7\xeb\xd7\xd0\xcf\xb8\xe4\xaf\xc0\xc0\xcf\xc2\xd4\xd8\xb0\xef\xd6\xfa\xa3\xac\xd2\xc0\xbe\xc9\xbf\xc9\xd2\xd4\xd5\xfd\xb3\xa3\xcf\xc2\xd4\xd8\xa1\xa3 <br />  \r\n2.\xd1\xb8\xc0\xd7\xb6\xd4\xd7\xca\xd4\xb4\xb5\xc4\xc6\xc1\xb1\xce\xd4\xbd\xc0\xb4\xd4\xbd\xd1\xcf\xd6\xd8\xa3\xac\xcb\xf9\xd2\xd4\xc7\xeb\xb4\xf3\xbc\xd2\xb2\xbb\xd2\xaa\xca\xb9\xd3\xc3\xd7\xee\xd0\xc2\xb0\xe6\xd1\xb8\xc0\xd7\xcf\xc2\xd4\xd86v\xb5\xc4\xd7\xca\xd4\xb4\xa3\xac\xbd\xa8\xd2\xe9\xca\xb9\xd3\xc3\xd1\xb8\xc0\xd75.8\xbb\xf2\xd5\xdf\xbc\xab\xcb\xd9\xd1\xb8\xc0\xd7\xa1\xa3 <br />\r\n3.\xb1\xbe\xd5\xbe\xcb\xf9\xd3\xd0\xd7\xca\xd4\xb4\xd6\xa7\xb3\xd6\xb0\xd9\xb6\xc8\xc3\xeb\xc0\xeb\xcf\xdf\xa3\xac\xd6\xa7\xb3\xd6\xb0\xd9\xb6\xc8\xcd\xf8\xc5\xcc\xd4\xda\xcf\xdf\xb9\xdb\xbf\xb4\xa3\xac\xb2\xbb\xbb\xe1\xca\xb9\xd3\xc3\xb5\xc4\xcd\xac\xd1\xa7\xbf\xc9\xd2\xd4\xe4\xaf\xc0\xc0\xcf\xc2\xd4\xd8\xb0\xef\xd6\xfa\xa1\xa3 <br />\r\n<strong> \xb1\xbe\xd5\xbe\xcb\xf9\xd3\xd0\xb5\xe7\xd3\xb0\xcd\xea\xc8\xab\xc3\xe2\xb7\xd1\xa3\xac\xcd\xc6\xbc\xf6\xca\xb9\xd3\xc3\xd1\xb8\xc0\xd7\xcf\xc2\xd4\xd8\xa3\xac\xcf\xc2\xd4\xd8\xb5\xc4\xc8\xcb\xd4\xbd\xb6\xe0\xcf\xc2\xd4\xd8\xcb\xd9\xb6\xc8\xd4\xbd\xbf\xec\xa3\xac\xb0\xd1\xd7\xca\xd4\xb4\xb7\xd6\xcf\xed\xb8\xf8\xc4\xfa\xb5\xc4\xc5\xf3\xd3\xd1\xbf\xc9\xd2\xd4\xb4\xf3\xb4\xf3\xcc\xe1\xb8\xdf\xcf\xc2\xd4\xd8\xcb\xd9\xb6\xc8\xa1\xa3</strong>  <br />\r\n</div>\r\n<div class="downtps"><strong>2019\xb8\xdf\xb7\xd6\xbf\xc6\xbb\xc3\xa1\xb6\xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xd3\xa2\xd0\xdb\xd4\xb6\xd5\xf7\xa1\xb71080p.\xb9\xfa\xd3\xa2\xcb\xab\xd3\xef.BD\xd6\xd0\xd3\xa2\xcb\xab\xd7\xd6\xcd\xf8\xd3\xd1\xc6\xc0\xc2\xdb\xa3\xba</strong>\r\n</div> \r\n</div>  \r\n<iframe name="ifc" id="ifc" src="/e/pl/?classid=32&id=33938" width="100%"  marginheight="0" border="0" frameborder="0" scrolling="no" height="0"\r\nonload="this.height=0;var fdh=(this.Document?this.Document.body.scrollHeight:this.contentDocument.body.offsetHeight);this.height=(fdh>700?fdh:700)" ></iframe>\r\n\r\n<div class="downtps dp">  </div>\r\n<div class="cr"></div>\r\n        </div>\r\n    </div>\r\n    <div class="col1">\r\n        <div class="box mt6">\r\n        \t<h3>\xc8\xc8\xc3\xc5\xb5\xe7\xd3\xb0\xb5\xe7\xca\xd3\xbe\xe7</h3>\r\n            <ul class="lt">\r\n            <li><a href="/mj/2015-04-12/QLDYX7.html" target="_blank"><font color=\'#FF0000\'>\xc3\xc0\xbe\xe7\xa1\xb6\xc8\xa8L\xb5\xc4\xd3\xce\xcf\xb7\xa1\xb7\xb5\xda\xb0\xcb\xbc\xbe\xc8\xab</font></a></li><li><a href="/mj/2015-03-02/24886.html" target="_blank"><font color=\'#FF0000\'>\xc3\xc0\xbe\xe7\xa1\xb6\xd0\xd0\xca\xac\xd7\xdf\xc8\xe2\xa1\xb7\xb5\xda\xbe\xc5\xbc\xbe[\xb8\xfc\xd0\xc2\xb8\xdf\xc7\xe5</font></a></li><li><a href="/dy/2014-11-21/24362.html" target="_blank"><font color=\'#FF0000\'>\xcd\xf8\xd5\xbe\xc6\xf4\xd3\xc3\xb1\xb8\xd3\xc3\xb5\xd8\xd6\xb7www.6vhao.com </font></a></li><li><a href="/dy/2017-06-27/29366.html" target="_blank"><font color=\'#FF0000\'>\xc3\xb2\xcb\xc6\xc4\xb3\xc0\xd7\xd2\xd1\xbb\xd6\xb8\xb4\xd5\xfd\xb3\xa3</font></a></li><li><a href="/mj/2011-10-17/16397.html" target="_blank"><font color=\'#FF0000\'>\xc3\xc0\xbe\xe7\xa1\xb6\xd0\xd0\xca\xac\xd7\xdf\xc8\xe2\xa1\xb7\xb5\xda1-4\xbc\xbe\xc8\xab</font></a></li><li><a href="/mj/2013-04-01/20273.html" target="_blank"><font color=\'#FF0000\'>\xc3\xc0\xbe\xe7\xa1\xb6\xb1\xf9\xd3\xeb\xbb\xf0\xd6\xae\xb8\xe8\xa1\xb7\xb5\xda\xcb\xc4\xbc\xbe\xc8\xab</font></a></li><li><a href="/dlz/2016-12-20/28299.html" target="_blank"><font color=\'#FF0000\'>\xa1\xb6\xb9\xed\xb4\xb5\xb5\xc6\xd6\xae\xbe\xab\xbe\xf8\xb9\xc5\xb3\xc7\xa1\xb7\xc8\xab\xbc\xaf</font></a></li><li><a href="/mj/2016-10-03/27892.html" target="_blank"><font color=\'#FF0000\'>\xc3\xc0\xbe\xe7\xa1\xb6\xce\xf7\xb2\xbf\xca\xc0\xbd\xe7\xa1\xb7\xb5\xda\xb6\xfe\xbc\xbe\xc8\xab</font></a></li><li><a href="/mj/2013-01-26/19814.html" target="_blank"><font color=\'#FF0000\'>\xc3\xc0\xbe\xe7\xa1\xb6\xcb\xb9\xb0\xcd\xb4\xef\xbf\xcb\xcb\xb9\xa3\xba\xd7\xe7\xd6\xe4\xd5\xdf\xd6\xae\xd5\xbd\xa1\xb7</font></a></li><li><a href="/mj/2014-10-08/24087.html" target="_blank"><font color=\'#FF0000\'>\xc3\xc0\xbe\xe7\xa1\xb6\xc9\xc1\xb5\xe7\xcf\xc0\xa1\xb7\xb5\xda\xce\xe5\xbc\xbe\xc8\xab</font></a></li><li><a href="/mj/2016-09-21/27808.html" target="_blank"><font color=\'#FF0000\'>\xc3\xc0\xbe\xe7\xa1\xb6\xc9\xf1\xb6\xdc\xbe\xd6\xcc\xd8\xb9\xa4\xa1\xb7\xb5\xda\xc1\xf9\xbc\xbe\xc8\xab</font></a></li><li><a href="/dy/2016-04-27/PFXDZCRZYLM.html" target="_blank"><font color=\'#FF0000\'>\xa1\xb6\xf2\xf9\xf2\xf0\xcf\xc0\xb4\xf3\xd5\xbd\xb3\xac\xc8\xcb\xa3\xba\xd5\xfd\xd2\xe5\xc0\xe8\xc3\xf7\xa1\xb772</font></a></li><li><a href="/dlz/2017-09-05/BaiYeZuiXiong.html" target="_blank"><font color=\'#FF0000\'>\xb6\xb9\xb0\xea9\xb7\xd6\xc9\xf1\xbe\xe7\xa1\xb6\xb0\xd7\xd2\xb9\xd7\xb7\xd0\xd7\xa1\xb7\xc8\xab\xbc\xaf</font></a></li><li><a href="/dy/2017-06-15/ShengQiNvXia.html" target="_blank"><font color=\'#FF0000\'>2017\xb6\xaf\xd7\xf7\xbf\xc6\xbb\xc3\xa1\xb6\xc9\xf1\xc6\xe6\xc5\xae\xcf\xc0\xa1\xb71080p.</font></a></li><li><a href="/dlz/2017-01-10/SDYXZ2017B.html" target="_blank">\xa1\xb6\xc9\xe4\xb5\xf1\xd3\xa2\xd0\xdb\xb4\xab2017\xb0\xe6\xa1\xb7</a></li><li><a href="/mj/2013-09-25/21456.html" target="_blank"><font color=\'#FF0000\'>\xc3\xc0\xbe\xe7\xa1\xb6\xc9\xf1\xb6\xdc\xbe\xd6\xcc\xd8\xb9\xa4\xa1\xb7\xb5\xda\xc8\xfd\xbc\xbe\xc8\xab</font></a></li><li><a href="/dy/2019-08-29/ShangHaiBaoLei.html" target="_blank"><font color=\'#FF0000\'>2019\xbf\xc6\xbb\xc3\xd5\xbd\xd5\xf9\xa1\xb6\xc9\xcf\xba\xa3\xb1\xa4\xc0\xdd\xa1\xb71080p.</font></a></li><li><a href="/dy/2015-01-01/24583.html" target="_blank"><font color=\'#FF0000\'>2014\xbf\xc6\xbb\xc3\xb4\xf3\xc6\xac\xa1\xb6\xd0\xc7\xbc\xca\xb4\xa9\xd4\xbd\xa1\xb7720p.\xb9\xfa</font></a></li><li><a href="/dy/2015-06-06/FCDMKSKBZL.html" target="_blank"><font color=\'#FF0000\'>2015\xb8\xdf\xb7\xd6\xb6\xaf\xd7\xf7\xa1\xb6\xb7\xe8\xbf\xf1\xb5\xc4\xc2\xf3\xbf\xcb\xcb\xb9\xa3\xba\xbf\xf1</font></a></li><li><a href="/dy/2016-07-29/DuLiRi2.html" target="_blank"><font color=\'#FF0000\'>2016\xb6\xaf\xd7\xf7\xbf\xc6\xbb\xc3\xa1\xb6\xb6\xc0\xc1\xa2\xc8\xd52\xa1\xb7720p.\xb9\xfa</font></a></li>   </ul>\r\n        </div>\r\n         <!--/box-->\r\n    <div class="box">\r\n        \t<h3>\xd7\xee\xd0\xc2\xb5\xe7\xd3\xb0\xcf\xc2\xd4\xd8</h3>\r\n            <ul class="lt">\r\n            <li><a href="/gq/2009-12-20/9698.html" target="_blank">\xba\xab\xb9\xfa\xb8\xdf\xb7\xd6\xbe\xe7\xc7\xe9\xa1\xb6\xc9\xb1\xc8\xcb\xbb\xd8\xd2\xe4\xa1\xb71080p.</a></li><li><a href="/dy/2019-09-11/GuiWaHuiHun.html" target="_blank">2019\xbf\xd6\xb2\xc0\xbe\xaa\xe3\xa4\xa1\xb6\xb9\xed\xcd\xde\xbb\xd8\xbb\xea\xa1\xb71080p.</a></li><li><a href="/dy/2019-09-12/ZZXYXYZ.html" target="_blank"><font color=\'#FF0000\'>2019\xb8\xdf\xb7\xd6\xbf\xc6\xbb\xc3\xa1\xb6\xd6\xa9\xd6\xeb\xcf\xc0\xa3\xba\xd3\xa2\xd0\xdb\xd4\xb6\xd5\xf7</font></a></li><li><a href="/dy/2019-09-18/NZSKLSN.html" target="_blank">2019\xb0\xae\xc7\xe9\xc6\xe6\xbb\xc3\xa1\xb6\xc4\xe6\xd7\xaa\xca\xb1\xbf\xd5\xc1\xb5\xc9\xcf\xc4\xe3\xa1\xb7</a></li><li><a href="/dy/2014-11-21/24362.html" target="_blank"><font color=\'#FF0000\'>\xcd\xf8\xd5\xbe\xc6\xf4\xd3\xc3\xb1\xb8\xd3\xc3\xb5\xd8\xd6\xb7www.6vhao.com </font></a></li><li><a href="/dy/2019-09-20/SDYJQ9.html" target="_blank"><font color=\'#FF0000\'>2019\xb6\xaf\xd7\xf7\xa1\xb6\xcb\xd9\xb6\xc8\xd3\xeb\xbc\xa4\xc7\xe99\xa3\xba\xcc\xd8\xb1\xf0\xd0\xd0\xb6\xaf</font></a></li><li><a href="/dy/2019-08-23/STXZ2DYXD.html" target="_blank"><font color=\'#FF0000\'>2019\xb6\xaf\xd7\xf7\xbe\xe7\xc7\xe9\xa1\xb6\xca\xb9\xcd\xbd\xd0\xd0\xd5\xdf2\xa3\xba\xb5\xfd\xd3\xb0\xd0\xd0</font></a></li><li><a href="/jddy/2019-09-15/33950.html" target="_blank"><font color=\'#FF0000\'>2019\xb8\xdf\xb7\xd6\xb6\xaf\xbb\xad\xa1\xb6\xcd\xe6\xbe\xdf\xd7\xdc\xb6\xaf\xd4\xb14\xa1\xb7108</font></a></li><li><a href="/dy/2019-09-17/PanTu.html" target="_blank">2019\xb8\xdf\xb7\xd6\xbe\xe7\xc7\xe9\xa1\xb6\xc5\xd1\xcd\xbd\xa1\xb71080p.BD\xd6\xd0</a></li><li><a href="/dy/2019-09-16/ZuoRiQiJi.html" target="_blank">2019\xc6\xe6\xbb\xc3\xcf\xb2\xbe\xe7\xa1\xb6\xd7\xf2\xc8\xd5\xc6\xe6\xbc\xa3\xa1\xb71080p.</a></li><li><a href="/dy/2019-09-16/KHSXZZDYLBEM.html" target="_blank">2018\xcf\xb2\xbe\xe7\xa1\xb6\xbf\xec\xbb\xee\xcb\xc4\xcf\xc0\xa3\xba\xd5\xe6\xd5\xfd\xb5\xc4\xd4\xbc\xc2\xb3</a></li><li><a href="/dy/2019-09-13/NuHaiRenXin.html" target="_blank">2018\xbe\xe7\xc7\xe9\xa1\xb6\xc5\xad\xba\xa3\xc8\xca\xd0\xc4\xa1\xb71080p.BD\xd6\xd0</a></li><li><a href="/dy/2019-09-13/HuanLeSong.html" target="_blank">2019\xcf\xb2\xbe\xe7\xa1\xb6\xbb\xb6\xc0\xd6\xcb\xcc\xa1\xb71080p.BD\xd6\xd0\xd3\xa2</a></li><li><a href="/jddy/2019-09-16/33951.html" target="_blank"><font color=\'#FF0000\'>2019\xb8\xdf\xb7\xd6\xb6\xaf\xbb\xad\xa1\xb6\xce\xb4\xc1\xcb\xd6\xae\xca\xc2 \xb5\xda\xd2\xbb\xbc\xbe\xa1\xb7</font></a></li><li><a href="/dy/2019-09-16/NHWZG.html" target="_blank">2019\xcf\xb2\xbe\xe7\xa1\xb6\xc5\xae\xba\xa2\xce\xd2\xd7\xee\xb8\xdf\xa1\xb7720p.BD\xd6\xd0</a></li><li><a href="/dy/2019-09-16/WoDeTianShi.html" target="_blank">2019\xbe\xaa\xe3\xa4\xbe\xe7\xc7\xe9\xa1\xb6\xce\xd2\xb5\xc4\xcc\xec\xca\xb9\xa1\xb7720p.B</a></li><li><a href="/dy/2019-08-29/ShangHaiBaoLei.html" target="_blank"><font color=\'#FF0000\'>2019\xbf\xc6\xbb\xc3\xd5\xbd\xd5\xf9\xa1\xb6\xc9\xcf\xba\xa3\xb1\xa4\xc0\xdd\xa1\xb71080p.</font></a></li><li><a href="/jddy/2019-07-22/33648.html" target="_blank">\xa1\xb6\xc1\xe9\xc1\xfd\xa1\xb7\xb8\xfc\xd0\xc2\xb5\xda05\xbc\xaf</a></li><li><a href="/jddy/2018-12-15/32419.html" target="_blank"><font color=\'#FF0000\'>\xa1\xb6\xb6\xb7\xc2\xde\xb4\xf3\xc2\xbd\xb6\xaf\xbb\xad\xb0\xe6\xa1\xb7\xb8\xfc\xd0\xc2\xb5\xda69\xbc\xaf</font></a></li><li><a href="/jddy/2019-07-21/33645.html" target="_blank">\xa1\xb6\xb6\xb7\xc6\xc6\xb2\xd4\xf1\xb7\xb6\xaf\xbb\xad\xb0\xe6 \xb5\xda\xc8\xfd\xbc\xbe\xa1\xb7\xb8\xfc\xd0\xc2\xb5\xda</a></li><li><a href="/dy/2019-09-10/AnNa.html" target="_blank"><font color=\'#FF0000\'>\xc2\xc0\xbf\xcb\xb1\xb4\xcb\xc92019\xb6\xaf\xd7\xf7\xa1\xb6\xb0\xb2\xc4\xc8\xa1\xb71080p.</font></a></li><li><a href="/dy/2019-09-14/FWDZD.html" target="_blank"><font color=\'#FF0000\'>\xba\xab\xb9\xfa2019\xd5\xbd\xd5\xf9\xbe\xe7\xc7\xe9\xa1\xb6\xb7\xef\xce\xe0\xb6\xb4\xd5\xbd\xb6\xb7\xa1\xb7</font></a></li><li><a href="/dy/2019-09-13/ZhiWu.html" target="_blank">2018\xbf\xd6\xb2\xc0\xcf\xb2\xbe\xe7\xa1\xb6\xd6\xaf\xce\xef\xa1\xb7720p.BD\xd6\xd0\xd3\xa2</a></li><li><a href="/dy/2019-09-13/YingDeBiSai.html" target="_blank">2019\xbe\xe7\xc7\xe9\xa1\xb6\xd3\xae\xb5\xc3\xb1\xc8\xc8\xfc\xa1\xb7720p.BD\xd6\xd0\xd3\xa2</a></li><li><a href="/dy/2019-09-14/XinShi.html" target="_blank">2019\xd5\xbd\xd5\xf9\xbe\xe7\xc7\xe9\xa1\xb6\xd0\xc5\xca\xb9\xa1\xb71080p.BD\xd6\xd0</a></li>            </ul>\r\n        </div>\r\n         <!--/box-->\r\n        <div class="box mt6">\r\n        \t<h3>\xd7\xee\xd0\xc2\xb5\xe7\xca\xd3\xbe\xe7\xcf\xc2\xd4\xd8</h3>\r\n            <ul class="lt">\r\n            <li><a href="/rj/2019-07-05/33532.html" target="_blank">\xc8\xd5\xbe\xe7\xa1\xb6\xca\xaa\xc1\xdc\xc1\xdc\xd5\xec\xcc\xbd\xcb\xae\xd2\xb0\xd3\xf0\xd2\xc2\xa1\xb7\xc8\xab\xbc\xaf</a></li><li><a href="/mj/2011-06-25/15294.html" target="_blank">\xc3\xc0\xbe\xe7\xa1\xb6\xbd\xf0\xd7\xb0\xc2\xc9\xca\xa6/\xcb\xdf\xcb\xcf\xcb\xab\xd0\xdb\xa1\xb7\xb5\xda\xbe\xc5\xbc\xbe</a></li><li><a href="/mj/2017-08-11/29617.html" target="_blank">\xc3\xc0\xbe\xe7\xa1\xb6\xc3\xb7\xc8\xfc\xb5\xc2\xcb\xb9\xcf\xc8\xc9\xfa\xa1\xb7\xb5\xda\xc8\xfd\xbc\xbe[\xb8\xfc\xd0\xc2</a></li><li><a href="/mj/2016-09-15/27775.html" target="_blank">\xc3\xc0\xbe\xe7\xa1\xb6\xc3\xc0\xb9\xfa\xbf\xd6\xb2\xc0\xb9\xca\xca\xc2\xa1\xb7\xb5\xda\xbe\xc5\xbc\xbe[\xb8\xfc\xd0\xc2</a></li><li><a href="/dlz/2019-09-04/33908.html" target="_blank">\xa1\xb6\xce\xb1\xb3\xae\xd5\xdf\xd6\xae\xc4\xa9\xc2\xb7\xa1\xb7\xc8\xab\xbc\xaf</a></li><li><a href="/dlz/2019-08-27/33852.html" target="_blank">\xa1\xb6\xc0\xcf\xbe\xc6\xb9\xdd\xa1\xb7\xc8\xab\xbc\xaf</a></li><li><a href="/dlz/2017-02-22/28652.html" target="_blank">\xa1\xb6\xb0\xae\xbb\xd8\xbc\xd2\xd6\xae\xbf\xaa\xd0\xc4\xcb\xd9\xb5\xdd\xa1\xb7\xb8\xfc\xd0\xc2\xb5\xda669\xbc\xaf</a></li><li><a href="/dlz/2019-09-02/33906.html" target="_blank">\xa1\xb6\xbd\xd6\xb7\xbb\xb2\xc6\xd2\xaf\xa1\xb7\xb8\xfc\xd0\xc2\xb5\xda14\xbc\xaf</a></li><li><a href="/dlz/2019-09-16/33958.html" target="_blank">\xa1\xb6\xbd\xf0\xcf\xfc\xb4\xf3\xcf\xc3\xa1\xb7\xb8\xfc\xd0\xc2\xb5\xda04\xbc\xaf</a></li><li><a href="/mj/2019-08-20/33825.html" target="_blank">\xc3\xc0\xbe\xe7\xa1\xb6\xd6\xc2\xc3\xfc\xc5\xae\xc8\xcb\xa1\xb7\xb5\xda\xd2\xbb\xbc\xbe[\xb8\xfc\xd0\xc2\xb8\xdf\xc7\xe5</a></li><li><a href="/mj/2019-07-19/33636.html" target="_blank">\xc3\xc0\xbe\xe7\xa1\xb6\xc6\xa4\xb6\xfb\xd1\xb7\xa1\xb7\xb5\xda\xd2\xbb\xbc\xbe\xc8\xab</a></li><li><a href="/mj/2018-03-27/30881.html" target="_blank"><font color=\'#FF0000\'>\xc3\xc0\xbe\xe7\xa1\xb6\xbc\xab\xb5\xd8\xb6\xf1\xc1\xe9\xa1\xb7\xb5\xda\xb6\xfe\xbc\xbe[\xb8\xfc\xd0\xc2\xb8\xdf\xc7\xe5</font></a></li><li><a href="/mj/2019-09-18/33966.html" target="_blank">\xc3\xc0\xbe\xe7\xa1\xb6\xc4\xd1\xd2\xd4\xd6\xc3\xd0\xc5\xa1\xb7\xb5\xda\xd2\xbb\xbc\xbe\xc8\xab</a></li><li><a href="/mj/2019-09-18/33967.html" target="_blank">\xc3\xc0\xbe\xe7\xa1\xb6\xce\xd2\xc3\xc7\xb5\xc4\xc4\xd0\xba\xa2\xa1\xb7\xb5\xda\xd2\xbb\xbc\xbe[\xb8\xfc\xd0\xc2\xb8\xdf</a></li><li><a href="/mj/2019-07-18/33621.html" target="_blank">\xc3\xc0\xbe\xe7\xa1\xb6\xc5\xcb\xb6\xe0\xc0\xad\xa1\xb7\xb5\xda\xd2\xbb\xbc\xbe[\xb8\xfc\xd0\xc2\xb8\xdf\xc7\xe51</a></li><li><a href="/mj/2014-10-03/24056.html" target="_blank"><font color=\'#FF0000\'>\xd3\xa2\xbe\xe7\xa1\xb6\xd4\xa1\xd1\xaa\xba\xda\xb0\xef\xa1\xb7\xb5\xda\xce\xe5\xbc\xbe[\xb8\xfc\xd0\xc2\xb8\xdf\xc7\xe5</font></a></li><li><a href="/rj/2019-07-09/33550.html" target="_blank">\xc8\xd5\xbe\xe7\xa1\xb6\xb7\xa8\xd2\xbd\xb3\xaf\xd1\xd5\xa1\xb7\xb8\xfc\xd0\xc2\xb5\xda10\xbc\xaf</a></li><li><a href="/rj/2019-08-01/33713.html" target="_blank">\xc8\xd5\xbe\xe7\xa1\xb6\xc2\xd6\xb5\xbd\xc4\xe3\xc1\xcb\xb7\xac\xcd\xe2\xc6\xaa \xb7\xbf\xc3\xc5\xd6\xae\xc4\xda\xa1\xb7</a></li><li><a href="/mj/2014-10-14/24129.html" target="_blank">\xc3\xc0\xbe\xe7\xa1\xb6\xb4\xa6\xc5\xae\xc7\xe9\xd4\xb5\xa1\xb7\xb5\xda\xce\xe5\xbc\xbe[\xb8\xfc\xd0\xc2\xb8\xdf\xc7\xe5</a></li><li><a href="/rj/2017-10-27/30062.html" target="_blank">\xc8\xd5\xbe\xe7\xa1\xb6\xba\xda\xc9\xab\xce\xe5\xd2\xb6\xb2\xdd\xa1\xb7\xb8\xfc\xd0\xc2\xb5\xda101\xbc\xaf</a></li><li><a href="/mj/2017-08-27/29724.html" target="_blank"><font color=\'#FF0000\'>\xc3\xc0\xbe\xe7\xa1\xb6\xb6\xe9\xc2\xe4\xbd\xd6\xb4\xab\xc6\xe6\xa1\xb7\xb5\xda\xc8\xfd\xbc\xbe[\xb8\xfc\xd0\xc2\xb8\xdf</font></a></li><li><a href="/dlz/2019-09-17/33959.html" target="_blank">\xa1\xb6\xbf\xd5\xbd\xb5\xc0\xfb\xc8\xd0\xa1\xb7\xb8\xfc\xd0\xc2\xb5\xda06\xbc\xaf</a></li><li><a href="/dlz/2019-08-27/33854.html" target="_blank">\xa1\xb6\xd3\xf6\xbc\xfb\xd0\xd2\xb8\xa3\xa1\xb7\xb8\xfc\xd0\xc2\xb5\xda35\xbc\xaf</a></li><li><a href="/dlz/2019-09-10/33930.html" target="_blank">\xa1\xb6\xb7\xc9\xbb\xa2\xd6\xae\xc0\xd7\xf6\xaa\xbc\xab\xd5\xbd\xa1\xb7\xb8\xfc\xd0\xc2\xb5\xda15\xbc\xaf</a></li><li><a href="/rj/2019-09-09/33925.html" target="_blank">\xc8\xd5\xbe\xe7\xa1\xb6\xb7\xe7\xc6\xbd\xc0\xcb\xbe\xb2\xb5\xc4\xcf\xd0\xcf\xbe\xa1\xb7\xb8\xfc\xd0\xc2\xb5\xda09</a></li>   </ul>\r\n        </div>\r\n         <!--/box-->\r\n        <div class="box mt6">\r\n        \t<h3>\xd7\xee\xd0\xc2\xd7\xdb\xd2\xd5\xd3\xce\xcf\xb7\xcf\xc2\xd4\xd8</h3>\r\n            <ul class="lt">\r\n            <li><a href="/zy/2019-05-06/33211.html" target="_blank">\xa1\xb62019\xc4\xea\xc3\xc0\xb9\xfa\xb9\xab\xb8\xe6\xc5\xc6\xd2\xf4\xc0\xd6\xb4\xf3\xbd\xb1\xa1\xb772</a></li><li><a href="/zy/2019-02-28/32825.html" target="_blank">\xa1\xb6\xb5\xda91\xbd\xec\xb0\xc2\xcb\xb9\xbf\xa8\xb0\xe4\xbd\xb1\xb5\xe4\xc0\xf1\xa1\xb7720p.H</a></li><li><a href="/zy/2019-02-09/32732.html" target="_blank">\xa1\xb62019\xb9\xe3\xb6\xab\xce\xc0\xca\xd3\xb4\xba\xcd\xed\xa1\xb71080p.HD\xb9\xfa</a></li><li><a href="/zy/2019-02-09/32731.html" target="_blank">\xa1\xb62019\xcc\xec\xbd\xf2\xce\xc0\xca\xd3\xb4\xba\xcd\xed\xa1\xb71080p.HD\xb9\xfa</a></li><li><a href="/zy/2019-02-06/32716.html" target="_blank">\xa1\xb62019\xb1\xb1\xbe\xa9\xce\xc0\xca\xd3\xb4\xba\xcd\xed\xa1\xb71080p.HD\xb9\xfa</a></li><li><a href="/zy/2019-02-06/32715.html" target="_blank">\xa1\xb62019\xb6\xab\xb7\xbd\xce\xc0\xca\xd3\xb4\xba\xbd\xda\xcd\xed\xbb\xe1\xa1\xb71080p.</a></li><li><a href="/zy/2019-02-06/32718.html" target="_blank">\xa1\xb62019\xba\xfe\xc4\xcf\xce\xc0\xca\xd3\xbb\xaa\xc8\xcb\xb4\xba\xcd\xed\xa1\xb71080p.</a></li><li><a href="/zy/2019-02-06/32717.html" target="_blank">\xa1\xb62019\xbd\xad\xcb\xd5\xce\xc0\xca\xd3\xb4\xba\xbd\xda\xcd\xed\xbb\xe1\xa1\xb71080p.</a></li><li><a href="/zy/2019-02-04/32707.html" target="_blank">\xa1\xb62019\xc1\xc9\xc4\xfe\xce\xc0\xca\xd3\xb4\xba\xcd\xed\xa1\xb71080p.HD\xb9\xfa</a></li><li><a href="/zy/2019-02-04/32706.html" target="_blank">\xa1\xb62019\xbd\xad\xce\xf7\xce\xc0\xca\xd3\xb4\xba\xcd\xed\xa1\xb71080p.HD\xb9\xfa</a></li>   </ul>\r\n        </div>\r\n         <!--/box-->\r\n    </div>\r\n        </div>\r\n         <!--/box-->\r\n    </div>\t\r\n</div><div id="a960"><script src="/d/960.js"></script> </div>\r\n<div id="a9602"><script src=/d/f5.js></script></div>\r\n<div id="footer">\r\n\t<p class="t"><a href="/index.html">\xcd\xf8\xd5\xbe\xc1\xf4\xd1\xd4</a> - <a href="/index.html">\xb9\xd8\xd3\xda\xce\xd2\xc3\xc7</a> - <a href="/index.html">\xb9\xe3\xb8\xe6\xd2\xb5\xce\xf1</a> - <a href="/index.html">\xd0\xc5\xcf\xa2\xb7\xb4\xc0\xa1</a> - <a href="/index.html">\xba\xcf\xd7\xf7\xbb\xef\xb0\xe9</a> - <a href="/index.html">\xcd\xf8\xd5\xbe\xb5\xd8\xcd\xbc</a></p>\r\n\t<p>Copyright &copy; 2009 <a href="http://www.hao6v.com"><b><font color=red>6V\xb5\xe7\xd3\xb0</font></b></a> \xb0\xe6\xc8\xa8\xcb\xf9\xd3\xd0<br />\r\n\t  \xd3\xe5ICP\xb1\xb809051310\xba\xc5\r\n</div>\r\n<span class="hidden"><script src=/d/tj.js></script></span>\r\n</body>\r\n</html>'
# html = etree.HTML(res.decode("gbk"))
# link_list = html.xpath("//table[1]//a")
# for link in link_list:
#     if "蜘蛛侠" in link.text:
#         print(link.text)
#         print(link.xpath("./@href")[0])

# m = "01.720p.mkv".split(".")
# ret1 = re.findall(r"^\d[0-9]$",m[0])
# print(ret1)
# movie_style = ["rmvb","mkv","mp4","rm","avi"]
# if m[-1].lower() in movie_style:
#     print("ok")

# m = b'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\r\n<html xmlns="http://www.w3.org/1999/xhtml">\r\n<head>\r\n<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />\r\n<title>\xb8\xdf\xbc\xb6\xcb\xd1\xcb\xf7 \xc9\xf1\xc6\xe6\xcb\xc4\xcf\xc0 - 66\xd3\xb0\xca\xd3 - \xd1\xb8\xc0\xd7\xb5\xe7\xd3\xb0\xcf\xc2\xd4\xd8_\xd4\xda\xcf\xdf\xb5\xe7\xd3\xb0</title>\r\n<meta name="keywords" content="\xb8\xdf\xbc\xb6\xcb\xd1\xcb\xf7 \xc9\xf1\xc6\xe6\xcb\xc4\xcf\xc0 - 66\xd3\xb0\xca\xd3 - \xd1\xb8\xc0\xd7\xb5\xe7\xd3\xb0\xcf\xc2\xd4\xd8_\xd4\xda\xcf\xdf\xb5\xe7\xd3\xb0" />\r\n<meta name="description" content="\xb8\xdf\xbc\xb6\xcb\xd1\xcb\xf7 \xc9\xf1\xc6\xe6\xcb\xc4\xcf\xc0 - 66\xd3\xb0\xca\xd3 - \xd1\xb8\xc0\xd7\xb5\xe7\xd3\xb0\xcf\xc2\xd4\xd8_\xd4\xda\xcf\xdf\xb5\xe7\xd3\xb0" />\r\n<link rel="stylesheet" rev="stylesheet" href="/images/style.css" type="text/css" />\r\n<script type="text/javascript" src="/js/common.js"></script>\r\n<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7" />\r\n</head>\r\n<body>\r\n\t<div id="header"><div id="top">  <a href="https://app.pp63.org/\xbf\xec\xbf\xb4.apk" target=_blank>APP\xb0\xb2\xd7\xbf\xb0\xe6</a>&nbsp;&nbsp;\r\n<a href="http://www.hao6v.com/dy/2012-12-07/19512.html" target=_blank>\xb9\xab\xb8\xe6\xc7\xf8</a>&nbsp;&nbsp;<a href="http://www.hao6v.com/dy/2019-01-02/32524.html" target="_blank">\xb6\xb9\xb0\xea2018\xb0\xf1\xb5\xa5</a>&nbsp;&nbsp;\r\n<a href="http://www.hao6v.com/gq/2012-09-01/18841.html" target=_blank><font color=\'#FF0000\'>6v\xb5\xe7\xd3\xb0\xc5\xc5\xd0\xd0\xb0\xf1</font></a>&nbsp;&nbsp;\r\n<a href="http://www.hao6v.com/dy/2011-09-20/16090.html" target=_blank>\xb1\xb1\xc3\xc0\xc6\xb1\xb7\xbf\xc5\xc5\xd0\xd0\xb0\xf1</a>&nbsp;&nbsp;\r\n<a href="http://www.hao6v.com/s/007/" target=_blank>007\xb5\xe7\xd3\xb0\xc8\xab\xbc\xaf</a>&nbsp;&nbsp;\r\n<a href="http://www.hao6v.com/s/gf250/" target=_blank>IMDB250\xb5\xe7\xd3\xb0</a>&nbsp;&nbsp;\r\n<a href="/s/gf/" target=_blank>\xb8\xdf\xc6\xc0\xb7\xd6\xb5\xe7\xd3\xb0</a>&nbsp;&nbsp;\r\n<a href="/s/hanguodianying/" target=_blank>\xc3\xc0\xb9\xfa\xb5\xe7\xd3\xb0</a>&nbsp;&nbsp;<a href="/s/xijudianying/" target=_blank>\xc5\xb7\xd6\xde\xb5\xe7\xd3\xb0</a>&nbsp;&nbsp;<a href="/s/yazhoudianying/" target=_blank>\xd1\xc7\xd6\xde\xb5\xe7\xd3\xb0</a>&nbsp;&nbsp;<a href="/s/mzdy/" target=_blank>\xc3\xc0\xd6\xde\xb5\xe7\xd3\xb0</a> &nbsp;<a href="http://www.hao6v.com/e/tool/gbook/?bid=1" target=_blank>\xb7\xc3\xbf\xcd\xc1\xf4\xd1\xd4</a></div>\r\n    \t<div class="log"><a href="/">6V\xb5\xe7\xd3\xb0</a></div>\r\n        <div class="topad"><script src="/d/f4.js"></script></div>\r\n<div class="cr"></div>\r\n        <div id="menu">\r\n      <p><a href="http://www.hao6v.com/">\xca\xd7\xd2\xb3</a>  <a href="http://www.hao6v.com/dy/" target=_blank>2019\xd7\xee\xd0\xc2\xb5\xe7\xd3\xb0</a> <a href="http://www.hao6v.com/gydy/" target=_blank>\xb9\xfa\xd3\xef\xc5\xe4\xd2\xf4\xb5\xe7\xd3\xb0</a> <a href="http://www.hao6v.com/zydy/" target=_blank>\xce\xa2\xb5\xe7\xd3\xb0</a> <a href="http://www.hao6v.com/gq/" target=_blank>\xbe\xad\xb5\xe4\xb8\xdf\xc7\xe5\xb5\xe7\xd3\xb0</a> <a href="http://www.hao6v.com/jddy/" target=_blank>\xb6\xaf\xbb\xad\xb5\xe7\xd3\xb0</a> <a href="http://www.hao6v.com/3D/" target=_blank>3D\xb5\xe7\xd3\xb0</a> <a href="http://www.hao6v.com/s/shoujiMP4dianying/" target=_blank>MP4\xca\xd6\xbb\xfa\xb5\xe7\xd3\xb0</a> <a href="http://www.hao6v.com/dlz/" target=_blank>\xb9\xfa\xbe\xe7</a> <a href="http://www.hao6v.com/rj/" target=_blank>\xc8\xd5\xba\xab\xbe\xe7</a> <a href="http://www.hao6v.com/mj/" target=_blank>\xc5\xb7\xc3\xc0\xbe\xe7</a> <a href="http://www.hao6v.com/zy/" target=_blank>\xd7\xdb\xd2\xd5\xbd\xda\xc4\xbf</a> <a href="http://www.hao6v.com/s/gangtaidianying/" target=_blank>\xb8\xdb\xcc\xa8\xb5\xe7\xd3\xb0</a> <a href="http://www.hao6v.com/s/jingdiandianying/" target=_blank>\xc8\xd5\xba\xab\xb5\xe7\xd3\xb0</a> </p>\r\n      <p class="bg"><a href="http://www.66e.cc/" target=_blank>66\xd3\xb0\xca\xd3\xcd\xf8</a> \xd7\xa8\xcc\xe2\xb7\xd6\xc0\xe0\xa3\xba<a href="http://www.hao6v.com/s/xiju/" target=_blank>\xcf\xb2\xbe\xe7</a><a href="http://www.hao6v.com/s/dongzuo/" target=_blank>\xb6\xaf\xd7\xf7</a><a href="http://www.hao6v.com/s/aiqing/" target=_blank>\xb0\xae\xc7\xe9</a><a href="http://www.hao6v.com/s/kehuan/" target=_blank>\xbf\xc6\xbb\xc3</a><a href="http://www.hao6v.com/s/qihuan/" target=_blank>\xc6\xe6\xbb\xc3</a><a href="http://www.hao6v.com/s/shenmi/" target=_blank>\xc9\xf1\xc3\xd8</a><a href="http://www.hao6v.com/s/huanxiang/" target=_blank>\xbb\xc3\xcf\xeb</a><a href="http://www.hao6v.com/s/kongbu/" target=_blank>\xbf\xd6\xb2\xc0</a><a href="http://www.hao6v.com/s/zhanzheng/" target=_blank>\xd5\xbd\xd5\xf9</a><a href="http://www.hao6v.com/s/maoxian/" target=_blank>\xc3\xb0\xcf\xd5</a><a href="http://www.hao6v.com/s/jingsong/" target=_blank>\xbe\xaa\xe3\xa4</a><a href="http://www.hao6v.com/s/juqingpian/" target=_blank>\xbe\xe7\xc7\xe9</a><a href="http://www.hao6v.com/s/zhuanji/" target=_blank>\xb4\xab\xbc\xc7</a><a href="http://www.hao6v.com/s/lishi/" target=_blank>\xc0\xfa\xca\xb7</a><a href="http://www.hao6v.com/s/jilu/" target=_blank>\xbc\xcd\xc2\xbc</a><a href="http://www.hao6v.com/s/yindudianying/" target=_blank>\xd3\xa1\xb6\xc8\xb5\xe7\xd3\xb0</a>  <a href="http://www.hao6v.com/s/guochandianying/" target=_blank>\xb9\xfa\xb2\xfa\xb5\xe7\xd3\xb0</a> <a href="http://www.hao6v.com/s/xijudianying/" target=_blank>\xc5\xb7\xd6\xde\xb5\xe7\xd3\xb0</a> <a href="http://www.hao6v.com/s/zhuanti/" target=_blank>\xd7\xa8\xcc\xe2\xcd\xc6\xbc\xf6</a> </p>\r\n        </div>\r\n  </div>\r\n\r\n<div id="a960"> <script src="/d/f1.js"></script> </div>\r\n<div id="search">\r\n<div class="ser">\r\n<form action="/e/search/index.php" method="post" name="searchform" id="searchform">\r\n<input type="hidden" name="show" value="title,smalltext" />\r\n<input type="hidden" name="tempid" value="1" />\r\n\r\n<span>\xd5\xbe\xc4\xda\xcb\xd1\xcb\xf7\xa3\xba<input name="keyboard" type="text" size="32" id="keyboard" class="inputText" /></span>\r\n<span class="sect"><select name="tbname">\r\n<option value="article">\xc8\xab\xd5\xbe</option>\r\n</select></span>\r\n<span><input type="image" class="inputSub" src="/images/search.gif" /></span>\r\n</form>\r\n</span>\r\n</div>\r\n<div class="help">\r\n<a href="http://www.hao6v.com/dy/2010-10-11/12868.html" target="_blank">6v\xb5\xe7\xd3\xb0\xcf\xc2\xd4\xd8\xb0\xef\xd6\xfa\xd3\xeb\xbd\xcc\xb3\xcc<br />\xb5\xe7\xd3\xb0\xd6\xaa\xca\xb6\xd0\xc2\xca\xd6\xb1\xd8\xbf\xb4</a>\r\n</div>\r\n<INPUT type="button" value=\'\xca\xd5\xb2\xd8\xb1\xbe\xd3\xb0\xc6\xac\' id="copy" onclick="javascript:d=document;window.external.AddFavorite(\'\'+d.location.href+\'\', \'\'+d.title+\'\')">\r\n<div class="help">\r\n\r\n<!-- Baidu Button BEGIN -->\r\n    <div id="bdshare" class="bdshare_t bds_tools get-codes-bdshare">\r\n        <span class="bds_more">\xb7\xd6\xcf\xed\xb5\xbd\xa3\xba</span>\r\n        <a class="bds_qzone"></a>\r\n        <a class="bds_tsina"></a>\r\n        <a class="bds_tqq"></a>\r\n        <a class="bds_renren"></a>\r\n        <a class="bds_baidu"></a>\r\n        <a class="bds_copy"></a>\r\n        <a class="bds_qq"></a>\r\n    </div>\r\n<script type="text/javascript" id="bdshare_js" data="type=tools&amp;uid=267792" ></script>\r\n<script type="text/javascript" id="bdshell_js"></script>\r\n<script type="text/javascript">\r\n\tdocument.getElementById("bdshell_js").src = "http://bdimg.share.baidu.com/static/js/shell_v2.js?t=" + new Date().getHours();\r\n</script>\r\n<!-- Baidu Button END -->\r\n</div>\r\n</div>\r\n\r\n<div id="main">\r\n<div class="box">\r\n        \t<div class="t">\xc4\xfa\xb5\xc4\xce\xbb\xd6\xc3\xa3\xba<a href=\'/index.html\'>\xca\xd7\xd2\xb3</a>&nbsp;>&nbsp;\xb8\xdf\xbc\xb6\xcb\xd1\xcb\xf7</div>\r\n <tr> \r\n                                        <td height="100%" valign="top"> <form name=search_news method=post action=\'http://www.hao6v.com/e/search/index.php\' onsubmit=\'return search_check(document.search_news);\'>\r\n                        <table width="100%" border="0" cellspacing="1" cellpadding="3">\r\n                          <input type=hidden name=show value="title">\r\n\t\t\t\t\t\t  <input type=hidden name=tempid value="1">\r\n                          <tr> \r\n                            <td height="20">\xb9\xd8\xbc\xfc\xd7\xd6\xa3\xba \r\n                              <input name="keyboard" type="text" id="keyboard" value="\xb9\xfa\xd3\xef\xc5\xe4\xd2\xf4" size="32">\r\n                              <select name="tbname" id="tbname">\r\n                                <option value="article">\xd1\xb8\xc0\xd7\xd7\xca\xd4\xb4</option>\r\n                              </select> \r\n                              <input type="submit" name="Submit22" value="\xcb\xd1\xcb\xf7"> \r\n                              &nbsp; \r\n                                     </td>\r\n                              &nbsp; <input type="button" name="Submit" value="\xb8\xdf\xbc\xb6\xcb\xd1\xcb\xf7" onclick="self.location.href=\'../../../search\'">\r\n                              (\xb6\xe0\xb8\xf6\xb9\xd8\xbc\xfc\xd7\xd6\xc7\xeb\xd3\xc3&quot;\xbf\xd5\xb8\xf1&quot;\xb8\xf1\xbf\xaa) </td>\r\n                          </tr>\r\n                        </table>\r\n                      </form>\r\n                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1" bgcolor="E8F5FB">\r\n                        <tr> \r\n                          <td height="25">\xcf\xb5\xcd\xb3\xcb\xd1\xcb\xf7\xb5\xbd\xd4\xbc\xd3\xd0<strong>4</strong>\xcf\xee\xb7\xfb\xba\xcf<strong>\xc9\xf1\xc6\xe6\xcb\xc4\xcf\xc0</strong>\xb5\xc4\xb2\xe9\xd1\xaf\xbd\xe1\xb9\xfb</td>\r\n                        </tr>\r\n                      </table>\r\n                       \r\n                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">\r\n        <tr> \r\n          <td><div align="center">\r\n\t\t\t  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">\r\n                <tr> \r\n                  \r\n            <td width="41%" height="25"><font color="#663333">\xa1\xa4[<a href=/dy/>2019\xd7\xee\xd0\xc2\xb5\xe7\xd3\xb0</a>]<span class="blue14"><a href=/dy/2015-09-10/SQSX2015.html target=_blank><font color=\'#FF0000\'>2015\xb6\xaf\xd7\xf7\xbf\xc6\xbb\xc3\xa1\xb6\xc9\xf1\xc6\xe6\xcb\xc4\xcf\xc02015\xa1\xb7720p.BD\xd6\xd0\xd3\xa2\xcb\xab\xd7\xd6</font></a></span></font></td>\r\n                  <td width="59%"><font color="#666666">\xb7\xa2\xb2\xbc\xca\xb1\xbc\xe4\xa3\xba2015-10-26 13:51:20</font></td>\r\n                </tr>\r\n              </table>\r\n            </div></td>\r\n        </tr>\r\n        <tr> \r\n          <td bgcolor="#EBF3FA"> \r\n            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">\r\n              <tr> \r\n                <td>\xa1\xf2\xd2\xeb\xa1\xa1\xa1\xa1\xc3\xfb\xa1\xa1\xc9\xf1\xc6\xe6\xcb\xc4\xcf\xc02015/\xd0\xc2\xc9\xf1\xc6\xe6\xcb\xc4\xcf\xc0/\xc9\xf1\xc6\xe64\xcf\xc0(\xb8\xdb)/\xbe\xaa\xc6\xe64\xb3\xac\xc8\xcb(\xcc\xa8)<br />\r\n\xa1\xf2\xc6\xac\xa1\xa1\xa1\xa1\xc3\xfb\xa1\xa1Fantastic Four<br />\r\n\xa1\xf2\xc4\xea\xa1\xa1\xa1\xa1\xb4\xfa\xa1\xa12015<br />\r\n\xa1\xf2\xb9\xfa\xa1\xa1\xa1\xa1\xbc\xd2\xa1\xa1\xc3\xc0\xb9\xfa/\xd3\xa2\xb9\xfa/\xb5\xc2\xb9\xfa<br />\r\n\xa1\xf2\xc0\xe0\xa1\xa1\xa1\xa1\xb1\xf0\xa1\xa1\xb6\xaf\xd7\xf7/\xbf\xc6\xbb\xc3/\xc3\xb0\xcf\xd5<br />\r\n\xa1\xf2\xd3\xef\xa1\xa1\xa1\xa1\xd1\xd4\xa1\xa1\xd3\xa2\xd3\xef</td>\r\n              </tr>\r\n              <tr>\r\n                <td><a href="/dy/2015-09-10/SQSX2015.html" target="_blank">/dy/2015-09-10/SQSX2015.html</a></td>\r\n              </tr>\r\n            </table>\r\n\t\t\t</td>\r\n        </tr>\r\n      </table>\r\n                       \r\n                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">\r\n        <tr> \r\n          <td><div align="center">\r\n\t\t\t  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">\r\n                <tr> \r\n                  \r\n            <td width="41%" height="25"><font color="#663333">\xa1\xa4[<a href=/gq/>\xbe\xad\xb5\xe4\xb8\xdf\xc7\xe5\xb5\xe7\xd3\xb0</a>]<span class="blue14"><a href=/gq/2011-08-06/15707.html target=_blank>\xbe\xad\xb5\xe4\xbf\xc6\xbb\xc3\xa1\xb6\xc9\xf1\xc6\xe6\xcb\xc4\xcf\xc02\xa1\xb7720p.\xb9\xfa\xd3\xa2\xcb\xab\xd3\xef.BD\xd6\xd0\xd3\xa2\xcb\xab\xd7\xd6\xb8\xdf\xc7\xe5MKV\xb0\xe6</a></span></font></td>\r\n                  <td width="59%"><font color="#666666">\xb7\xa2\xb2\xbc\xca\xb1\xbc\xe4\xa3\xba2013-07-14 00:25:04</font></td>\r\n                </tr>\r\n              </table>\r\n            </div></td>\r\n        </tr>\r\n        <tr> \r\n          <td bgcolor="#EBF3FA"> \r\n            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">\r\n              <tr> \r\n                <td>\xa1\xf2\xd2\xeb\xa1\xa1\xa1\xa1\xc3\xfb\xa1\xa1\xc9\xf1\xc6\xe6\xcb\xc4\xcf\xc02<br />\r\n\xa1\xf2\xc6\xac\xa1\xa1\xa1\xa1\xc3\xfb\xa1\xa14: Rise of the Silver Surfer <br />\r\n\xa1\xf2\xc4\xea\xa1\xa1\xa1\xa1\xb4\xfa\xa1\xa12007<br />\r\n\xa1\xf2\xb9\xfa\xa1\xa1\xa1\xa1\xbc\xd2\xa1\xa1\xc3\xc0\xb9\xfa/\xb5\xc2\xb9\xfa/\xd3\xa2\xb9\xfa<br />\r\n\xa1\xf2\xc0\xe0\xa1\xa1\xa1\xa1\xb1\xf0\xa1\xa1\xb6\xaf\xd7\xf7/\xc3\xb0\xcf\xd5/\xbb\xc3\xcf\xeb/\xbf\xc6\xbb\xc3<br />\r\n\xa1\xf2\xd3\xef\xa1\xa1\xa1\xa1\xd1\xd4\xa1\xa1\xd3\xa2\xd3\xef<br />\r\n\xa1\xf2\xd7\xd6\xa1\xa1\xa1\xa1\xc4\xbb\xa1\xa1\xd6\xd0\xd3\xa2\xcb\xab</td>\r\n              </tr>\r\n              <tr>\r\n                <td><a href="/gq/2011-08-06/15707.html" target="_blank">/gq/2011-08-06/15707.html</a></td>\r\n              </tr>\r\n            </table>\r\n\t\t\t</td>\r\n        </tr>\r\n      </table>\r\n                       \r\n                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">\r\n        <tr> \r\n          <td><div align="center">\r\n\t\t\t  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">\r\n                <tr> \r\n                  \r\n            <td width="41%" height="25"><font color="#663333">\xa1\xa4[<a href=/gq/>\xbe\xad\xb5\xe4\xb8\xdf\xc7\xe5\xb5\xe7\xd3\xb0</a>]<span class="blue14"><a href=/gq/2009-01-09/5333.html target=_blank>\xbe\xad\xb5\xe4\xbf\xc6\xbb\xc3\xa1\xb6\xc9\xf1\xc6\xe6\xcb\xc4\xcf\xc01\xa1\xb7720p.\xb9\xfa\xd3\xa2\xcb\xab\xd3\xef.BD\xd6\xd0\xd3\xa2\xcb\xab\xd7\xd6\xb8\xdf\xc7\xe5MKV\xb0\xe6</a></span></font></td>\r\n                  <td width="59%"><font color="#666666">\xb7\xa2\xb2\xbc\xca\xb1\xbc\xe4\xa3\xba2013-07-14 00:25:03</font></td>\r\n                </tr>\r\n              </table>\r\n            </div></td>\r\n        </tr>\r\n        <tr> \r\n          <td bgcolor="#EBF3FA"> \r\n            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">\r\n              <tr> \r\n                <td>\xa1\xbe\xd6\xd0\xce\xc4\xa1\xa1\xc3\xfb\xa1\xbf\xc9\xf1\xc6\xe6\xcb\xc4\xcf\xc0/\xbe\xaa\xc6\xe64\xb3\xac\xc8\xcb/F4\xb3\xac\xc8\xcb/\xb3\xac\xc8\xcb\xd7\xdc\xb6\xaf\xd4\xb1<br />\r\n\xa1\xbe\xc6\xac\xa1\xa1\xa1\xa1\xc3\xfb\xa1\xbfFantastic Four<br />\r\n\xa1\xbe\xc4\xea\xa1\xa1\xa1\xa1\xb4\xfa\xa1\xbf2005<br />\r\n\xa1\xbe\xb9\xfa\xa1\xa1\xa1\xa1\xbc\xd2\xa1\xbf\xb5\xc2\xb9\xfa/\xc3\xc0\xb9\xfa<br />\r\n\xa1\xbe\xc0\xe0\xa1\xa1\xa1\xa1\xb1\xf0\xa1\xbf\xc3\xb0\xcf\xd5/\xbb\xc3\xcf\xeb/\xbf\xc6\xbb\xc3/\xb6\xaf\xd7\xf7<br />\r\n\xa1\xbe\xd3\xef\xa1\xa1\xa1\xa1\xd1\xd4\xa1\xbf\xd3\xa2\xd3\xef<br />\r\n\xa1\xbeIMDB\xc6\xc0\xb7\xd6</td>\r\n              </tr>\r\n              <tr>\r\n                <td><a href="/gq/2009-01-09/5333.html" target="_blank">/gq/2009-01-09/5333.html</a></td>\r\n              </tr>\r\n            </table>\r\n\t\t\t</td>\r\n        </tr>\r\n      </table>\r\n                       \r\n                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">\r\n        <tr> \r\n          <td><div align="center">\r\n\t\t\t  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">\r\n                <tr> \r\n                  \r\n            <td width="41%" height="25"><font color="#663333">\xa1\xa4[<a href=/gydy/>\xb9\xfa\xd3\xef\xc5\xe4\xd2\xf4\xb5\xe7\xd3\xb0</a>]<span class="blue14"><a href=/gydy/2008-12-11/4871.html target=_blank><strong><font color=\'#1111EE\'>[\xc9\xf1\xc6\xe6\xcb\xc4\xcf\xc02 DVD\xb9\xfa\xd3\xef\xc5\xe4\xd2\xf4][\xbe\xad\xb5\xe4\xbf\xc6\xbb\xc3\xb4\xf3\xc6\xac]</font></strong></a></span></font></td>\r\n                  <td width="59%"><font color="#666666">\xb7\xa2\xb2\xbc\xca\xb1\xbc\xe4\xa3\xba2008-12-11 09:49:58</font></td>\r\n                </tr>\r\n              </table>\r\n            </div></td>\r\n        </tr>\r\n        <tr> \r\n          <td bgcolor="#EBF3FA"> \r\n            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">\r\n              <tr> \r\n                <td>[\xc9\xf1\xc6\xe6\xcb\xc4\xcf\xc02 DVD\xb9\xfa\xd3\xef\xc5\xe4\xd2\xf4][\xbe\xad\xb5\xe4\xbf\xc6\xbb\xc3\xb4\xf3\xc6\xac]</td>\r\n              </tr>\r\n              <tr>\r\n                <td><a href="/gydy/2008-12-11/4871.html" target="_blank">/gydy/2008-12-11/4871.html</a></td>\r\n              </tr>\r\n            </table>\r\n\t\t\t</td>\r\n        </tr>\r\n      </table>\r\n                       </td>\r\n                  </tr>\r\n                  <tr> \r\n                    <td height="100%" valign="top"> <div align="center"></div></td>\r\n                  </tr>\r\n                  <tr> \r\n                    <td height="12" valign="top"></td>\r\n                  </tr>  \r\n</div>\r\n</div>\r\n\r\n<div id="footer">\r\n\t<p class="t"><a href="/index.html">\xcd\xf8\xd5\xbe\xc1\xf4\xd1\xd4</a> - <a href="/index.html">\xb9\xd8\xd3\xda\xce\xd2\xc3\xc7</a> - <a href="/index.html">\xb9\xe3\xb8\xe6\xd2\xb5\xce\xf1</a> - <a href="/index.html">\xd0\xc5\xcf\xa2\xb7\xb4\xc0\xa1</a> - <a href="/index.html">\xba\xcf\xd7\xf7\xbb\xef\xb0\xe9</a> - <a href="/index.html">\xcd\xf8\xd5\xbe\xb5\xd8\xcd\xbc</a></p>\r\n\t<p>Copyright &copy; 2009 <a href="http://www.hao6v.com"><b><font color=red>6VHAO</font>.COM</b></a> \xb0\xe6\xc8\xa8\xcb\xf9\xd3\xd0<br />\r\n\t  \xd3\xe5ICP\xb1\xb809051310\xba\xc5\r\n</div>\r\n<span class="hidden"><script src=/d/tj.js></script></span>\r\n'
# m = m.decode("gbk")
#
# html = etree.HTML(m)
# con_list = html.xpath("//table//font[1]/span/a/font")
# print(con_list)

ret = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>2018¸ß·Ö¶¯»­¡¶Ö©ÖëÏÀ£ºÆ½ÐÐÓîÖæ.¼Ó³¤°æ¡·1080p.BDÖÐÓ¢Ë«×Ö£¬Ãâ·ÑÏÂÔØ£¬Ñ¸À×ÏÂÔØ£¬¶¯»­µçÓ°£¬6vµçÓ°ÏÂÔØÍø</title>
<meta name="keywords" content="2018¸ß·Ö¶¯»­¡¶Ö©ÖëÏÀ£ºÆ½ÐÐÓîÖæ.¼Ó³¤°æ¡·1080p.BDÖÐÓ¢Ë«×ÖÏÂÔØ£¬2018¸ß·Ö¶¯»­¡¶Ö©ÖëÏÀ£ºÆ½ÐÐÓîÖæ.¼Ó³¤°æ¡·1080p.BDÖÐÓ¢Ë«×ÖÑ¸À×ÏÂÔØ" />
<meta name="description" content="¡òÒë¡¡¡¡Ãû¡¡Ö©ÖëÏÀ£ºÆ½ÐÐÓîÖæ / Spider-Man: a New Universe / Ö©ÖëÈË£ºÐÂÓîÖæ(Ì¨) / Ö©ÖëÏÀ£ºÆ½ÐÐÊÀ½ç / Ö©ÖëÏÀ£ºÐÂ¼ÍÔª / Ö©ÖëÏÀ£ºÌøÈëÖ©ÖëÓîÖæ(¸Û)<br />
¡òÆ¬¡¡¡¡Ãû¡¡Spider-Man: Into the Spider-Verse<br />
¡òÄê¡¡¡¡´ú¡¡2018<br />
¡ò²ú¡¡¡¡µØ¡¡ÃÀ¹ú<br />
¡òÀà¡¡¡¡±ð¡¡¶¯×÷ / ¿Æ»Ã / ¶¯»­ / Ã°ÏÕ<br />
¡òÓï¡¡¡¡ÑÔ¡¡Ó¢Óï / Î÷°àÑÀÓï<br />
¡ò×Ö¡¡¡¡Ä»¡¡ÖÐÓ¢Ë«×Ö<br />
¡òÉÏÓ³ÈÕÆÚ¡¡2018-12-14(ÃÀ¹ú) / 2018-12-21(ÖÐ¹ú´óÂ½)<br />
¡òIMDbÆÀ·Ö¡¡8.7/10 from 96568 users<br />
¡ò¶¹°êÆÀ·Ö¡¡8.7/10 from 207368 users<br />
¡òÆ¬¡¡¡¡³¤¡¡116·ÖÖÓ(ÖÐ¹ú´óÂ½)<br />
¡òµ¼¡¡¡¡ÑÝ¡¡±«²ª&amp;middot;Åå¶ûÎ÷¿­µÙ Bob Persichetti / ±ËµÃ&amp;middot;À­Ä·Æë Peter Ramsey / ÂÞµÂÄá&amp;middot;ÂÞË¹Âü Rodney Rothman<br />
¡ò±à¡¡¡¡¾ç¡¡·Æ¶û&amp;middot;ÂÞµÂ Phil Lord / ÂÞµÂÄá&amp;middot;ÂÞË¹Âü Rodney Rothman / ²¼À³¶÷&amp;middot;±¾µÏË¹ Brian Bendis / ÈøÀ­&amp;middot;Æ¤¿­Àû Sara Pichelli / Ê·µÙ·ò&amp;middot;µÏÌØ¿Ü Steve Ditko / Ë¹Ì¹&amp;middot;Àî Stan Lee / David Hine / Fabrice Sapolsky<br />
¡òÖ÷¡¡¡¡ÑÝ¡¡É³Ã·¿Ë&amp;middot;Ä¦¶û Shameik Moore<br />
¡¡¡¡¡¡¡¡¡¡¡¡½Ü¿Ë&amp;middot;Ô¼º²Ñ· Jake M. Johnson<br />
¡¡¡¡¡¡¡¡¡¡¡¡º£Àò&amp;middot;Ë¹Ì¹·Æ¶ûµÂ Hailee Steinfeld<br />
¡¡¡¡¡¡¡¡¡¡" />
<link rel="stylesheet" rev="stylesheet" href="/images/style.css" type="text/css" />
<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7" />
</head>
<body>
	<div id="header"><div id="top"> <a href="http://www.hao6v.com/">Ê×Ò³</a>
<a href="http://www.hao6v.com/dy/2012-12-07/19512.html" target=_blank>¹«¸æÇø</a>&nbsp;&nbsp;<a href="http://www.hao6v.com/dy/2019-01-02/32524.html" target="_blank">¶¹°ê2018°ñµ¥</a>&nbsp;&nbsp;<a href="https://www.66s.cc/" target=_blank>ÔÚÏß¹Û¿´</a>&nbsp;&nbsp;
<a href="http://www.hao6v.com/gq/2012-09-01/18841.html" target=_blank><font color='#FF0000'>6vµçÓ°ÅÅÐÐ°ñ</font></a>&nbsp;&nbsp;
<a href="http://www.hao6v.com/dy/2011-09-20/16090.html" target=_blank>±±ÃÀÆ±·¿ÅÅÐÐ°ñ</a>&nbsp;&nbsp;
<a href="http://www.hao6v.com/s/007/" target=_blank>007µçÓ°È«¼¯</a>&nbsp;&nbsp;
<a href="http://www.hao6v.com/s/gf250/" target=_blank>IMDB250µçÓ°</a>&nbsp;&nbsp;
<a href="/s/gf/" target=_blank>¸ßÆÀ·ÖµçÓ°</a>&nbsp;&nbsp;
<a href="/s/hanguodianying/" target=_blank>ÃÀ¹úµçÓ°</a>&nbsp;&nbsp;<a href="/s/xijudianying/" target=_blank>Å·ÖÞµçÓ°</a>&nbsp;&nbsp;<a href="/s/yazhoudianying/" target=_blank>ÑÇÖÞµçÓ°</a>&nbsp;&nbsp;<a href="/s/mzdy/" target=_blank>ÃÀÖÞµçÓ°</a> &nbsp;<a href="http://www.hao6v.com/e/tool/gbook/?bid=1" target=_blank>·Ã¿ÍÁôÑÔ</a></div>
    	<div class="log"><a href="/">6VµçÓ°</a></div>
        <div class="topad"><script src="/d/f4.js"></script></div>
<div class="cr"></div>
        <div id="menu">
      <p><a href="http://www.hao6v.com/">Ê×Ò³</a>  <a href="http://www.hao6v.com/dy/" target=_blank>2019×îÐÂµçÓ°</a> <a href="http://www.hao6v.com/gydy/" target=_blank>¹úÓïÅäÒôµçÓ°</a> <a href="http://www.hao6v.com/zydy/" target=_blank>Î¢µçÓ°</a> <a href="http://www.hao6v.com/gq/" target=_blank>¾­µä¸ßÇåµçÓ°</a> <a href="http://www.hao6v.com/jddy/" target=_blank>¶¯»­µçÓ°</a> <a href="http://www.hao6v.com/3D/" target=_blank>3DµçÓ°</a> <a href="http://www.hao6v.com/s/shoujiMP4dianying/" target=_blank>MP4ÊÖ»úµçÓ°</a> <a href="http://www.hao6v.com/dlz/" target=_blank>¹ú¾ç</a> <a href="http://www.hao6v.com/rj/" target=_blank>ÈÕº«¾ç</a> <a href="http://www.hao6v.com/mj/" target=_blank>Å·ÃÀ¾ç</a> <a href="http://www.hao6v.com/zy/" target=_blank>×ÛÒÕ½ÚÄ¿</a> <a href="http://www.hao6v.com/s/gangtaidianying/" target=_blank>¸ÛÌ¨µçÓ°</a> <a href="http://www.hao6v.com/s/jingdiandianying/" target=_blank>ÈÕº«µçÓ°</a> </p>
      <p class="bg"><a href="http://www.66ys.tv/" target=_blank>66Ó°ÊÓÍø</a> ×¨Ìâ·ÖÀà£º<a href="http://www.hao6v.com/s/xiju/" target=_blank>Ï²¾ç</a><a href="http://www.hao6v.com/s/dongzuo/" target=_blank>¶¯×÷</a><a href="http://www.hao6v.com/s/aiqing/" target=_blank>°®Çé</a><a href="http://www.hao6v.com/s/kehuan/" target=_blank>¿Æ»Ã</a><a href="http://www.hao6v.com/s/qihuan/" target=_blank>Ææ»Ã</a><a href="http://www.hao6v.com/s/shenmi/" target=_blank>ÉñÃØ</a><a href="http://www.hao6v.com/s/huanxiang/" target=_blank>»ÃÏë</a><a href="http://www.hao6v.com/s/kongbu/" target=_blank>¿Ö²À</a><a href="http://www.hao6v.com/s/zhanzheng/" target=_blank>Õ½Õù</a><a href="http://www.hao6v.com/s/maoxian/" target=_blank>Ã°ÏÕ</a><a href="http://www.hao6v.com/s/jingsong/" target=_blank>¾ªã¤</a><a href="http://www.hao6v.com/s/juqingpian/" target=_blank>¾çÇé</a><a href="http://www.hao6v.com/s/zhuanji/" target=_blank>´«¼Ç</a><a href="http://www.hao6v.com/s/lishi/" target=_blank>ÀúÊ·</a><a href="http://www.hao6v.com/s/jilu/" target=_blank>¼ÍÂ¼</a><a href="http://www.hao6v.com/s/yindudianying/" target=_blank>Ó¡¶ÈµçÓ°</a>  <a href="http://www.hao6v.com/s/guochandianying/" target=_blank>¹ú²úµçÓ°</a> <a href="http://www.hao6v.com/s/xijudianying/" target=_blank>Å·ÖÞµçÓ°</a> <a href="http://www.hao6v.com/s/zhuanti/" target=_blank>×¨ÌâÍÆ¼ö</a> </p>
        </div>
  </div>

<div id="a960"><script src="/d/f1.js"></script> <script src="/d/f2.js"></script></div>
<div id="search">
<div class="ser">
<form action="http://so.hao6v.com/e/search/index.php" method="post" name="searchform" id="searchform">
<input type="hidden" name="show" value="title,smalltext" />
<input type="hidden" name="tempid" value="1" />

<span>Õ¾ÄÚËÑË÷£º<input name="keyboard" type="text" size="32" id="keyboard" class="inputText" /></span>
<span class="sect"><select name="tbname">
<option value="article">È«Õ¾</option>
</select></span>
<span><input type="image" class="inputSub" src="/images/search.gif" /></span>
</form>
</span>
</div>
<div class="help">
<a href="http://www.hao6v.com/dy/2010-10-11/12868.html" target="_blank">6vµçÓ°ÏÂÔØ°ïÖúÓë½Ì³Ì<br /><font color='#FF0000'>ÎÞ·¨ÏÂÔØµÄ½øÀ´¿´¿´</font></a>
</div>
<INPUT type="button" value='ÊÕ²Ø±¾Ó°Æ¬' id="copy" onclick="javascript:d=document;window.external.AddFavorite(''+d.location.href+'', ''+d.title+'')">
<div class="help"><div class="bdsharebuttonbox"><a href="#" class="bds_more" data-cmd="more"></a><a href="#" class="bds_bdhome" data-cmd="bdhome" title="·ÖÏíµ½°Ù¶ÈÐÂÊ×Ò³"></a><a href="#" class="bds_sqq" data-cmd="sqq" title="·ÖÏíµ½QQºÃÓÑ"></a><a href="#" class="bds_weixin" data-cmd="weixin" title="·ÖÏíµ½Î¢ÐÅ"></a><a href="#" class="bds_douban" data-cmd="douban" title="·ÖÏíµ½¶¹°êÍø"></a><a href="#" class="bds_mshare" data-cmd="mshare" title="·ÖÏíµ½Ò»¼ü·ÖÏí"></a><a href="#" class="bds_qzone" data-cmd="qzone" title="·ÖÏíµ½QQ¿Õ¼ä"></a><a href="#" class="bds_tsina" data-cmd="tsina" title="·ÖÏíµ½ÐÂÀËÎ¢²©"></a><a href="#" class="bds_tieba" data-cmd="tieba" title="·ÖÏíµ½°Ù¶ÈÌù°É"></a><a href="#" class="bds_tqq" data-cmd="tqq" title="·ÖÏíµ½ÌÚÑ¶Î¢²©"></a></div>
<script>window._bd_share_config={"common":{"bdSnsKey":{},"bdText":"","bdMini":"1","bdMiniList":false,"bdPic":"","bdStyle":"0","bdSize":"16"},"share":{}};with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion='+~(-new Date()/36e5)];</script></div></div>
<div id="main">
	<div class="col6">
    	<div class="box">
        	<div class="t">ÄúµÄÎ»ÖÃ£º<a href="http://www.hao6v.com/index.html">Ê×Ò³</a>&nbsp;>&nbsp;<a href="http://www.hao6v.com/jddy/">¶¯»­µçÓ°</a> > ÏÂÔØÒ³Ãæ</div>
            	<h1>2018¸ß·Ö¶¯»­¡¶Ö©ÖëÏÀ£ºÆ½ÐÐÓîÖæ.¼Ó³¤°æ¡·1080p.BDÖÐÓ¢Ë«×Ö</h1>

<div id="endText"><div class="fl"><script type="text/javascript" src="http://www.hao6v.com/d/gg3001.js"></script></div><div class="fr"><script type="text/javascript" src="http://www.hao6v.com/d/js/acmsd/thea3.js"></script></div><div class="cr"></div><br />
<strong><a href="http://www.hao6v.com/jddy/2018-12-27/ZZXPXYZ.html">2018¸ß·Ö¶¯»­¡¶Ö©ÖëÏÀ£ºÆ½ÐÐÓîÖæ.¼Ó³¤°æ¡·1080p.BDÖÐÓ¢Ë«×Ö</a> - ÄÚÈÝ½éÉÜ£º</strong>
<p><img alt="" src="https://tu.66vod.net/2018/5452.jpg" /></p>
<p><br />
¡òÒë¡¡¡¡Ãû¡¡Ö©ÖëÏÀ£ºÆ½ÐÐÓîÖæ / Spider-Man: a New Universe / Ö©ÖëÈË£ºÐÂÓîÖæ(Ì¨) / Ö©ÖëÏÀ£ºÆ½ÐÐÊÀ½ç / Ö©ÖëÏÀ£ºÐÂ¼ÍÔª / Ö©ÖëÏÀ£ºÌøÈëÖ©ÖëÓîÖæ(¸Û)<br />
¡òÆ¬¡¡¡¡Ãû¡¡Spider-Man: Into the Spider-Verse<br />
¡òÄê¡¡¡¡´ú¡¡2018<br />
¡ò²ú¡¡¡¡µØ¡¡<a href="http://www.hao6v.com/s/hanguodianying/" target="_blank"  title="ÃÀ¹úµçÓ°">ÃÀ¹ú</a><br />
¡òÀà¡¡¡¡±ð¡¡<a href="http://www.hao6v.com/s/dongzuo/" target="_blank"  title="¶¯×÷Æ¬">¶¯×÷</a> / <a href="http://www.hao6v.com/s/kehuan/" target="_blank"  title="¿Æ»ÃÆ¬">¿Æ»Ã</a> / <a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a> / <a href="http://www.hao6v.com/s/maoxian/" target="_blank"  title="Ã°ÏÕÆ¬">Ã°ÏÕ</a><br />
¡òÓï¡¡¡¡ÑÔ¡¡Ó¢Óï / Î÷°àÑÀÓï<br />
¡ò×Ö¡¡¡¡Ä»¡¡ÖÐÓ¢Ë«×Ö<br />
¡òÉÏÓ³ÈÕÆÚ¡¡2018-12-14(<a href="http://www.hao6v.com/s/hanguodianying/" target="_blank"  title="ÃÀ¹úµçÓ°">ÃÀ¹ú</a>) / 2018-12-21(<a href="http://www.hao6v.com/s/guochandianying/" target="_blank"  title="¹ú²úµçÓ°">ÖÐ¹ú</a>´óÂ½)<br />
¡òIMDbÆÀ·Ö¡¡8.7/10 from 96568 users<br />
¡ò¶¹°êÆÀ·Ö¡¡8.7/10 from 207368 users<br />
¡òÆ¬¡¡¡¡³¤¡¡116·ÖÖÓ(<a href="http://www.hao6v.com/s/guochandianying/" target="_blank"  title="¹ú²úµçÓ°">ÖÐ¹ú</a>´óÂ½)<br />
¡òµ¼¡¡¡¡ÑÝ¡¡±«²ª&middot;Åå¶ûÎ÷¿­µÙ Bob Persichetti / ±ËµÃ&middot;À­Ä·Æë Peter Ramsey / ÂÞµÂÄá&middot;ÂÞË¹Âü Rodney Rothman<br />
¡ò±à¡¡¡¡¾ç¡¡·Æ¶û&middot;ÂÞµÂ Phil Lord / ÂÞµÂÄá&middot;ÂÞË¹Âü Rodney Rothman / ²¼À³¶÷&middot;±¾µÏË¹ Brian Bendis / ÈøÀ­&middot;Æ¤¿­Àû Sara Pichelli / Ê·µÙ·ò&middot;µÏÌØ¿Ü Steve Ditko / Ë¹Ì¹&middot;Àî Stan Lee / David Hine / Fabrice Sapolsky<br />
¡òÖ÷¡¡¡¡ÑÝ¡¡É³Ã·¿Ë&middot;Ä¦¶û Shameik Moore<br />
¡¡¡¡¡¡¡¡¡¡¡¡½Ü¿Ë&middot;Ô¼º²Ñ· Jake M. Johnson<br />
¡¡¡¡¡¡¡¡¡¡¡¡º£Àò&middot;Ë¹Ì¹·Æ¶ûµÂ Hailee Steinfeld<br />
¡¡¡¡¡¡¡¡¡¡¡¡ÂíºÕÉ³À­&middot;°¢Àï Mahershala Ali<br />
¡¡¡¡¡¡¡¡¡¡¡¡²¼À³¶÷&middot;Ì©Àï&middot;ºàÀû Brian Tyree Henry<br />
¡¡¡¡¡¡¡¡¡¡¡¡ÀòÀò&middot;ÌÀÄ·ÁÖ Lily Tomlin<br />
¡¡¡¡¡¡¡¡¡¡¡¡ÀÍÂ×&middot;Î¬ÀÕË¹ Lauren V&eacute;lez<br />
¡¡¡¡¡¡¡¡¡¡¡¡×ôÒÁ&middot;¿ËÂÞÎ¬×È Zo&euml; Kravitz<br />
¡¡¡¡¡¡¡¡¡¡¡¡Ô¼º²&middot;Ä¾À¼Äá John Mulaney<br />
¡¡¡¡¡¡¡¡¡¡¡¡½ð¿É&middot;¸ñÂ× Kimiko Glenn<br />
¡¡¡¡¡¡¡¡¡¡¡¡Äá¹ÅÀ­Ë¹&middot;¿­Ææ Nicolas Cage<br />
¡¡¡¡¡¡¡¡¡¡¡¡¿­ÉªÁÕ&middot;¹þ¶÷ Kathryn Hahn<br />
¡¡¡¡¡¡¡¡¡¡¡¡ÁÐÎ¬&middot;Ê©Èð²©¶û Liev Schreiber<br />
¡¡¡¡¡¡¡¡¡¡¡¡¿ËÀïË¹&middot;ÅÉ¶÷ Chris Pine<br />
¡¡¡¡¡¡¡¡¡¡¡¡ÄÈËþÀö&middot;ÄªÈðË¿ Natalie Morales<br />
¡¡¡¡¡¡¡¡¡¡¡¡°ÂË¹¿¨&middot;ÒÁÈø¿Ë Oscar Isaac<br />
¡¡¡¡¡¡¡¡¡¡¡¡¸ñÀïËþ&middot;Àî Greta Lee<br />
¡¡¡¡¡¡¡¡¡¡¡¡Ë¹Ì¹&middot;Àî Stan Lee<br />
¡¡¡¡¡¡¡¡¡¡¡¡ÇÇÂê&middot;Ëþ¿ÆÄÚ Jorma Taccone<br />
¡¡¡¡¡¡¡¡¡¡¡¡»ª½ð&middot;¿ÆÎ÷°Â Joaqu&iacute;n Cosio<br />
¡¡¡¡¡¡¡¡¡¡¡¡ÀÙ¿Ë&middot;±´¶û Lake Bell<br />
¡¡¡¡¡¡¡¡¡¡¡¡Ã·ÀÕÄÝ&middot;º£¶÷Ë¹ Melanie Haynes<br />
¡¡¡¡¡¡¡¡¡¡¡¡Äá¿Ë&middot;½Ü¶÷ Nick Jaine<br />
¡¡¡¡¡¡¡¡¡¡¡¡ÄÂÄá²·&middot;À­ºÕÂü Muneeb Rehman<br />
¡¡¡¡¡¡¡¡¡¡¡¡Carlos Zaragoza<br />
¡¡¡¡¡¡¡¡¡¡¡¡÷ìÎ÷&middot;ÂÞË¹&middot;²¼À³ÄÚË¹ Darcy Rose Byrnes<br />
¡¡¡¡¡¡¡¡¡¡¡¡Àï·ò&middot;»ô¶Ù Rif Hutton<br />
¡¡¡¡¡¡¡¡¡¡¡¡¹þÀïÉ­&middot;ÄÎÌØ Harrison Knight<br />
¡¡¡¡¡¡¡¡¡¡¡¡À³¿ËË¹&middot;ÀÊ Lex Lang<br />
¡¡¡¡¡¡¡¡¡¡¡¡¿­ÌØÁÕ&middot;Âó¿ÏÄÉ-Íþ¶û½ðÉ­ Caitlin McKenna-Wilkinson<br />
¡¡¡¡¡¡¡¡¡¡¡¡Ë¹¿ÆÌØ&middot;ÃÅÎ¬¶û Scott Menville<br />
¡¡¡¡¡¡¡¡¡¡¡¡¿ËÀïË¹ÍÐ¸¥&middot;Ã×ÀÕ Christopher Miller<br />
¡¡¡¡¡¡¡¡¡¡¡¡µÂÎ¬¿¨&middot;ÅÁÀûºÕ Devika Parikh<br />
¡¡¡¡¡¡¡¡¡¡¡¡¿ÂÌØÄÝ&middot;Åå¶û¶Ù Courtney Peldon<br />
¡¡¡¡¡¡¡¡¡¡¡¡¿ËÀïË¹µÙ&middot;·¨ÈðË¹ Chrystee Pharris<br />
¡¡¡¡¡¡¡¡¡¡¡¡½Ü¿üÁÕ&middot;Æ¤Åµ¶û Jacqueline Pinol<br />
¡¡¡¡¡¡¡¡¡¡¡¡¼ÖË¹Í¡&middot;³Á¿¨ÂÞ Justin Shenkarow<br />
¡¡¡¡¡¡¡¡¡¡¡¡Ã·ÀûÉ¯&middot;Ë¹ÌØÄ· Melissa Sturm</p>
<p>¡ò¼ò¡¡¡¡½é<br />
¡¡¡¡Âõ¶ûË¹£¨É³Ã·¿Ë&middot;Ä¦¶û ÅäÒô£©µÄ¸¸Ç×ÊÇÒ»Î»Ò»°åÒ»ÑÛµÄ¾¯¹Ù£¬¶øËûµÄÄ¸Ç×ÔòÊÇÒ»Ãû¹¤×÷ÇÚ·ÜµÄ»¤Ê¿¡£´È°®µÄ¸¸Ä¸¶ÔÓÚº¢×ÓµÄ³É¾Í·Ç³£×ÔºÀ£¬Ò²Ï£ÍûËûÄÜ¹»ÈÚÈëÐÂ¼ÓÈëµÄÕâËùÓÅÐãµÄÑ§Ð££¬ÔÚÕâÀïÈ¡µÃ³É¹¦¡£È»¶øÂõ¶ûË¹µÄÉú»îÒòÎªÒ»´ÎÒâÍâ±äµÃ¸ü¼Ó¸´ÔÓ¡£Ëû±»Ò»Ö»·ÅÉäÐÔÖ©ÖëÒ§ÉË£¬²¢Òò´Ë»ñµÃÁË¶¾Òº³å»÷¡¢Î±×°Òþ²Ø¡¢Ö©ÖëÅÀÐÐ¡¢³¬·²ÌýÁ¦¡¢Ö©Öë¸ÐÓ¦µÈÒ»ÏµÁÐ³¬ÄÜÁ¦¡£Óë´ËÍ¬Ê±£¬Õâ×ù³ÇÊÐÀï×î³ôÃûÕÑ×ÅµÄ<a href="http://www.hao6v.com/e/search/result/?searchid=283788" target="_blank"  title="·¸×ïÆ¬">·¸×ï</a>Í·Ä¿½ð²¢£¨ÁÐÎ¬&middot;Ê©Èð²©¶û ÅäÒô£©ÒÑ¾­½¨Á¢ÆðÒ»Ì¨¸ß¶ÈÒþÃØµÄ³¬¼¶¶Ô×²»ú£¬ÕâÌ¨¶Ô×²»ú¿ªÆôÁËÍ¨ÍùÆäËûÓîÖæµÄÊ±¿ÕÍ¨µÀ£¬À´×ÔÆäËûÓîÖæ¡¢²»Í¬°æ±¾µÄÖ©ÖëÏÀ£¨°üÀ¨ÖÐÄê±ËµÃ&middot;ÅÁ¿Ë¡¢Å®Ö©ÖëÏÀ¸ñÎÂ¡¢°µÓ°Ö©ÖëÏÀ¡¢Ö©ÖíÏÀºÍÅËÄÝ&middot;ÅÁ¿Ë£©Ò²À´µ½ÁËÂõ¶ûË¹ËùÔÚµÄÊÀ½ç¡£ÔÚÕâÐ©ÐÂÀÏ½ÇÉ«µÄ°ïÖúÏÂ£¬Âõ¶ûË¹ÂýÂýÑ§Ï°¡¢Öð½¥½ÓÊÜÌôÕ½£¬Ò²Ñ§»áÁË×÷ÎªÒ»Ãû³¬¼¶Ó¢ÐÛËùÒª³Ðµ£µÄÔðÈÎ¡£Ëû×îÖÕÒâÊ¶µ½£¬ÈÎºÎÈË¶¼¿ÉÒÔ´÷ÉÏ³¬¼¶Ó¢ÐÛµÄÃæ¾ß£¬ÎªÕýÒå¶øÕ½&hellip;&hellip;</p>
<p>¡ò»ñ½±Çé¿ö<br />
¡¡¡¡µÚ91½ì°ÂË¹¿¨½ðÏñ½±(2019)<br />
¡¡¡¡×î¼Ñ<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>³¤Æ¬(ÌáÃû) ±«²ª&middot;Åå¶ûÎ÷¿­µÙ / ·Æ¶û&middot;ÂÞµÂ / ÂÞµÂÄá&middot;ÂÞË¹Âü / ¿ËÀïË¹ÍÐ¸¥&middot;Ã×ÀÕ / ±ËµÃ&middot;À­Ä·Æë</p>
<p>¡¡¡¡µÚ76½ì½ðÇò½±(2019)<br />
¡¡¡¡µçÓ°Àà ×î¼Ñ<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>³¤Æ¬</p>
<p>¡¡¡¡µÚ72½ìÓ¢¹úµçÓ°Ñ§Ôº½±(2019)<br />
¡¡¡¡µçÓ°½± ×î¼Ñ<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>Æ¬</p>
<p>¡¡¡¡µÚ46½ì<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>°²ÄÝ½±(2019)<br />
¡¡¡¡×î¼Ñ<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>³¤Æ¬<br />
¡¡¡¡×î¼Ñµ¼ÑÝ ±«²ª&middot;Åå¶ûÎ÷¿­µÙ / ÂÞµÂÄá&middot;ÂÞË¹Âü / ±ËµÃ&middot;À­Ä·Æë<br />
¡¡¡¡×î¼Ñ±à¾ç ·Æ¶û&middot;ÂÞµÂ / ÂÞµÂÄá&middot;ÂÞË¹Âü<br />
¡¡¡¡×î¼Ñ¼ô¼­<br />
¡¡¡¡×î¼ÑÒÕÊõÖ¸µ¼<br />
¡¡¡¡×î¼Ñ<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>½ÇÉ«<br />
¡¡¡¡×î¼Ñ½ÇÉ«Éè¼Æ</p>
<p>¡¡¡¡µÚ30½ì<a href="http://www.hao6v.com/s/hanguodianying/" target="_blank"  title="ÃÀ¹úµçÓ°">ÃÀ¹ú</a>ÖÆÆ¬ÈË¹¤»á½±(2019)<br />
¡¡¡¡×î¼Ñ<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>Æ¬ÖÆÆ¬ÈË½±</p>
<p>¡¡¡¡µÚ69½ì<a href="http://www.hao6v.com/s/hanguodianying/" target="_blank"  title="ÃÀ¹úµçÓ°">ÃÀ¹ú</a>¼ô¼­¹¤»á½±(2019)<br />
¡¡¡¡<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>Æ¬×î¼Ñ¼ô¼­ Robert Fisher Jr.</p>
<p>¡¡¡¡µÚ23½ì<a href="http://www.hao6v.com/s/hanguodianying/" target="_blank"  title="ÃÀ¹úµçÓ°">ÃÀ¹ú</a>ÒÕÊõÖ¸µ¼¹¤»á½±(2019)<br />
¡¡¡¡µçÓ°½± ×î¼Ñ<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>µçÓ°ÒÕÊõÖ¸µ¼(ÌáÃû) Justin Thompson</p>
<p>¡¡¡¡µÚ66½ì<a href="http://www.hao6v.com/s/hanguodianying/" target="_blank"  title="ÃÀ¹úµçÓ°">ÃÀ¹ú</a>ÒôÐ§¼ô¼­Ð­»á½±(2019)<br />
¡¡¡¡½ð¾íÖá½± ×î¼Ñ<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>Æ¬ÒôÐ§¼ô¼­<br />
¡¡¡¡½ð¾íÖá½± ×î¼ÑÅäÀÖ¼ô¼­</p>
<p>¡¡¡¡µÚ17½ì<a href="http://www.hao6v.com/s/hanguodianying/" target="_blank"  title="ÃÀ¹úµçÓ°">ÃÀ¹ú</a>ÊÓ¾õÐ§¹ûÐ­»á½±(2019)</p>
<p>¡¡¡¡×î¼Ñ<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>µçÓ°ÊÓ¾õÐ§¹û</p>
<p>¡¡¡¡×î¼Ñ<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>µçÓ°CG<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>½ÇÉ«</p>
<p>¡¡¡¡×î¼Ñ<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>µçÓ°CG±³¾°<br />
¡¡¡¡×î¼Ñ<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>µçÓ°Ä£Äâ<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>Ð§¹û</p>
<p>¡¡¡¡µÚ55½ì<a href="http://www.hao6v.com/s/hanguodianying/" target="_blank"  title="ÃÀ¹úµçÓ°">ÃÀ¹ú</a>ÉùÒôÐ§¹ûÐ­»á½±(2019)<br />
¡¡¡¡<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>µçÓ°×î¼ÑÒôÐ§(ÌáÃû)</p>
<p>¡¡¡¡µÚ84½ìÅ¦Ô¼Ó°ÆÀÈËÐ­»á½±(2018)<br />
¡¡¡¡×î¼Ñ<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>Æ¬</p>
<p>¡¡¡¡µÚ24½ì<a href="http://www.hao6v.com/s/hanguodianying/" target="_blank"  title="ÃÀ¹úµçÓ°">ÃÀ¹ú</a>ÆÀÂÛ¼ÒÑ¡ÔñµçÓ°½±(2019)<br />
¡¡¡¡×î¼Ñ<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>Æ¬</p>
<p>¡¡¡¡µÚ53½ì<a href="http://www.hao6v.com/s/hanguodianying/" target="_blank"  title="ÃÀ¹úµçÓ°">ÃÀ¹ú</a>¹ú¼ÒÓ°ÆÀÈËÐ­»á½±(2019)<br />
¡¡¡¡×î¼ÑÄÐÅä½Ç(ÌáÃû) ²¼À³¶÷&middot;Ì©Àï&middot;ºàÀû</p>
<p>¡¡¡¡µÚ17½ì»ªÊ¢¶ÙÓ°ÆÀÈËÐ­»á½±(2018)<br />
¡¡¡¡×î¼Ñ<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>Æ¬(ÌáÃû)<br />
¡¡¡¡×î¼ÑÅäÒô(ÌáÃû) É³Ã·¿Ë&middot;Ä¦¶û</p>
<p>¡¡¡¡µÚ44½ìÂåÉ¼í¶Ó°ÆÀÈËÐ­»á½±(2018)<br />
¡¡¡¡×î¼Ñ<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>Æ¬</p>
<p>¡¡¡¡µÚ31½ìÖ¥¼Ó¸çÓ°ÆÀÈËÐ­»á½±(2018)<br />
¡¡¡¡×î¼Ñ<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>Æ¬</p>
<p>¡¡¡¡µÚ17½ì¾É½ðÉ½Ó°ÆÀÈËÐ­»á½±(2018)<br />
¡¡¡¡×î¼Ñ<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>Æ¬</p>
<p>¡¡¡¡µÚ52½ì¿°ÈøË¹Ó°ÆÀÈËÐ­»á½±(2018)<br />
¡¡¡¡×î¼Ñ<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>Æ¬</p>
<p>&nbsp;<br />
¡¡¡¡µÚ12½ìµ×ÌØÂÉÓ°ÆÀÈËÐ­»á½±(2018)<br />
¡¡¡¡×î¼Ñ<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>Æ¬</p>
<p>¡¡¡¡µÚ22½ì<a href="http://www.hao6v.com/s/hanguodianying/" target="_blank"  title="ÃÀ¹úµçÓ°">ÃÀ¹ú</a>ÔÚÏßÓ°ÆÀÈËÐ­»á½±(2019)<br />
¡¡¡¡×î¼Ñ<a href="http://www.hao6v.com/jddy/" target="_blank"  title="¶¯»­µçÓ°">¶¯»­</a>Æ¬<br />
&nbsp;</p>
<p><img alt="" src="https://tu.66vod.net/2019/0504.jpg" /></p>
<p><img alt="" src="https://tu.66vod.net/2019/0784.jpg" /><hr />
</p>
<p><strong><span style="font-size: large"><span style="color: #ff0000">¡¾ÏÂÔØµØÖ·¡¿</span></span></strong></p>
<p>
<table cellspacing="1" cellpadding="10" width="100%" bgcolor="#0099cc" border="0">
    <tbody>
        <tr>
            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px">ÔÚÏß¹Û¿´£º<a target="_blank" href="https://www.66s.cc/donghuapian/10319.html">https://www.66s.cc/donghuapian/10319.html</a></td>
        </tr>
        <tr>
            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px">BT£º<a href="http://bt.pp63.org/2019/Ö©ÖëÏÀ£ºÆ½ÐÐÓîÖæ.¼Ó³¤°æ.1080p.BDÖÐÓ¢Ë«×Ö[×îÐÂµçÓ°www.66ys.tv].mp4.torrent">¼Ó³¤°æ.1080p.BDÖÐÓ¢Ë«×Ö.mp4</a></td>
        </tr>
        <tr>
            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px">´ÅÁ¦£º<a href="magnet:?xt=urn:btih:7R22KTKNHGLIYM3TPPRQ4P2YVRT5TPJG&amp;dn=%e8%9c%98%e8%9b%9b%e4%be%a0%ef%bc%9a%e5%b9%b3%e8%a1%8c%e5%ae%87%e5%ae%99%2e%e5%8a%a0%e9%95%bf%e7%89%88%2e1080p%2eBD%e4%b8%ad%e8%8b%b1%e5%8f%8c%e5%ad%97%5b%e6%9c%80%e6%96%b0%e7%94%b5%e5%bd%b1www%2e66ys%2etv%5d%2emp4&amp;tr=udp%3a%2f%2f9%2erarbg%2eto%3a2710%2fannounce&amp;tr=udp%3a%2f%2f9%2erarbg%2eme%3a2710%2fannounce&amp;tr=http%3a%2f%2ftr%2ecili001%2ecom%3a8070%2fannounce&amp;tr=http%3a%2f%2ftracker%2etrackerfix%2ecom%3a80%2fannounce&amp;tr=udp%3a%2f%2fopen%2edemonii%2ecom%3a1337&amp;tr=udp%3a%2f%2ftracker%2eopentrackr%2eorg%3a1337%2fannounce&amp;tr=udp%3a%2f%2fp4p%2earenabg%2ecom%3a1337">¼Ó³¤°æ.1080p.BDÖÐÓ¢Ë«×Ö.mp4</a></td>
        </tr>
        <tr>
            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px">µçÂ¿£º<a href="ed2k://|file|%E8%9C%98%E8%9B%9B%E4%BE%A0%EF%BC%9A%E5%B9%B3%E8%A1%8C%E5%AE%87%E5%AE%99.%E5%8A%A0%E9%95%BF%E7%89%88.1080p.BD%E4%B8%AD%E8%8B%B1%E5%8F%8C%E5%AD%97[%E6%9C%80%E6%96%B0%E7%94%B5%E5%BD%B1www.66ys.tv].mp4|2798423587|708A133B2641E8BFD562C165D5BF5D7E|h=S5TTJZ6SJ2ARRDS3VSVQ5AA2P2HUC7J3|/">¼Ó³¤°æ.1080p.BDÖÐÓ¢Ë«×Ö.mp4</a></td>
        </tr>
        <tr>
            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px">ÍøÅÌÁ´½Ó£º<a target="_blank" href="https://pan.baidu.com/s/1a4plv0hu6YkIy4lm5_KNmg">https://pan.baidu.com/s/1a4plv0hu6YkIy4lm5_KNmg</a> <br />
            ÌáÈ¡Âë£ºerfm <br />
            ¸´ÖÆÕâ¶ÎÄÚÈÝºó´ò¿ª°Ù¶ÈÍøÅÌÊÖ»úApp£¬²Ù×÷¸ü·½±ãÅ¶</td>
        </tr>
        <tr>
            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px"><a href="ed2k://|file|%E8%9C%98%E8%9B%9B%E4%BE%A0%EF%BC%9A%E5%B9%B3%E8%A1%8C%E5%AE%87%E5%AE%99.1080p.%E5%9B%BD%E8%8B%B1%E7%B2%A4%E5%8F%B0%E5%9B%9B%E8%AF%AD.BD%E7%89%B9%E6%95%88%E4%B8%AD%E8%8B%B1%E5%8F%8C%E5%AD%97%E6%97%A0%E6%B0%B4%E5%8D%B0[%E6%9C%80%E6%96%B0%E7%94%B5%E5%BD%B1www.66ys.tv].mkv|11254380505|62C6F9FDE10CD785F6BB55A1395C293E|h=GKXJ7N753KGV27WQCAYMABCNVMTAUI3A|/">Ö©ÖëÏÀ£ºÆ½ÐÐÓîÖæ.1080p.¹úÓ¢ÔÁÌ¨ËÄÓï.BDÌØÐ§ÖÐÓ¢Ë«×ÖÎÞË®Ó¡.mkv</a></td>
        </tr>
        <tr>
            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px">´ÅÁ¦£º<a href="magnet:?xt=urn:btih:SPGYDZOQK7XEWVIDDEV7IUFBFAWFDL4N&amp;dn=%e8%9c%98z%e4%be%a0%ef%bc%9a%e5%b9%b3x%e5%ae%87%e5%ae%99%2e1080p%2e%e5%9b%bd%e8%8b%b1%e5%8f%8c%e8%af%ad%2eBD%e4%b8%ad%e8%8b%b1%e5%8f%8c%e5%ad%97%5b%e6%9c%80%e6%96%b0%e7%94%b5%e5%bd%b1www%2e66ys%2etv%5d%2emp4&amp;tr=udp%3a%2f%2f9%2erarbg%2eto%3a2710%2fannounce&amp;tr=udp%3a%2f%2f9%2erarbg%2eme%3a2710%2fannounce&amp;tr=http%3a%2f%2ftr%2ecili001%2ecom%3a8070%2fannounce&amp;tr=http%3a%2f%2ftracker%2etrackerfix%2ecom%3a80%2fannounce&amp;tr=udp%3a%2f%2fopen%2edemonii%2ecom%3a1337&amp;tr=udp%3a%2f%2ftracker%2eopentrackr%2eorg%3a1337%2fannounce&amp;tr=udp%3a%2f%2fp4p%2earenabg%2ecom%3a1337">Ö©ÖëÏÀ£ºÆ½ÐÐÓîÖæ.1080p.¹úÓ¢Ë«Óï.BDÖÐÓ¢Ë«×Ö.mp4</a></td>
        </tr>
        <tr>
            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px">´ÅÁ¦£º<a href="magnet:?xt=urn:btih:J6LCECQ36TLPJKXTEDQAPNIHGWIGYZV3&amp;dn=%e8%9c%98z%e4%be%a0%ef%bc%9a%e5%b9%b3x%e5%ae%87%e5%ae%99%2e720p%2e%e5%9b%bd%e8%8b%b1%e5%8f%8c%e8%af%ad%2eBD%e4%b8%ad%e8%8b%b1%e5%8f%8c%e5%ad%97%5b%e6%9c%80%e6%96%b0%e7%94%b5%e5%bd%b1www%2e66ys%2etv%5d%2emp4&amp;tr=udp%3a%2f%2f9%2erarbg%2eto%3a2710%2fannounce&amp;tr=udp%3a%2f%2f9%2erarbg%2eme%3a2710%2fannounce&amp;tr=http%3a%2f%2ftr%2ecili001%2ecom%3a8070%2fannounce&amp;tr=http%3a%2f%2ftracker%2etrackerfix%2ecom%3a80%2fannounce&amp;tr=udp%3a%2f%2fopen%2edemonii%2ecom%3a1337&amp;tr=udp%3a%2f%2ftracker%2eopentrackr%2eorg%3a1337%2fannounce&amp;tr=udp%3a%2f%2fp4p%2earenabg%2ecom%3a1337">Ö©ÖëÏÀ£ºÆ½ÐÐÓîÖæ.720p.¹úÓ¢Ë«Óï.BDÖÐÓ¢Ë«×Ö.mp4</a></td>
        </tr>
        <tr>
            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px">µçÂ¿£º<a href="ed2k://|file|%E8%9C%98z%E4%BE%A0%EF%BC%9A%E5%B9%B3x%E5%AE%87%E5%AE%99.1080p.%E5%9B%BD%E8%8B%B1%E5%8F%8C%E8%AF%AD.BD%E4%B8%AD%E8%8B%B1%E5%8F%8C%E5%AD%97[%E6%9C%80%E6%96%B0%E7%94%B5%E5%BD%B1www.66ys.tv].mp4|2802362856|557366E508B38BAD229DE4FD18ABF063|h=IMW3RH5GX6LOZHBO7GV3TCPS5374K5D5|/">Ö©ÖëÏÀ£ºÆ½ÐÐÓîÖæ.1080p.¹úÓ¢Ë«Óï.BDÖÐÓ¢Ë«×Ö.mp4</a></td>
        </tr>
        <tr>
            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px">µçÂ¿£º<a href="ed2k://|file|%E8%9C%98z%E4%BE%A0%EF%BC%9A%E5%B9%B3x%E5%AE%87%E5%AE%99.720p.%E5%9B%BD%E8%8B%B1%E5%8F%8C%E8%AF%AD.BD%E4%B8%AD%E8%8B%B1%E5%8F%8C%E5%AD%97[%E6%9C%80%E6%96%B0%E7%94%B5%E5%BD%B1www.66ys.tv].mp4|1925708422|5D0A35BDC8DF931F5D32B6038F92819D|h=4WCRHPEK2BMJ73WBI6DZL5CM5GUEORD7|/">Ö©ÖëÏÀ£ºÆ½ÐÐÓîÖæ.720p.¹úÓ¢Ë«Óï.BDÖÐÓ¢Ë«×Ö.mp4</a></td>
        </tr>
        <tr>
            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px">ÍøÅÌÁ´½Ó£º<a target="_blank" href="https://pan.baidu.com/s/1uO3j1-zqXzdsFx_iUszb8w">https://pan.baidu.com/s/1uO3j1-zqXzdsFx_iUszb8w</a> <br />
            ÌáÈ¡Âë£ºtz79 <br />
            ¸´ÖÆÕâ¶ÎÄÚÈÝºó´ò¿ª°Ù¶ÈÍøÅÌÊÖ»úApp£¬²Ù×÷¸ü·½±ãÅ¶</td>
        </tr>
        <tr>
            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px">´ÅÁ¦£º<a href="magnet:?xt=urn:btih:H4HV3PG5DCEFMNBZ5BGNHCOTQZI7O55H&amp;dn=zzx%ef%bc%9a%e5%b9%b3x%e5%ae%87%e5%ae%99%2e1080p%2eBD%e4%b8%ad%e8%8b%b1%e5%8f%8c%e5%ad%97%5b%e6%9c%80%e6%96%b0%e7%94%b5%e5%bd%b1www%2e66ys%2etv%5d%2emp4&amp;tr=udp%3a%2f%2f9%2erarbg%2eto%3a2710%2fannounce&amp;tr=udp%3a%2f%2f9%2erarbg%2eme%3a2710%2fannounce&amp;tr=http%3a%2f%2ftr%2ecili001%2ecom%3a8070%2fannounce&amp;tr=http%3a%2f%2ftracker%2etrackerfix%2ecom%3a80%2fannounce&amp;tr=udp%3a%2f%2fopen%2edemonii%2ecom%3a1337&amp;tr=udp%3a%2f%2ftracker%2eopentrackr%2eorg%3a1337%2fannounce&amp;tr=udp%3a%2f%2fp4p%2earenabg%2ecom%3a1337">Ö©ÖëÏÀ£ºÆ½ÐÐÓîÖæ.1080p.BDÖÐÓ¢Ë«×Ö.mp4</a></td>
        </tr>
        <tr>
            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px">´ÅÁ¦£º<a href="magnet:?xt=urn:btih:HB5PCOVLFM35JO5DFHP3S5JCSPBGF526&amp;dn=zzx%ef%bc%9a%e5%b9%b3x%e5%ae%87%e5%ae%99%2e720p%2eBD%e4%b8%ad%e8%8b%b1%e5%8f%8c%e5%ad%97%5b%e6%9c%80%e6%96%b0%e7%94%b5%e5%bd%b1www%2e66ys%2etv%5d%2emp4&amp;tr=udp%3a%2f%2f9%2erarbg%2eto%3a2710%2fannounce&amp;tr=udp%3a%2f%2f9%2erarbg%2eme%3a2710%2fannounce&amp;tr=http%3a%2f%2ftr%2ecili001%2ecom%3a8070%2fannounce&amp;tr=http%3a%2f%2ftracker%2etrackerfix%2ecom%3a80%2fannounce&amp;tr=udp%3a%2f%2fopen%2edemonii%2ecom%3a1337&amp;tr=udp%3a%2f%2ftracker%2eopentrackr%2eorg%3a1337%2fannounce&amp;tr=udp%3a%2f%2fp4p%2earenabg%2ecom%3a1337">Ö©ÖëÏÀ£ºÆ½ÐÐÓîÖæ.720p.BDÖÐÓ¢Ë«×Ö.mp4</a></td>
        </tr>
        <tr>
            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px">µçÂ¿£º<a href="ed2k://|file|zzx%EF%BC%9A%E5%B9%B3x%E5%AE%87%E5%AE%99.1080p.BD%E4%B8%AD%E8%8B%B1%E5%8F%8C%E5%AD%97[%E6%9C%80%E6%96%B0%E7%94%B5%E5%BD%B1www.66ys.tv].mp4|4810443913|E00EEAF33EF170DBC70AD6CF0E8694D0|h=GFUED4UYBREQKBEPFUDQOXUDLFNTTMZG|/">Ö©ÖëÏÀ£ºÆ½ÐÐÓîÖæ.1080p.BDÖÐÓ¢Ë«×Ö.mp4</a></td>
        </tr>
        <tr>
            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px">µçÂ¿£º<a href="ed2k://|file|zzx%EF%BC%9A%E5%B9%B3x%E5%AE%87%E5%AE%99.720p.BD%E4%B8%AD%E8%8B%B1%E5%8F%8C%E5%AD%97[%E6%9C%80%E6%96%B0%E7%94%B5%E5%BD%B1www.66ys.tv].mp4|2763273310|F3EA81917A9189CA1A5A39266530DC2C|h=NAIDITONLZNHCV5FSYAHPMMWWS7Y6YZY|/">Ö©ÖëÏÀ£ºÆ½ÐÐÓîÖæ.720p.BDÖÐÓ¢Ë«×Ö.mp4</a></td>
        </tr>
        <tr>
            <td bgcolor="#ffffbb" width="100%" style="word-break: break-all; line-height: 18px">ÍøÅÌÁ´½Ó£º<a target="_blank" href="https://pan.baidu.com/s/1EQRa03v6I05P_-QI4xXjvg">https://pan.baidu.com/s/1EQRa03v6I05P_-QI4xXjvg</a> <br />
            ÌáÈ¡Âë£º2p1d <br />
            ¸´ÖÆÕâ¶ÎÄÚÈÝºó´ò¿ª°Ù¶ÈÍøÅÌÊÖ»úApp£¬²Ù×÷¸ü·½±ãÅ¶</td>
        </tr>
    </tbody>
</table>
</p><div align="center"><div class="fl"><script type="text/javascript" src="http://www.hao6v.com/d/gg3002.js"></script></div><div class="fr"><script type="text/javascript" src="http://www.hao6v.com/d/f6.js"></script></div><div class="cr"></div></div>
<div class="tps">
ÉÏÒ»Æª <br> <a href="http://www.hao6v.com/jddy/2018-12-22/DJDGS.html" rel="prev" target="_blank">2018¶¯»­¡¶¾«Áé±¦¿ÉÃÎ£º´ó¼ÒµÄ¹ÊÊÂ¡·1080p.BDÖÐ×Ö</a>
<br>
ÏÂÒ»Æª <br> <a href="http://www.hao6v.com/jddy/2018-12-30/WDPHW2DNHLW.html" rel="next" target="_blank">2018¸ß·Ö¶¯»­¡¶ÎÞµÐÆÆ»µÍõ2£º´óÄÖ»¥ÁªÍø¡·1080p.¹úÓ¢ÔÁÈýÓï.BDÖÐÓ¢Ë«×Ö</a>
</div>
<div class="tps">  <strong> 2018¸ß·Ö¶¯»­¡¶Ö©ÖëÏÀ£ºÆ½ÐÐÓîÖæ.¼Ó³¤°æ¡·1080p.BDÖÐÓ¢Ë«×Ö ÏÂÔØ°ïÖú£ºÈçÎÞ·¨ÏÂÔØÇëÏÈ¿´<a href="http://www.hao6v.com/dy/2010-10-11/12868.html" target="_blank">ÏÂÔØ°ïÖú</a>
¡£ </strong>  <br />  
1.ÏÂÔØÊ±Ñ¸À×Èí¼þÈçÌáÊ¾¡®ÈÎÎñ´íÎó£¬Î´Öª´íÎó£¬Ãô¸Ð×ÊÔ´£¬Î¥¹æÄÚÈÝ£¬°æÈ¨µÈµÈ¡¯¶¼ÊÇÑ¸À×ÆÁ±Î×ÊÔ´µÄ±íÏÖ£¬ºÍ6vÎÞ¹Ø¡£Çë×ÐÏ¸ä¯ÀÀÏÂÔØ°ïÖú£¬ÒÀ¾É¿ÉÒÔÕý³£ÏÂÔØ¡£ <br />  
2.Ñ¸À×¶Ô×ÊÔ´µÄÆÁ±ÎÔ½À´Ô½ÑÏÖØ£¬ËùÒÔÇë´ó¼Ò²»ÒªÊ¹ÓÃ×îÐÂ°æÑ¸À×ÏÂÔØ6vµÄ×ÊÔ´£¬½¨ÒéÊ¹ÓÃÑ¸À×5.8»òÕß¼«ËÙÑ¸À×¡£ <br />
3.±¾Õ¾ËùÓÐ×ÊÔ´Ö§³Ö°Ù¶ÈÃëÀëÏß£¬Ö§³Ö°Ù¶ÈÍøÅÌÔÚÏß¹Û¿´£¬²»»áÊ¹ÓÃµÄÍ¬Ñ§¿ÉÒÔä¯ÀÀÏÂÔØ°ïÖú¡£ <br />
<strong> ±¾Õ¾ËùÓÐµçÓ°ÍêÈ«Ãâ·Ñ£¬ÍÆ¼öÊ¹ÓÃÑ¸À×ÏÂÔØ£¬ÏÂÔØµÄÈËÔ½¶àÏÂÔØËÙ¶ÈÔ½¿ì£¬°Ñ×ÊÔ´·ÖÏí¸øÄúµÄÅóÓÑ¿ÉÒÔ´ó´óÌá¸ßÏÂÔØËÙ¶È¡£</strong>  <br />
</div>
<div class="downtps"><strong>2018¸ß·Ö¶¯»­¡¶Ö©ÖëÏÀ£ºÆ½ÐÐÓîÖæ.¼Ó³¤°æ¡·1080p.BDÖÐÓ¢Ë«×ÖÍøÓÑÆÀÂÛ£º</strong>
</div> 
</div>  
<iframe name="ifc" id="ifc" src="/e/pl/?classid=35&id=32485" width="100%"  marginheight="0" border="0" frameborder="0" scrolling="no" height="0"
onload="this.height=0;var fdh=(this.Document?this.Document.body.scrollHeight:this.contentDocument.body.offsetHeight);this.height=(fdh>700?fdh:700)" ></iframe>

<div class="downtps dp">  </div>
<div class="cr"></div>
        </div>
    </div>
    <div class="col1">
        <div class="box mt6">
        	<h3>ÈÈÃÅµçÓ°µçÊÓ¾ç</h3>
            <ul class="lt">
            <li><a href="http://www.hao6v.com/mj/2015-04-12/QLDYX7.html" target="_blank"><font color='#FF0000'>ÃÀ¾ç¡¶È¨LµÄÓÎÏ·¡·µÚÆß¼¾È«</font></a></li><li><a href="http://www.hao6v.com/mj/2015-03-02/24886.html" target="_blank"><font color='#FF0000'>ÃÀ¾ç¡¶ÐÐÊ¬×ßÈâ¡·µÚ¾Å¼¾[¸üÐÂ¸ßÇå</font></a></li><li><a href="http://www.hao6v.com/dy/2014-11-21/24362.html" target="_blank"><font color='#FF0000'>ÍøÕ¾ÆôÓÃ±¸ÓÃµØÖ·www.6vhao.com </font></a></li><li><a href="http://www.hao6v.com/dy/2017-06-27/29366.html" target="_blank"><font color='#FF0000'>Ã²ËÆÄ³À×ÒÑ»Ö¸´Õý³£</font></a></li><li><a href="http://www.hao6v.com/mj/2011-10-17/16397.html" target="_blank"><font color='#FF0000'>ÃÀ¾ç¡¶ÐÐÊ¬×ßÈâ¡·µÚ1-4¼¾È«</font></a></li><li><a href="http://www.hao6v.com/mj/2013-04-01/20273.html" target="_blank"><font color='#FF0000'>ÃÀ¾ç¡¶±ùÓë»ðÖ®¸è¡·µÚËÄ¼¾È«</font></a></li><li><a href="http://www.hao6v.com/dlz/2016-12-20/28299.html" target="_blank"><font color='#FF0000'>¡¶¹í´µµÆÖ®¾«¾ø¹Å³Ç¡·È«¼¯</font></a></li><li><a href="http://www.hao6v.com/mj/2016-10-03/27892.html" target="_blank"><font color='#FF0000'>ÃÀ¾ç¡¶Î÷²¿ÊÀ½ç¡·µÚ¶þ¼¾È«</font></a></li><li><a href="http://www.hao6v.com/mj/2013-01-26/19814.html" target="_blank"><font color='#FF0000'>ÃÀ¾ç¡¶Ë¹°Í´ï¿ËË¹£º×çÖäÕßÖ®Õ½¡·</font></a></li><li><a href="http://www.hao6v.com/mj/2014-10-08/24087.html" target="_blank"><font color='#FF0000'>ÃÀ¾ç¡¶ÉÁµçÏÀ¡·µÚÎå¼¾[¸üÐÂ¸ßÇå1</font></a></li><li><a href="http://www.hao6v.com/dy/2016-04-27/PFXDZCRZYLM.html" target="_blank"><font color='#FF0000'>¡¶òùòðÏÀ´óÕ½³¬ÈË£ºÕýÒåÀèÃ÷¡·72</font></a></li><li><a href="http://www.hao6v.com/mj/2016-09-21/27808.html" target="_blank"><font color='#FF0000'>ÃÀ¾ç¡¶Éñ¶Ü¾ÖÌØ¹¤¡·µÚÎå¼¾È«</font></a></li><li><a href="http://www.hao6v.com/dlz/2017-09-05/BaiYeZuiXiong.html" target="_blank"><font color='#FF0000'>¶¹°ê9·ÖÉñ¾ç¡¶°×Ò¹×·Ð×¡·È«¼¯</font></a></li><li><a href="http://www.hao6v.com/dy/2017-06-15/ShengQiNvXia.html" target="_blank"><font color='#FF0000'>2017¶¯×÷¿Æ»Ã¡¶ÉñÆæÅ®ÏÀ¡·1080p.</font></a></li><li><a href="http://www.hao6v.com/dlz/2017-01-10/SDYXZ2017B.html" target="_blank">¡¶ÉäµñÓ¢ÐÛ´«2017°æ¡·</a></li><li><a href="http://www.hao6v.com/mj/2013-09-25/21456.html" target="_blank"><font color='#FF0000'>ÃÀ¾ç¡¶Éñ¶Ü¾ÖÌØ¹¤¡·µÚÈý¼¾È«</font></a></li><li><a href="http://www.hao6v.com/dy/2015-01-01/24583.html" target="_blank"><font color='#FF0000'>2014¿Æ»Ã´óÆ¬¡¶ÐÇ¼Ê´©Ô½¡·720p.¹ú</font></a></li><li><a href="http://www.hao6v.com/dy/2015-06-06/FCDMKSKBZL.html" target="_blank"><font color='#FF0000'>2015¸ß·Ö¶¯×÷¡¶·è¿ñµÄÂó¿ËË¹£º¿ñ</font></a></li><li><a href="http://www.hao6v.com/dy/2016-07-29/DuLiRi2.html" target="_blank"><font color='#FF0000'>2016¶¯×÷¿Æ»Ã¡¶¶ÀÁ¢ÈÕ2¡·720p.¹ú</font></a></li><li><a href="http://www.hao6v.com/dy/2017-05-31/YiXingJueXing.html" target="_blank"><font color='#FF0000'>2017¶¯×÷¿Æ»Ã¡¶ÒìÐÇ¾õÐÑ¡·720p.¹ú</font></a></li>   </ul>
        </div>
         <!--/box-->
    <div class="box">
        	<h3>×îÐÂµçÓ°ÏÂÔØ</h3>
            <ul class="lt">
            <li><a href="http://www.hao6v.com/dy/2019-02-14/XiaoTouJiaZu.html" target="_blank"><font color='#FF0000'>2018¸ß·Ö¾çÇé¡¶Ð¡Íµ¼Ò×å¡·1080p.</font></a></li><li><a href="http://www.hao6v.com/gq/2019-03-24/ShunLiuNiLiu.html" target="_blank">¾­µä¶¯×÷¾çÇé¡¶Ë³Á÷ÄæÁ÷¡·720p.B</a></li><li><a href="http://www.hao6v.com/gq/2019-03-19/YaoShouDuShi.html" target="_blank">¾­µä¶¯×÷¿Æ»Ã¡¶ÑýÊÞ¶¼ÊÐ¡·720p.¹ú</a></li><li><a href="http://www.hao6v.com/dy/2019-01-05/DaHuangFeng.html" target="_blank"><font color='#FF0000'>2018¸ß·Ö¿Æ»Ã¡¶´ó»Æ·ä¡·1080p.BD</font></a></li><li><a href="http://www.hao6v.com/jddy/2018-12-27/ZZXPXYZ.html" target="_blank"><font color='#FF0000'>2018¸ß·Ö¶¯»­¡¶Ö©ÖëÏÀ£ºÆ½ÐÐÓîÖæ</font></a></li><li><a href="http://www.hao6v.com/dy/2019-03-24/MSYBZD.html" target="_blank">2018¾çÇé¡¶Ã¨ÊÇÒª±§×ÅµÄ¡·720p.B</a></li><li><a href="http://www.hao6v.com/dy/2019-03-24/BenXiangDaHai.html" target="_blank">2018Ææ»Ã¾çÇé¡¶±¼Ïò´óº£¡·720p.B</a></li><li><a href="http://www.hao6v.com/dy/2019-03-24/32978.html" target="_blank">2018¾çÇé¡¶Ñ©Ôá¡·4K.HD¹úÓïÖÐ×Ö</a></li><li><a href="http://www.hao6v.com/dy/2019-03-24/32979.html" target="_blank">2018¾çÇé¡¶ÆÆÃÅ¡·4K.HD¹úÓïÖÐ×Ö</a></li><li><a href="http://www.hao6v.com/dy/2019-03-24/32977.html" target="_blank">2018¾çÇé¡¶ÄÚÁªÉý´«Ææ¡·1080p.HD</a></li><li><a href="http://www.hao6v.com/dy/2019-03-24/32975.html" target="_blank">2017¾çÇé¡¶ÎÒµÄÉÏ¸ß¡·1080p.HD¹ú</a></li><li><a href="http://www.hao6v.com/dy/2019-03-24/32980.html" target="_blank">2018¾çÇé¡¶´ò¹¤ÀÏ°å¡·1080p.HD¹ú</a></li><li><a href="http://www.hao6v.com/dy/2019-03-22/32961.html" target="_blank">2019ÐüÒÉ¡¶ÎçÒ¹ÃÔ°¸¡·1080p.HD¹ú</a></li><li><a href="http://www.hao6v.com/dy/2019-03-22/32963.html" target="_blank">2019¶¯×÷¡¶ÓÀÉúÖ®µØ¡·720p.BDÖÐÓ¢</a></li><li><a href="http://www.hao6v.com/dy/2019-03-19/TianQu.html" target="_blank">2018¾çÇé¡¶ÌìÇþ¡·1080p.HD¹úÓïÖÐ</a></li><li><a href="http://www.hao6v.com/dy/2019-03-21/32955.html" target="_blank">2019°®Çé¡¶¶À¼Ò¼ÇÒäÖ®ÓÂ¸Ò°®¡·10</a></li><li><a href="http://www.hao6v.com/dy/2019-03-21/32957.html" target="_blank">2019°®Çé¡¶¶À¼Ò¼ÇÒäÖ®ÔÙ¼û°®¡·10</a></li><li><a href="http://www.hao6v.com/dy/2019-03-22/LianZhengFengYun.html" target="_blank"><font color='#FF0000'>2019¾çÇé¡¶Á®Õþ·çÔÆ¡·1080p.¹úÔÁ</font></a></li><li><a href="http://www.hao6v.com/dy/2019-03-21/SiWangTianShi.html" target="_blank">2018¸ß·Ö¾çÇé¡¶ËÀÍöÌìÊ¹¡·720p.B</a></li><li><a href="http://www.hao6v.com/dy/2019-01-04/GJPCZR.html" target="_blank">2018¾çÇé¡¶¹ú¼ÒÆÆ²úÖ®ÈÕ¡·720p.H</a></li><li><a href="http://www.hao6v.com/dy/2019-03-20/32950.html" target="_blank">2019¾çÇéÃ°ÏÕ¡¶Ò»Ìõ¹·µÄ»Ø¼ÒÂ·¡·</a></li><li><a href="http://www.hao6v.com/dy/2019-03-12/FuZongTong.html" target="_blank"><font color='#FF0000'>2018¸ß·Ö¾çÇé¡¶¸±×ÜÍ³¡·1080p.BD</font></a></li><li><a href="http://www.hao6v.com/dy/2019-03-20/STHAL.html" target="_blank">2018´«¼Ç¾çÇé¡¶Ë¹Ì¹ºÍ°ÂÀû¡·1080</a></li><li><a href="http://www.hao6v.com/dy/2019-03-20/ChongShuRenSheng.html" target="_blank">2018°®ÇéÏ²¾ç¡¶ÖØËÜÈËÉú¡·720p.B</a></li><li><a href="http://www.hao6v.com/dy/2019-03-21/LuoZi.html" target="_blank"><font color='#FF0000'>2018¸ß·Ö¾çÇé¡¶Ââ×Ó¡·1080p.BDÖÐ</font></a></li>            </ul>
        </div>
         <!--/box-->
        <div class="box mt6">
        	<h3>×îÐÂµçÊÓ¾çÏÂÔØ</h3>
            <ul class="lt">
            <li><a href="http://www.hao6v.com/rj/2019-03-24/32982.html" target="_blank">ÈÕ¾ç¡¶±ôËÀÖ®ÑÛ¡·¸üÐÂµÚ01¼¯</a></li><li><a href="http://www.hao6v.com/mj/2019-03-16/32919.html" target="_blank"><font color='#FF0000'>ÃÀ¾ç¡¶°®£¬ËÀÍöºÍ»úÆ÷ÈË¡·µÚÒ»¼¾</font></a></li><li><a href="http://www.hao6v.com/dlz/2019-02-15/DongGong.html" target="_blank">¡¶¶«¹¬¡·¸üÐÂµÚ48¼¯</a></li><li><a href="http://www.hao6v.com/mj/2016-12-17/28263.html" target="_blank">ÃÀ¾ç¡¶ÏÈ¼ûÖ®Ã÷¡·µÚ¶þ¼¾[¸üÐÂ¸ßÇå</a></li><li><a href="http://www.hao6v.com/mj/2016-09-23/ZEHMD.html" target="_blank">ÃÀ¾ç¡¶×ï¶ñºÚÃûµ¥¡·µÚÁù¼¾[¸üÐÂ¸ß</a></li><li><a href="http://www.hao6v.com/mj/2017-02-21/28646.html" target="_blank">ÃÀ¾ç¡¶°Á¹ÇÖ®Õ½¡·µÚÈý¼¾[¸üÐÂ¸ßÇå</a></li><li><a href="http://www.hao6v.com/mj/2016-09-20/27799.html" target="_blank">ÃÀ¾ç¡¶ÎÞÑÔÓÐ°®¡·µÚÈý¼¾[¸üÐÂ¸ßÇå</a></li><li><a href="http://www.hao6v.com/mj/2015-08-14/25830.html" target="_blank">ÃÀ¾ç¡¶Ã¤µã¡·µÚËÄ¼¾[¸üÐÂ¸ßÇå16]</a></li><li><a href="http://www.hao6v.com/mj/2019-02-17/32762.html" target="_blank">ÃÀ¾ç¡¶Ä©ÈÕÑ²Âß¶Ó¡·µÚÒ»¼¾[¸üÐÂ¸ß</a></li><li><a href="http://www.hao6v.com/dlz/2019-02-26/32808.html" target="_blank">¡¶¸£¶ûÄ¦Ê¦ÄÌ¡·¸üÐÂµÚ20¼¯</a></li><li><a href="http://www.hao6v.com/dlz/2017-02-22/28652.html" target="_blank">¡¶°®»Ø¼ÒÖ®¿ªÐÄËÙµÝ¡·¸üÐÂµÚ540¼¯</a></li><li><a href="http://www.hao6v.com/dlz/2019-03-15/32909.html" target="_blank">¡¶°Ý¼û¹¬Ö÷´óÈË2¡·¸üÐÂµÚ09¼¯</a></li><li><a href="http://www.hao6v.com/dlz/2019-03-02/32847.html" target="_blank"><font color='#FF0000'>¡¶¶¼Í¦ºÃ¡·¸üÐÂµÚ41¼¯</font></a></li><li><a href="http://www.hao6v.com/mj/2019-03-21/32959.html" target="_blank">ÃÀ¾ç¡¶¶ñÐÐ¡·µÚÒ»¼¾[¸üÐÂ¸ßÇå02]</a></li><li><a href="http://www.hao6v.com/mj/2019-01-06/32562.html" target="_blank">ÃÀ¾ç¡¶É±ÊÖÒ»°à¡·µÚÒ»¼¾[¸üÐÂ¸ßÇå</a></li><li><a href="http://www.hao6v.com/rj/2018-10-19/32008.html" target="_blank">ÈÕ¾ç¡¶Ïà°ô µÚ17¼¾¡·È«¼¯</a></li><li><a href="http://www.hao6v.com/dlz/2019-02-27/32821.html" target="_blank">¡¶ÒÐÌìÍÀÁú¼Ç2019¡·¸üÐÂµÚ30¼¯</a></li><li><a href="http://www.hao6v.com/mj/2017-09-12/29805.html" target="_blank"><font color='#FF0000'>ÃÀ¾ç¡¶°ÂÎ¬¶ûºÅ¡·µÚ¶þ¼¾[¸üÐÂ¸ßÇå</font></a></li><li><a href="http://www.hao6v.com/mj/2017-01-26/28496.html" target="_blank">¼Ó¾ç¡¶Ö°³¡ÀÏÂè¡·µÚÈý¼¾[¸üÐÂ¸ßÇå</a></li><li><a href="http://www.hao6v.com/mj/2019-03-08/32874.html" target="_blank">ÃÀ¾ç¡¶Ãµ¹åÖ®Ãû¡·µÚÒ»¼¾[¸üÐÂ¸ßÇå</a></li><li><a href="http://www.hao6v.com/mj/2017-09-26/29890.html" target="_blank"><font color='#FF0000'>ÃÀ¾ç¡¶ÐÇ¼ÊÃÔº½£º·¢ÏÖºÅ¡·µÚ¶þ¼¾</font></a></li><li><a href="http://www.hao6v.com/rj/2019-03-03/32857.html" target="_blank">º«¾ç¡¶´¥¼°ÕæÐÄ¡·¸üÐÂµÚ14¼¯</a></li><li><a href="http://www.hao6v.com/rj/2019-03-16/32918.html" target="_blank">º«¾ç¡¶¸½Éí¡·¸üÐÂµÚ06¼¯</a></li><li><a href="http://www.hao6v.com/mj/2014-10-08/24086.html" target="_blank">ÃÀ¾ç¡¶Ð×¹í¶ñÁé¡·µÚÊ®ËÄ¼¾[¸üÐÂ¸ß</a></li><li><a href="http://www.hao6v.com/mj/2016-09-20/27798.html" target="_blank"><font color='#FF0000'>ÃÀ¾ç¡¶¸çÌ·¡·µÚÎå¼¾[¸üÐÂ¸ßÇå10]</font></a></li>   </ul>
        </div>
         <!--/box-->
        <div class="box mt6">
        	<h3>×îÐÂ×ÛÒÕÓÎÏ·ÏÂÔØ</h3>
            <ul class="lt">
            <li><a href="http://www.hao6v.com/zy/2019-02-28/32825.html" target="_blank">¡¶µÚ91½ì°ÂË¹¿¨°ä½±µäÀñ¡·720p.H</a></li><li><a href="http://www.hao6v.com/zy/2019-02-09/32732.html" target="_blank">¡¶2019¹ã¶«ÎÀÊÓ´ºÍí¡·1080p.HD¹ú</a></li><li><a href="http://www.hao6v.com/zy/2019-02-09/32731.html" target="_blank">¡¶2019Ìì½òÎÀÊÓ´ºÍí¡·1080p.HD¹ú</a></li><li><a href="http://www.hao6v.com/zy/2019-02-06/32716.html" target="_blank">¡¶2019±±¾©ÎÀÊÓ´ºÍí¡·1080p.HD¹ú</a></li><li><a href="http://www.hao6v.com/zy/2019-02-06/32715.html" target="_blank">¡¶2019¶«·½ÎÀÊÓ´º½ÚÍí»á¡·1080p.</a></li><li><a href="http://www.hao6v.com/zy/2019-02-06/32718.html" target="_blank">¡¶2019ºþÄÏÎÀÊÓ»ªÈË´ºÍí¡·1080p.</a></li><li><a href="http://www.hao6v.com/zy/2019-02-06/32717.html" target="_blank">¡¶2019½­ËÕÎÀÊÓ´º½ÚÍí»á¡·1080p.</a></li><li><a href="http://www.hao6v.com/zy/2019-02-04/32707.html" target="_blank">¡¶2019ÁÉÄþÎÀÊÓ´ºÍí¡·1080p.HD¹ú</a></li><li><a href="http://www.hao6v.com/zy/2019-02-04/32706.html" target="_blank">¡¶2019½­Î÷ÎÀÊÓ´ºÍí¡·1080p.HD¹ú</a></li><li><a href="http://www.hao6v.com/zy/2019-02-04/32705.html" target="_blank">¡¶2019É½Î÷ÎÀÊÓ´ºÍí¡·1080p.HD¹ú</a></li>   </ul>
        </div>
         <!--/box-->
    </div>
        </div>
         <!--/box-->
    </div>	
</div><div id="a960"><script src="/d/960.js"></script> </div>
<div id="a9602"><script src=/d/f5.js></script></div>
<div id="footer">
	<p class="t"><a href="/index.html">ÍøÕ¾ÁôÑÔ</a> - <a href="/index.html">¹ØÓÚÎÒÃÇ</a> - <a href="/index.html">¹ã¸æÒµÎñ</a> - <a href="/index.html">ÐÅÏ¢·´À¡</a> - <a href="/index.html">ºÏ×÷»ï°é</a> - <a href="/index.html">ÍøÕ¾µØÍ¼</a></p>
	<p>Copyright &copy; 2009 <a href="http://www.hao6v.com"><b><font color=red>6VµçÓ°</font></b></a> °æÈ¨ËùÓÐ<br />
	  ÓåICP±¸09051310ºÅ
</div>
<span class="hidden"><script src=/d/tj.js></script></span>
</body>
</html>
"""
# html = etree.HTML(ret)
# link_list = html.xpath("//table[1]//a")
# for link in link_list:
#     print(link)
#     print(link.text.encode("utf-8").decode("gbk"))

h = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>高级搜索 神探夏洛克 - 66影视 - 迅雷电影下载_在线电影</title>
<meta name="keywords" content="高级搜索 神探夏洛克 - 66影视 - 迅雷电影下载_在线电影" />
<meta name="description" content="高级搜索 神探夏洛克 - 66影视 - 迅雷电影下载_在线电影" />
<link rel="stylesheet" rev="stylesheet" href="/images/style.css" type="text/css" />
<script type="text/javascript" src="/js/common.js"></script>
<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7" />
</head>
<body>
	<div id="header"><div id="top">  <a href="https://app.pp63.org/快看.apk" target=_blank>APP安卓版</a>&nbsp;&nbsp;
<a href="http://www.hao6v.com/dy/2012-12-07/19512.html" target=_blank>公告区</a>&nbsp;&nbsp;<a href="http://www.hao6v.com/dy/2019-01-02/32524.html" target="_blank">豆瓣2018榜单</a>&nbsp;&nbsp;
<a href="http://www.hao6v.com/gq/2012-09-01/18841.html" target=_blank><font color='#FF0000'>6v电影排行榜</font></a>&nbsp;&nbsp;
<a href="http://www.hao6v.com/dy/2011-09-20/16090.html" target=_blank>北美票房排行榜</a>&nbsp;&nbsp;
<a href="http://www.hao6v.com/s/007/" target=_blank>007电影全集</a>&nbsp;&nbsp;
<a href="http://www.hao6v.com/s/gf250/" target=_blank>IMDB250电影</a>&nbsp;&nbsp;
<a href="/s/gf/" target=_blank>高评分电影</a>&nbsp;&nbsp;
<a href="/s/hanguodianying/" target=_blank>美国电影</a>&nbsp;&nbsp;<a href="/s/xijudianying/" target=_blank>欧洲电影</a>&nbsp;&nbsp;<a href="/s/yazhoudianying/" target=_blank>亚洲电影</a>&nbsp;&nbsp;<a href="/s/mzdy/" target=_blank>美洲电影</a> &nbsp;<a href="http://www.hao6v.com/e/tool/gbook/?bid=1" target=_blank>访客留言</a></div>
    	<div class="log"><a href="/">6V电影</a></div>
        <div class="topad"><script src="/d/f4.js"></script></div>
<div class="cr"></div>
        <div id="menu">
      <p><a href="http://www.hao6v.com/">首页</a>  <a href="http://www.hao6v.com/dy/" target=_blank>2019最新电影</a> <a href="http://www.hao6v.com/gydy/" target=_blank>国语配音电影</a> <a href="http://www.hao6v.com/zydy/" target=_blank>微电影</a> <a href="http://www.hao6v.com/gq/" target=_blank>经典高清电影</a> <a href="http://www.hao6v.com/jddy/" target=_blank>动画电影</a> <a href="http://www.hao6v.com/3D/" target=_blank>3D电影</a> <a href="http://www.hao6v.com/s/shoujiMP4dianying/" target=_blank>MP4手机电影</a> <a href="http://www.hao6v.com/dlz/" target=_blank>国剧</a> <a href="http://www.hao6v.com/rj/" target=_blank>日韩剧</a> <a href="http://www.hao6v.com/mj/" target=_blank>欧美剧</a> <a href="http://www.hao6v.com/zy/" target=_blank>综艺节目</a> <a href="http://www.hao6v.com/s/gangtaidianying/" target=_blank>港台电影</a> <a href="http://www.hao6v.com/s/jingdiandianying/" target=_blank>日韩电影</a> </p>
      <p class="bg"><a href="http://www.66e.cc/" target=_blank>66影视网</a> 专题分类：<a href="http://www.hao6v.com/s/xiju/" target=_blank>喜剧</a><a href="http://www.hao6v.com/s/dongzuo/" target=_blank>动作</a><a href="http://www.hao6v.com/s/aiqing/" target=_blank>爱情</a><a href="http://www.hao6v.com/s/kehuan/" target=_blank>科幻</a><a href="http://www.hao6v.com/s/qihuan/" target=_blank>奇幻</a><a href="http://www.hao6v.com/s/shenmi/" target=_blank>神秘</a><a href="http://www.hao6v.com/s/huanxiang/" target=_blank>幻想</a><a href="http://www.hao6v.com/s/kongbu/" target=_blank>恐怖</a><a href="http://www.hao6v.com/s/zhanzheng/" target=_blank>战争</a><a href="http://www.hao6v.com/s/maoxian/" target=_blank>冒险</a><a href="http://www.hao6v.com/s/jingsong/" target=_blank>惊悚</a><a href="http://www.hao6v.com/s/juqingpian/" target=_blank>剧情</a><a href="http://www.hao6v.com/s/zhuanji/" target=_blank>传记</a><a href="http://www.hao6v.com/s/lishi/" target=_blank>历史</a><a href="http://www.hao6v.com/s/jilu/" target=_blank>纪录</a><a href="http://www.hao6v.com/s/yindudianying/" target=_blank>印度电影</a>  <a href="http://www.hao6v.com/s/guochandianying/" target=_blank>国产电影</a> <a href="http://www.hao6v.com/s/xijudianying/" target=_blank>欧洲电影</a> <a href="http://www.hao6v.com/s/zhuanti/" target=_blank>专题推荐</a> </p>
        </div>
  </div>

<div id="a960"> <script src="/d/f1.js"></script> </div>
<div id="search">
<div class="ser">
<form action="/e/search/index.php" method="post" name="searchform" id="searchform">
<input type="hidden" name="show" value="title,smalltext" />
<input type="hidden" name="tempid" value="1" />

<span>站内搜索：<input name="keyboard" type="text" size="32" id="keyboard" class="inputText" /></span>
<span class="sect"><select name="tbname">
<option value="article">全站</option>
</select></span>
<span><input type="image" class="inputSub" src="/images/search.gif" /></span>
</form>
</span>
</div>
<div class="help">
<a href="http://www.hao6v.com/dy/2010-10-11/12868.html" target="_blank">6v电影下载帮助与教程<br />电影知识新手必看</a>
</div>
<INPUT type="button" value='收藏本影片' id="copy" onclick="javascript:d=document;window.external.AddFavorite(''+d.location.href+'', ''+d.title+'')">
<div class="help">

<!-- Baidu Button BEGIN -->
    <div id="bdshare" class="bdshare_t bds_tools get-codes-bdshare">
        <span class="bds_more">分享到：</span>
        <a class="bds_qzone"></a>
        <a class="bds_tsina"></a>
        <a class="bds_tqq"></a>
        <a class="bds_renren"></a>
        <a class="bds_baidu"></a>
        <a class="bds_copy"></a>
        <a class="bds_qq"></a>
    </div>
<script type="text/javascript" id="bdshare_js" data="type=tools&amp;uid=267792" ></script>
<script type="text/javascript" id="bdshell_js"></script>
<script type="text/javascript">
	document.getElementById("bdshell_js").src = "http://bdimg.share.baidu.com/static/js/shell_v2.js?t=" + new Date().getHours();
</script>
<!-- Baidu Button END -->
</div>
</div>

<div id="main">
<div class="box">
        	<div class="t">您的位置：<a href='/index.html'>首页</a>&nbsp;>&nbsp;高级搜索</div>
 <tr> 
                                        <td height="100%" valign="top"> <form name=search_news method=post action='http://www.hao6v.com/e/search/index.php' onsubmit='return search_check(document.search_news);'>
                        <table width="100%" border="0" cellspacing="1" cellpadding="3">
                          <input type=hidden name=show value="title">
						  <input type=hidden name=tempid value="1">
                          <tr> 
                            <td height="20">关键字： 
                              <input name="keyboard" type="text" id="keyboard" value="国语配音" size="32">
                              <select name="tbname" id="tbname">
                                <option value="article">迅雷资源</option>
                              </select> 
                              <input type="submit" name="Submit22" value="搜索"> 
                              &nbsp; 
                                     </td>
                              &nbsp; <input type="button" name="Submit" value="高级搜索" onclick="self.location.href='../../../search'">
                              (多个关键字请用&quot;空格&quot;格开) </td>
                          </tr>
                        </table>
                      </form>
                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1" bgcolor="E8F5FB">
                        <tr> 
                          <td height="25">系统搜索到约有<strong>2</strong>项符合<strong>神探夏洛克</strong>的查询结果</td>
                        </tr>
                      </table>
                       
                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">
        <tr> 
          <td><div align="center">
			  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">
                <tr> 
                  
            <td width="41%" height="25"><font color="#663333">・[<a href=/dy/>2019最新电影</a>]<span class="blue14"><a href=/dy/2016-01-02/STXLT.html target=_blank>2016剧情《神探夏洛克》720p.国英双语.BD中英双字</a></span></font></td>
                  <td width="59%"><font color="#666666">发布时间：2016-04-03 13:25:16</font></td>
                </tr>
              </table>
            </div></td>
        </tr>
        <tr> 
          <td bgcolor="#EBF3FA"> 
            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">
              <tr> 
                <td>◎译　　名　神探夏洛克/新世纪福尔摩斯(台)/神探夏洛克：恶劣的新娘/神探夏洛克：可恶的新娘/神探夏洛克剧场版/神探夏洛克：2016新年特别篇<br />
◎片　　名　Sherlock: The Abominable Bride<br />
◎年</td>
              </tr>
              <tr>
                <td><a href="/dy/2016-01-02/STXLT.html" target="_blank">/dy/2016-01-02/STXLT.html</a></td>
              </tr>
            </table>
			</td>
        </tr>
      </table>
                       
                      <table width="100%" border="0" align="center" cellpadding="3" cellspacing="1">
        <tr> 
          <td><div align="center">
			  <table width="99%" border="0" align="center" cellpadding="3" cellspacing="1">
                <tr> 
                  
            <td width="41%" height="25"><font color="#663333">・[<a href=/mj/>欧剧.美剧连载</a>]<span class="blue14"><a href=/mj/2012-01-04/17099.html target=_blank>英剧《神探夏洛克/新福尔摩斯》第三季[更新03/高清03]</a></span></font></td>
                  <td width="59%"><font color="#666666">发布时间：2014-01-13 22:07:33</font></td>
                </tr>
              </table>
            </div></td>
        </tr>
        <tr> 
          <td bgcolor="#EBF3FA"> 
            <table width="98%" border="0" align="center" cellpadding="3" cellspacing="1">
              <tr> 
                <td> <br />
<br />
【片名】神探夏洛克 第二季/Sherlock S2<br />
【电视台】：英国BBC1<br />
【首播时间】：2009年（本季首播：2012年1月1日）<br />
【类型】罪案/迷你剧<br />
【影片长度】90分钟*3集<br />
【海报制作】subaru444</td>
              </tr>
              <tr>
                <td><a href="/mj/2012-01-04/17099.html" target="_blank">/mj/2012-01-04/17099.html</a></td>
              </tr>
            </table>
			</td>
        </tr>
      </table>
                       </td>
                  </tr>
                  <tr> 
                    <td height="100%" valign="top"> <div align="center"></div></td>
                  </tr>
                  <tr> 
                    <td height="12" valign="top"></td>
                  </tr>  
</div>
</div>

<div id="footer">
	<p class="t"><a href="/index.html">网站留言</a> - <a href="/index.html">关于我们</a> - <a href="/index.html">广告业务</a> - <a href="/index.html">信息反馈</a> - <a href="/index.html">合作伙伴</a> - <a href="/index.html">网站地图</a></p>
	<p>Copyright &copy; 2009 <a href="http://www.hao6v.com"><b><font color=red>6VHAO</font>.COM</b></a> 版权所有<br />
	  渝ICP备09051310号
</div>
<span class="hidden"><script src=/d/tj.js></script></span>"""

html = etree.HTML(h)
root_list = html.xpath("//div[@id='main']//table//td[1]/text()")
print(root_list)

