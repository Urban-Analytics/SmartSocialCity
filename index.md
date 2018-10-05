---
layout: page
title:  SmartSocialCity
tagline: 
---

<img style="float:right; padding:10px ;width:200px; height:auto;" src="./figures/LOGO_ESRC.jpg" alt="ESRC logo" />



This is the website for the _SmartSocilCity_ research project, a new initiative at the [University of Leeds](http://www.leeds.ac.uk/) that has been funded by the Economic and Social Research Council ([ESRC](https://esrc.ukri.org/)) and the [Alan Turing Institute](http://turing.ac.uk/)

 - For the latest news, see the [blog]({{site.baseurl}}/blog.html).
 - For some relevant presentations, see [presentations]({{site.baseurl}}/presentations.html).
 - If you have any questions, or would like to discuss the project, then please contact the Principal Investigator: [Alison Heppenstall](http://www.geog.leeds.ac.uk/people/a.j.heppenstall/).
 - For the model code and other programming work see the [GitHub page](https://github.com/Urban-Analytics/SmartSocialCity)


## Latest Posts

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

