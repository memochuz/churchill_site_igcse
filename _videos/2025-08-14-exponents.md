---
layout: video
title: Laws of Exponents
description: These videos cover the fundamental laws of exponents, including the product of powers, power of a power, and quotient of powers. They explain how to simplify expressions using these rules and provide examples to illustrate each concept. The videos are designed to help students understand and confidently apply the laws of exponents.
date: 2025-08-05
image: '/images/Exponents/laws_exponents_video.png'
video_embed: https://www.youtube.com/embed/ZLlwb4syPx4?si=RYpjojp-KWYo7m3C
video_embeds:
    - https://www.youtube.com/embed/tHCM6qNdVSc?si=IUY2mNaQDjPDmpZZ
    - https://www.youtube.com/embed/83K4uW50HRU?si=sgXPLEVKvj8RlXRr
    - https://www.youtube.com/embed/RkFurqc0HTk?si=fZ6UTM9tmDrtcAH5
    - https://www.youtube.com/embed/FvRDjFHg0E8?si=zDSoXH7AIKiEp5qS
    - https://www.youtube.com/embed/DvNYkbafpIY?si=REZYCq1YXKby2Iw5
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