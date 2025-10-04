#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import re
from datetime import datetime

import yaml

YAML_EARBUDS_COLLECTIONS = '../yaml/earbuds-newsletter-items.yaml'

MD_README = '../README.md'

B19_PREFIX = 'https://b19.se/data/opml/earbuds/'

def readYAML(filepath):
  content = None
  with open(filepath, 'r') as stream:
    try:
      content = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
      print(exc)
    finally:
      pass

  return content

def writeMarkdown(filepath, contents):
  s = "\n".join(contents) + "\n"
  with open(filepath, "w") as f:
    f.write(contents)


def main():
  buffer = []

  buffer.append(f"# Earbuds Podcast Collective - OPML Podcast Collections")
  buffer.append("\n")

  buffer.append("All the material of the newsletters are property of Earbuds Podcast Collective, I have just rendererd an [OPML](https://en.wikipedia.org/wiki/OPML) out of them and make no claims to their work.")
  buffer.append("\n")

  buffer.append("Go to the [Earbuds Podcast Collective](https://earbuds.audio/) for more information.")
  buffer.append("\n")

  buffer.append("All collections are browseable and downloadable at [b19.se/data/opml/earbuds/](https://b19.se/data/opml/earbuds/).")


  buffer.append("\n\n")
  buffer.append(f"## Issues ...")
  buffer.append("\n\n")

  data = readYAML(YAML_EARBUDS_COLLECTIONS)
  if data != None:
    buffer.append(f"| Weekly issus of the Earbuds Podcast Collective Newletters                           | Date       |")
    buffer.append(f"| ----------------------------------------------------------------------------------- | ---------- |")

    for issue in data['issues']:
      #print(issue)

      if "podcasts" not in issue:
        continue

      if issue['podcasts'] == None:
        continue

      if len(issue['podcasts']) < 1:
        continue

      if str(issue['date']) == "1970-01-01":
        continue

      line = []
    
      filename = issue['opml']

      line.append(f"| ")
      line.append(f"[{issue['name']}]({B19_PREFIX}{filename})")
      line.append(f" | ")
      line.append(f"{issue['date']}")
      line.append(f" |")

      table_line = "".join(line)
      buffer.append(table_line)


  buffer.append("\n\n\n")

  doc = "\n".join(buffer)
  writeMarkdown(MD_README, doc)


if __name__ == '__main__':
  main()
