---
layout: video
title: Simplification of Radicals
description: These videos provide a clear and practical guide to the simplification of radicals, focusing on square roots and including a variety of worked examples. They demonstrate step-by-step methods to simplify expressions, helping students build confidence and understanding in handling radicals effectively.
date: 2025-08-05
image: '/images/Radicals/simp_radicals_banner.png'
video_embed: https://www.youtube.com/embed/HaoGK8L93Q4?si=XoC6uwsHjdcJXruM
video_embeds:
    - https://www.youtube.com/embed/BPY7gmT32XE?si=HT0SV4ZX3d7tIb9-
---

{% if page.video_embeds %}
  <div class="post-videos">
    {% for video in page.video_embeds %}
    <div class="post-video__wrap" style="margin-bottom: 1.5rem;">
      <iframe src="{{ video }}" loading="lazy" width="640" height="360" frameborder="0"
              webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
    </div>
    {% endfor %}
  </div>
  {% endif %}