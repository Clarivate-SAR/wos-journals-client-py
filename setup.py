"""
    Web of Science™ Journals API

    This API provides journal-level metadata and metrics for all journals in the Journal Citation Reports™ covered in the Web of Science Core Collection, including the Journal Impact Factor™ and other new metrics. Integrate journal data into your internal systems or retrieve journal indicators for bibliometrics studies.  ## Resources This API follows the REST approach to disclose resources in URL format. Only the GET method is currently available to perform requests over HTTP.  The API is available on the [Clarivate Developer Portal](https://developer.clarivate.com/apis/wos-journal). The access requires registration on the Portal and approval from the Clarivate Sales/Product teams to entitle to the API.  ## Credentials All requests require authentication with an API Key authentication flow. For more details, check the [Guide](https://developer.clarivate.com/help/api-access#key_access).   ## Content You can learn more about content at [Journal Citation Reports™ Product page](https://clarivate.com/webofsciencegroup/solutions/journal-citation-reports/), or in the [documentation](http://jcr.help.clarivate.com/Content/home.htm).  ## <a name=\"search\"></a> Search (query parameter `q=`) This API supports free-text search for a journal name, abbreviation, ISSN code, publisher, and Web of Science™ category name (only `/categories` endpoint). You need to provide a complete and valid ISSN code pattern; otherwise, the API will not look up for ISSN codes.  ### Boolean operators | Operator    | Description  | Example| |-----|-----|------------------| | + / \" \" | Search by two or more terms in the same field. Blank space is the same as an AND operator. The search retrieves all the records that contain the terms, e.g., | `/journals?q=matrix biology`<br> `/journals?q=nature+group` | | OR | Search by at least one term in the field. The search retrieves all the records that contain one of the terms, e.g., | `/journals?q=gas OR oil` | | NOT / - | Search by excluding specific terms. The search retrieves all the records that match the query specifics, e.g., | `/journals?q=genetics -nature` |  ### Special symbols The wildcards ( __*__ ) are allowed in the search that starts with the search query&#58; `/journals?q=nano*` will search indications that start from __nano__&#58; for example, _Nanotechnology_ or _nanotubes_.  Please note&#58; the free text search query (with the parameter `q=`) should contain at least three symbols.  ## Filtering The API supports several filters for Journals and Web of Science™ Categories, narrowing down the initial list of entities or search results.  There are two types of filters:  - Filter by one or multiple **values**: *edition*, *categoryCode*, *jcrYear*, *jifQuartile* - Filter by **range**: *jif*, *jifPercentile*  ### Filter by values The filter name goes before the equals sign, followed by one or multiple filter values, separated by a semicolon, like `categoryCode=RZ;RU`. You can combine various filters with or without the search. Filters are separated by an ampersand (**&amp;**): `q=nature&categoryCode=RU;KM&jcrYear=2018`  Please note&#58; filter by *jcrYear* allows only one year value as an input  ### <a name='range'></a> Filter by range The API supports range filtering for Journal Impact Factor (*jif*) or Journal Impact Factor Percentile (*jifPercentile*) with the following operators:  - ***eq*** (equal): if a Journal Impact Factor (Percentile) is equal to a specific number.<br /> For example: for `jif=eq:5.032` the result will include journals with Journal Impact Factor = 5.032.<br /> Not combinable with any other operator - ***gt*** (greater than): if a Journal Impact Factor (Percentile) is greater than a specific number.<br /> For example: for `jif=gt:5` the result will include journals with Journal Impact Factor = 5.001 and higher.<br /> Combinable with *lt* and *lte* operators - ***gte*** (greater than equal): if a Journal Impact Factor (Percentile) is greater than or equal to a specific number.<br /> For example: for `jif=gte:5` the result will include journals with Journal Impact Factor = 5.000 and higher.<br /> Combinable with *lt* and *lte* operators - ***lt*** (less than): if a Journal Impact Factor (Percentile) is less than a specific number.<br /> For example: for `jif=lt:5` the result will include journals with Journal Impact Factor = 4.999 and less.<br /> Combinable with *gt* and *gte* operators - ***gt*** (less than equal): if a Journal Impact Factor (Percentile) is less than a specific number.<br /> For example: for `jif=lte:5` the result will include journals with Journal Impact Factor = 5.000 and less.<br /> Combinable with *gt* and *gte* operators  Use `AND` to combine two operators, e.g.,`jifPercentile=gte:50 AND lte:80` responses with all journals in a percentile range from 50% to 80% (both included).  ## Pagination To ensure fast response time, each search or multiple entity calls (such as `/journals` or `/categories/ID/cited/year/YYYY`) retrieve only a certain number of hits/records.  There are two optional request parameters to browse along with the result&#58; _limit_ and _page_.  - limit&#58; Number of returned results, ranging from 0 to 50 (default **10**) - page&#58; Specifying a page to retrieve (default **1**)  Moreover, this information is shown in the response body, in the tag **metadata**&#58;  ```json \"metadata\": {   \"total\": 91,   \"page\": 1,   \"limit\": 10 } ``` ## Errors The WoS Journals API uses conventional HTTP success or failure status codes. For errors, some extra information is included to indicate what went wrong in the JSON response. The list of HTTP codes is listed below.  | Code  | Title  | Description | |---|---|---| | 400  | Bad request  | Request syntax error | | 401  | Unauthorized  | The API key is invalid or missed | | 404  | Not found  | The resource is not found | | 405 | Method not allowed | Method other than GET is not allowed | | 50X  | Server errors  | Technical error with servers| Each error response (except `401 Unauthorized` error) contains the code of the error, the title of the error and detailed description of the error: a misprint in an endpoint, wrong URL parameter, etc. The example of the error message is shown below:  ```json \"error\": {   \"status\": 404,   \"title\": \"Resource couldn't be found\",   \"details\": \"There is no information in WoS Journals API about the identifier ABC_DEF for the Journals content area. Sorry :(\" } ``` For the `401 Unauthorized` error the response body is a little bit different: ```json {   \"error_description\": \"The access token is missing\",   \"error\": \"invalid_request\" } ```  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "wos-journals-client-py"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="Web of Science™ Journals API",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Web of Science™ Journals API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Clarivate Content as a Service Licence",
    long_description="""\
    This API provides journal-level metadata and metrics for all journals in the Journal Citation Reports™ covered in the Web of Science Core Collection, including the Journal Impact Factor™ and other new metrics. Integrate journal data into your internal systems or retrieve journal indicators for bibliometrics studies.  ## Resources This API follows the REST approach to disclose resources in URL format. Only the GET method is currently available to perform requests over HTTP.  The API is available on the [Clarivate Developer Portal](https://developer.clarivate.com/apis/wos-journal). The access requires registration on the Portal and approval from the Clarivate Sales/Product teams to entitle to the API.  ## Credentials All requests require authentication with an API Key authentication flow. For more details, check the [Guide](https://developer.clarivate.com/help/api-access#key_access).   ## Content You can learn more about content at [Journal Citation Reports™ Product page](https://clarivate.com/webofsciencegroup/solutions/journal-citation-reports/), or in the [documentation](http://jcr.help.clarivate.com/Content/home.htm).  ## &lt;a name&#x3D;\&quot;search\&quot;&gt;&lt;/a&gt; Search (query parameter &#x60;q&#x3D;&#x60;) This API supports free-text search for a journal name, abbreviation, ISSN code, publisher, and Web of Science™ category name (only &#x60;/categories&#x60; endpoint). You need to provide a complete and valid ISSN code pattern; otherwise, the API will not look up for ISSN codes.  ### Boolean operators | Operator    | Description  | Example| |-----|-----|------------------| | + / \&quot; \&quot; | Search by two or more terms in the same field. Blank space is the same as an AND operator. The search retrieves all the records that contain the terms, e.g., | &#x60;/journals?q&#x3D;matrix biology&#x60;&lt;br&gt; &#x60;/journals?q&#x3D;nature+group&#x60; | | OR | Search by at least one term in the field. The search retrieves all the records that contain one of the terms, e.g., | &#x60;/journals?q&#x3D;gas OR oil&#x60; | | NOT / - | Search by excluding specific terms. The search retrieves all the records that match the query specifics, e.g., | &#x60;/journals?q&#x3D;genetics -nature&#x60; |  ### Special symbols The wildcards ( __*__ ) are allowed in the search that starts with the search query&amp;#58; &#x60;/journals?q&#x3D;nano*&#x60; will search indications that start from __nano__&amp;#58; for example, _Nanotechnology_ or _nanotubes_.  Please note&amp;#58; the free text search query (with the parameter &#x60;q&#x3D;&#x60;) should contain at least three symbols.  ## Filtering The API supports several filters for Journals and Web of Science™ Categories, narrowing down the initial list of entities or search results.  There are two types of filters:  - Filter by one or multiple **values**: *edition*, *categoryCode*, *jcrYear*, *jifQuartile* - Filter by **range**: *jif*, *jifPercentile*  ### Filter by values The filter name goes before the equals sign, followed by one or multiple filter values, separated by a semicolon, like &#x60;categoryCode&#x3D;RZ;RU&#x60;. You can combine various filters with or without the search. Filters are separated by an ampersand (**&amp;amp;**): &#x60;q&#x3D;nature&amp;categoryCode&#x3D;RU;KM&amp;jcrYear&#x3D;2018&#x60;  Please note&amp;#58; filter by *jcrYear* allows only one year value as an input  ### &lt;a name&#x3D;&#39;range&#39;&gt;&lt;/a&gt; Filter by range The API supports range filtering for Journal Impact Factor (*jif*) or Journal Impact Factor Percentile (*jifPercentile*) with the following operators:  - ***eq*** (equal): if a Journal Impact Factor (Percentile) is equal to a specific number.&lt;br /&gt; For example: for &#x60;jif&#x3D;eq:5.032&#x60; the result will include journals with Journal Impact Factor &#x3D; 5.032.&lt;br /&gt; Not combinable with any other operator - ***gt*** (greater than): if a Journal Impact Factor (Percentile) is greater than a specific number.&lt;br /&gt; For example: for &#x60;jif&#x3D;gt:5&#x60; the result will include journals with Journal Impact Factor &#x3D; 5.001 and higher.&lt;br /&gt; Combinable with *lt* and *lte* operators - ***gte*** (greater than equal): if a Journal Impact Factor (Percentile) is greater than or equal to a specific number.&lt;br /&gt; For example: for &#x60;jif&#x3D;gte:5&#x60; the result will include journals with Journal Impact Factor &#x3D; 5.000 and higher.&lt;br /&gt; Combinable with *lt* and *lte* operators - ***lt*** (less than): if a Journal Impact Factor (Percentile) is less than a specific number.&lt;br /&gt; For example: for &#x60;jif&#x3D;lt:5&#x60; the result will include journals with Journal Impact Factor &#x3D; 4.999 and less.&lt;br /&gt; Combinable with *gt* and *gte* operators - ***gt*** (less than equal): if a Journal Impact Factor (Percentile) is less than a specific number.&lt;br /&gt; For example: for &#x60;jif&#x3D;lte:5&#x60; the result will include journals with Journal Impact Factor &#x3D; 5.000 and less.&lt;br /&gt; Combinable with *gt* and *gte* operators  Use &#x60;AND&#x60; to combine two operators, e.g.,&#x60;jifPercentile&#x3D;gte:50 AND lte:80&#x60; responses with all journals in a percentile range from 50% to 80% (both included).  ## Pagination To ensure fast response time, each search or multiple entity calls (such as &#x60;/journals&#x60; or &#x60;/categories/ID/cited/year/YYYY&#x60;) retrieve only a certain number of hits/records.  There are two optional request parameters to browse along with the result&amp;#58; _limit_ and _page_.  - limit&amp;#58; Number of returned results, ranging from 0 to 50 (default **10**) - page&amp;#58; Specifying a page to retrieve (default **1**)  Moreover, this information is shown in the response body, in the tag **metadata**&amp;#58;  &#x60;&#x60;&#x60;json \&quot;metadata\&quot;: {   \&quot;total\&quot;: 91,   \&quot;page\&quot;: 1,   \&quot;limit\&quot;: 10 } &#x60;&#x60;&#x60; ## Errors The WoS Journals API uses conventional HTTP success or failure status codes. For errors, some extra information is included to indicate what went wrong in the JSON response. The list of HTTP codes is listed below.  | Code  | Title  | Description | |---|---|---| | 400  | Bad request  | Request syntax error | | 401  | Unauthorized  | The API key is invalid or missed | | 404  | Not found  | The resource is not found | | 405 | Method not allowed | Method other than GET is not allowed | | 50X  | Server errors  | Technical error with servers| Each error response (except &#x60;401 Unauthorized&#x60; error) contains the code of the error, the title of the error and detailed description of the error: a misprint in an endpoint, wrong URL parameter, etc. The example of the error message is shown below:  &#x60;&#x60;&#x60;json \&quot;error\&quot;: {   \&quot;status\&quot;: 404,   \&quot;title\&quot;: \&quot;Resource couldn&#39;t be found\&quot;,   \&quot;details\&quot;: \&quot;There is no information in WoS Journals API about the identifier ABC_DEF for the Journals content area. Sorry :(\&quot; } &#x60;&#x60;&#x60; For the &#x60;401 Unauthorized&#x60; error the response body is a little bit different: &#x60;&#x60;&#x60;json {   \&quot;error_description\&quot;: \&quot;The access token is missing\&quot;,   \&quot;error\&quot;: \&quot;invalid_request\&quot; } &#x60;&#x60;&#x60;  # noqa: E501
    """
)
