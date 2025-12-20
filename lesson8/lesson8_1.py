{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6571e712",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "import asyncio,json\n",
    "from crawl4ai import AsyncWebCrawler,CrawlerRunConfig,CacheMode\n",
    "from crawl4ai.extraction_strategy import JsonCssExtractionStrategy\n",
    "from pprint import pprint\n",
    "\n",
    "async def main():\n",
    "    \n",
    "    schema ={\n",
    "        \"name\":\"匯率資訊\",\n",
    "        \"baseSelector\":\"table[title='牌告匯率'] tr\",\n",
    "        \"fields\":[\n",
    "            {\n",
    "                \"name\":\"幣別\",\n",
    "                \"selector\":\"td[data-table='幣別'] div.print_show\",\n",
    "                \"type\":\"text\"\n",
    "            },\n",
    "            {\n",
    "                \"name\":\"本行即期買入\",\n",
    "                \"selector\":\"td[data-table='本行即期買入']\",\n",
    "                \"type\":\"text\"\n",
    "            },\n",
    "            {\n",
    "                \"name\":\"本行即期賣出\",\n",
    "                \"selector\":\"td[data-table='本行即期賣出']\",\n",
    "                \"type\":\"text\"\n",
    "            }\n",
    "            \n",
    "        ]\n",
    "    }\n",
    "\n",
    "    extraction_strategy = JsonCssExtractionStrategy(schema)\n",
    "\n",
    "    run_config = CrawlerRunConfig(\n",
    "        cache_mode=CacheMode.BYPASS,\n",
    "        extraction_strategy=extraction_strategy\n",
    "        )\n",
    "    async with AsyncWebCrawler() as crawler:\n",
    "        url='https://rate.bot.com.tw/xrt?Lang=zh-TW'\n",
    "        result = await crawler.arun(\n",
    "            url=url,\n",
    "            config=run_config)\n",
    "        data = json.loads(result.extracted_content)\n",
    "        pprint(data)\n",
    "        \n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    asyncio.run(main())"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
