# VICINITY Product Scraper

Production Finds scraper for [VICINITY](https://www.vicinityclo.de/).

- Source: `scraper-vinicity`
- Store: Shopify, EN + EUR (root storefront is EN + EUR)
- Schedule: `43 1 * * 2,6` UTC (Tuesdays & Saturdays)
- Currency: EUR
- Gender default: Unisex
- Embeddings: local SigLIP `google/siglip-base-patch16-384`
- Secrets: `SUPABASE_URL`, `SUPABASE_KEY`
- Catalog crawl: store-wide `/products.json?limit=250&page=N` (~799 products)
- Upsert batch size: 5 with single-row fallback; never sends `embedding_version`
