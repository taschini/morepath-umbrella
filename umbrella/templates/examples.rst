Examples
========

Demo apps
---------

The Morepath organization on GitHub maintains a few demo apps:
{% for label, link, pypi, desc in examples|sort %}

`{{ label }} <{{link}}>`_

  {{ desc }}.
{%- endfor %}
