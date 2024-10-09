---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======

* Ph.D in Statistics, University of Kent, 2021
* M.S. in Statistics, Yunnan University, 2012
* B.S. in Statistics, Yunnan University, 2009

Work experience
======

* October 2023 -- Now : Neuroimaging Data Analyst KTP Associate
  * University of Kent and Innovision IP Ltd.

* September 2021 -- September 2023: Research Officer
  * The London School of Economics and Political Science

* Summer 2021: Research Assistant
  * University of Kent

Skills
======

* Interpersonal Skills:
  * Problem-solving
  * Team Work
  * Time and task management
  * Risk management
  * Project management
  * Leadership
  * Critical thinking

* Technical skills:
  * R
  * Python (Tensorflow, Pytorch)
  * C++/C
  * Matlab
  * LaTeX
  * SQL
  * Git
  * Linux
  * Cluster computing
  * Microsoft Office

Publications
======

  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Talks
======

  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>

Teaching
======

  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
