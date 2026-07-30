from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str
    redis_url: str

    # - OpenAI/Anthropic API keys
    # - JWT (SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES)
    # - Rate limiting (REQUESTS_PER_MINUTE)
    # - Retry (RETRY_ATTEMPTS, PROVIDER_TIMEOUT_SECONDS)
    # - Circuit breaker (FAILURE_THRESHOLD, RECOVERY_TIMEOUT_SECONDS)
    # - Semantic cache (CACHE_TTL_SECONDS)
    # - Logging (LOG_LEVEL)
    # - Environment (ENVIRONMENT)

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()  # type: ignore[call-arg]