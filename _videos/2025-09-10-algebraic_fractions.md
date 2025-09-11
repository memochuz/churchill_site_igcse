---
layout: video
title: Algebraic Fractions
description: This video shows some examples of how to add and subtract algebraic fractions using the least common multiple (LCM). In some cases, this approach is the same as the quick method, multiplying the denominators and cross-multiplying.
date: 2025-09-09
image: '/images/Videos/algebraic_fractions_videos.png'
video_embed: https://www.youtube.com/embed/Jvf_zDyd7KI?si=rlRE9bSzt3aclQ1Q
video_embeds:
    - https://www.youtube.com/embed/YtHMjuB9f_g?si=HsIWJ7vilkmbRaqB
    - https://www.youtube.com/embed/3fY1AqnrUhQ?si=f3HOPQiEWCdj4Bce
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