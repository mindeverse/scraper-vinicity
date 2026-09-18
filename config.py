"""VICINITY scraper configuration."""
import os
from dataclasses import dataclass, field
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    BRAND_NAME: str = "VICINITY"
    SOURCE: str = "scraper-vinicity"
    BRAND_COLUMN: str = "VICINITY"
    SECOND_HAND: bool = False
    LANDING_PAGE: str = "https://www.vicinityclo.de/"
    BASE_URL: str = "https://www.vicinityclo.de"
    CURRENCY: str = "EUR"
    COUNTRY: str = "EN"
    PRODUCTS_JSON_LIMIT: int = 250

    RATE_LIMIT_DELAY: float = 1.0
    BATCH_SIZE: int = 5
    STALE_MISS_THRESHOLD: int = 2
    REQUEST_TIMEOUT: int = 30
    USER_AGENT: str = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    )
    GENDER_DEFAULT: str = "Unisex"

    SUPABASE_URL: str = field(default_factory=lambda: os.getenv("SUPABASE_URL", ""))
    SUPABASE_KEY: str = field(default_factory=lambda: os.getenv("SUPABASE_KEY", ""))

    EMBEDDING_MODEL: str = "google/siglip-base-patch16-384"
    EMBEDDING_DIM: int = 768
    # NOTE: embedding_version is never upserted to the DB (supabase_client strips it)
    EMBEDDING_VERSION: int = 0


cfg = Config()
