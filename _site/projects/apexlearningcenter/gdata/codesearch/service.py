# -*- coding: utf-8 -*-
#
# Copyright (c) 2007 Benoit Chesneau <benoitc@metavers.net>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.


"""CodesearchService extends GDataService to streamline Google Codesearch 
operations"""

__author__ = 'Benoit Chesneau'

try:
  from xml.etree import cElementTree as ElementTree
except ImportError:
  try:
    import cElementTree as ElementTree
  except ImportError:
    from elementtree import ElementTree
import atom
import gdata.service
import gdata.codesearch


class CodesearchService(gdata.service.GDataService): 
    """Client extension for Google codesearch service"""
    
    def __init__(self, email=None, password=None, source=None, 
            server='www.google.com', additional_headers=None):
        """Constructor for the CodesearchService.

        Args:
            email: string (optional) The e-mail address of the account to use for
                   authentication.
            password: string (optional) The password of the account to use for
                      authentication.
            source: string (optional) The name of the user's application.
            server: string (optional) The server the feed is hosted on.
            additional_headers: dict (optional) Any additional HTTP headers to be
                                transmitted to the service in the form of key-value
                                pairs.
        Yields:
            A CodesearchService object used to communicate with the Google Codesearch
            service.
        """

        gdata.service.GDataService.__init__(self,
                email=email, password=password, service='codesearch',
                source=source,server=server,
                additional_headers=additional_headers)
    
    def Query(self, uri, converter=gdata.codesearch.CodesearchFeedFromString):
        """Queries the Codesearch feed and returns the resulting feed of
           entries.

        Args:
        uri: string The full URI to be queried. This can contain query
             parameters, a hostname, or simply the relative path to a Document
             List feed. The DocumentQuery object is useful when constructing
             query parameters.
        converter: func (optional) A function which will be executed on the
                   retrieved item, generally to render it into a Python object.
                   By default the CodesearchFeedFromString function is used to
                   return a CodesearchFeed object. This is because most feed
                   queries will result in a feed and not a single entry.

        Returns :
            A CodesearchFeed objects representing the feed returned by the server
        """
        return self.Get(uri, converter=converter)

    def GetSnippetsFeed(self, text_query=None):
        """Retrieve Codesearch feed for a keyword

        Args:
            text_query : string (optional) The contents of the q query parameter. This
                         string is URL escaped upon conversion to a URI.
        Returns:
            A CodesearchFeed objects representing the feed returned by the server
        """

        query=gdata.codesearch.service.CodesearchQuery(text_query=text_query)
        feed = self.Query(query.ToUri())
        return feed


class CodesearchQuery(gdata.service.Query):
    """Object used to construct the query to the Google Codesearch feed. here only as a shorcut"""

    def __init__(self, feed='/codesearch/feeds/search', text_query=None, 
            params=None, categories=None):
        """Constructor for Codesearch Query.

        Args:
            feed: string (optional) The path for the feed. (e.g. '/codesearch/feeds/search')
            text_query: string (optional) The contents of the q query parameter. This
                        string is URL escaped upon conversion to a URI.
            params: dict (optional) Parameter value string pairs which become URL
                    params when translated to a URI. These parameters are added to
                    the query's items.
            categories: list (optional) List of category strings which should be
                        included as query categories. See gdata.service.Query for
                        additional documentation.

        Yelds:
            A CodesearchQuery object to construct a URI based on Codesearch feed
        """

        gdata.service.Query.__init__(self, feed, text_query, params, categories)
