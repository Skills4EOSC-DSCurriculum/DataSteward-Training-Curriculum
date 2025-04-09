from typing import List
from urllib.parse import urlparse

import markdown
from mkdocs.config.defaults import MkDocsConfig

# Source (removed the code for IGNORE_DOMAINS)
# https://github.com/squidfunk/mkdocs-material/discussions/3660#discussioncomment-6725823


class ExternalLinksTreeProcessor(markdown.treeprocessors.Treeprocessor):
    """
    Adds target="_blank" and rel="noopener" to external links.
    """

    def __init__(self, md):
        super().__init__(md)

    def run(self, root):
        for element in root.iter():
            if element.tag == "a":
                href = element.get("href", "")

                # parse the href and check if it's an absolute URL with http or https scheme
                parsed_url = urlparse(href)

                if parsed_url.scheme in ["http", "https"]:
                    # remove port, if present
                    domain = parsed_url.netloc.split(":")[0]

                    element.set("target", "_blank")
                    element.set("rel", "noopener")


class ExternalLinksExtension(markdown.Extension):
    def __init__(self, **kwargs):
        super(ExternalLinksExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md: markdown.Markdown):
        md.treeprocessors.register(
            ExternalLinksTreeProcessor(md), "external_links", -1000
        )


def on_config(config: MkDocsConfig, **kwargs):
    # inject the markdown extension
    config.markdown_extensions.append(ExternalLinksExtension())
    return config
