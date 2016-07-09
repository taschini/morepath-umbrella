Morepath Umbrella
=================

This project puts together the Morepath framework with related projects:

* The libraries developed together with Morepath:
{%- for label, link in libraries|sort %}
  - [{{ label }}]({{ link }})
{%- endfor %}
* The extensions developed and supported within the [Morepath organization on GitHub](https://github.com/morepath):
{%- for label, link in extensions|sort %}
  - [{{ label }}]({{ link }})
{%- endfor %}
* The example applications developed and supported within the [Morepath organization on GitHub](https://github.com/morepath):
{%- for label, link in examples|sort %}
  - [{{ label }}]({{ link }})
{%- endfor %}

