from datetime import datetime
from email.utils import formatdate

REPO_LINK = "https://github.com/Ledesta/my-first-project"
FEED_TITLE = "Ledesta RSS Feed"
FEED_DESCRIPTION = "Automated RSS feed for Ledesta test posts."

with open("posts.txt", "r", encoding="utf-8") as file:
    content = file.read().strip()

blocks = content.split("\n\n")

items = ""

for block in blocks:
    lines = block.splitlines()
    title = lines[0].replace("TITLE:", "").strip()
    link = lines[1].replace("LINK:", "").strip()
    description = lines[2].replace("DESCRIPTION:", "").strip()

    pub_date = formatdate(localtime=True)

    items += f"""
    <item>
      <title>{title}</title>
      <link>{link}</link>
      <description>{description}</description>
      <pubDate>{pub_date}</pubDate>
    </item>
"""

rss = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
  <channel>
    <title>{FEED_TITLE}</title>
    <link>{REPO_LINK}</link>
    <description>{FEED_DESCRIPTION}</description>
    <language>en-us</language>
{items}
  </channel>
</rss>
"""

with open("rss.xml", "w", encoding="utf-8") as file:
    file.write(rss)

print("rss.xml created successfully.")